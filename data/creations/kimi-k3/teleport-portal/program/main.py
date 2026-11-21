import math

W = H = 48
CELL = 24  # each frame occupies a 24x48 half

# palette
DEEP   = '#1b0b2e'
DARK   = '#3b1266'
MID    = '#6b21a8'
BRIGHT = '#9333ea'
LIGHT  = '#c084fc'
PALE   = '#e9d5ff'
WHITE  = '#faf5ff'
HALO   = '#e6c8ff'
GLOW   = (200, 150, 255, 80)

sheet = new_canvas(W, H, background=None, name="portal_frames")


def vortex(c, cx, cy, R, phase, twist, x0, x1):
    for y in range(H):
        for x in range(x0, x1):
            dx = x - cx
            dy = y - cy
            r = math.hypot(dx, dy)
            if r > R:
                continue
            th = math.atan2(dy, dx)
            t = (th / (2 * math.pi) * 3 + r / R * twist + phase) % 1.0
            if r < 1.8:
                col = WHITE
            elif r < 3.4:
                col = PALE if t < 0.5 else LIGHT
            else:
                if t < 0.16:
                    col = PALE
                elif t < 0.34:
                    col = LIGHT
                elif t < 0.55:
                    col = BRIGHT
                elif t < 0.78:
                    col = MID
                else:
                    col = DARK
                if r > R - 1.4 and col in (DARK, MID):
                    col = DEEP
            c.set(x, y, col)


# ---- frame 1 (left half): purple energy vortex ----
vortex(sheet, 11.5, 23.5, R=10.0, phase=0.0, twist=2.6, x0=0, x1=CELL)
for (x, y) in [(5, 12), (18, 9), (4, 34), (19, 38)]:
    sheet.set(x, y, PALE)

# ---- frame 2 (right half): rotated vortex + glowing halo ----
vortex(sheet, 35.5, 23.5, R=10.0, phase=0.45, twist=3.1, x0=CELL, x1=W)
cx, cy = 35.5, 23.5
for y in range(H):
    for x in range(CELL, W):
        r = math.hypot(x - cx, y - cy)
        if 10.3 <= r < 11.8:
            sheet.set(x, y, HALO)
        elif 11.8 <= r < 13.2:
            sheet.set(x, y, GLOW)
for (x, y) in [(35, 11), (46, 24), (35, 36), (25, 24)]:
    sheet.set(x, y, HALO)

sheet.color(GLOW)  # ensure registered
print(sheet.stats_text())
view(sheet)
finish(sheet)
