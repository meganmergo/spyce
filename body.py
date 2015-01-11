import re
import math

import physics


class CelestialBody:
    """Celestial Body

    Minimalistic model of celestial bodies (stars, planets, moons)
    It includes a few handy methods to plan orbital travel.
    """

    def __init__(self, name, gravitational_parameter=0, radius=0,
                 rotational_period=0, orbit=None, **_):
        """Definition of a celestial body

        Arguments:
        name
        gravitational_parameter  m^3/s^2
        radius                   m, optional
        rotational_period        s, optional, 0 for tidal lock
        orbit                    Orbit, optional
        """
        self.name = name
        self.radius = float(radius)
        self.gravitational_parameter = float(gravitational_parameter)
        self.orbit = orbit

        self.mass = self.gravitational_parameter/physics.G

        self.satellites = []
        if self.orbit is not None:
            self.orbit.primary.satellites.append(self)

        if rotational_period == 0 and orbit is not None:
            self.rotational_period = self.orbit.period
        else:
            self.rotational_period = float(rotational_period)

    def __repr__(self):
        """Appear as <Name> in a Python interpreter"""
        return "<%s>" % (self.name)

    def __str__(self):
        """Cast to string using the name"""
        return self.name

    def gravity(self, a=0):
        """Gravity at given altitude (m/s^2)

        Defaults to surface gravity
        """
        # see https://en.wikipedia.org/wiki/Shell_theorem
        r = self.radius+a
        mu = self.gravitational_parameter
        if a < 0:
            mu *= r**3/self.radius**3
        return mu / r**2

    def sphere_of_influence(self):
        """Radius of the sphere of influence (m)"""
        if self.orbit is None:
            return float("inf")

        mu_p = self.orbit.primary.gravitational_parameter
        mu_b = self.gravitational_parameter
        return self.orbit.semi_major_axis * (mu_b / mu_p)**0.4

    def solar_day(self):
        """Duration of the solar day (s)"""
        d = self.rotational_period
        y = self.orbit.period
        return d * y/(y-d)

    def time2str(self, s):
        """Convert a duration (s) to a human-readable string

        The string will use conventional minutes and hours,
        as well as local days (based on rotational period)
        and local years (based on orbital period)

        See str2time()
        """
        n = s < 0
        s = abs(float(s))
        y, s = divmod(s, self.orbit.period)
        d, s = divmod(s, self.rotational_period)
        h, s = divmod(s, 3600)
        m, s = divmod(s, 60)
        return "%s%uy, %ud, %u:%u:%.1f" % ("-" if n else "+", y, d, h, m, s)

    def str2time(self, t):
        """Convert a string formated time to a duration (s)

        See time2str()
        """
        x = re.search("([0-9]*)y", t)
        y = 0 if x is None else int(x.group(1))

        x = re.search("([0-9]*)d", t)
        d = 0 if x is None else int(x.group(1))

        time_re = "((([0-9]{1,2}):)?([0-9]{1,2}):)?([0-9]{1,2}(\.[0-9]*)?)$"
        x = re.search(time_re, t)
        h = 0 if x is None else int(x.group(3))
        m = 0 if x is None else int(x.group(4))
        s = 0 if x is None else float(x.group(5))

        s += y * self.orbit.period
        s += d * self.rotational_period
        s += h * 3600
        s += m * 60

        if t[0] == "-":
            s = -s

        return s

    def escape_velocity(self, distance):
        """Escape velocity at a given distance (m)"""
        return math.sqrt(2*gravitational_parameter/distance)

    def angular_diameter(self, distance):
        """Angular diameter / apparent size at a given distance (m)"""
        return math.atan(self.radius/distance)
