from pixelbench_api import *
import math, random

random.seed(7)
W = H = 256

# palette
COL = dict(
    bg="#0a0a14", bg2="#12121f", bg3="#1a1a2c",
    stone="#3a3a46", stone2="#4c4c5a", stone3="#2b2b35",
    brass="#8a6a2f", brass2="#c9a24b", brass3="#e8cf7a", brass4="#5c451d",
    glow="#ffe9a8", core="#fff6d8", core2="#ffd76b", core3="#ff9d3c",
    rune="#6ee8ff", rune2="#2fa8c9",
    crys="#9fd8ff", crys2="#5aa8e8", crys3="#d8a8ff", crys4="#8a5ac9",
    dark="#050508", shadow="#141420",
)

c = new_canvas(W, H, COL["bg"], name="result")

# ---------- background: dark hall ----------
c.rect(0, 0, W, H, COL["bg"])
# subtle vertical gradient bands
for y in range(H):
    t = y / H
    col = COL["bg"] if t < 0.45 else (COL["bg2"] if t < 0.75 else COL["bg3"])
    c.line(0, y, W - 1, y, col)
# distant arches
for ax in (18, 70, 186, 238):
    c.path(f"M{ax} 200 L{ax} 120 Q{ax+22} 92 {ax+44} 120 L{ax+44} 200", COL["shadow"], fill=False)
# floor line
c.line(0, 208, W - 1, 208, COL["stone3"])
c.rect(0, 208, W, 48, COL["stone3"])
for x in range(0, W, 32):
    c.line(x, 208, x, 255, "#232330")
for y in range(216, 256, 14):
    c.line(0, y, W - 1, y, "#232330")

# ---------- glow behind the machine ----------
for r in range(96, 30, -4):
    a = int(30 + (96 - r) * 1.2)
    c.circle(128, 108, r, f"#2a2410" if r % 8 else f"#332a12", fill=True)

# ---------- pedestal ----------
def stone_rect(x, y, w, h, base, hi, lo):
    c.rect(x, y, w, h, base)
    c.line(x, y, x + w - 1, y, hi)
    c.line(x, y, x, y + h - 1, hi)
    c.line(x, y + h - 1, x + w - 1, y + h - 1, lo)
    c.line(x + w - 1, y, x + w - 1, y + h - 1, lo)

# steps
stone_rect(84, 232, 88, 12, COL["stone"], COL["stone2"], COL["stone3"])
stone_rect(92, 220, 72, 12, COL["stone2"], "#5e5e6e", COL["stone"])
stone_rect(100, 208, 56, 12, COL["stone2"], "#62626f", COL["stone3"])
# column
stone_rect(106, 168, 44, 40, COL["stone"], COL["stone2"], COL["stone3"])
for y in range(172, 206, 6):
    c.line(106, y, 149, y, COL["stone3"])
# flutes
for x in range(111, 148, 7):
    c.line(x, 170, x, 206, "#33333f")
# capital
stone_rect(102, 162, 52, 8, COL["stone2"], "#6a6a78", COL["stone3"])
# engraved sigil on column
c.circle(128, 188, 7, COL["brass2"], fill=False)
c.line(128, 181, 128, 195, COL["brass2"])
c.line(121, 188, 135, 188, COL["brass2"])

# ---------- armillary rings ----------
CX, CY = 128, 108

def ring(cx, cy, r, col, thick=1):
    c.circle(cx, cy, r, col, fill=False)
    if thick > 1:
        c.circle(cx, cy, r - 1, col, fill=False)

def ticks(cx, cy, r, n, col, ln=2):
    for i in range(n):
        a = 2 * math.pi * i / n
        x0 = cx + r * math.cos(a); y0 = cy + r * math.sin(a)
        x1 = cx + (r + ln) * math.cos(a); y1 = cy + (r + ln) * math.sin(a)
        c.line(int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1)), col)

def ellipse_ring(cx, cy, rx, ry, col):
    c.ellipse(cx, cy, rx, ry, col, fill=False)

# outer brass ring band
ring(CX, CY, 86, COL["brass4"]); ring(CX, CY, 85, COL["brass"]); ring(CX, CY, 84, COL["brass2"])
ticks(CX, CY, 82, 48, COL["brass3"], 2)
# second ring
ring(CX, CY, 76, COL["brass"]); ring(CX, CY, 75, COL["brass2"]); ring(CX, CY, 73, COL["brass4"])
# tilted great circles (ellipses) — the armillary sphere look
ellipse_ring(CX, CY, 86, 30, COL["brass2"])
ellipse_ring(CX, CY, 86, 29, COL["brass4"])
ellipse_ring(CX, CY, 60, 78, COL["brass"])
ellipse_ring(CX, CY, 59, 77, COL["brass4"])
ellipse_ring(CX, CY, 40, 84, COL["brass2"])
ellipse_ring(CX, CY, 39, 83, COL["brass4"])
# meridian ring with tick teeth
ellipse_ring(CX, CY, 70, 70, COL["brass"])
ticks(CX, CY, 67, 36, COL["brass3"], 2)

# ---------- runes along a ring ----------
rune_r = 80
for i in range(24):
    a = 2 * math.pi * i / 24 + 0.13
    x = int(round(CX + rune_r * math.cos(a)))
    y = int(round(CY + rune_r * math.sin(a)))
    # tiny rune glyph: 2-3 pixels
    c.set(x, y, COL["rune"])
    c.set(x + 1, y, COL["rune2"])
    if i % 3 == 0:
        c.set(x, y - 1, COL["rune"])
    if i % 4 == 0:
        c.set(x, y + 1, COL["rune2"])

# ---------- gears at the base of the mechanism ----------
def gear(cx, cy, r, body, dark, hole_col):
    n = max(8, r)
    for i in range(n):
        a = 2 * math.pi * i / n
        x0 = cx + r * math.cos(a); y0 = cy + r * math.sin(a)
        x1 = cx + (r + 2) * math.cos(a); y1 = cy + (r + 2) * math.sin(a)
        c.line(int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1)), body)
    c.circle(cx, cy, r, body, fill=True)
    c.circle(cx, cy, r - 2, dark, fill=False)
    c.circle(cx, cy, max(1, r // 3), hole_col, fill=True)

gear(96, 196, 8, COL["brass2"], COL["brass4"], COL["brass4"])
gear(160, 196, 8, COL["brass2"], COL["brass4"], COL["brass4"])
gear(128, 200, 6, COL["brass3"], COL["brass"], COL["brass"])
gear(112, 190, 5, COL["brass"], COL["brass4"], COL["brass4"])
gear(144, 190, 5, COL["brass"], COL["brass4"], COL["brass4"])

# support arms from pedestal to sphere
c.line(112, 176, 108, 150, COL["brass"])
c.line(144, 176, 148, 150, COL["brass"])
c.line(106, 150, 150, 150, COL["brass2"])
c.line(106, 151, 150, 151, COL["brass4"])

# ---------- alchemical dials (small gauges on the arms) ----------
def dial(cx, cy, r):
    c.circle(cx, cy, r, COL["brass4"], fill=True)
    c.circle(cx, cy, r, COL["brass2"], fill=False)
    c.circle(cx, cy, r - 2, "#1a1a26", fill=True)
    a = 0.8
    c.line(cx, cy, int(cx + (r - 3) * math.cos(a)), int(cy + (r - 3) * math.sin(a)), COL["rune"])
    c.set(cx, cy, COL["brass3"])

dial(106, 150, 5)
dial(150, 150, 5)
dial(128, 158, 6)

# ---------- crystal spheres orbiting ----------
def crystal(cx, cy, r, base, hi, lo):
    c.circle(cx, cy, r, base, fill=True)
    c.circle(cx, cy, r, lo, fill=False)
    # highlight
    c.set(cx - r // 2, cy - r // 2, hi)
    c.set(cx - r // 2 + 1, cy - r // 2, hi)
    c.set(cx - r // 2, cy - r // 2 + 1, hi)

crystal(58, 70, 6, COL["crys"], "#ffffff", COL["crys2"])
crystal(200, 88, 5, COL["crys3"], "#f0e0ff", COL["crys4"])
crystal(186, 160, 6, COL["crys"], "#ffffff", COL["crys2"])
crystal(70, 158, 5, COL["crys3"], "#f0e0ff", COL["crys4"])
crystal(128, 26, 5, COL["crys"], "#ffffff", COL["crys2"])
# orbit threads
c.circle(CX, CY, 74, COL["rune2"], fill=False)

# ---------- central radiant core ----------
c.circle(CX, CY, 22, COL["core3"], fill=True)
c.circle(CX, CY, 18, COL["core2"], fill=True)
c.circle(CX, CY, 13, COL["core"], fill=True)
c.circle(CX, CY, 8, "#ffffff", fill=True)
# core ring housing
c.circle(CX, CY, 24, COL["brass2"], fill=False)
c.circle(CX, CY, 25, COL["brass4"], fill=False)
ticks(CX, CY, 25, 24, COL["brass3"], 2)
# rays
for i in range(16):
    a = 2 * math.pi * i / 16 + 0.2
    x0 = CX + 27 * math.cos(a); y0 = CY + 27 * math.sin(a)
    x1 = CX + (34 if i % 2 else 30) * math.cos(a)
    y1 = CY + (34 if i % 2 else 30) * math.sin(a)
    c.line(int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1)), COL["glow"])

# inner mechanism spokes
for i in range(6):
    a = 2 * math.pi * i / 6
    c.line(int(CX + 26 * math.cos(a)), int(CY + 26 * math.sin(a)),
           int(CX + 70 * math.cos(a)), int(CY + 70 * math.sin(a)), COL["brass4"])

# engraved star on mid ring
star = []
for i in range(10):
    ang = -math.pi / 2 + math.pi * i / 5
    rr = 52 if i % 2 == 0 else 22
    star.append((CX + rr * math.cos(ang), CY + rr * math.sin(ang)))
c.poly(star, COL["brass3"], fill=False)

# ---------- dramatic lighting ----------
# light pool on floor under the machine
c.ellipse(128, 226, 46, 10, "#3a3018", fill=True)
c.ellipse(128, 226, 34, 7, "#4a3d1e", fill=True)
# candle sconces on side walls
for sx in (14, 240):
    c.rect(sx, 150, 3, 14, "#2a2a34")
    c.set(sx + 1, 148, "#ffcf6b")
    c.set(sx + 1, 147, "#ffe9a8")
    c.circle(sx + 1, 147, 3, "#3a2c14", fill=True)
# vignette: darken corners
for (vx, vy, vw, vh) in [(0, 0, 26, 26), (230, 0, 26, 26), (0, 230, 26, 26), (230, 230, 26, 26)]:
    for yy in range(vy, vy + vh):
        for xx in range(vx, vx + vw):
            dx = (xx - (vx + vw / 2)) / (vw / 2)
            dy = (yy - (vy + vh / 2)) / (vh / 2)
            if dx * dx + dy * dy > 1.0:
                c.set(xx, yy, COL["dark"])

# ---------- dark outline pass ----------
c.outline(COL["dark"])

print(c.stats_text())
save("arcane-instrument-giant", c)
finish(c)
