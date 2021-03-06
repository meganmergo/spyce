#!/usr/bin/env python3
import sys

import spyce.load
from spyce.orbit import Orbit
from spyce.human import to_human_time, to_si_prefix


def main():
    # parse orbited body
    if len(sys.argv) <= 1:
        print(
            'Usage: %s BODY [SIZE]\n'
            'Give information on possible satellites constellations\n'
            'BODY is the primary around which the constellation orbits\n'
            'SIZE is the number of satellites in the constellation\n'
            % sys.argv[0], file=sys.stderr)
        sys.exit(1)
    primary = spyce.load.from_name(sys.argv[1])

    # antennas from RemoteTech
    antennas = [
        ('Reflectron DP-10', 0.5e6),
        ('Communotron 16', 2.5e6),
        ('CommTech EXP-VR-2T', 3e6),
        ('Communotron 32', 5e6),
        ('Comms DTS-M1', 50e6),
        ('Reflectron KR-7', 90e6),
        ('Communotron 88-88', 40e9),
        ('Reflectron KR-14', 60e9),
        ('CommTech 1', 350e9),
        ('Reflectron GX-120', 400e9),
    ]

    for antenna, communication_range in antennas:
        # get characteristics of constellation
        if len(sys.argv) <= 2:
            size = primary.constellation_minimum_size(communication_range)
        else:
            size = int(sys.argv[2])
        min_a, max_a = primary.constellation_radius(communication_range, size)

        # compute period and altitude ranges
        min_period = to_human_time(Orbit(primary, min_a).period)
        max_period = to_human_time(Orbit(primary, max_a).period)
        min_a = to_si_prefix(min_a - primary.radius, 'm')
        max_a = to_si_prefix(max_a - primary.radius, 'm')

        # print everthing
        print(u'%-20s %i× %s (%s) -- %s (%s)' %
              (antenna+':', size, min_a, min_period, max_a, max_period))


if __name__ == '__main__':
    main()
