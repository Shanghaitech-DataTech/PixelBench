from pixelbench_api import *

c = new_canvas(64, 64, background="#10152a", name="store")

NIGHT   = c.color("#10152a", "night")
NIGHT2  = c.color("#181f3a", "night2")
WALL    = c.color("#3d3f55", "wall")
WALL_D  = c.color("#2c2e40", "wall_dark")
ROOF    = c.color("#232433", "roof")
SIGN    = c.color("#2a2c40", "sign")
SIGNLT  = c.color("#ffcf6e", "sign_light")
AWN_A   = c.color("#a83240", "awning_red")
AWN_B   = c.color("#e6ddca", "awning_cream")
WIN     = c.color("#ffd98a", "window")
WIN_HI  = c.color("#fff3c4", "window_hi")
WIN_SH  = c.color("#c99a4e", "window_shade")
FRAME   = c.color("#1c1d2b", "frame")
DOOR_G  = c.color("#ffdf9e", "door_glass")
GROUND  = c.color("#22253a", "ground")
WALK    = c.color("#2c3049", "walk")
PUDDLE  = c.color("#33436b", "puddle")
REFL    = c.color("#d9b96e", "reflection")
RAIN    = c.color("#46588c", "rain")
COAT    = c.color("#e8b830", "raincoat")
COAT_D  = c.color("#b8891f", "coat_dark")
BOOTS   = c.color("#1a1a26", "boots")
UMB_R   = c.color("#c04050", "umb_red")
UMB_B   = c.color("#3a6ab0", "umb_blue")
BIKE    = c.color("#8f92a8", "bike")
TIRE    = c.color("#191a24", "tire")
SKIN    = c.color("#d8a878", "skin")

# --- sky gradient ---
c.rect(0, 0, 64, 20, NIGHT)
c.rect(0, 20, 64, 28, NIGHT2)

# --- building ---
c.rect(18, 6, 46, 42, WALL)          # main wall
c.rect(18, 6, 46, 3, ROOF)           # roof cap
c.rect(18, 9, 46, 5, SIGN)           # sign band
for sx in range(21, 62, 6):          # sign lights (no text)
    c.rect(sx, 11, 3, 1, SIGNLT)
c.rect(18, 14, 46, 1, WALL_D)

# --- awning (striped, scalloped) ---
for x in range(18, 64):
    col = AWN_A if ((x - 18) // 4) % 2 == 0 else AWN_B
    c.line(x, 15, x, 19, col)
    if (x - 18) % 4 == 3:
        c.set(x, 20, col)

# --- windows ---
def window(x0, x1, y0=22, y1=36):
    c.rect(x0, y0, x1 - x0, y1 - y0, WIN)
    c.rect(x0, y0, x1 - x0, 3, WIN_HI)              # bright top
    c.rect(x0, y1 - 6, x1 - x0, 6, WIN_SH)          # lower shade
    # interior shelf silhouettes
    c.rect(x0 + 2, y0 + 6, (x1 - x0) - 4, 1, WIN_SH)
    c.rect(x0 + 2, y0 + 10, (x1 - x0) - 4, 1, WIN_SH)
    # mullions
    for mx in range(x0 + 5, x1 - 1, 6):
        c.line(mx, y0, mx, y1 - 1, FRAME)
    c.rect(x0, y0, x1 - x0, 1, FRAME)
    c.rect(x0, y1 - 1, x1 - x0, 1, FRAME)

window(20, 36)
window(50, 63)

# --- door ---
c.rect(38, 22, 10, 24, FRAME)
c.rect(39, 23, 8, 15, DOOR_G)
c.line(42, 23, 42, 37, FRAME)                       # glass split
c.rect(39, 39, 8, 6, WALL_D)                        # door base
c.set(45, 39, WIN_HI)                               # handle

# --- wall glow around openings (dither) ---
GLOW = c.color("#6b5f45", "glow")
for gx in range(18, 64):
    for gy in range(15, 44):
        if c.get(gx, gy) == 0 and (gx + gy) % 3 == 0:
            if 16 <= gx <= 40 or 48 <= gx <= 63:
                c.set(gx, gy, GLOW)

# --- ground ---
c.rect(0, 46, 64, 18, GROUND)
c.rect(0, 46, 64, 3, WALK)
c.line(0, 49, 64, 49, c.color("#191c2e", "walk_edge"))

# --- puddles with reflections ---
def puddle(cx, cy, rx, ry):
    c.ellipse(cx, cy, rx, ry, PUDDLE)

puddle(11, 55, 8, 2)
puddle(31, 59, 11, 2)
puddle(53, 56, 9, 2)
# light reflections under windows/door
for x in range(22, 35):
    if (x + 0) % 2 == 0:
        c.line(x, 53, x, 57, REFL)
for x in range(39, 48):
    if x % 2 == 0:
        c.line(x, 50, x, 56, REFL)
for x in range(51, 62):
    if x % 2 == 1:
        c.line(x, 54, x, 58, REFL)
c.set(31, 59, WIN_HI); c.set(30, 59, REFL)

# --- umbrella rack by the door ---
c.rect(49, 40, 5, 6, c.color("#3a3c52", "rack"))
c.rect(49, 40, 5, 1, c.color("#4a4c64", "rack_top"))
c.line(50, 34, 50, 40, UMB_R)      # umbrella shafts/handles
c.line(52, 33, 52, 40, UMB_B)
c.line(54, 35, 54, 40, COAT_D)
c.set(50, 33, UMB_R); c.set(52, 32, UMB_B); c.set(54, 34, COAT_D)

# --- bicycle parked at left ---
def wheel(cx, cy, r):
    c.circle(cx, cy, r, TIRE, fill=False)
    c.set(cx, cy, BIKE)
wheel(6, 44, 3)
wheel(15, 44, 3)
c.line(6, 44, 10, 40, BIKE)
c.line(10, 40, 15, 44, BIKE)
c.line(10, 40, 10, 38, BIKE)        # handlebar stem
c.line(9, 38, 12, 38, BIKE)
c.line(9, 41, 12, 44, BIKE)         # seat tube / frame
c.set(9, 40, BIKE)

# --- person in raincoat entering ---
c.rect(41, 27, 5, 12, COAT)         # coat body
c.rect(41, 25, 5, 3, COAT)          # hood
c.set(43, 27, COAT_D)               # hood shading
c.line(41, 39, 42, 44, c.color("#2a2a3a", "pants"))
c.line(44, 39, 45, 44, c.color("#2a2a3a", "pants2"))
c.rect(41, 44, 2, 2, BOOTS)
c.rect(44, 44, 2, 2, BOOTS)
c.line(40, 29, 40, 34, COAT_D)      # arm
c.line(46, 29, 46, 33, COAT_D)
c.set(43, 26, SKIN)

# --- rain streaks ---
import random
random.seed(7)
for i in range(70):
    x = random.randint(0, 63)
    y = random.randint(0, 60)
    c.set(x, y, RAIN)
    if random.random() < 0.7:
        nx, ny = x - 1, y + 1
        if 0 <= nx < 64 and 0 <= ny < 64:
            c.set(nx, ny, RAIN)

print(c.stats_text())
finish(c)
