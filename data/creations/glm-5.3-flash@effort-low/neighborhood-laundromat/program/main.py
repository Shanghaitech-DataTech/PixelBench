from pixelbench_api import *

c = new_canvas(64, 64, background="#dfe7ee", name="laundromat")

# palette
WALL      = c.color("#dfe7ee")
WALL_LO   = c.color("#ccd6e0")
FLOOR     = c.color("#b6c0ca")
FLOOR_D   = c.color("#a2adb8")
BODY      = c.color("#eef3f7")
BODY_SH   = c.color("#d3dce4")
OUTLINE   = c.color("#5d6b78")
RING      = c.color("#93a5b4")
GLASS     = c.color("#3f5a6e")
GLASS_HI  = c.color("#6d8ea3")
PANEL     = c.color("#7c90a0")
LED       = c.color("#5ec98a")
FACE      = c.color("#ffffff")
HAND      = c.color("#333c44")
LIGHT     = c.color("#f4fbff")
BASKET    = c.color("#79c0e6")
BASKET_D  = c.color("#57a4cf")
CLOTH1    = c.color("#f2a6b8")
CLOTH2    = c.color("#f3df8c")
TOP       = c.color("#cfd8e0")
LEG       = c.color("#8794a1")
TOWEL     = c.color("#e9cbd9")
SHADOW    = c.color("#9fabb6")

# ---- room ----
c.rect(0, 0, 64, 44, WALL)
c.rect(0, 40, 64, 4, WALL_LO)          # wall base
c.rect(0, 44, 64, 20, FLOOR)
for fx in range(0, 64, 8):             # floor tile lines
    c.line(fx, 44, fx - 4, 63, FLOOR_D)
for fy in range(48, 64, 8):
    c.line(0, fy, 63, fy, FLOOR_D)
c.line(0, 43, 63, 43, SHADOW)

# ceiling fluorescent light (cool white)
c.rect(8, 1, 48, 2, LIGHT)
c.rect(10, 3, 44, 1, "#e6f2fa")

# ---- wall clock ----
c.circle(32, 9, 4, OUTLINE)
c.circle(32, 9, 3, FACE)
c.set(32, 9, HAND)
c.line(32, 9, 32, 6, HAND)   # minute
c.line(32, 9, 34, 9, HAND)   # hour

# ---- washing machine helper ----
def machine(x, y, w, h, r, dx, dy):
    c.rect(x, y, w, h, BODY)
    c.rect(x, y, 1, h, BODY_SH)                 # left shade
    c.rect(x, y, w, 1, BODY_SH)
    c.rect(x + w - 1, y, 1, h, OUTLINE)
    c.rect(x, y + h - 1, w, 1, OUTLINE)
    c.rect(x, y - 1, w, 1, OUTLINE)
    # control panel
    c.rect(x + 1, y + 1, w - 2, 2, PANEL)
    c.set(x + 2, y + 2, LED)
    # porthole door
    cx, cy = x + dx, y + dy
    c.circle(cx, cy, r + 1, RING)
    c.circle(cx, cy, r, GLASS)
    c.circle(cx - 1, cy - 1, r - 3, GLASS_HI) if r >= 3 else c.set(cx - 1, cy - 1, GLASS_HI)

# ---- back row (4 small machines, against wall) ----
for i in range(4):
    x = 2 + i * 11
    machine(x, 17, 10, 14, 3, x + 5, 25)
    c.line(x, 31, x + 9, 31, SHADOW)

# ---- front row (4 larger machines) ----
for i in range(4):
    x = 1 + i * 13
    machine(x, 33, 12, 18, 4, x + 6, 44)
    c.rect(x, 51, 12, 1, SHADOW)

# ---- laundry basket (front left) ----
c.rect(6, 52, 13, 9, BASKET)
c.rect(6, 52, 13, 1, BASKET_D)
c.rect(6, 60, 13, 1, BASKET_D)
c.rect(6, 52, 1, 9, BASKET_D)
c.rect(18, 52, 1, 9, BASKET_D)
# clothes overflowing
c.circle(9, 52, 2, CLOTH1)
c.circle(13, 51, 2, CLOTH2)
c.circle(16, 52, 2, CLOTH1)
c.set(11, 52, CLOTH2)
# basket rib lines
for yy in (55, 58):
    c.line(7, yy, 17, yy, BASKET_D)

# ---- folding table (front right) ----
c.rect(44, 46, 19, 2, TOP)
c.rect(44, 48, 19, 1, "#bfc9d2")
c.rect(45, 49, 1, 13, LEG)
c.rect(61, 49, 1, 13, LEG)
# folded towels on table
c.rect(48, 43, 7, 3, TOWEL)
c.rect(48, 43, 7, 1, "#f2dce7")
c.rect(56, 44, 5, 2, CLOTH2)
# table shadow on floor
c.line(44, 62, 63, 62, SHADOW)

print(c.stats_text())
finish(c)
