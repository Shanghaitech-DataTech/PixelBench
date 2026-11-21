from pixelbench_api import *

c = new_canvas(32, 32, name="factory")

OUTLINE = "#23232b"
BRICK = "#b0482f"
BRICK_D = "#8f3a24"
MORTAR = "#6e2c1b"
ROOF = "#565661"
ROOF_D = "#3a3a43"
ROOF_HI = "#6f6f7b"
CHIM = "#c9c9d1"
CHIM_D = "#8b8b95"
CHIM_HI = "#eaeaf0"
DOOR = "#191920"
DOOR_L = "#2e2e38"
WIND = "#f2d97c"
WIND_D = "#c9a94e"
VENT = "#34343e"
VENT_D = "#23232b"
SMOKE_A = "#d6d6d6"
SMOKE_B = "#a2a2aa"
SHADOW = (0, 0, 0, 80)

# --- ground shadow ---
c.rect(5, 29, 22, 1, SHADOW)

# --- brick walls ---
c.rect(6, 14, 20, 15, BRICK)
c.line(6, 14, 25, 14, BRICK_D)          # shadow cast by roof overhang
for y in (16, 21, 25):                  # horizontal mortar courses
    c.line(7, y, 24, y, MORTAR)
for (x0, y0, y1) in ((12, 14, 15), (19, 14, 15),
                     (13, 17, 20), (11, 22, 24), (16, 22, 24)):
    c.line(x0, y0, x0, y1, MORTAR)

# --- flat roof ---
c.rect(5, 12, 22, 2, ROOF)
c.rect(5, 13, 22, 1, ROOF_D)
c.line(6, 12, 25, 12, ROOF_HI)

# --- chimney ---
c.rect(10, 5, 4, 7, CHIM)
c.line(10, 5, 10, 11, CHIM_HI)
c.line(13, 5, 13, 11, CHIM_D)
c.rect(9, 4, 6, 1, CHIM_D)

# --- roof vents ---
c.rect(17, 10, 3, 2, VENT)
c.rect(18, 11, 1, 1, CHIM_D)
c.rect(21, 10, 3, 2, VENT)
c.rect(22, 11, 1, 1, CHIM_D)

# --- loading door ---
c.rect(13, 23, 6, 6, DOOR)
c.line(13, 22, 18, 22, MORTAR)
c.line(14, 24, 14, 27, DOOR_L)
c.line(17, 24, 17, 27, DOOR_L)

# --- windows ---
for fx in (8, 19):
    c.rect(fx, 17, 3, 3, WIND)
    c.rect(fx, 22, 3, 3, WIND)
    c.line(fx + 1, 17, fx + 1, 19, WIND_D)
    c.line(fx + 1, 22, fx + 1, 24, WIND_D)

# --- clean dark silhouette ---
c.outline(OUTLINE)

# --- smoke on its own layer (so outline stays clean) ---
s = new_canvas(32, 32, name="smoke")
s.rect(9, 0, 6, 1, SMOKE_B)
s.rect(8, 1, 8, 1, SMOKE_B)
s.rect(9, 2, 6, 1, SMOKE_B)
s.rect(10, 3, 4, 1, SMOKE_B)
s.set(10, 0, SMOKE_A)
s.set(13, 0, SMOKE_A)
s.set(9, 1, SMOKE_A)
s.set(11, 1, SMOKE_A)
s.set(14, 1, SMOKE_A)
s.set(11, 2, SMOKE_A)
s.set(13, 2, SMOKE_A)

result = flatten([c, s], name="rts-factory-icon")

print(result.stats_text())
finish(result)
