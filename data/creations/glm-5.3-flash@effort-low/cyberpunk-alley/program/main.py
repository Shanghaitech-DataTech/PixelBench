from pixelbench_api import *

c = new_canvas(128, 128, background="#07070f", name="cyberpunk-alley")

# ---------- palette ----------
BG      = c.color("#07070f")
WALL_L  = c.color("#151522")
WALL_R  = c.color("#181826")
WALL_D  = c.color("#10101b")
EDGE    = c.color("#232338")
GROUND  = c.color("#0c0c15")
GROUND2 = c.color("#11111c")
MAG     = c.color("#ff2fb0")
MAG_D   = c.color("#7a1856")
CYN     = c.color("#2ff0ff")
CYN_D   = c.color("#0f6b78")
YEL     = c.color("#ffd23f")
YEL_D   = c.color("#7a641c")
PNK     = c.color("#ff5c7a")
PNK_D   = c.color("#7a2c3c")
PUR     = c.color("#8a3fff")
SIL     = c.color("#04040a")
RIM     = c.color("#59d9ff")
WARM    = c.color("#ffb45c")
WARM_D  = c.color("#5c3a1c")
WHITE   = c.color("#e8f4ff")
HAZE    = c.color("#1a1430")

# ---------- sky / haze ----------
c.rect(0, 0, 128, 24, "#0a0a16")
c.rect(0, 18, 128, 6, HAZE)

# ---------- buildings ----------
c.rect(0, 0, 44, 94, WALL_L)        # left wall
c.rect(86, 0, 42, 94, WALL_R)       # right wall
c.rect(44, 22, 42, 72, WALL_D)      # back wall
c.rect(43, 0, 2, 94, EDGE)          # corner edges
c.rect(84, 0, 2, 94, EDGE)

# window grids on side walls (dim, some lit)
import random
random.seed(7)
for wy in range(8, 88, 12):
    for wx in range(4, 40, 9):
        col = "#1e1e30"
        r = random.random()
        if r < 0.12: col = "#3a2f18"
        elif r < 0.2: col = "#16323a"
        c.rect(wx, wy, 5, 6, col)
for wy in range(6, 88, 12):
    for wx in range(90, 126, 9):
        col = "#202032"
        r = random.random()
        if r < 0.1: col = "#3a2f18"
        elif r < 0.16: col = "#16323a"
        c.rect(wx, wy, 5, 6, col)

# pipes on left wall
c.rect(18, 0, 2, 94, "#1c1c2c")
c.rect(21, 0, 1, 94, "#242438")
for py in range(10, 94, 22):
    c.rect(17, py, 6, 2, "#26263a")

# back wall details: doorway with warm light
c.rect(58, 58, 13, 36, "#0a0a12")
c.rect(60, 60, 9, 34, WARM_D)
c.rect(61, 62, 7, 32, WARM)
c.rect(62, 64, 5, 30, "#ffdca0")
# small cyan sign above door
c.rect(56, 48, 17, 7, "#062026")
c.rect(57, 49, 15, 5, CYN_D)
c.text(58, 50, "24H", CYN, font="5x7")

# AC boxes on right wall
c.rect(96, 30, 10, 7, "#20202f")
c.rect(108, 52, 9, 6, "#20202f")

# ---------- ground ----------
c.rect(0, 94, 128, 34, GROUND)
# perspective seams
for x in range(0, 128, 16):
    c.line(x, 94, 40 + (x - 40) // 2 + 20, 127, "#08080f")
c.rect(0, 94, 128, 2, "#141420")

# ---------- neon signs ----------
def glowbox(x, y, w, h, dim, bright):
    c.rect(x - 1, y - 1, w + 2, h + 2, dim)
    c.rect(x, y, w, h, bright)

# left vertical magenta sign (kanji)
glowbox(5, 16, 12, 44, MAG_D, "#3a0a28")
c.rect(6, 17, 10, 42, MAG_D)
for ch, yy in zip("電気街", (19, 30, 41)):
    c.text(7, yy, ch, MAG, font="8px")
c.rect(5, 16, 12, 1, MAG)
c.rect(5, 59, 12, 1, MAG)

# left horizontal cyan sign
glowbox(0, 66, 26, 9, "#06282e", CYN_D)
c.rect(1, 67, 24, 7, "#0a3a44")
c.text(3, 69, "BAR", CYN, font="5x7")
c.rect(0, 66, 26, 1, CYN)

# right vertical yellow sign
glowbox(112, 12, 12, 42, YEL_D, "#3a300a")
c.rect(113, 13, 10, 40, YEL_D)
for ch, yy in zip("酒場", (16, 27)):
    c.text(114, yy, ch, YEL, font="8px")
c.text(114, 40, "3F", "#ffb45c", font="5x7")
c.rect(112, 12, 12, 1, YEL)
c.rect(112, 53, 12, 1, YEL)

# right horizontal pink sign
glowbox(94, 64, 30, 9, "#33101c", PNK_D)
c.rect(95, 65, 28, 7, "#4a1526")
c.text(97, 67, "HOTEL", PNK, font="5x7")
c.rect(94, 64, 30, 1, PNK)

# magenta strip light down left edge of back wall
c.rect(44, 26, 2, 60, MAG_D)
c.rect(44, 26, 1, 60, "#b0257f")
c.rect(83, 40, 1, 46, PUR)

# ---------- vending machines ----------
def vending(x, y, glow, glow_d):
    c.rect(x, y, 12, 30, "#101019")           # body
    c.rect(x + 1, y + 2, 10, 18, glow_d)      # lit panel
    c.rect(x + 2, y + 3, 8, 16, glow)
    for ry in range(y + 5, y + 17, 4):        # product rows
        c.rect(x + 3, ry, 6, 2, "#ffffff" if ry % 8 else glow)
    c.rect(x + 2, y + 22, 8, 4, "#0a0a12")    # slot
    c.rect(x + 3, y + 23, 6, 2, "#1c1c2a")
    c.rect(x, y, 12, 1, glow)                 # top light strip
    # light spill on wall/ground
    c.rect(x - 2, y + 28, 16, 2, glow_d)

vending(88, 62, CYN, "#0a3a44")
vending(30, 68, "#ff8844", "#3a1c0a")

# ---------- power cables ----------
def cable(x0, y0, x1, y1, sag, col):
    pts = []
    n = 16
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t + sag * 4 * t * (1 - t)
        pts.append((round(x), round(y)))
    for a, b in zip(pts, pts[1:]):
        c.line(a[0], a[1], b[0], b[1], col)

cable(0, 8, 128, 4, 9, "#22223a")
cable(0, 14, 128, 10, 7, "#1a1a2e")
cable(44, 22, 86, 22, 6, "#22223a")
cable(20, 0, 60, 20, 5, "#1a1a2e")
# hanging lamp on a cable
c.rect(60, 18, 1, 4, "#22223a")
c.rect(57, 22, 7, 3, "#2a2a40")
c.rect(59, 25, 3, 2, WARM)

# ---------- puddles + reflections ----------
c.ellipse(64, 108, 30, 7, "#0a0a13")
c.ellipse(64, 108, 30, 7, "#0e0e18", fill=False)
c.ellipse(20, 116, 12, 4, "#0a0a13")
c.ellipse(104, 118, 14, 4, "#0a0a13")
c.ellipse(46, 100, 8, 2, "#0d0d16")

# neon reflections (vertical smears in puddles)
def reflect(x, y0, y1, col, dim):
    c.line(x, y0, x, y1, col)
    c.line(x - 1, y0 + 2, x - 1, y1, dim)
    c.line(x + 1, y0 + 1, x + 1, y1 - 1, dim)

reflect(10, 100, 122, "#8a1a5e", "#4a1038")     # magenta sign
reflect(6, 104, 118, "#0f5a66", "#0a3a44")      # cyan sign
reflect(118, 100, 124, "#8a7420", "#4a3c14")    # yellow sign
reflect(108, 100, 120, "#8a2c40", "#4a1826")    # pink sign
reflect(93, 98, 112, "#0f5a66", "#0a3a44")      # vending cyan
reflect(35, 102, 114, "#8a4420", "#4a2412")     # vending orange
reflect(64, 96, 100, "#8a6a3a", "#4a3a20")      # doorway warm
# shimmer dashes
for dx, dy in [(56, 104), (70, 106), (60, 112), (74, 112), (52, 118), (68, 120)]:
    c.rect(dx, dy, 3, 1, "#161624")

# ---------- person with transparent umbrella ----------
# silhouette, centre, walking away from viewer
c.circle(63, 76, 4, SIL)                 # head
c.rect(59, 80, 9, 20, SIL)               # torso
c.rect(58, 82, 2, 12, SIL)               # left arm
c.rect(69, 82, 2, 10, SIL)               # right arm
c.rect(60, 100, 3, 12, SIL)              # legs
c.rect(65, 100, 3, 12, SIL)
c.rect(59, 111, 5, 2, SIL)               # shoes
c.rect(64, 111, 5, 2, SIL)
# rim light (cyan from right, magenta kiss from left)
for y in range(76, 100):
    c.set(68, y, RIM)
c.set(67, 76, RIM); c.set(68, 77, RIM)
for y in range(82, 94):
    c.set(58, y, "#7a1a56")
c.set(63, 72, RIM)  # top of head

# umbrella: translucent canopy + ribs + stem
c.path("M46,68 A17,17 0 0 1 80,68 Z", (140, 190, 255, 70), fill=True)
c.path("M46,68 A17,17 0 0 1 80,68", (190, 225, 255, 160), fill=False)
c.line(63, 51, 63, 68, (190, 225, 255, 160))
c.line(52, 60, 52, 68, (160, 200, 255, 120))
c.line(74, 60, 74, 68, (160, 200, 255, 120))
c.line(63, 68, 70, 84, "#0a0a12")        # stem to hand
c.rect(68, 82, 3, 3, SIL)                # hand grip
# neon glow caught on canopy edge
c.set(63, 51, (255, 120, 210, 200))
c.set(46, 68, (120, 235, 255, 190))
c.set(80, 68, (120, 235, 255, 190))

# ---------- light pools / contrast ----------
c.ellipse(94, 94, 12, 3, "#123a44")      # cyan spill at vending base
c.ellipse(36, 100, 10, 3, "#3a2010")     # orange spill
c.ellipse(64, 96, 8, 2, "#3a2a14")       # doorway spill
c.rect(44, 90, 1, 4, "#7a1a5e")
c.rect(84, 90, 1, 4, "#3f1f80")

print(c.stats_text())
save("cyberpunk-alley", c)
finish(c)
