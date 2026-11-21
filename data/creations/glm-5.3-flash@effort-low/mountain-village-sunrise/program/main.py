from pixelbench_api import *

W = H = 128
c = new_canvas(W, H, background="#2b1b3d", name="village")

# ---- sky gradient (sunrise) ----
sky = ["#2b1b3d", "#4a2352", "#7a2f5a", "#b34a5e", "#e0705c", "#f2a15f", "#f8c876"]
for y in range(H):
    t = y / (H - 1)
    i = min(int(t * len(sky)), len(sky) - 1)
    c.line(0, y, W - 1, y, sky[i])

# ---- sun with glow ----
cx, cy = 64, 62
c.circle(cx, cy, 13, "#ffd98a")
c.circle(cx, cy, 9, "#fff3c4")
c.circle(cx, cy, 5, "#ffffff")

# ---- distant mountains (far, hazy purple) ----
def ridge(points, colour):
    pts = points + [(W, H), (0, H)]
    c.poly(pts, colour)

ridge([(0, 70), (20, 44), (38, 62), (52, 38), (70, 58), (86, 42), (104, 60), (118, 48), (127, 58)], "#5a3a6e")
# snow caps on far peaks
c.poly([(52, 38), (58, 45), (54, 46), (50, 44)], "#e8d8e8")
c.poly([(86, 42), (91, 48), (87, 49), (84, 47)], "#e8d8e8")

# ---- mid mountains ----
ridge([(0, 88), (14, 66), (30, 80), (46, 62), (64, 78), (80, 64), (96, 78), (112, 68), (127, 82)], "#6e4a72")
c.poly([(46, 62), (51, 68), (48, 69), (44, 67)], "#f0e0e0")
c.poly([(80, 64), (85, 70), (81, 71), (78, 69)], "#f0e0e0")

# ---- ground / valley ----
c.rect(0, 96, W, 32, "#3f5a3a")
c.rect(0, 96, W, 3, "#4d6b44")

# ---- stone path (focal lead, winding to center) ----
path_col = ["#9a8f82", "#84796d", "#b0a598"]
pts = [(64, 127), (63, 120), (66, 112), (62, 104), (64, 97)]
for (px, py) in pts:
    w = 7 if py > 118 else (5 if py > 108 else 4)
    c.rect(px - w // 2, py, w, 2, path_col[0])
    c.set(px - w // 2 + 1, py, path_col[2])
    c.set(px + w // 2 - 1, py + 1, path_col[1])

# ---- pine trees ----
def pine(x, base, h, dark="#1e3a2a", mid="#2c5038", light="#3d6a48"):
    for i in range(h):
        w = max(1, int((h - i) * 0.9))
        col = dark if i < h // 3 else (mid if i < 2 * h // 3 else light)
        c.line(x - w // 2, base - i, x + w // 2, base - i, col)
    c.rect(x, base, 1, 2, "#3a2a1c")

# background pines (small, hazy)
for (x, b, h) in [(8, 96, 9), (16, 97, 11), (24, 96, 8), (104, 96, 9), (112, 97, 12), (121, 96, 10)]:
    pine(x, b, h, "#26402f", "#2f4f3a", "#3a5f45")

# foreground pines framing the focal point
pine(6, 128, 34)
pine(18, 128, 26)
pine(121, 128, 36)
pine(109, 128, 27)

# ---- houses ----
def house(x, y, w, h, wall, roof, door, roof_dark):
    # wall
    c.rect(x, y, w, h, wall)
    # timber lines
    for i in range(x, x + w, 4):
        c.line(i, y, i, y + h - 1, "#5a4030")
    c.line(x, y + h // 2, x + w - 1, y + h // 2, "#5a4030")
    # roof
    c.poly([(x - 2, y), (x + w // 2, y - 8), (x + w + 1, y)], roof)
    c.poly([(x - 2, y), (x + w // 2, y - 8)], roof_dark)
    # door
    c.rect(x + w // 2 - 2, y + h - 6, 4, 6, door)
    # window (warm glow)
    c.rect(x + 3, y + 3, 3, 3, "#ffd98a")
    c.rect(x + w - 6, y + 3, 3, 3, "#ffd98a")

# left house
house(24, 84, 20, 14, "#8a6a4a", "#6e3a34", "#3a2a1c", "#5a2c28")
# center house (focal)
house(54, 80, 22, 16, "#9a7a55", "#7a4038", "#3a2a1c", "#603028")
# right house
house(88, 86, 18, 12, "#8a6a4a", "#6e3a34", "#3a2a1c", "#5a2c28")

# ---- chimneys + smoke ----
def chimney(x, y):
    c.rect(x, y, 3, 5, "#5a4a44")
    c.rect(x, y, 3, 1, "#6e5c54")

chimney(60, 70)
chimney(96, 78)
chimney(28, 76)

def smoke(x, y, col="#e8d8d0"):
    c.set(x, y, col)
    c.set(x + 1, y - 1, col)
    c.set(x + 2, y - 3, col)
    c.set(x + 1, y - 5, col)
    c.set(x + 3, y - 7, col)
    c.set(x + 2, y - 9, col)
    c.set(x + 4, y - 11, col)
    c.set(x + 3, y - 13, col)

smoke(61, 69)
smoke(97, 77, "#d8ccc8")
smoke(29, 75, "#d8ccc8")

# ---- warm light haze around focal house ----
for i, col in enumerate(["#f8c876", "#f2a15f"]):
    r = 16 - i * 4
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            if dx * dx + dy * dy <= r * r:
                pass  # keep it subtle; skip haze fill

# birds
for (bx, by) in [(40, 30), (46, 34), (90, 26)]:
    c.line(bx - 2, by, bx, by - 1, "#3a2438")
    c.line(bx, by - 1, bx + 2, by, "#3a2438")

print(c.stats_text())
save("mountain-village-sunrise", c)
finish(c)
