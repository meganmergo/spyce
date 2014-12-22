import math
import random


import vector

# easily verified
assert vector.dot([1, 0, 0], [0, 1, 1]) == 0
assert vector.norm([8, 9, 12]) == 17
assert vector.cross([0, 1, 0], [1, 0, 0]) == [0, 0, -1]
assert vector.angle([0, 1, 0], [1, 0, 0]) == -math.pi/2

# initial results
assert vector.dot([1, 4, 7], [2, 5, 8]) == 78
assert vector.norm([4, 5, 6]) == 8.774964387392123
assert vector.cross([9, 8, 7], [2, 3, 1]) == [-13, 5, 11]
assert vector.angle([4, 7, 5], [3, 5, 8]) == -0.3861364787976416
assert vector.angle([4, 5, 7], [3, 8, 5]) == +0.3861364787976416


import matrix


def checkdiff(A, B):
    for i in range(3):
        for j in range(3):
            a = A[i][j]
            b = B[i][j]
            if abs(a - b) > 1e-10:
                return False
    return True

# easily verified
i = matrix.identity()
m = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
r = matrix.rotation(90, 1, 0, 0)
assert i == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert matrix.dot_v(i, [1, 2, 3]) == [1, 2, 3]
assert matrix.dot_v(m, [1, 2, 3]) == [2, 4, 6]
assert matrix.dot_m(i, i) == i
assert matrix.dot_m(m, m) == [[4, 0, 0], [0, 4, 0], [0, 0, 4]]
assert r == matrix.rotation_rad(math.pi/2, 1, 0, 0)
assert checkdiff(r, [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]])

# initial results
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
m = [
    [0.33482917221585295, 0.8711838511445769, -0.3590656248350022],
    [-0.66651590413407, 0.4883301324737331, 0.5632852130622015],
    [0.6660675453507625, 0.050718627969319086, 0.7441650662368666],
]
assert matrix.dot_m(A, B) == [[42, 36, 30], [96, 81, 66], [150, 126, 102]]
assert matrix.dot_m(B, A) == [[18, 24, 30], [54, 69, 84], [90, 114, 138]]
assert checkdiff(matrix.rotation_rad(5, 1, 2, 3), m)


import orbit


class Object:
    pass
b = Object()
b.mass = 1e30

a = random.uniform(1e07, 1e09)
e = random.uniform(0.1,  0.9)
o = orbit.Orbit(b, a, e)
assert (o.apoapsis + o.periapsis) / 2 - a < 1e-3

p = random.uniform(1e07, 1e10)
a = random.uniform(1e07, 1e09)
o = orbit.Orbit.from_period_apsis(b, p, a)
assert o.period - p < 1e-5
assert (o.apoapsis - a < 1e-3) or (o.periapsis - a) < 1e-3


import body

A = body.CelestialBody("A", 1e30)
o = orbit.Orbit(A, random.uniform(1e10, 1e11))
b_mass = random.uniform(1e07, 1e09)
b_radius = random.uniform(1e7, 1e8)
b_rot_period = random.uniform(1e3, 1e5)
B = body.CelestialBody("B", b_mass, b_radius, b_rot_period, o)
t = random.randint(1e6, 1e8)
assert round(B.str2time(B.time2str(t))) == t


import solar
import kerbol


def check_mass(b):
    assert b.mass > 1e9
    for s in b.satellites:
        check_mass(s)
check_mass(solar .Sun)
check_mass(kerbol.Kerbol)


import cfg
try:  # Python 2
    from StringIO import StringIO
except ImportError:  # Python 3
    from io import StringIO

assert cfg.parse(StringIO("""
PART
{
name = somepart
}
""")) == {'PART': {'name': 'somepart'}}

assert cfg.parse(StringIO("""
PART
{
MODULE
{
name = somemodule
}
}""")) == {'PART': {'MODULE': {'name': 'somemodule'}}}

part = cfg.parse(StringIO("""
PART
{
MODULE
{
name = first
}
MODULE
{
name = second
}
}
"""))
assert part == {'PART': {'MODULE': [{'name': 'first'}, {'name': 'second'}]}}

part = part['PART']
assert cfg.dic_get_group(part, 'MODULE', 'first') == {'name': 'first'}
