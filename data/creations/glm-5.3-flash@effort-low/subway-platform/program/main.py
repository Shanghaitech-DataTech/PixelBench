from pixelbench_api import *

c = new_canvas(64, 64, background="#0d0d14", name="subway")

# --- palette ---
INK    = c.color("#0d0d14")
WALL   = c.color("#1c2333")
WALL2  = c.color("#232c40")
TILE   = c.color("#2e3a55")
DOORF  = c.color("#3a4a6b")   # screen door frame
GLASS  = c.color("#4d6a99")   # glass
GLASS2 = c.color("#5d7fb5")
FLOOR  = c.color("#39404f")
FLOOR2 = c.color("#454e60")
YELLOW = c.color("#e8c14a")
TRAIN  = c.color("#c8ccd4")
TRAIN2 = c.color("#9aa2ad")
WIN    = c.color("#7fd4e8")
WIN2   = c.color("#a8e6f2")
RED    = c.color("#c94f4f")
SKIN   = c.color("#d9a878")
HAIR   = c.color("#3a2c22")
COAT   = c.color("#5a6b8c")
COAT2  = c.color("#8c5a5a")
PANTS  = c.color("#2a3140")
STREAK = c.color("#6f8fbf")
LIGHT  = c.color("#f2ead6")
SHADOW = c.color("#14181f")

# --- back wall with tiles ---
c.rect(0, 0, 64, 34, WALL)
for y in range(2, 34, 4):
    c.line(0, y, 63, y, WALL2)
for x in range(4, 64, 8):
    c.line(x, 2, x, 33, WALL2)

# ceiling strip / lights
c.rect(0, 0, 64, 2, SHADOW)
for lx in (10, 34, 58):
    c.rect(lx, 1, 4, 1, LIGHT)

# station sign band
c.rect(4, 6, 26, 8, TILE)
c.rect(4, 6, 26, 1, LIGHT)
c.text(7, 8, "CENTRAL", INK)
c.rect(4, 14, 26, 1, YELLOW)

# --- track area (behind screen doors) ---
c.rect(0, 34, 64, 12, SHADOW)

# --- train arriving, left side, motion streaks to convey speed ---
# streaks
for i in range(6):
    y = 36 + i * 2
    c.line(0, y, 14 - i, y, STREAK)
c.rect(0, 34, 20, 12, TRAIN)
c.rect(0, 34, 20, 2, TRAIN2)
c.rect(0, 44, 20, 2, TRAIN2)
# train windows
for wx in (2, 7, 12):
    c.rect(wx, 37, 4, 5, WIN)
c.rect(2, 37, 1, 5, WIN2)
# headlight glow
c.rect(19, 39, 2, 4, LIGHT)
c.rect(21, 40, 2, 2, YELLOW)
# red tail detail
c.rect(0, 40, 1, 2, RED)

# --- platform screen doors (glass panels) from x=22 to 63 ---
c.rect(22, 26, 42, 20, DOORF)  # door band
for px in range(22, 64, 10):
    c.rect(px, 26, 1, 20, DOORF)
# glass panes between frames
for px in (23, 33, 43, 53):
    c.rect(px, 27, 9, 14, GLASS)
    c.rect(px, 27, 9, 1, GLASS2)
    c.line(px + 1, 39, px + 4, 28, GLASS2)  # reflection
# yellow warning stripe along door bottom
c.rect(22, 44, 42, 1, YELLOW)
# door top header
c.rect(22, 24, 42, 2, DOORF)

# --- platform floor (foreground, perspective-ish) ---
c.rect(0, 45, 64, 19, FLOOR)
for y in range(47, 64, 4):
    c.line(0, y, 63, y, FLOOR2)
# platform edge yellow line
c.rect(0, 45, 64, 1, YELLOW)
c.rect(0, 46, 64, 1, SHADOW)

# --- bench ---
c.rect(46, 50, 14, 2, COAT)   # seat
c.rect(46, 52, 2, 5, PANTS)   # legs
c.rect(58, 52, 2, 5, PANTS)
c.rect(46, 48, 14, 2, COAT)   # backrest

# --- passenger 1: standing, looking at train (left, near doors) ---
def person(x, y, coat, hair, pants, pose=0):
    c.set(x, y, SKIN)          # head
    c.rect(x, y - 1, 3, 1, hair)
    c.rect(x - 1, y + 1, 3, 4, coat)   # torso
    c.rect(x, y + 5, 1, 3, pants)
    c.rect(x + 2, y + 5, 1, 3, pants)

# p1: standing, arm raised checking watch
person(26, 28, COAT, HAIR, PANTS)
c.set(29, 30, COAT)   # raised arm
c.set(30, 29, SKIN)

# p2: walking briskly (mid, leaning forward, one leg back)
c.set(38, 30, SKIN)
c.rect(38, 29, 3, 1, HAIR)
c.rect(37, 31, 3, 4, COAT2)
c.rect(38, 35, 1, 2, PANTS)
c.set(40, 36, PANTS)  # trailing leg
c.set(36, 35, PANTS)  # forward leg
c.set(40, 30, COAT2)  # swinging arm

# p3: sitting on bench
c.set(52, 46, SKIN)
c.rect(52, 45, 3, 1, HAIR)
c.rect(51, 47, 3, 4, COAT)
c.rect(52, 51, 1, 2, PANTS)
c.set(54, 51, PANTS)
c.set(50, 48, COAT)   # arm resting

# speed lines above train
for sx, sy, ln in ((1, 33, 10), (4, 32, 8), (8, 33, 6)):
    c.line(sx, sy, sx + ln, sy, STREAK)

print(c.stats_text())
save("subway", c)
finish(c)
