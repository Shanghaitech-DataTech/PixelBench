import math

# ---------------------------------------------------------------- palette
out = new_canvas(64, 64, name="output")

DARK  = out.color("#6e1206", "dark")     # scorched outer edge
RED   = out.color("#b7230f", "red")
ORED  = out.color("#e8541a", "ored")     # orange-red blast
ORNG  = out.color("#ff8a1f", "orange")
AMBER = out.color("#ffb52b", "amber")
YELL  = out.color("#ffe24f", "yellow")
PALE  = out.color("#fff8c4", "pale")
HOT   = out.color("#ffffff", "hot")

CX = CY = 15.5   # centre of a 32x32 frame cell


def blob(cv, r, color, lobes, lobe_r, phase=0.0, ring=0.85):
    """Cauliflower blob: a disc plus a rim of smaller discs."""
    cv.circle(round(CX), round(CY), int(r), color)
    for i in range(lobes):
        a = phase + 2.0 * math.pi * i / lobes
        cv.circle(round(CX + math.cos(a) * r * ring),
                  round(CY + math.sin(a) * r * ring), int(lobe_r), color)


def polar(a, d):
    """Cell-local point, clamped so nothing spills into the neighbouring frame."""
    x = max(0, min(31, round(CX + math.cos(a) * d)))
    y = max(0, min(31, round(CY + math.sin(a) * d)))
    return x, y


# ================================================ frame 1: yellow fireball core
f1 = new_canvas(32, 32, name="f1")

blob(f1, 8, ORNG,  7, 2, phase=0.20)
blob(f1, 7, AMBER, 6, 2, phase=0.95)
blob(f1, 5, YELL,  6, 2, phase=1.60, ring=0.9)
f1.circle(round(CX), round(CY), 3, PALE)
f1.circle(round(CX), round(CY), 1, HOT)
f1.set(14, 14, HOT)
f1.set(17, 17, PALE)

# flickering tongues of flame just off the rim
for a in (0.40, 1.50, 2.70, 3.80, 5.10):
    x0, y0 = polar(a, 8)
    x1, y1 = polar(a, 10)
    f1.line(x0, y0, x1, y1, AMBER)
    f1.set(x1, y1, YELL)

# first hints of outward motion
for a, d in ((0.9, 12), (2.4, 12), (4.0, 12), (5.5, 12)):
    f1.set(*polar(a, d), ORNG)

# ================================================ frame 2: expanding blast
f2 = new_canvas(32, 32, name="f2")

blob(f2, 11, DARK,  9, 3, phase=0.15)
blob(f2, 9,  RED,   8, 3, phase=0.60)
blob(f2, 7,  ORED,  7, 3, phase=1.00)
blob(f2, 5,  ORNG,  6, 2, phase=1.45)
blob(f2, 3,  AMBER, 5, 2, phase=0.30)
f2.circle(round(CX), round(CY), 2, YELL)
f2.set(15, 15, PALE)

# torn notches, so the silhouette is ragged rather than round
for a, d, r in ((0.45, 13, 1), (2.00, 14, 1), (3.60, 13, 1), (5.10, 14, 1)):
    f2.circle(*polar(a, d), r, None)

# cooling pockets inside the fireball
for a, d in ((1.3, 8), (2.8, 8), (4.4, 9), (5.9, 8)):
    f2.set(*polar(a, d), RED)

# sparks thrown clear of the blast front
sparks = [(0.00, 12, 3), (0.65, 11, 4), (1.25, 12, 3), (1.90, 11, 4),
          (2.55, 12, 3), (3.14, 12, 3), (3.80, 11, 4), (4.45, 12, 3),
          (5.05, 11, 4), (5.70, 12, 3)]
for a, start, length in sparks:
    x0, y0 = polar(a, start)
    x1, y1 = polar(a, start + length)
    f2.line(x0, y0, x1, y1, AMBER)
    f2.set(x1, y1, YELL)

# detached embers at the very edge of the cell
for a, d in ((0.35, 15), (1.57, 15), (2.90, 15), (4.20, 15), (4.71, 15), (5.90, 15)):
    f2.set(*polar(a, d), ORNG)
for a, d in ((0.95, 14), (2.30, 14), (3.45, 14), (5.40, 14)):
    f2.set(*polar(a, d), YELL)

# ================================================ assemble the 2-frame strip
out.blit(f1, 0, 16)
out.blit(f2, 32, 16)

view(out)
print(out.stats_text())
finish(out)
