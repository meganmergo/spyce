"""Parsing utilities for KSP"""

import os
import copy
import glob
import pathlib

import spyce.rocket


def locate(subpath="GameData"):
    """Locate path in KSP installation directory"""

    candidates = (
        "~/.steam/steam", "~/.local/share/Steam",  # GNU/Linux
        "C:\Program Files\Steam", "C:\Program Files (x86)\Steam",  # Windows
        "~/Library/Application Support/Steam",  # Mac
    )

    for steam in candidates:
        steam = pathlib.Path(steam).expanduser()
        if not steam.exists():
            continue
        for apps in ("SteamApps", "steamapps"):
            path = steam / apps / "common" / "Kerbal Space Program" / subpath
            if path.exists():
                return path
    raise FileNotFoundError("cannot find KSP folder")


def files(directory="GameData", extension=".cfg"):
    """Iterate through KSP files"""
    pattern = str(locate(directory)) + '/**/*' + extension
    yield from glob.iglob(pattern, recursive=True)


def parse(f):
    """Parse a KSP .cfg file into Python dict"""

    cfg_dict = {}
    for line in f:
        line = line.split("//", 1)[0]  # strip comments
        line = line.strip()

        if line == "}":  # end of block
            break

        if not line:
            continue

        if "=" in line:  # assignment
            key, value = line.split("=", 1)
            key, value = key.strip(), value.strip()
        else:  # start of block
            parts = line.split(None, 1)
            key = parts[0]

            if parts[1:] == ["{"] or next(f).strip() == "{":
                value = parse(f)  # parse recursively
            else:
                raise SyntaxError("Expected '{'")

        # save key/value
        if key in cfg_dict:
            p = cfg_dict[key]
            if not isinstance(p, list):
                cfg_dict[key] = [p]
            cfg_dict[key].append(value)
        else:
            cfg_dict[key] = value

    return cfg_dict


def dict_get_group(cfg_dict, group, name):
    """Get element of a given name in a given group

    For example, find the MODULE named ModuleEngine.
    """

    try:
        g = cfg_dict[group]
    except KeyError:
        return None

    if isinstance(g, list):
        for v in g:
            if v.get("name") == name:
                return v
    elif g.get("name") == name:
        return g
    return None


def part_from_cfg(cfg_dict):
    """Create a part out of a parsed .cfg file"""

    # general
    name = cfg_dict['name']
    title = cfg_dict.get('title', name)
    dry_mass = float(cfg_dict.get('mass', 100.)) * 1e3  # given in tons
    coefficient_of_drag = float(cfg_dict.get('maximum_drag', .2))
    part = spyce.rocket.RocketPart(name, title, dry_mass, coefficient_of_drag)

    # engine
    r = dict_get_group(cfg_dict, 'MODULE', 'ModuleEngines') or \
        dict_get_group(cfg_dict, 'MODULE', 'ModuleEnginesFX')
    if r is not None:
        max_thrust = float(r.get('maxThrust', 0.)) * 1e3  # given in kN
        a = r['atmosphereCurve']['key']
        a = a[1] if isinstance(a, list) else a
        specific_impulse = float(a.split(' ')[1])
        part.make_engine(max_thrust, specific_impulse)

    # tank
    r = dict_get_group(cfg_dict, 'RESOURCE', 'LiquidFuel')
    if r is not None:
        q_fuel = float(r.get('amount', 0.))
        q_prop = q_fuel / 0.9 * 2  # fuel + oxidizer (liters)
        m_prop = q_prop * 5  # (kg)
        part.make_tank(m_prop)

    return part


def get_parts():
    """Generate all rocket parts from a local KSP installation"""
    parts = {}
    for path in files(os.path.join("GameData", "Squad", "Parts")):
        # "utf-8-sig" gets rid of the Byte Order Mask
        with open(path, encoding="utf-8-sig") as f:
            cfg_dict = parse(f)
        part = part_from_cfg(cfg_dict['PART'])
        parts[part.name] = part
    return parts


class PartSet:
    def __init__(self):
        self.parts = get_parts()

    def make(self, *names):
        return {copy.copy(self.parts[name]) for name in names}
