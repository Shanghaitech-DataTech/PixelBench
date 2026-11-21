from pixelbench_api import *

out = input_canvas.copy(name='output')

# ====== COLOR REGISTRATION ======
blood_red     = out.color((160, 12, 30))
blood_dark    = out.color((95, 10, 25))
blood_lite    = out.color((210, 30, 45))
dark_bg       = out.color((32, 6, 15))
dark_bg2      = out.color((20, 4, 10))
dark_bg3      = out.color((42, 10, 20))
black_castle  = out.color((14, 4, 12))
dark_castle   = out.color((24, 7, 18))
dark_castle2  = out.color((20, 5, 14))
mid_castle    = out.color((36, 10, 22))
glow_window  = out.color((230, 100, 40))
glow_window2 = out.color((190, 55, 25))
star_col     = out.color((255, 230, 120))
water_dark   = out.color((22, 4, 10))
water_red    = out.color((45, 10, 18))
water_r      = out.color((70, 15, 25))
si_building = out.color((20, 5, 13))
purple_tint = out.color((30, 5, 35))

import random
random.seed(42)

# ====== 1. BACKGROUND ======
for y in range(128):
    for x in range(256):
        if y < 6:
            out.set(x, y, dark_bg3)
        elif y < 22:
            out.set(x, y, dark_bg)
        elif y < 42:
            out.set(x, y, dark_bg2)
        elif y < 55:
            out.set(x, y, dark_bg)
        elif y < 62:
            # horizon
            out.set(x, y, (24, 5, 12))
        else:
            # water area - subtle darkening gradient
            t = (y - 62) / 66.0
            r = int(28 - 14 * t)
            g = int(5 - 2 * t)
            b = int(10 - 5 * t)
            out.set(x, y, (r, g, b))

# ====== 2. BLOOD MOON ======
moon_cx, moon_cy = 172, 28
moon_r = 23
# Halo ring
out.circle(moon_cx, moon_cy, moon_r + 6, blood_dark, fill=False)
out.circle(moon_cx, moon_cy, moon_r, blood_red, fill=True)
# Craters
for cx_, cy_, cr in [(8, -5, 3), (-7, 6, 4), (5, 7, 3), (-10, -8, 3), (0, 1, 2), (-3, 10, 2), (10, -10, 2)]:
    out.circle(moon_cx + cx_, moon_cy + cy_, cr, blood_dark, fill=True)
# Bright rim highlight
out.ellipse(moon_cx - 8, moon_cy - 13, 11, 7, blood_lite, fill=False)
out.circle(moon_cx - 12, moon_cy - 14, 2, blood_lite, fill=True)
out.circle(moon_cx - 6, moon_cy - 16, 2, blood_lite, fill=True)

# ====== 3. STARS ======
for i in range(55):
    sx = random.randint(0, 255)
    sy = random.randint(0, 52)
    if (sx - moon_cx)**2 + (sy - moon_cy)**2 > (moon_r + 10)**2:
        out.set(sx, sy, star_col)

# ====== 4. DISTANT SILHOUETTES ======
for bx, bw, bh in [(0, 8, 8), (10, 7, 13), (22, 10, 7), (35, 7, 15),
                    (50, 8, 8), (62, 7, 17), (75, 12, 10), (90, 8, 7),
                    (135, 8, 11), (148, 10, 9), (158, 7, 14),
                    (196, 12, 12), (212, 7, 13), (224, 10, 8), (238, 9, 14), (248, 8, 9)]:
    out.rect(bx, 55 - bh, bw, bh + 2, si_building, fill=True)

# ====== 5. CASTLE ======
cx, cy = 100, 65

# === Main keep: large central structure ===
out.rect(cx, cy, 55, 38, black_castle, fill=True)
# Central tower
out.rect(cx + 17, cy - 28, 22, 28, black_castle, fill=True)
# Tall central spire
out.poly([(cx+19, cy-20), (cx+28, cy-44), (cx+37, cy-20)], dark_castle, fill=True)
# Spire tip - thin
out.poly([(cx+26, cy-44), (cx+28, cy-52), (cx+30, cy-44)], dark_castle2, fill=True)
# Spire highlights
out.line(cx+22, cy-35, cx+26, cy-28, dark_castle2)

# === Left tower ===
out.rect(cx - 32, cy + 5, 30, 33, black_castle, fill=True)
out.rect(cx - 26, cy - 10, 18, 15, black_castle, fill=True)
out.poly([(cx-24, cy-8), (cx-17, cy-26), (cx-10, cy-8)], dark_castle, fill=True)

# === Right tower ===
out.rect(cx + 55, cy + 5, 30, 33, black_castle, fill=True)
out.rect(cx + 63, cy - 10, 18, 15, black_castle, fill=True)
out.poly([(cx+65, cy-8), (cx+72, cy-26), (cx+79, cy-8)], dark_castle, fill=True)

# === Far left tower ===
out.rect(cx - 62, cy + 12, 24, 25, black_castle, fill=True)
out.poly([(cx-58, cy+12), (cx-50, cy-10), (cx-42, cy+12)], dark_castle, fill=True)

# === Far right tower ===
out.rect(cx + 90, cy + 12, 24, 25, black_castle, fill=True)
out.poly([(cx+94, cy+12), (cx+102, cy-10), (cx+110, cy+12)], dark_castle, fill=True)

# === Connecting walls ===
out.rect(cx - 62, cy + 18, 175, 20, black_castle, fill=True)

# === Battlements ===
for wx in range(cx - 62, cx + 113, 9):
    out.rect(wx, cy + 14, 5, 4, black_castle, fill=True)

# === Far corner turrets ===
out.rect(3, cy + 18, 16, 20, black_castle, fill=True)
out.poly([(5, cy+18), (11, cy+2), (17, cy+18)], dark_castle, fill=True)

out.rect(238, cy + 18, 16, 20, black_castle, fill=True)
out.poly([(240, cy+18), (246, cy+2), (252, cy+18)], dark_castle, fill=True)

# === Mid turrets ===
out.rect(cx - 90, cy + 16, 18, 22, black_castle, fill=True)
out.poly([(cx-88, cy+16), (cx-81, cy+0), (cx-74, cy+16)], dark_castle, fill=True)

out.rect(cx + 123, cy + 16, 18, 22, black_castle, fill=True)
out.poly([(cx+125, cy+16), (cx+132, cy+0), (cx+139, cy+16)], dark_castle, fill=True)

# === Additional small tower between left and main ===
out.rect(cx - 5, cy + 10, 8, 30, black_castle, fill=True)
out.poly([(cx-3, cy+10), (cx-1, cy-3), (cx+1, cy+10)], dark_castle2, fill=True)

# === Small tower between right and main ===
out.rect(cx + 48, cy + 10, 8, 30, black_castle, fill=True)
out.poly([(cx+50, cy+10), (cx+52, cy-3), (cx+54, cy+10)], dark_castle2, fill=True)

# === Small tower on far left wall ===
out.rect(cx - 48, cy + 12, 10, 26, black_castle, fill=True)
out.poly([(cx-46, cy+12), (cx-43, cy-2), (cx-40, cy+12)], dark_castle2, fill=True)

# === Small tower on far right wall ===
out.rect(cx + 78, cy + 12, 10, 26, black_castle, fill=True)
out.poly([(cx+80, cy+12), (cx+83, cy-2), (cx+86, cy+12)], dark_castle2, fill=True)

# === Far far left tower ===
out.rect(25, cy + 16, 20, 22, black_castle, fill=True)

# === Far far right tower ===
out.rect(213, cy + 16, 20, 22, black_castle, fill=True)

# === Tower on far left horizon ===
out.rect(55, cy + 12, 14, 26, black_castle, fill=True)
out.poly([(57, cy+12), (62, cy-4), (67, cy+12)], dark_castle, fill=True)

# === Tower on far right horizon ===
out.rect(187, cy + 12, 14, 26, black_castle, fill=True)
out.poly([(189, cy+12), (194, cy-4), (199, cy+12)], dark_castle, fill=True)

# ====== 6. GLOWING WINDOWS ======
# Main keep
for wy in range(cy + 5, cy + 32, 8):
    out.rect(cx + 12, wy, 3, 4, glow_window, fill=True)
    out.rect(cx + 28, wy, 3, 4, glow_window, fill=True)
    out.rect(cx + 40, wy, 3, 4, glow_window, fill=True)
    out.rect(cx + 8, wy, 3, 2, glow_window2, fill=True)
    out.rect(cx + 45, wy, 3, 2, glow_window2, fill=True)

# Left tower
for wy in range(cy + 10, cy + 34, 8):
    out.rect(cx - 22, wy, 3, 4, glow_window, fill=True)
    out.rect(cx - 15, wy, 3, 2, glow_window2, fill=True)

# Right tower
for wy in range(cy + 10, cy + 34, 8):
    out.rect(cx + 65, wy, 3, 4, glow_window, fill=True)
    out.rect(cx + 72, wy, 3, 2, glow_window2, fill=True)

# Far towers
for wy in range(cy + 16, cy + 34, 8):
    out.rect(cx - 52, wy, 3, 3, glow_window, fill=True)
    out.rect(cx + 96, wy, 3, 3, glow_window, fill=True)

# Wall windows
out.rect(cx + 55, cy + 22, 3, 4, glow_window, fill=True)
out.rect(cx + 20, cy + 25, 3, 3, glow_window2, fill=True)
out.rect(cx + 48, cy + 22, 3, 2, glow_window2, fill=True)
out.rect(cx - 42, cy + 22, 3, 3, glow_window, fill=True)

# Small tower windows
out.rect(cx - 3, cy + 16, 2, 3, glow_window, fill=True)
out.rect(cx + 52, cy + 16, 2, 3, glow_window, fill=True)

# Corner turret windows
out.rect(8, cy + 22, 2, 3, glow_window, fill=True)
out.rect(244, cy + 22, 2, 3, glow_window, fill=True)

# ====== 7. WATER REFLECTIONS ======
# Moon reflection streaks
for i, rx in enumerate(range(moon_cx - 14, moon_cx + 14, 3)):
    rlen = random.randint(6, 12)
    for ry in range(65, 65 + rlen):
        intensity = 1.0 - (ry - 65) / 16.0
        if intensity > 0.25:
            rr = int(65 * intensity)
            gg = int(10 * intensity)
            bb = int(18 * intensity)
            out.set(rx, ry, (rr, gg, bb))

# Castle reflection
for rx in range(cx - 20, cx + 60, 5):
    for ry in range(70, 72 + random.randint(3, 8)):
        if random.random() < 0.4:
            out.set(rx, ry, water_r)

# Water shimmer
for i in range(25):
    wx = random.randint(0, 255)
    wy = random.randint(66, 125)
    out.set(wx, wy, water_red)

# ====== 8. EMBERS ======
for i in range(25):
    ex = random.randint(5, 250)
    ey = random.randint(50, 125)
    c = random.choice([(255, 140, 30), (230, 60, 20), (255, 180, 50), (200, 40, 15)])
    out.set(ex, ey, c)
    
# ====== 9. ADD PURPLE HAZE NEAR CASTLE ======
# A subtle purple energy glow around the castle
for t in range(8):
    hx = random.randint(cx - 60, cx + 110)
    hy = random.randint(cy - 30, cy + 30)
    out.set(hx, hy, purple_tint)

finish(out)
print("Done")
print(out.stats_text())
