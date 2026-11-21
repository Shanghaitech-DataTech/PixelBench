from pixelbench_api import *
import math

c = new_canvas(128, 128, "#000000")

# Palette definition - Poolcore aesthetic (Strict limit <= 86)
P = {
    # Deep voids & corridor
    'void_black': '#040b10',
    'void_deep': '#07151e',
    'void_dark': '#0d212b',
    'void_mid': '#16323f',
    
    # Blue mosaic tiles (walls, columns, coping, walkway)
    'grout': '#285365',
    'tile_dark': '#3e788e',
    'tile_mid': '#5a9cb2',
    'tile_base': '#7cbfd3',
    'tile_light': '#a2dbec',
    'tile_pale': '#cbeff7',
    'tile_white': '#ebf9fc',
    'tile_bright': '#ffffff',
    
    # Ceiling & Fluorescent lights
    'ceil_dark': '#486470',
    'ceil_mid': '#708e9a',
    'ceil_light': '#9fc0cc',
    'ceil_bright': '#cfe3eb',
    'light_glow': '#8de6f5',
    'light_bright': '#d8f8ff',
    'light_core': '#ffffff',
    
    # Submerged Pool Floor & Water (crystal clear pale blue)
    'under_deep': '#0e2f3c',
    'under_dark': '#144252',
    'under_mid': '#1e5c70',
    'under_base': '#2c7c94',
    'under_light': '#409cb5',
    'under_pale': '#62c2da',
    'under_shallow': '#8de0f1',
    'caustic_soft': '#aaeaf6',
    
    # Water Surface, Ripples & Reflections
    'surf_dark': '#205a6d',
    'surf_light': '#bbf3fd',
    'surf_bright': '#e2faff',
    'surf_shimmer': '#ffffff',
    
    # White Water Slide (3D fiberglass flume)
    'slide_shadow_deep': '#223842',
    'slide_shadow_med': '#3a5766',
    'slide_shadow_lgt': '#587a8b',
    'slide_body': '#8ca8b6',
    'slide_light': '#c5dbe4',
    'slide_white': '#eef5f8',
    'slide_highlight': '#ffffff',
    'slide_water': '#4ecde4',
    'slide_water_hi': '#bdf4fd',
    'slide_support': '#2a4450',
    
    # Yellow Swim Ring
    'ring_shadow': '#5c3100',
    'ring_dark': '#965702',
    'ring_base': '#dc9407',
    'ring_light': '#fed41e',
    'ring_bright': '#ffed5c',
    'ring_high': '#fffce6',
    
    # The Girl
    'hair_black': '#101015',
    'hair_dark': '#221c24',
    'hair_mid': '#403241',
    'hair_light': '#665368',
    'skin_shadow': '#8c5243',
    'skin_mid': '#c47866',
    'skin_light': '#ebb09c',
    'skin_high': '#fce3da',
    'suit_dark': '#152d3f',
    'suit_strap': '#de586a',
    
    # Chrome metal
    'chrome_dark': '#283f4a',
    'chrome_light': '#b0cfdc',
    'chrome_bright': '#ffffff',
}

# Pre-register colors
for name, hex_val in P.items():
    c.color(hex_val, name)

# -------------------------------------------------------------
# 1. CEILING (y: 0 to 22)
# -------------------------------------------------------------
for y in range(23):
    if y < 4:
        col = P['ceil_dark']
    elif y < 10:
        col = P['ceil_mid']
    elif y < 16:
        col = P['ceil_light']
    else:
        col = P['ceil_bright']
    c.line(0, y, 127, y, col)

# Ceiling tile joints
for x in range(0, 128, 16):
    c.line(x, 0, x, 22, P['ceil_dark'])
for y in range(0, 23, 7):
    c.line(0, y, 127, y, P['ceil_dark'])

# Fluorescent Light Fixtures (recessed cool strip fixtures)
for fx, fw in [(18, 30), (74, 34)]:
    c.rect(fx - 2, 6, fw + 4, 6, P['light_glow'])
    c.rect(fx, 7, fw, 4, P['light_bright'])
    c.rect(fx + 2, 8, fw - 4, 2, P['light_core'])

# -------------------------------------------------------------
# 2. FAR WALL & TILED ARCHWAY (y: 23 to 48)
# -------------------------------------------------------------
# Wall mosaic tiles (4x4 tile grid)
for ty in range(23, 49, 4):
    for tx in range(0, 128, 4):
        col = P['tile_base'] if ((tx // 4 + ty // 4) % 2 == 0) else P['tile_light']
        c.rect(tx, ty, 4, 4, col)
        c.set(tx, ty, P['tile_pale'])
        c.line(tx, ty + 3, tx + 3, ty + 3, P['grout'])
        c.line(tx + 3, ty, tx + 3, ty + 3, P['grout'])

# Central Liminal Archway (x: 48 to 74, y: 23 to 48)
arch_x = 48
arch_w = 26
arch_r = 13
arch_cx = arch_x + arch_r # 61
arch_cy = 23 + arch_r    # 36

# Arch opening - interior deep flooded hall
# Draw only upper half circle plus rectangle down to 48
for dy in range(-arch_r, 1):
    dx_max = int(math.sqrt(arch_r * arch_r - dy * dy))
    c.line(arch_cx - dx_max, arch_cy + dy, arch_cx + dx_max, arch_cy + dy, P['void_deep'])
c.rect(arch_x, arch_cy, arch_w + 1, 49 - arch_cy, P['void_deep'])

# Inside arch: flooded water floor extending into the distance
c.rect(arch_x, 42, arch_w + 1, 7, P['void_dark'])
c.rect(arch_x + 2, 44, arch_w - 3, 5, P['under_deep'])

# Distant illuminated passage deep in the corridor
c.rect(arch_cx - 4, 32, 8, 11, P['void_black'])
c.circle(arch_cx, 32, 4, P['void_black'], fill=True)
c.rect(arch_cx - 2, 33, 4, 8, P['light_glow'])
c.line(arch_cx - 1, 34, arch_cx + 1, 34, P['light_core'])
c.line(arch_cx - 1, 35, arch_cx + 1, 35, P['light_core'])
c.line(arch_cx - 3, 43, arch_cx + 3, 43, P['light_glow']) # water reflection

# Arch border (white tile rim - upper semicircle and vertical jambs only)
for deg in range(180, 361):
    rad = math.radians(deg)
    bx = int(round(arch_cx + math.cos(rad) * (arch_r + 1)))
    by = int(round(arch_cy + math.sin(rad) * (arch_r + 1)))
    if by >= 23:
        c.set(bx, by, P['tile_white'])
    gx = int(round(arch_cx + math.cos(rad) * (arch_r + 2)))
    gy = int(round(arch_cy + math.sin(rad) * (arch_r + 2)))
    if gy >= 23:
        c.set(gx, gy, P['grout'])

c.line(arch_x - 1, arch_cy, arch_x - 1, 48, P['tile_white'])
c.line(arch_x + arch_w + 1, arch_cy, arch_x + arch_w + 1, 48, P['tile_white'])
c.line(arch_x - 2, arch_cy, arch_x - 2, 48, P['grout'])
c.line(arch_x + arch_w + 2, arch_cy, arch_x + arch_w + 2, 48, P['grout'])

# Clean up ceiling overlap above y=23
for y in range(0, 23):
    for x in range(arch_x - 4, arch_x + arch_w + 5):
        if y < 4:
            c.set(x, y, P['ceil_dark'])
        elif y < 10:
            c.set(x, y, P['ceil_mid'])
        elif y < 16:
            c.set(x, y, P['ceil_light'])
        else:
            c.set(x, y, P['ceil_bright'])

# -------------------------------------------------------------
# 3. TILED COLUMNS & WALKWAY
# -------------------------------------------------------------
def draw_column(cx0, cx1, cy0, cy1):
    w = cx1 - cx0
    for y in range(cy0, cy1):
        for x in range(cx0, cx1):
            rel = (x - cx0) / float(w)
            if rel < 0.2:
                col = P['tile_white']
            elif rel < 0.45:
                col = P['tile_light']
            elif rel < 0.75:
                col = P['tile_base']
            else:
                col = P['tile_dark']
            c.set(x, y, col)
            if y % 4 == 0 or x % 4 == 0:
                c.set(x, y, P['grout'])
    c.line(cx0, cy0, cx0, cy1 - 1, P['tile_bright'])
    c.line(cx1 - 1, cy0, cx1 - 1, cy1 - 1, P['grout'])

# Left column
draw_column(10, 22, 16, 52)
# Right column
draw_column(106, 118, 16, 52)

# Back pool coping / rim across y = 48 to 51
c.rect(0, 48, 128, 2, P['tile_white'])
c.line(0, 48, 127, 48, P['tile_bright'])
c.rect(0, 50, 128, 2, P['tile_dark'])
c.line(0, 51, 127, 51, P['grout'])

# Left walkway (x: 0 to 12, y: 52 to 127)
for y in range(52, 128):
    for x in range(12):
        col = P['tile_light'] if ((x // 4 + y // 4) % 2 == 0) else P['tile_base']
        c.set(x, y, col)
        if x % 4 == 0 or y % 4 == 0:
            c.set(x, y, P['grout'])
    c.set(11, y, P['tile_white'])
    c.set(12, y, P['tile_dark'])

# Chrome pool ladder
c.line(9, 66, 9, 78, P['chrome_bright'])
c.line(8, 66, 8, 78, P['chrome_dark'])
c.line(13, 70, 13, 86, P['chrome_bright'])
c.line(14, 70, 14, 86, P['chrome_dark'])
c.line(9, 66, 11, 64, P['chrome_bright'])
c.line(11, 64, 13, 70, P['chrome_bright'])
c.line(12, 75, 14, 75, P['chrome_light'])
c.line(12, 80, 14, 80, P['chrome_light'])

# -------------------------------------------------------------
# 4. CRYSTAL CLEAR WATER & UNDERWATER POOL FLOOR (y: 52 to 127)
# -------------------------------------------------------------
for y in range(52, 128):
    t = (y - 52) / 76.0
    if t < 0.12:
        col = P['under_shallow']
    elif t < 0.3:
        col = P['under_pale']
    elif t < 0.55:
        col = P['under_light']
    elif t < 0.8:
        col = P['under_base']
    else:
        col = P['under_mid']
    c.line(13, y, 127, y, col)

# Submerged Floor Perspective Tiles
vp_x, vp_y = 61, 46
y_grid_steps = [54, 57, 61, 66, 73, 81, 91, 102, 115]

# Checkerboard alternating tiles on floor
for i in range(len(y_grid_steps) - 1):
    y0 = y_grid_steps[i]
    y1 = y_grid_steps[i + 1]
    for x_idx in range(-12, 18):
        if (i + x_idx) % 2 == 0:
            shade = P['under_pale'] if y0 < 70 else (P['under_light'] if y0 < 95 else P['under_base'])
            for y in range(y0, y1):
                ty = (y - vp_y) / float(128 - vp_y)
                wobble = math.sin(y * 0.25 + x_idx * 0.8) * 1.0
                x_left = int(round(vp_x + (x_idx * 16 - vp_x) * ty + wobble))
                x_right = int(round(vp_x + ((x_idx + 1) * 16 - vp_x) * ty + wobble))
                x_left = max(13, min(127, x_left))
                x_right = max(13, min(127, x_right))
                if x_right > x_left + 1:
                    c.line(x_left + 1, y, x_right - 1, y, shade)

# Submerged grout lines (perspective diagonals)
for x_idx in range(-12, 18):
    for y in range(52, 128):
        ty = (y - vp_y) / float(128 - vp_y)
        wobble = math.sin(y * 0.25 + x_idx * 0.8) * 1.0
        px = int(round(vp_x + (x_idx * 16 - vp_x) * ty + wobble))
        if 13 <= px < 128:
            c.set(px, y, P['under_dark'])

# Submerged horizontal grid lines
for gy in y_grid_steps:
    for x in range(13, 128):
        wobble = int(round(math.sin(x * 0.18 + gy * 0.4) * 1.0))
        py = gy + wobble
        if 52 <= py < 128:
            c.set(x, py, P['under_dark'])

# Subtle, soft caustics
for y in range(55, 125, 3):
    for x in range(16, 126):
        val = math.sin(x * 0.16 + y * 0.28) * math.cos(x * 0.22 - y * 0.16)
        if val > 0.72:
            c.set(x, y, P['caustic_soft'])
            if val > 0.88 and (x + y) % 4 == 0:
                c.set(x, y, P['surf_shimmer'])

# Surface reflections of ceiling lights
for fx, fw in [(26, 14), (74, 16)]:
    for y in range(52, 85, 2):
        spread = (y - 52) * 0.1
        shimmer_x = int(fx + math.sin(y * 0.4) * (2 + spread))
        length = int(fw * (1.0 - (y - 52) / 45.0))
        if length > 0 and 13 <= shimmer_x < 128 - length:
            c.line(shimmer_x, y, shimmer_x + length, y, P['light_bright'])
            if y < 66:
                c.line(shimmer_x + 2, y, shimmer_x + length - 2, y, P['light_core'])

# -------------------------------------------------------------
# 5. WATER SLIDE: ELEGANT CURVING 3D WHITE WATER SLIDE
# -------------------------------------------------------------
def catmull_rom_2d(p0, p1, p2, p3, num_pts):
    pts = []
    for s in range(num_pts):
        t = s / float(num_pts)
        t2 = t * t
        t3 = t2 * t
        x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
        y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
        pts.append((x, y))
    return pts

waypoints = [
    (140, 10),
    (127, 16),
    (106, 26),
    (88, 42),
    (98, 60),
    (82, 76),
    (78, 84),
    (76, 92)
]

slide_path = []
for i in range(len(waypoints) - 3):
    seg = catmull_rom_2d(waypoints[i], waypoints[i+1], waypoints[i+2], waypoints[i+3], 25)
    slide_path.extend(seg)

# Support pillars holding the slide
c.rect(106, 50, 3, 24, P['slide_support'])
c.line(106, 50, 106, 74, P['slide_shadow_med'])
c.rect(88, 42, 2, 22, P['slide_support'])

# Render slide body with rich 3D shading
total_pts = len(slide_path)
for idx, (sx, sy) in enumerate(slide_path):
    t = idx / float(total_pts)
    rad = 4.4 + 1.8 * t
    ir = int(math.ceil(rad))
    ix = int(round(sx))
    iy = int(round(sy))
    
    if idx < total_pts - 1:
        tx = slide_path[idx + 1][0] - sx
        ty = slide_path[idx + 1][1] - sy
    else:
        tx = sx - slide_path[idx - 1][0]
        ty = sy - slide_path[idx - 1][1]
    
    t_len = math.hypot(tx, ty) or 1.0
    nx, ny = -ty / t_len, tx / t_len
    
    for dy in range(-ir, ir + 1):
        for dx in range(-ir, ir + 1):
            dist = math.hypot(dx, dy)
            if dist <= rad:
                px = ix + dx
                py = iy + dy
                if 0 <= px < 128 and 0 <= py < 128:
                    p_norm = (dx * nx + dy * ny) / rad
                    v_rel = dy / rad
                    
                    if dist >= rad - 1.2:
                        # Outer tube rim & shading
                        if v_rel < -0.3 or p_norm < -0.35:
                            col = P['slide_highlight']
                        elif v_rel > 0.35:
                            col = P['slide_shadow_deep']
                        elif v_rel > 0.05 or p_norm > 0.35:
                            col = P['slide_shadow_med']
                        else:
                            col = P['slide_light']
                    else:
                        # Inner flume trough
                        if v_rel > 0.35:
                            col = P['slide_shadow_med']
                        elif v_rel > -0.15:
                            # Running water inside the flume!
                            if abs(p_norm) < 0.45:
                                col = P['slide_water_hi'] if p_norm < 0.1 else P['slide_water']
                            else:
                                col = P['slide_water'] if abs(p_norm) < 0.7 else P['slide_light']
                        else:
                            col = P['slide_white']
                    c.set(px, py, col)

# Continuous highlight along the upper crest of the slide
for i in range(len(slide_path) - 1):
    sx1, sy1 = slide_path[i]
    sx2, sy2 = slide_path[i + 1]
    hx1, hy1 = int(round(sx1 - 2.5)), int(round(sy1 - 3.2))
    hx2, hy2 = int(round(sx2 - 2.5)), int(round(sy2 - 3.2))
    if 0 <= hx1 < 128 and 0 <= hy1 < 128 and 0 <= hx2 < 128 and 0 <= hy2 < 128:
        c.line(hx1, hy1, hx2, hy2, P['slide_highlight'])

# Crisp dark contour along the outer underside of the slide
for i in range(len(slide_path) - 1):
    sx, sy = slide_path[i]
    t = i / float(total_pts)
    rad = 4.4 + 1.8 * t
    bx = int(round(sx + rad * 0.7))
    by = int(round(sy + rad * 0.7))
    if 0 <= bx < 128 and 0 <= by < 128:
        c.set(bx, by, P['slide_shadow_deep'])

# Mouth of the slide entering the pool at (78, 84)
mouth_x, mouth_y = 78, 84
# Elliptical flume mouth
c.ellipse(mouth_x, mouth_y, 7, 5, P['slide_shadow_deep'], fill=True)
c.ellipse(mouth_x, mouth_y, 6, 4, P['slide_water'], fill=True)
c.ellipse(mouth_x, mouth_y - 1, 4, 2, P['slide_water_hi'], fill=True)
c.ellipse(mouth_x, mouth_y, 7, 5, P['slide_highlight'], fill=False)

# Water pouring out into pool
c.poly([(mouth_x - 4, mouth_y + 2), (mouth_x + 4, mouth_y + 2), (mouth_x + 5, mouth_y + 6), (mouth_x - 5, mouth_y + 6)], P['slide_water'], fill=True)
c.line(mouth_x - 3, mouth_y + 3, mouth_x + 3, mouth_y + 3, P['slide_water_hi'])
c.line(mouth_x - 4, mouth_y + 5, mouth_x + 4, mouth_y + 5, P['slide_water_hi'])

# Splash foam & gentle ripples at slide entry
c.ellipse(mouth_x, mouth_y + 6, 8, 3, P['surf_shimmer'], fill=False)
c.ellipse(mouth_x, mouth_y + 7, 14, 5, P['surf_light'], fill=False)
c.ellipse(mouth_x, mouth_y + 8, 20, 7, P['caustic_soft'], fill=False)

# Slide white reflection in water below x=80..95, y=86..100
for y in range(86, 102, 2):
    rx = int(82 + math.sin(y * 0.35) * 2.5)
    rw = max(2, int(10 - (y - 86) * 0.6))
    if rx + rw < 128:
        c.line(rx, y, rx + rw, y, P['slide_light'])
        c.line(rx + 1, y, rx + rw - 1, y, P['slide_white'])

# -------------------------------------------------------------
# 6. GIRL FLOATING IN YELLOW SWIM RING (Center of pool)
# -------------------------------------------------------------
gx = 50
gy = 88

# Expanding gentle ripple rings around swim ring
c.ellipse(gx, gy + 3, 20, 9, P['surf_light'], fill=False)
c.ellipse(gx, gy + 3, 27, 12, P['caustic_soft'], fill=False)
c.ellipse(gx, gy + 4, 35, 15, P['under_shallow'], fill=False)

# Soft shadow on pool floor directly below
c.ellipse(gx, gy + 16, 12, 6, P['under_deep'], fill=True)

# Submerged legs dangling through the inner ring
c.line(gx - 3, gy + 5, gx - 4, gy + 12, P['skin_shadow'])
c.line(gx + 3, gy + 5, gx + 4, gy + 13, P['skin_shadow'])
c.set(gx - 4, gy + 12, P['skin_mid'])
c.set(gx + 4, gy + 13, P['skin_mid'])

# Yellow Swim Ring (3D Torus)
ring_rx = 13
ring_ry = 8
hole_rx = 5
hole_ry = 3

for dy in range(-ring_ry, ring_ry + 1):
    for dx in range(-ring_rx, ring_rx + 1):
        outer_val = (dx / float(ring_rx))**2 + (dy / float(ring_ry))**2
        inner_val = (dx / float(hole_rx))**2 + (dy / float(hole_ry))**2
        if outer_val <= 1.0 and inner_val >= 1.0:
            px = gx + dx
            py = gy + dy + 1
            norm_y = dy / float(ring_ry)
            norm_x = dx / float(ring_rx)
            if norm_y > 0.4:
                col = P['ring_shadow'] if norm_y > 0.75 else P['ring_dark']
            elif norm_y > 0.0:
                col = P['ring_base']
            elif norm_y > -0.5:
                col = P['ring_light']
            else:
                col = P['ring_bright']
            
            # Smooth curved specular highlight on top-left of tube
            if norm_y < -0.3 and -0.8 < norm_x < 0.1:
                col = P['ring_high']
            
            c.set(px, py, col)

# Crisp white specular glints on yellow vinyl
c.line(gx - 8, gy - 3, gx - 4, gy - 4, P['light_core'])

# The Girl (Seen from behind, sitting peacefully inside the ring)
# Upper back / shoulders
c.rect(gx - 4, gy - 2, 9, 4, P['skin_mid'])
c.rect(gx - 3, gy - 2, 7, 3, P['skin_light'])
c.set(gx - 2, gy - 1, P['skin_high'])
c.set(gx + 2, gy - 1, P['skin_high'])

# Swimsuit: dark teal/navy with coral strap across back
c.rect(gx - 3, gy + 1, 7, 2, P['suit_dark'])
c.line(gx - 3, gy + 1, gx + 3, gy + 1, P['suit_strap'])

# Delicate arms resting over the yellow float
c.line(gx - 4, gy - 1, gx - 8, gy + 1, P['skin_mid'])
c.line(gx - 8, gy + 1, gx - 11, gy + 3, P['skin_light'])
c.set(gx - 11, gy + 4, P['skin_shadow']) # little hand

c.line(gx + 4, gy - 1, gx + 8, gy + 1, P['skin_mid'])
c.line(gx + 8, gy + 1, gx + 11, gy + 3, P['skin_light'])
c.set(gx + 11, gy + 4, P['skin_shadow'])

# Neck
c.rect(gx - 2, gy - 5, 5, 4, P['skin_mid'])
c.rect(gx - 1, gy - 5, 3, 3, P['skin_light'])

# Head & Hair (Dark, sleek bob hair seen from behind)
head_cx = gx
head_cy = gy - 8
head_r = 5
c.circle(head_cx, head_cy, head_r, P['hair_dark'], fill=True)
c.circle(head_cx, head_cy, head_r, P['hair_black'], fill=False)
# Lower hair line / bob cut
c.rect(head_cx - 4, head_cy + 2, 9, 3, P['hair_black'])
c.rect(head_cx - 3, head_cy + 2, 7, 2, P['hair_dark'])
# Sleek highlights on hair
c.line(head_cx - 3, head_cy - 3, head_cx + 2, head_cy - 3, P['hair_mid'])
c.line(head_cx - 2, head_cy - 4, head_cx + 1, head_cy - 4, P['hair_light'])
c.set(head_cx - 1, head_cy - 4, P['light_bright'])

# Water contact / meniscus around swim ring (gentle curve around ring)
c.line(gx - 13, gy + 6, gx - 8, gy + 8, P['under_deep'])
c.line(gx + 8, gy + 8, gx + 13, gy + 6, P['under_deep'])
c.line(gx - 7, gy + 9, gx + 7, gy + 9, P['under_deep'])
c.line(gx - 10, gy + 7, gx - 5, gy + 9, P['surf_bright'])
c.line(gx + 5, gy + 9, gx + 10, gy + 7, P['surf_bright'])

view(c)
finish(c)
