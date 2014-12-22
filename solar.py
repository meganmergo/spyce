import body
import orbit



"""Solar system

Definition of the major celestial bodies from our solar system
"""

# from https://en.wikipedia.org/wiki/List_of_gravitationally_rounded_objects_of_the_Solar_System and sublinks
# the information seems to be hard-coded IRL

# avoids having to manually convert to seconds
_h = 3600
_d = 86400.002

# primary star
Sun        = body.CelestialBody("Sun",       1.98855e30, 696342.0e3,   25.05      *_d)

# planets
Mercury    = body.CelestialBody("Mercury",   3.3022e23,    2439.7e3,   25.38      *_d, orbit.Orbit.from_deg(Sun,   57909050e3, 0.205631, 174.796, 6.34,  48.331,  29.124))
Venus      = body.CelestialBody("Venus",     4.8676e24,    6051.8e3, -243.0185    *_d, orbit.Orbit.from_deg(Sun,  108208000e3, 0.006773,  50.115, 2.19,  76.678,  55.186))
Earth      = body.CelestialBody("Earth",     5.9722e24,    6371.0e3,    0.99726968*_d, orbit.Orbit.from_deg(Sun,  149598261e3, 0.016711, 357.517, 1.58, 348.739, 114.208))
Mars       = body.CelestialBody("Mars",      6.4185e23,    3389.5e3,    1.025957  *_d, orbit.Orbit.from_deg(Sun,  227939100e3, 0.093315,  19.356, 1.67,  49.562, 286.537))
Jupiter    = body.CelestialBody("Jupiter",   1.8986e27,   69911.0e3,    9.925     *_h, orbit.Orbit.from_deg(Sun,  778547200e3, 0.048775,  18.818, 0.32, 100.492, 275.066))
Saturn     = body.CelestialBody("Saturn",    5.6846e26,   58232.0e3,   10.57      *_h, orbit.Orbit.from_deg(Sun, 1433449370e3, 0.055723, 320.347, 0.93, 113.643, 336.014))
Uranus     = body.CelestialBody("Uranus",    8.6810e25,   25362.0e3,    0.71833   *_d, orbit.Orbit.from_deg(Sun, 2870671400e3, 0.047220, 142.239, 1.02,  73.999,  96.999))
Neptune    = body.CelestialBody("Neptune",   1.0243e26,   24622.0e3,    0.6713    *_d, orbit.Orbit.from_deg(Sun, 4498542600e3, 0.008677, 259.886, 0.72, 131.783, 273.219))

# dwarf planets
Ceres      = body.CelestialBody("Ceres",      9.43e20,  476e3,  0.3781  *_d, orbit.Orbit.from_deg(Sun,  0.414e12, 0.075797,  10.557,  9.20,  80.328,   72.292))
Pluto      = body.CelestialBody("Pluto",     1.305e22, 1184e3, -6.387230*_d, orbit.Orbit.from_deg(Sun,  5.874e12, 0.244671,  14.860, 11.88, 110.286,  113.763))
Haumea     = body.CelestialBody("Haumea",    4.006e21, 1920e3,  0.163146*_d, orbit.Orbit.from_deg(Sun,  6.452e12, 0.19501,  202.67,  28.22, 121.10,   239.18))
Eris       = body.CelestialBody("Eris",      1.670e22, 1163e3, 25.9     *_h, orbit.Orbit.from_deg(Sun, 10.166e12, 0.437083, 203.216, 43.89,  36.031,  150.800))

# MOONS

# rocky (dwarf-)planets
Moon       = body.CelestialBody("Moon",   7.3477e22, 1737100, 0, orbit.Orbit.from_deg(Earth, 384399e3, 0.0549,  0,  5.145,        0, 0))
Phobos     = body.CelestialBody("Phobos", 1.0659e16, 11266.7, 0, orbit.Orbit.from_deg(Mars,    9376e3, 0.0151,  0,  26.04,        0, 0))
Deimos     = body.CelestialBody("Deimos", 1.4762e15,   6.2e3, 0, orbit.Orbit.from_deg(Mars,   23463e3, 0.00033, 0,  27.58,        0, 0))
Charon     = body.CelestialBody("Charon",   1.52e21,  2306e3, 0, orbit.Orbit.from_deg(Pluto, 19.571e3, 0.0,     0, 112.783, 223.046, 0))

# moons of gas giants are sorted in label order (discovery date)

# https://en.wikipedia.org/wiki/Moons_of_Jupiter#Table
Io         = body.CelestialBody("Io",          8931900e16,      3660.0e3/2, 0, orbit.Orbit.from_deg(Jupiter,   421700e3, 0.0041,  0,   0.050, 0, 0))
Europa     = body.CelestialBody("Europa",      4800000e16,      3121.6e3/2, 0, orbit.Orbit.from_deg(Jupiter,   671034e3, 0.0094,  0,   0.471, 0, 0))
Ganymede   = body.CelestialBody("Ganymede",   14819000e16,      5262.4e3/2, 0, orbit.Orbit.from_deg(Jupiter,  1070412e3, 0.0011,  0,   0.204, 0, 0))
Callisto   = body.CelestialBody("Callisto",   10759000e16,      4820.6e3/2, 0, orbit.Orbit.from_deg(Jupiter,  1882709e3, 0.0074,  0,   0.205, 0, 0))
Amalthea   = body.CelestialBody("Amalthea",        208e16,       250.0e3/2, 0, orbit.Orbit.from_deg(Jupiter,   181366e3, 0.0032,  0,   0.374, 0, 0))
Himalia    = body.CelestialBody("Himalia",         670e16,       170.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 11451971e3, 0.1513,  0,  30.486, 0, 0))
Elara      = body.CelestialBody("Elara",            89e16,        86.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 11778034e3, 0.1948,  0,  29.691, 0, 0))
Pasiphae   = body.CelestialBody("Pasiphae",         30e16,        60.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23609042e3, 0.3743,  0, 141.803, 0, 0))
Sinope     = body.CelestialBody("Sinope",            7.5e16,      38.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 24057865e3, 0.2750,  0, 153.778, 0, 0))
Lysithea   = body.CelestialBody("Lysithea",          6.3e16,      36.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 11740560e3, 0.1322,  0,  27.006, 0, 0))
Carme      = body.CelestialBody("Carme",            13e16,        46.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23197992e3, 0.2342,  0, 165.047, 0, 0))
Ananke     = body.CelestialBody("Ananke",            3.0e16,      28.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 21454952e3, 0.3445,  0, 151.564, 0, 0))
Leda       = body.CelestialBody("Leda",              0.6e16,      16.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 11187781e3, 0.1673,  0,  27.562, 0, 0))
Thebe      = body.CelestialBody("Thebe",            43e16,       116.0e3/2, 0, orbit.Orbit.from_deg(Jupiter,   221889e3, 0.0175,  0,   1.076, 0, 0))
Adrastea   = body.CelestialBody("Adrastea",          0.2e16,      20.0e3/2, 0, orbit.Orbit.from_deg(Jupiter,   128690e3, 0.0015,  0,   0.03,  0, 0))
Metis      = body.CelestialBody("Metis",             3.6e16,      60.0e3/2, 0, orbit.Orbit.from_deg(Jupiter,   127690e3, 0.00002, 0,   0.06,  0, 0))
Callirrhoe = body.CelestialBody("Callirrhoe",        0.087e16,     9.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23214986e3, 0.2582,  0, 139.849, 0, 0))
Themisto   = body.CelestialBody("Themisto",          0.069e16,     8.0e3/2, 0, orbit.Orbit.from_deg(Jupiter,  7393216e3, 0.2115,  0,  45.762, 0, 0))
Megaclite  = body.CelestialBody("Megaclite",         0.021e16,     5.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 24687239e3, 0.3077,  0, 150.398, 0, 0))
Taygete    = body.CelestialBody("Taygete",           0.016e16,     5.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 22438648e3, 0.3678,  0, 164.890, 0, 0))
Chaldene   = body.CelestialBody("Chaldene",          0.0075e16,    4.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 22713444e3, 0.2916,  0, 167.070, 0, 0))
Harpalyke  = body.CelestialBody("Harpalyke",         0.012e16,     4.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 21063814e3, 0.2440,  0, 147.223, 0, 0))
Kalyke     = body.CelestialBody("Kalyke",            0.019e16,     5.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23180773e3, 0.2139,  0, 165.505, 0, 0))
Iocaste    = body.CelestialBody("Iocaste",           0.019e16,     5.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 20722566e3, 0.2874,  0, 147.248, 0, 0))
Erinome    = body.CelestialBody("Erinome",           0.0045e16,    3.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 22986266e3, 0.2552,  0, 163.737, 0, 0))
Isonoe     = body.CelestialBody("Isonoe",            0.0075e16,    4.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23800647e3, 0.1775,  0, 165.127, 0, 0))
Praxidike  = body.CelestialBody("Praxidike",         0.043e16,     7.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 20823948e3, 0.1840,  0, 144.205, 0, 0))
Autonoe    = body.CelestialBody("Autonoe",           0.0090e16,    4.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 24264445e3, 0.3690,  0, 151.058, 0, 0))
Thyone     = body.CelestialBody("Thyone",            0.0090e16,    4.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 21405570e3, 0.2525,  0, 147.276, 0, 0))
Hermippe   = body.CelestialBody("Hermippe",          0.0090e16,    4.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 21182086e3, 0.2290,  0, 151.242, 0, 0))
Aitne      = body.CelestialBody("Aitne",             0.0045e16,    3.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 22285161e3, 0.3927,  0, 165.562, 0, 0))
Eurydome   = body.CelestialBody("Eurydome",          0.0045e16,    3.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23230858e3, 0.3769,  0, 149.324, 0, 0))
Euanthe    = body.CelestialBody("Euanthe",           0.0045e16,    3.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 20464854e3, 0.2000,  0, 143.409, 0, 0))
Euporie    = body.CelestialBody("Euporie",           0.0015e16,    2.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 19088434e3, 0.0960,  0, 144.694, 0, 0))
Orthosie   = body.CelestialBody("Orthosie",          0.0015e16,    2.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 20567971e3, 0.2433,  0, 142.366, 0, 0))
Sponde     = body.CelestialBody("Sponde",            0.0015e16,    2.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 24252627e3, 0.4431,  0, 154.372, 0, 0))
Kale       = body.CelestialBody("Kale",              0.0015e16,    2.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 22409207e3, 0.2011,  0, 165.372, 0, 0))
Pasithee   = body.CelestialBody("Pasithee",          0.0015e16,    2.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23307318e3, 0.3288,  0, 165.759, 0, 0))
Hegemone   = body.CelestialBody("Hegemone",          0.0045e16,    3.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23702511e3, 0.4077,  0, 152.506, 0, 0))
Mneme      = body.CelestialBody("Mneme",             0.0015e16,    2.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 21129786e3, 0.3169,  0, 149.732, 0, 0))
Aoede      = body.CelestialBody("Aoede",             0.0090e16,    4.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23044175e3, 0.6011,  0, 160.482, 0, 0))
Thelxinoe  = body.CelestialBody("Thelxinoe",         0.0015e16,    2.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 20453753e3, 0.2684,  0, 151.292, 0, 0))
Arche      = body.CelestialBody("Arche",             0.0045e16,    3.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23717051e3, 0.1492,  0, 164.587, 0, 0))
Kallichore = body.CelestialBody("Kallichore",        0.0015e16,    2.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23111823e3, 0.2041,  0, 164.605, 0, 0))
Helike     = body.CelestialBody("Helike",            0.0090e16,    4.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 20540266e3, 0.1374,  0, 154.586, 0, 0))
Carpo      = body.CelestialBody("Carpo",             0.0045e16,    3.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 17144873e3, 0.2735,  0,  56.001, 0, 0))
Eukelade   = body.CelestialBody("Eukelade",          0.0090e16,    4.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23483694e3, 0.2828,  0, 163.996, 0, 0))
Cyllene    = body.CelestialBody("Cyllene",           0.0015e16,    2.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23396269e3, 0.4115,  0, 140.148, 0, 0))
Kore       = body.CelestialBody("Kore",              0.0015e16,    2.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 23345093e3, 0.1951,  0, 137.371, 0, 0))
Herse      = body.CelestialBody("Herse",             0.0015e16,    2.0e3/2, 0, orbit.Orbit.from_deg(Jupiter, 22134306e3, 0.2379,  0, 162.490, 0, 0))

# https://en.wikipedia.org/wiki/Moons_of_Saturn#Confirmed_moons
Mimas      = body.CelestialBody("Mimas",          3749.3e16,     396.4e3/2, 0, orbit.Orbit.from_deg(Saturn,   185404, 0.0202,   0,    1.566,  0, 0))
Enceladus  = body.CelestialBody("Enceladus",     10802.2e16,     504.2e3/2, 0, orbit.Orbit.from_deg(Saturn,   237950, 0.0047,   0,    0.010,  0, 0))
Tethys     = body.CelestialBody("Tethys",        61744.9e16,    1062.0e3/2, 0, orbit.Orbit.from_deg(Saturn,   294619, 0.0001,   0,    0.168,  0, 0))
Dione      = body.CelestialBody("Dione",        109545.2e16,    1128.8e3/2, 0, orbit.Orbit.from_deg(Saturn,   377396, 0.0022,   0,    0.002,  0, 0))
Rhea       = body.CelestialBody("Rhea",         230651.8e16,    1527.0e3/2, 0, orbit.Orbit.from_deg(Saturn,   527108, 0.000258, 0,    0.327,  0, 0))
Titan      = body.CelestialBody("Titan",      13452000.0e16,    5131.0e3/2, 0, orbit.Orbit.from_deg(Saturn,  1221930, 0.0288,   0,    0.3485, 0, 0))
Hyperion   = body.CelestialBody("Hyperion",        562.0e16,     270.0e3/2, 0, orbit.Orbit.from_deg(Saturn,  1481010, 0.123006, 0,    0.568,  0, 0))
Iapetus    = body.CelestialBody("Iapetus",      180563.5e16,    1468.6e3/2, 0, orbit.Orbit.from_deg(Saturn,  3560819, 0.028613, 0,   15.47,   0, 0))
Phoebe     = body.CelestialBody("Phoebe",          829.2e16,     213.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 12869700, 0.156242, 0,  173.047,  0, 0))
Janus      = body.CelestialBody("Janus",           189.75e16,    179.0e3/2, 0, orbit.Orbit.from_deg(Saturn,   151472, 0.00068,  0,    0.165,  0, 0))
Epimetheus = body.CelestialBody("Epimetheus",       52.66e16,    116.2e3/2, 0, orbit.Orbit.from_deg(Saturn,   151422, 0.00098,  0,    0.335,  0, 0))
Helene     = body.CelestialBody("Helene",            2.446e16,    35.2e3/2, 0, orbit.Orbit.from_deg(Saturn,   377396, 0.0022,   0,    0.212,  0, 0))
Telesto    = body.CelestialBody("Telesto",           0.941e16,    24.8e3/2, 0, orbit.Orbit.from_deg(Saturn,   294619, 0.000,    0,    1.158,  0, 0))
Calypso    = body.CelestialBody("Calypso",           0.63e16,     21.4e3/2, 0, orbit.Orbit.from_deg(Saturn,   294619, 0.000,    0,    1.473,  0, 0))
Atlas      = body.CelestialBody("Atlas",             0.66e16,     30.2e3/2, 0, orbit.Orbit.from_deg(Saturn,   137670, 0.0012,   0,    0.003,  0, 0))
Prometheus = body.CelestialBody("Prometheus",       15.95e16,     86.2e3/2, 0, orbit.Orbit.from_deg(Saturn,   139380, 0.0022,   0,    0.008,  0, 0))
Pandora    = body.CelestialBody("Pandora",          13.71e16,     81.4e3/2, 0, orbit.Orbit.from_deg(Saturn,   141720, 0.0042,   0,    0.050,  0, 0))
Pan        = body.CelestialBody("Pan",               0.495e16,    28.2e3/2, 0, orbit.Orbit.from_deg(Saturn,   133584, 0.000035, 0,    0.001,  0, 0))
Ymir       = body.CelestialBody("Ymir",              0.397e16,    18.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 22429673, 0.3349,   0,  172.143,  0, 0))
Paaliaq    = body.CelestialBody("Paaliaq",           0.725e16,    22.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 15103400, 0.3631,   0,   46.151,  0, 0))
Tarvos     = body.CelestialBody("Tarvos",            0.23e16,     15.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 18562800, 0.5305,   0,   37.679,  0, 0))
Ijiraq     = body.CelestialBody("Ijiraq",            0.118e16,    12.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 11355316, 0.3161,   0,   50.212,  0, 0))
Suttungr   = body.CelestialBody("Suttungr",          0.023e16,     7.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 19579000, 0.131,    0,  174.321,  0, 0))
Kiviuq     = body.CelestialBody("Kiviuq",            0.279e16,    16.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 11294800, 0.3288,   0,   49.087,  0, 0))
Mundilfari = body.CelestialBody("Mundilfari",        0.023e16,     7.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 18725800, 0.198,    0,  169.378,  0, 0))
Albiorix   = body.CelestialBody("Albiorix",          2.23e16,     32.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 16266700, 0.477,    0,   38.042,  0, 0))
Skathi     = body.CelestialBody("Skathi",            0.035e16,     8.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 15672500, 0.246,    0,  149.084,  0, 0))
Erriapus   = body.CelestialBody("Erriapus",          0.068e16,    10.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 17236900, 0.4724,   0,   38.109,  0, 0))
Siarnaq    = body.CelestialBody("Siarnaq",           4.35e16,     40.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 17776600, 0.24961,  0,   45.798,  0, 0))
Thrymr     = body.CelestialBody("Thrymr",            0.023e16,     7.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 20278100, 0.453,    0,  174.524,  0, 0))
Narvi      = body.CelestialBody("Narvi",             0.023e16,     7.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 19395200, 0.320,    0,  137.292,  0, 0))
Methone    = body.CelestialBody("Methone",           0.002e16,     3.2e3/2, 0, orbit.Orbit.from_deg(Saturn,   194440, 0.0001,   0,    0.007,  0, 0))
Pallene    = body.CelestialBody("Pallene",           0.005e16,     5.0e3/2, 0, orbit.Orbit.from_deg(Saturn,   212280, 0.0040,   0,    0.181,  0, 0))
Polydeuces = body.CelestialBody("Polydeuces",        0.003e16,     2.6e3/2, 0, orbit.Orbit.from_deg(Saturn,   377396, 0.0192,   0,    0.177,  0, 0))
Daphnis    = body.CelestialBody("Daphnis",           0.0084e16,    7.6e3/2, 0, orbit.Orbit.from_deg(Saturn,   136505, 0.,       0,    0,      0, 0))
Aegir      = body.CelestialBody("Aegir",             0.015e16,     6.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 20482900, 0.237,    0,  167.425,  0, 0))
Bebhionn   = body.CelestialBody("Bebhionn",          0.015e16,     6.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 17153520, 0.333,    0,   40.484,  0, 0))
Bergelmir  = body.CelestialBody("Bergelmir",         0.015e16,     6.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 19104000, 0.152,    0,  157.384,  0, 0))
Bestla     = body.CelestialBody("Bestla",            0.023e16,     7.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 20570000, 0.5145,   0,  147.395,  0, 0))
Farbauti   = body.CelestialBody("Farbauti",          0.009e16,     5.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 19984800, 0.209,    0,  158.361,  0, 0))
Fenrir     = body.CelestialBody("Fenrir",            0.005e16,     4.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 21930644, 0.131,    0,  162.832,  0, 0))
Fornjot    = body.CelestialBody("Fornjot",           0.015e16,     6.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 24504879, 0.186,    0,  167.886,  0, 0))
Hati       = body.CelestialBody("Hati",              0.015e16,     6.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 19709300, 0.291,    0,  163.131,  0, 0))
Hyrrokkin  = body.CelestialBody("Hyrrokkin",         0.035e16,     8.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 19168300, 0.3604,   0,  153.272,  0, 0))
Kari       = body.CelestialBody("Kari",              0.023e16,     7.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 22321200, 0.3405,   0,  148.384,  0, 0))
Loge       = body.CelestialBody("Loge",              0.015e16,     6.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 22984322, 0.1390,   0,  166.539,  0, 0))
Skoll      = body.CelestialBody("Skoll",             0.015e16,     6.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 17473800, 0.418,    0,  155.624,  0, 0))
Surtur     = body.CelestialBody("Surtur",            0.015e16,     6.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 22288916, 0.3680,   0,  166.918,  0, 0))
Anthe      = body.CelestialBody("Anthe",             0.0007e16,    1.0e3/2, 0, orbit.Orbit.from_deg(Saturn,   197700, 0.0001,   0,    0.1,    0, 0))
Jarnsaxa   = body.CelestialBody("Jarnsaxa",          0.015e16,     6.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 18556900, 0.1918,   0,  162.861,  0, 0))
Greip      = body.CelestialBody("Greip",             0.015e16,     6.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 18065700, 0.3735,   0,  182.666,  0, 0))
Tarqeq     = body.CelestialBody("Tarqeq",            0.023e16,     7.0e3/2, 0, orbit.Orbit.from_deg(Saturn, 17910600, 0.1081,   0,   49.904,  0, 0))
Aegaeon    = body.CelestialBody("Aegaeon",           0.0001e16,    0.5e3/2, 0, orbit.Orbit.from_deg(Saturn,   167500, 0.0002,   0,    0.001,  0, 0))

# https://en.wikipedia.org/wiki/Moons_of_Uranus#List_of_Moons_of_Uranus
Ariel      = body.CelestialBody("Ariel",        135300.0e16,    1157.8e3/2, 0, orbit.Orbit.from_deg(Uranus,   191020e3, 0.0012,  0,   0.260))
Umbriel    = body.CelestialBody("Umbriel",      117200.0e16,    1169.4e3/2, 0, orbit.Orbit.from_deg(Uranus,   266300e3, 0.0039,  0,   0.205))
Titania    = body.CelestialBody("Titania",      352700.0e16,    1576.8e3/2, 0, orbit.Orbit.from_deg(Uranus,   435910e3, 0.0011,  0,   0.340))
Oberon     = body.CelestialBody("Oberon",       301400.0e16,    1522.8e3/2, 0, orbit.Orbit.from_deg(Uranus,   583520e3, 0.0014,  0,   0.052))
Miranda    = body.CelestialBody("Miranda",        6590.0e16,     471.6e3/2, 0, orbit.Orbit.from_deg(Uranus,   129390e3, 0.0013,  0,   4.232))
Cordelia   = body.CelestialBody("Cordelia",          4.4e16,      40.0e3/2, 0, orbit.Orbit.from_deg(Uranus,    49770e3, 0.00026, 0,   0.08479))
Ophelia    = body.CelestialBody("Ophelia",           5.3e16,      43.0e3/2, 0, orbit.Orbit.from_deg(Uranus,    53790e3, 0.00992, 0,   0.1036))
Bianca     = body.CelestialBody("Bianca",            9.2e16,      51.0e3/2, 0, orbit.Orbit.from_deg(Uranus,    59170e3, 0.00092, 0,   0.193))
Cressida   = body.CelestialBody("Cressida",         34.0e16,      80.0e3/2, 0, orbit.Orbit.from_deg(Uranus,    61780e3, 0.00036, 0,   0.006))
Desdemona  = body.CelestialBody("Desdemona",        18.0e16,      64.0e3/2, 0, orbit.Orbit.from_deg(Uranus,    62680e3, 0.00013, 0,   0.11125))
Juliet     = body.CelestialBody("Juliet",           56.0e16,      94.0e3/2, 0, orbit.Orbit.from_deg(Uranus,    64350e3, 0.00066, 0,   0.065))
Portia     = body.CelestialBody("Portia",          170.0e16,     135.0e3/2, 0, orbit.Orbit.from_deg(Uranus,    66090e3, 0.00005, 0,   0.059))
Rosalind   = body.CelestialBody("Rosalind",         25.0e16,      72.0e3/2, 0, orbit.Orbit.from_deg(Uranus,    69940e3, 0.00011, 0,   0.279))
Belinda    = body.CelestialBody("Belinda",          49.0e16,      90.0e3/2, 0, orbit.Orbit.from_deg(Uranus,    75260e3, 0.00007, 0,   0.031))
Puck       = body.CelestialBody("Puck",            290.0e16,     162.0e3/2, 0, orbit.Orbit.from_deg(Uranus,    86010e3, 0.00012, 0,   0.3192))
Caliban    = body.CelestialBody("Caliban",          25.0e16,      72.0e3/2, 0, orbit.Orbit.from_deg(Uranus,  7230000e3, 0.1587,  0, 139.885))
Sycorax    = body.CelestialBody("Sycorax",         230.0e16,     150.0e3/2, 0, orbit.Orbit.from_deg(Uranus, 12179000e3, 0.5224,  0, 152.456))
Prospero   = body.CelestialBody("Prospero",          8.5e16,      50.0e3/2, 0, orbit.Orbit.from_deg(Uranus, 16418000e3, 0.4448,  0, 146.017))
Setebos    = body.CelestialBody("Setebos",           7.5e16,      48.0e3/2, 0, orbit.Orbit.from_deg(Uranus, 17459000e3, 0.5914,  0, 145.883))
Stephano   = body.CelestialBody("Stephano",          2.2e16,      32.0e3/2, 0, orbit.Orbit.from_deg(Uranus,  8002000e3, 0.2292,  0, 141.873))
Trinculo   = body.CelestialBody("Trinculo",          0.39e16,     18.0e3/2, 0, orbit.Orbit.from_deg(Uranus,  8571000e3, 0.2200,  0, 166.252))
Francisco  = body.CelestialBody("Francisco",         0.72e16,     22.0e3/2, 0, orbit.Orbit.from_deg(Uranus,  4276000e3, 0.1459,  0, 147.459))
Margaret   = body.CelestialBody("Margaret",          0.54e16,     20.0e3/2, 0, orbit.Orbit.from_deg(Uranus, 14345000e3, 0.6608,  0,  51.455))
Ferdinand  = body.CelestialBody("Ferdinand",         0.53e16,     20.0e3/2, 0, orbit.Orbit.from_deg(Uranus, 20900000e3, 0.3682,  0, 167.346))
Perdita    = body.CelestialBody("Perdita",           1.80e16,     30.0e3/2, 0, orbit.Orbit.from_deg(Uranus,    76400e3, 0.0012,  0,   0.000))
Mab        = body.CelestialBody("Mab",               1.00e16,     25.0e3/2, 0, orbit.Orbit.from_deg(Uranus,    97700e3, 0.0025,  0,   0.1335))
Cupid      = body.CelestialBody("Cupid",             0.38e16,     18.0e3/2, 0, orbit.Orbit.from_deg(Uranus,    74800e3, 0.0013,  0,   0.1))

# https://en.wikipedia.org/wiki/Moons_of_Neptune#Table
Triton     = body.CelestialBody("Triton",       140800e16,      2705.2e3/2, 0, orbit.Orbit.from_deg(Neptune,  354.759e6,  0.0000, 0, 129.812, 0, 0))
Nereid     = body.CelestialBody("Nereid",         2700e16,       340.0e3/2, 0, orbit.Orbit.from_deg(Neptune, 5513.787e6,  0.7507, 0,   7.090, 0, 0))
Naiad      = body.CelestialBody("Naiad",            19e16,        66.0e3/2, 0, orbit.Orbit.from_deg(Neptune,   48.227e6,  0.0004, 0,   4.75,  0, 0))
Thalassa   = body.CelestialBody("Thalassa",         35e16,        82.0e3/2, 0, orbit.Orbit.from_deg(Neptune,   50.075e6,  0.0002, 0,   0.21,  0, 0))
Despina    = body.CelestialBody("Despina",         210e16,       150.0e3/2, 0, orbit.Orbit.from_deg(Neptune,   52.526e6,  0.0002, 0,   0.06,  0, 0))
Galatea    = body.CelestialBody("Galatea",         375e16,       176.0e3/2, 0, orbit.Orbit.from_deg(Neptune,   61.953e6,  0.0000, 0,   0.06,  0, 0))
Larissa    = body.CelestialBody("Larissa",         495e16,       194.0e3/2, 0, orbit.Orbit.from_deg(Neptune,   73.548e6,  0.0014, 0,   0.205, 0, 0))
Proteus    = body.CelestialBody("Proteus",        5035e16,       420.0e3/2, 0, orbit.Orbit.from_deg(Neptune,  117.647e6,  0.0005, 0,   0.026, 0, 0))
Halimede   = body.CelestialBody("Halimede",         16e16,        62.0e3/2, 0, orbit.Orbit.from_deg(Neptune,   16.611e9,  0.2646, 0, 112.712, 0, 0))
Psamathe   = body.CelestialBody("Psamathe",          4e16,        40.0e3/2, 0, orbit.Orbit.from_deg(Neptune,   49.096e12, 0.3809, 0, 126.312, 0, 0))
Sao        = body.CelestialBody("Sao",               6e16,        44.0e3/2, 0, orbit.Orbit.from_deg(Neptune,   22.228e9,  0.1365, 0,  53.483, 0, 0))
Laomedeia  = body.CelestialBody("Laomedeia",         5e16,        42.0e3/2, 0, orbit.Orbit.from_deg(Neptune,   23.567e12, 0.3969, 0,  37.874, 0, 0))
Neso       = body.CelestialBody("Neso",             15e16,        60.0e3/2, 0, orbit.Orbit.from_deg(Neptune,   49.285e12, 0.5714, 0, 136.439, 0, 0))
