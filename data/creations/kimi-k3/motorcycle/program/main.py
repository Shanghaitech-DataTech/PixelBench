import math

# ---- palette ----
TIRE   = "#111318"   # thick black tires
RIM    = "#7a808a"   # gray rim ring
RIMDK  = "#17181d"   # dark inside rim
SPOKE  = "#e6eaef"   # white spokes
HUB    = "#a9afb8"   # gray hub
HUBDK  = "#3a3e45"
SILVER = "#b9bfc8"   # silver metal (fork, frame)
SILVDK = "#7e848e"
FAIR   = "#3c4048"   # wide dark gray fairing
FAIRDK = "#2b2e35"
BODY   = "#17181d"   # black bodywork (tank, tail)
BODYHI = "#2a2d35"
RED    = "#d42a33"   # red accents
RED_DK = "#8a1c23"
ENG    = "#a2a8b1"   # round silver gray engine cover
ENGDK  = "#5f656e"
ENGLT  = "#ccd1d8"
CRANK  = "#20232a"
SCREEN = "#0d0e13"   # black windscreen
LIGHT  = "#f2f4f7"   # headlight

c = new_canvas(128, 128, None, name="moto")

# ---- wheels ----
def wheel(cx, cy):
    c.circle(cx, cy, 17, TIRE)               # thick tire
    c.circle(cx, cy, 12, RIM)                # gray rim ring
    c.circle(cx, cy, 11, RED, fill=False)    # red pinstripe
    c.circle(cx, cy, 10, RIMDK)              # dark inner
    for k in range(5):                       # white spokes
        a = math.radians(-90 + k * 72)
        x2 = round(cx + 10 * math.cos(a))
        y2 = round(cy + 10 * math.sin(a))
        c.line(cx, cy, x2, y2, SPOKE)
    c.circle(cx, cy, 4, HUB)                 # gray hub
    c.circle(cx, cy, 1, HUBDK)

wheel(34, 84)
wheel(96, 84)

# ---- swingarm (to rear hub) ----
c.line(57, 74, 35, 83, SILVER)
c.line(57, 76, 35, 85, SILVDK)
c.circle(56, 75, 2, SILVDK)

# ---- exhaust: low pipe + short muffler ----
c.line(70, 79, 52, 86, SILVDK)
c.poly([(43, 82), (51, 86), (51, 90), (43, 87)], ENG, fill=True)
c.poly([(43, 82), (45, 83), (45, 88), (43, 87)], CRANK, fill=True)

# ---- front fork: silver (drawn before fairing so it tucks behind) ----
c.line(95, 83, 88, 47, SILVER)
c.line(96, 83, 89, 46, SILVER)
c.line(97, 83, 90, 46, SILVDK)
c.line(98, 82, 91, 46, SILVDK)

# ---- silver tubular frame ----
c.line(82, 50, 66, 68, SILVER)
c.line(66, 68, 52, 72, SILVER)
c.line(52, 72, 49, 56, SILVER)
c.line(66, 68, 59, 54, SILVER)

# ---- engine ----
c.rect(50, 62, 24, 16, CRANK)                # crankcase block
c.circle(61, 71, 8, ENG)                     # round engine cover
c.circle(61, 71, 8, ENGDK, fill=False)
c.circle(61, 71, 5, ENGLT, fill=False)
for bx, by in ((61, 66), (61, 76), (56, 71), (66, 71)):
    c.set(bx, by, ENGDK)
c.set(61, 71, ENGDK)

# ---- tail: upswept, black ----
c.path("M 53 50 L 54 46 C 46 43 34 41 24 37 C 18 35 13 37 14 42 "
       "C 15 47 26 51 38 52 C 44 53 50 52 53 50 Z", BODY)
c.path("M 22 39 C 30 42 40 44 46 45", BODYHI, fill=False)   # top sheen

# ---- fairing: wide dark gray ----
c.path("M 58 54 C 66 45 80 41 91 44 C 102 47 109 52 111 59 "
       "C 112 66 107 72 98 75 C 87 79 73 79 65 74 C 59 70 56 62 58 54 Z", FAIR)
# lower shading
c.path("M 63 70 C 72 77 88 78 100 73 C 95 77 85 79 76 78 C 69 77 64 74 63 70 Z", FAIRDK)
# headlight
c.poly([(102, 55), (110, 58), (103, 63)], LIGHT, fill=True)

# ---- fuel tank: black ----
c.path("M 47 51 C 53 43 67 41 76 46 C 80 49 79 54 72 57 C 63 60 52 59 48 56 Z", BODY)
c.path("M 53 47 C 59 43 68 43 74 46", BODYHI, fill=False)

# ---- front fender ----
c.path("M 82 77 A 15 15 0 0 1 110 77", FAIR, fill=False)

# ---- handlebar + mirror ----
c.line(89, 46, 84, 44, BODY)
c.set(83, 44, BODY)
c.line(96, 45, 100, 39, BODY)
c.set(101, 38, BODY)
c.set(102, 39, BODY)

# ---- windscreen: small, black, tilted ----
c.poly([(91, 46), (81, 35), (84, 31), (95, 43)], SCREEN, fill=True)

# ---- red accents ----
c.path("M 64 71 C 76 77 94 75 105 67", RED, fill=False)   # fairing swoosh
c.line(100, 52, 106, 56, RED)                              # nose slash
c.line(21, 46, 47, 51, RED)                                # tail stripe
c.rect(11, 39, 4, 5, RED)                                  # tail light
c.rect(11, 39, 1, 5, RED_DK)

# ---- footpeg ----
c.line(48, 84, 53, 84, SILVER)
c.set(53, 83, SILVDK)

print(c.stats_text())
view(c)
finish(c)
