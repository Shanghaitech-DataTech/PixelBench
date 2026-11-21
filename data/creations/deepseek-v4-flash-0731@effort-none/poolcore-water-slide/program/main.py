from pixelbench_api import *
import math
import random

W, H = 128, 128
c = new_canvas(W, H, name="poolcore")

# ----- Palette (well under 86 limit) -----
C = {}
C['wall_top']   = (210, 224, 234)
C['tile_light'] = (226, 234, 242)
C['tile_dark']  = (195, 211, 225)
C['tile_line']  = (170, 190, 208)
C['floor_light']= (183, 203, 218)
C['floor_dark'] = (165, 187, 204)
C['colm_tile']  = (215, 226, 236)
C['colm_shade'] = (188, 203, 218)
C['light_glow'] = (240, 244, 250)
C['light_white']= (252, 252, 252)

C['w1'] = (165, 210, 233)
C['w2'] = (130, 188, 220)
C['w3'] = (100, 165, 205)
C['w4'] = (70, 140, 188)
C['w5'] = (48, 112, 165)
C['w6'] = (35, 88, 140)

C['wgrid'] = (85, 152, 198)
C['refl']   = (200, 228, 240)
C['ripple'] = (165, 215, 238)
C['ripple2']= (155, 205, 230)
C['ripple3']= (140, 195, 222)

C['slide_w']  = (245, 247, 250)
C['slide_s']  = (210, 215, 222)
C['slide_d']  = (175, 183, 195)
C['slide_uw'] = (185, 205, 220)

C['ring']    = (240, 205, 60)
C['ring_d']  = (205, 170, 40)
C['ring_h']  = (250, 228, 120)
C['ring_red']= (200, 90, 80)

C['skin']    = (152, 120, 105)
C['skin_d']  = (125, 100, 86)
C['hair']    = (72, 57, 47)
C['hair_l']  = (95, 78, 62)
C['suit']    = (60, 110, 160)
C['suit_d']  = (45, 85, 125)

C['ring_refl'] = (205, 180, 80)
C['water_line']= (180, 215, 235)  # water surface edge color

# ===== CEILING (y 0-16) =====
c.rect(0, 0, 128, 16, C['wall_top'])
# Ceiling tiles
for x in range(0, 128, 16):
    c.line(x, 0, x, 16, C['tile_line'])
c.line(0, 8, 127, 8, C['tile_line'])

# Fluorescent light bars
c.rect(22, 2, 84, 5, C['light_glow'])
c.rect(24, 3, 80, 3, C['light_white'])
c.rect(22, 10, 84, 4, C['light_glow'])
c.rect(24, 10, 80, 2, C['light_white'])
# Ceiling light glow spread
for x in range(20, 100):
    c.set(x, 15, C['light_glow'])

# ===== UPPER WALL (y 16-58) =====
for y in range(16, 58):
    for x in range(0, 128):
        tx = (x // 16) % 2
        ty = ((y - 16) // 10) % 2
        if (tx + ty) % 2 == 0:
            c.set(x, y, C['tile_light'])
        else:
            c.set(x, y, C['tile_dark'])

# Wall tile grid
for x in range(0, 128, 16):
    c.line(x, 16, x, 58, C['tile_line'])
for y in range(16, 58, 10):
    c.line(0, y, 127, y, C['tile_line'])

# Light glow wash on wall
for y in range(16, 34):
    for x in range(24, 104):
        if y < 22:
            c.set(x, y, C['light_glow'])
        elif y < 28:
            c.set(x, y, C['tile_light'])

# ===== TILED COLUMNS =====
# Left column
for y in range(16, 58):
    for x in range(6, 22):
        if ((x // 4) + (y // 4)) % 2 == 0:
            c.set(x, y, C['colm_tile'])
        else:
            c.set(x, y, C['colm_shade'])
    c.set(21, y, C['colm_shade'])
for y in range(16, 58):
    c.set(7, y, C['colm_shade'])

# Right column
for y in range(16, 58):
    for x in range(108, 122):
        if ((x // 4) + (y // 4)) % 2 == 0:
            c.set(x, y, C['colm_tile'])
        else:
            c.set(x, y, C['colm_shade'])
    c.set(108, y, C['colm_shade'])
for y in range(16, 58):
    c.set(120, y, C['colm_shade'])

# ===== FLOOR EDGE / POOL DECK (y 58-68) =====
# Near perspective floor tiles
for y in range(58, 68):
    for x in range(0, 128):
        tx = (x // 16) % 2
        ty = ((y - 58) // 5) % 2
        if (tx + ty) % 2 == 0:
            c.set(x, y, C['floor_light'])
        else:
            c.set(x, y, C['floor_dark'])
for x in range(0, 128, 16):
    c.line(x, 58, x, 68, C['tile_line'])

# ===== POOL WATER (y 68-127) =====
water_bands = [
    (68, 75, C['w1']),
    (76, 85, C['w2']),
    (86, 96, C['w3']),
    (97, 108, C['w4']),
    (109, 118, C['w5']),
    (119, 127, C['w6']),
]
for y0, y1, wcol in water_bands:
    c.rect(0, y0, 128, y1 - y0 + 1, wcol)

# ===== POOL BOTTOM TILE GRID =====
for y in range(76, 128, 13):
    c.line(0, y, 127, y, C['wgrid'])
for x in range(0, 128, 16):
    c.line(x, 76, x, 127, C['wgrid'])

# Lighter tile patches on the pool bottom (checked pattern through clear water)
for ty_ in range(4):
    for tx_ in range(8):
        if (tx_ + ty_) % 2 == 0:
            sx = tx_ * 16
            sy = 76 + ty_ * 13
            # lighten the center of the square
            for ly in range(sy+2, min(sy+7, 128)):
                for lx in range(sx+2, min(sx+7, 128)):
                    c.set(lx, ly, C['wgrid'])
        else:
            # some tiles slightly darker
            sx = tx_ * 16
            sy = 76 + ty_ * 13
            for ly in range(sy+2, min(sy+7, 128)):
                for lx in range(sx+2, min(sx+7, 128)):
                    px = c.get(lx, ly)
                    c.set(lx, ly, C['w3'])

# ===== WATER SURFACE EDGE =====
c.line(0, 68, 127, 68, C['water_line'])
# Sparkle along the edge
for x in range(0, 128, 3):
    c.set(x, 68, C['refl'])
for x in range(1, 128, 5):
    c.set(x, 69, C['light_glow'])

# ===== LIGHT REFLECTIONS ON WATER =====
# Broad light columns from the ceiling
for x in range(30, 96, 6):
    c.line(x, 69, x, 82, C['refl'])
# Narrow bright streaks
for x in range(35, 92, 4):
    c.line(x, 68, x, 74, C['light_glow'])

# ===== AMBIENT RIPPLES =====
for rx_, ry_, rcol in [
    (14, 11, C['ripple']),
    (22, 17, C['ripple2']),
    (30, 23, C['ripple3']),
]:
    c.ellipse(80, 92, rx_, ry_, rcol, fill=False)

# Smaller ripples scattered
c.ellipse(30, 90, 10, 6, C['ripple2'], fill=False)
c.ellipse(105, 100, 8, 5, C['ripple3'], fill=False)
c.ellipse(65, 82, 6, 4, C['ripple'], fill=False)

# ===== WATER SLIDE =====
# Compute slide curve through the scene
slide_pts = []
for t in range(0, 101, 2):
    tt = t / 100.0
    x = (1-tt)**3 * 14 + 3*(1-tt)**2*tt * 8 + 3*(1-tt)*tt**2 * 28 + tt**3 * 50
    y = (1-tt)**3 * 24 + 3*(1-tt)**2*tt * 46 + 3*(1-tt)*tt**2 * 76 + tt**3 * 110
    slide_pts.append((x, y))

# Slide entrance structure (top of slide on wall)
# A small opening/structure on the wall where the slide exits
c.rect(8, 20, 14, 8, C['slide_w'])
c.rect(8, 20, 14, 2, C['slide_d'])
c.rect(8, 26, 14, 2, C['colm_shade'])

# Main slide tube (filled circles along the curve)
r_start, r_end = 6, 9
for i, (x, y) in enumerate(slide_pts):
    t_idx = i / (len(slide_pts) - 1)
    r = int(r_start + (r_end - r_start) * t_idx)
    c.circle(int(x), int(y), r, C['slide_w'])

# Slide underside shading
for i, (x, y) in enumerate(slide_pts):
    t_idx = i / (len(slide_pts) - 1)
    r = r_start + (r_end - r_start) * t_idx
    for dy_ in range(1, int(r)+1):
        for dx_ in range(-int(r), int(r)+1):
            if dx_*dx_ + dy_*dy_ <= r*r and dy_ > int(r*0.35):
                px, py = int(x) + dx_, int(y) + dy_
                if 0 <= px < 128 and 0 <= py < 128:
                    c.set(px, py, C['slide_s'])

# Darker lower edge shadow
for i, (x, y) in enumerate(slide_pts):
    t_idx = i / (len(slide_pts) - 1)
    r = r_start + (r_end - r_start) * t_idx
    for dx_ in range(-int(r*0.5), int(r*0.5)+1):
        for shift in range(3):
            px, py = int(x) + dx_, int(y) + int(r) - shift
            if 0 <= px < 128 and 0 <= py < 128:
                c.set(px, py, C['slide_d'])

# Slide top highlight line
for i in range(0, len(slide_pts), 1):
    x, y = slide_pts[i]
    t_idx = i / (len(slide_pts) - 1)
    r = r_start + (r_end - r_start) * t_idx
    for dx_ in range(-int(r*0.6), int(r*0.6)+1):
        py = int(y) - int(r*0.5)
        px = int(x) + dx_
        if 0 <= px < 128 and 0 <= py < 128:
            c.set(px, py, C['light_white'])

# ===== SUBMERGED PART OF SLIDE =====
for y in range(80, 128):
    for x in range(28, 68):
        px = c.get(x, y)
        pr, pg, pb, pa = c.palette()[px]['rgba']
        if pa > 0 and pr > 150:
            c.set(x, y, C['slide_uw'])

# More water transparency on submerged slide (darker for deeper)
for y in range(90, 128):
    for x in range(32, 66):
        px = c.get(x, y)
        pr, pg, pb, pa = c.palette()[px]['rgba']
        if pa > 0 and pr > 130:
            c.set(x, y, C['w4'])

# Ripple at slide entry
c.ellipse(52, 102, 10, 5, C['ripple'], fill=False)
c.ellipse(52, 102, 16, 8, C['ripple2'], fill=False)
c.ellipse(52, 102, 22, 11, C['ripple3'], fill=False)

# ===== GIRL IN YELLOW SWIM RING =====
gx, gy = 80, 96

# ===== RIPPLES around girl =====
c.ellipse(gx, gy+1, 15, 11, C['ripple'], fill=False)
c.ellipse(gx, gy+1, 22, 16, C['ripple2'], fill=False)
c.ellipse(gx, gy+1, 30, 22, C['ripple3'], fill=False)
c.ellipse(gx, gy+1, 38, 28, C['ripple3'], fill=False)

# (ring reflection handled after drawing girl)

# ===== GIRL'S BACK VIEW =====
# Place girl higher and body more visible with natural round shapes

# ===== RING REFLECTION in water (subtle silhouette streak) =====
# Very subtle thin horizontal streaks below the ring
c.ellipse(gx, gy + 12, 9, 2, C['ring_refl'], fill=False)
c.ellipse(gx+1, gy + 15, 7, 2, C['ring_refl'], fill=False)
c.ellipse(gx+1, gy + 19, 5, 2, C['ring_refl'], fill=False)

# ===== YELLOW SWIM RING (draw ring first, above the reflection) =====
# Outer ring ellipse
c.ellipse(gx, gy, 13, 10, C['ring'])
# Inner hole (fill with water)
for yy_ in range(gy-7, gy+8):
    for xx_ in range(gx-8, gx+9):
        if ((xx_-gx)**2)/7**2 + ((yy_-gy)**2)/5.5**2 < 1.0:
            c.set(xx_, yy_, C['w3'])

# ===== GIRL'S BODY visible through ring opening =====
# Torso (swimsuit back) in ring
c.ellipse(gx, gy+2, 4, 5, C['suit'])
# Swimsuit highlight
c.ellipse(gx-1, gy+1, 2, 3, C['suit_d'])

# Shoulders visible above ring 
c.ellipse(gx, gy-2, 5, 3, C['skin'])

# Neck
c.rect(gx-1, gy-8, 3, 7, C['skin'])

# Head (round, from behind, hair)
c.circle(gx, gy-11, 5, C['hair'])
# Hair sheen on top
c.circle(gx, gy-12, 4, C['hair_l'])
# Hair shine highlight details
c.circle(gx-2, gy-13, 2, C['hair_l'])
c.circle(gx+1, gy-14, 2, C['hair_l'])

# Hair falling down around the head in strands
c.set(gx-4, gy-13, C['hair'])
c.set(gx-5, gy-12, C['hair'])
c.set(gx+4, gy-13, C['hair'])
c.set(gx+5, gy-12, C['hair'])

# Hair cascade over shoulders
c.path(f"M {gx-6} {gy-8} Q {gx-7} {gy-3} {gx-5} {gy+1}", C['hair'], fill=False)
c.path(f"M {gx+6} {gy-8} Q {gx+7} {gy-3} {gx+5} {gy+1}", C['hair'], fill=False)
# Some hair strands near shoulders
c.set(gx-6, gy-5, C['hair'])
c.set(gx-6, gy-3, C['hair'])
c.set(gx+6, gy-5, C['hair'])
c.set(gx+6, gy-3, C['hair'])

# Swimsuit straps
c.line(gx-4, gy-4, gx-2, gy, C['suit_d'])
c.line(gx+4, gy-4, gx+2, gy, C['suit_d'])

# Arms draped over the ring
c.line(gx-11, gy-1, gx-5, gy-4, C['skin'])
c.line(gx+11, gy-1, gx+5, gy-4, C['skin'])

# ===== Ring details =====
# Highlight arc top-left
c.path(f"M {gx-12} {gy-3} A 10 8 0 0 1 {gx-4} {gy-8}", C['ring_h'], fill=False)

# Ring dark lower-right
c.path(f"M {gx+4} {gy+8} A 10 7 0 0 1 {gx-5} {gy+7}", C['ring_d'], fill=False)

# Red segments on ring (red strips on yellow ring)
for seg_ang in [30, 120, 210, 300]:
    for a10 in range(int((seg_ang-15)*10), int((seg_ang+15)*10), 5):
        ang = a10 / 10.0
        for rr in range(7, 10):
            rx = int(gx + rr * math.cos(math.radians(ang)))
            ry = int(gy + rr * math.sin(math.radians(ang)) * 0.77)
            if 0 <= rx < 128 and 0 <= ry < 128:
                c.set(rx, ry, C['ring_red'])

# Ring inner edge highlight
c.path(f"M {gx-6} {gy+7} A 7 5 0 0 0 {gx-2} {gy+8}", C['ring_h'], fill=False)

# ===== POOL COLUMN REFLECTIONS =====
for x in range(8, 22, 2):
    for y in range(70, 84, 2):
        c.set(x, y, C['refl'])
for x in range(118, 126, 2):
    for y in range(70, 84, 2):
        c.set(x, y, C['refl'])

# ===== ATMOSPHERIC WATER DETAILS =====
# Subtle water shimmer/sparkle
for _ in range(30):
    rx_ = random.randint(5, 122)
    ry_ = random.randint(70, 115)
    c.set(rx_, ry_, random.choice([C['refl'], C['ripple'], C['ripple2']]))

# ===== DREAMY ATMOSPHERE: subtle overall light fading =====
# Water surface reflection of the white ceiling lights spreading near the surface
for y in range(68, 78):
    for x in range(36, 94, 2):
        if (x + y) % 3 == 0:
            c.set(x, y, C['refl'])

# Haze near the ceiling/wall transition
for y in range(16, 24):
    for x in range(40, 88):
        if y < 20:
            c.set(x, y, C['light_glow'])

# Subtle dreamy glow around the light fixtures
for x in range(24, 104):
    c.set(x, 16, C['light_glow'])

# ===== STATS =====
print(c.stats_text())

result = c
finish(result)
