from pixelbench_api import *

c = new_canvas(128, 128, name="alley")

def reg(spec):
    return c.color(spec)

# ---------- palette ----------
SKY0, SKY1, SKY2, SKY3, SKY4 = reg("#030409"), reg("#05070f"), reg("#070c18"), reg("#0a0f1e"), reg("#0d1424")
FAR, FAR2 = reg("#0c1120"), reg("#0e1526")
BUILD, BUILD2 = reg("#060910"), reg("#0a0f1a")
WINDOW, WINDIM, WINCY = reg("#ffd75e"), reg("#6e5f2e"), reg("#77d8ff")
DARK = reg("#02030a")
CABLE = reg("#010207")

PINK, PINK_GLOW, PINKD = reg("#ff2d95"), reg("#8a1b52"), reg("#5a1238")
CYAN, CYAN_GLOW, CYAND = reg("#00e5ff"), reg("#0b5f73"), reg("#0a3a4a")
YELLOW, YELLOW_GLOW, YELD = reg("#ffd635"), reg("#8a7420"), reg("#5a4a18")
GREEN, GREEN_GLOW = reg("#3cff5e"), reg("#1f6b2c")
ORANGE, ORANGE_GLOW = reg("#ff9c2e"), reg("#804d16")

GND0, GND1, GND2, GND3, GND4 = reg("#0a0e1a"), reg("#0c1120"), reg("#0a0e18"), reg("#070a12"), reg("#05070c")
PUD, PUD2, PUD3 = reg("#101a30"), reg("#182640"), reg("#0c1324")

RAIN = reg((140, 172, 230, 70))
RAINB = reg((205, 228, 255, 115))

UMB, UMBHI, UMBD = reg((150, 205, 240, 95)), reg((214, 238, 255, 150)), reg((40, 70, 110, 150))
BODY = reg("#02030a")

VEND, VENDG = reg("#0e1422"), reg("#16202f")
CANR, CANC, CANY = reg("#ff4757"), reg("#35c8ff"), reg("#ffd93d")
VENDLOW = reg((190, 240, 180, 90))

# ---------- sky ----------
sk = [SKY0, SKY1, SKY2, SKY3, SKY4]
for y in range(0, 90):
    c.rect(0, y, 128, 1, sk[min(y // 8, 4)])

# ---------- far skyline ----------
towers = [(0, 28, 10), (10, 20, 14), (24, 14, 16), (40, 26, 12), (52, 16, 18),
          (70, 10, 16), (86, 20, 14), (100, 26, 12), (112, 16, 14)]
for (x, top, w) in towers:
    c.rect(x, top, w, 88 - top, FAR)
# roof boxes / antennae
c.rect(6, 16, 6, 4, FAR2)
c.rect(28, 8, 4, 6, FAR2)
c.rect(66, 4, 3, 6, FAR2)
c.rect(96, 10, 8, 4, FAR2)
c.rect(118, 12, 5, 4, FAR2)

# far-building windows
import random
random.seed(3)
for x in range(2, 126, 4):
    for y in range(18, 86, 7):
        r = random.random()
        if r < 0.22:
            c.rect(x, y, 2, 3, WINDIM)
        elif r < 0.30:
            c.rect(x, y, 2, 3, WINDOW)
        elif r < 0.36:
            c.rect(x, y, 2, 3, WINCY)

# ---------- cables (behind near buildings) ----------
c.path("M0 8 Q64 26 127 10", CABLE, fill=False)
c.path("M0 16 Q64 34 127 18", CABLE, fill=False)
c.path("M0 24 Q64 42 127 26", CABLE, fill=False)
c.line(30, 17, 30, 34, CABLE)
c.line(100, 12, 100, 26, CABLE)

# ---------- foreground buildings ----------
# left
c.rect(0, 38, 30, 51, BUILD)          # x0-29, y38-88
c.rect(0, 28, 12, 10, BUILD)
c.rect(14, 32, 8, 6, BUILD2)
c.rect(18, 66, 10, 14, BUILD)
# right
c.rect(100, 30, 28, 59, BUILD)        # x100-127, y30-88
c.rect(108, 20, 16, 10, BUILD)
c.rect(106, 54, 10, 6, BUILD2)
c.rect(120, 44, 7, 10, BUILD2)

# neon circle sign on left building
c.circle(15, 58, 9, PINK_GLOW)
c.circle(15, 58, 5, PINK, fill=False)

# pink hanging sign "SAKURA"
c.rect(31, 43, 38, 16, PINK_GLOW)
c.rect(33, 45, 34, 12, DARK)
c.rect(34, 46, 32, 10, PINK_GLOW)
c.rect(33, 45, 34, 12, PINK, fill=False)
c.text(35, 47, "SAKURA", PINK, spacing=0)
c.rect(44, 56, 12, 1, PINK)
# pink light pool on ground
c.rect(20, 90, 52, 8, PINKD)

# cyan sign on right building "RAMEN"
c.rect(98, 42, 30, 14, CYAN_GLOW)
c.rect(100, 44, 28, 10, DARK)
c.rect(99, 45, 28, 8, CYAN_GLOW)
c.rect(99, 44, 28, 10, CYAN, fill=False)
c.text(100, 46, "RAMEN", CYAN, spacing=0)
# vertical cyan strip
c.rect(100, 66, 3, 22, CYAN_GLOW)
c.rect(100, 66, 1, 22, CYAN)

# yellow rooftop sign "HOTEL"
c.rect(68, 16, 34, 12, YELLOW_GLOW)
c.rect(68, 18, 34, 8, DARK)
c.text(69, 19, "HOTEL", YELLOW)
# distant orange window light on far tower
c.rect(120, 58, 4, 5, ORANGE_GLOW)
c.rect(121, 59, 2, 3, ORANGE)

# ---------- vending machine ----------
c.rect(100, 68, 24, 28, VEND)          # body x100-123 y68-95
c.rect(102, 69, 20, 8, GREEN_GLOW)
c.rect(104, 70, 16, 3, GREEN)
c.rect(102, 78, 20, 10, VENDG)
for i, cx in enumerate([104, 108, 111, 115]):
    for j, cc in enumerate([CANR, CANC, CANY, CANR]):
        c.rect(cx, 80 + j * 4, 3, 3, cc)
c.rect(102, 79, 20, 1, VENDLOW)
c.rect(102, 91, 20, 4, BUILD2)
c.rect(102, 94, 20, 1, GREEN_GLOW)
# light spill
c.ellipse(112, 99, 14, 6, VENDLOW)

# ---------- ground ----------
gnd = [GND0, GND1, GND2, GND3, GND4]
for y in range(90, 128):
    c.rect(0, y, 128, 1, gnd[min((y - 90) // 8, 4)])

# cable in front of buildings
c.path("M30 50 Q66 68 100 46", CABLE, fill=False)
c.line(62, 60, 62, 74, CABLE)

# grate with steam
c.rect(68, 92, 10, 3, BUILD2)
c.line(70, 92, 70, 94, DARK)
c.line(74, 92, 74, 94, DARK)
c.line(69, 89, 71, 88, ORANGE_GLOW)
c.line(72, 86, 73, 85, ORANGE_GLOW)
c.line(75, 83, 76, 82, CYAND)

# ---------- puddles ----------
c.ellipse(40, 102, 22, 5, PUD)
c.ellipse(38, 112, 26, 6, PUD2)
c.ellipse(40, 102, 22, 5, PUD3, fill=False)
c.ellipse(84, 108, 18, 5, PUD)
c.ellipse(84, 118, 20, 6, PUD2)
c.ellipse(120, 112, 7, 4, PUD)
# puddle reflections (neon smears)
for (px, pc, n) in [(30, PINK, 6), (38, PINKD, 7), (52, CYAN, 3), (76, CYAND, 5),
                   (90, YELD, 4), (104, YELLOW, 5), (118, CYAN, 4)]:
    for i in range(n):
        c.set(px + i, 108 + (i % 3), pc)
c.rect(64, 116, 26, 1, CYAND)
c.rect(70, 118, 18, 1, CYAN_GLOW)
c.rect(40, 118, 14, 1, PINKD)
c.rect(42, 120, 10, 1, PINK)
# long glinting streak
c.rect(24, 104, 52, 1, PUD3)

# ---------- person with transparent umbrella ----------
# glow haze around person from signs
c.ellipse(54, 76, 12, 20, PINKD)
c.ellipse(54, 60, 14, 8, CYAND)
# transparent umbrella
c.ellipse(54, 50, 15, 8, UMB)
c.ellipse(54, 50, 14, 7, UMBHI, fill=False)
for rx in [-10, -5, 0, 5, 10]:
    c.line(54 + rx, 50, 54 + rx, 56, UMBHI)
c.ellipse(54, 50, 3, 2, UMBD, fill=False)
# person silhouette
c.line(54, 57, 52, 66, BODY)   # pole
c.line(51, 66, 47, 59, BODY)   # arm
c.circle(54, 62, 3, BODY)       # head
c.rect(52, 65, 5, 12, BODY)    # coat
c.line(52, 65, 52, 76, CYAN_GLOW)   # rim light from sign
c.rect(52, 77, 2, 12, BODY)    # legs
c.rect(56, 77, 2, 12, BODY)
c.rect(51, 88, 3, 2, BODY)
c.rect(56, 88, 3, 2, BODY)
# reflection of umbrella + body on wet ground
c.ellipse(54, 96, 11, 3, UMBD)
c.rect(50, 95, 8, 2, UMBD)
c.ellipse(54, 100, 9, 2, RAIN)

# ---------- rain ----------
random.seed(11)
for i in range(52):
    x = (i * 31 + 7) % 128
    if x < 5:
        x += 7
    y = (i * 17 + 3) % 118
    ln = 6 + (i % 6)
    colr = RAINB if i % 3 == 0 else RAIN
    c.line(x, y, x - 5, y + ln, colr)
# bright rain near lights
for (x, y) in [(40, 30), (52, 22), (108, 34), (70, 40), (60, 70), (30, 80), (96, 60), (112, 76)]:
    if y > 112:
        y = 112
    c.line(x, y, x - 5, y + 9, RAINB)

# ---------- outline light edges on building corners ----------
c.rect(29, 38, 1, 50, CYAN_GLOW)
c.rect(127, 30, 1, 58, PINK_GLOW)
c.rect(0, 88, 30, 1, CYAND)
c.rect(100, 88, 28, 1, PINKD)

print(c.stats_text())
print("colors:", len(c.palette()))
finish(c)
