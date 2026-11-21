import math
import numpy as np

# Canvas setup
W, H = 256, 256

# Coherent, rich palette tailored for arcane brass instrument & gothic observatory
PALETTE = [
    # 0..6: Background void, night sky & nebula
    ("#040409", "bg_void"),        # 0
    ("#090a14", "bg_deep"),        # 1
    ("#0d1222", "sky_dark"),       # 2
    ("#151c34", "sky_mid"),        # 3
    ("#241c3e", "sky_nebula"),     # 4
    ("#4a597a", "star_dim"),       # 5
    ("#d6e8ff", "star_bright"),    # 6
    # 7..14: Stone Architecture & Masonry
    ("#0e101a", "stone_darkest"),  # 7
    ("#171926", "stone_dark"),     # 8
    ("#222536", "stone_shadow"),   # 9
    ("#31364b", "stone_mid"),      # 10
    ("#444b66", "stone_light"),    # 11
    ("#5d6588", "stone_bright"),   # 12
    ("#7f88b0", "stone_hi"),       # 13
    ("#a8b2db", "stone_lightest"), # 14
    # 15..19: Floor flagstones
    ("#0d0e17", "floor_dark"),     # 15
    ("#181928", "floor_mid"),      # 16
    ("#24263a", "floor_light"),    # 17
    ("#363852", "floor_hi"),       # 18
    ("#07070d", "floor_joint"),    # 19
    # 20..26: Pedestal Stone & Carvings
    ("#191624", "ped_base"),       # 20
    ("#262234", "ped_shadow"),     # 21
    ("#3a354c", "ped_mid"),        # 22
    ("#524b69", "ped_light"),      # 23
    ("#6f678c", "ped_bright"),     # 24
    ("#9187b2", "ped_hi"),         # 25
    ("#b8ade0", "ped_lightest"),   # 26
    # 27..38: Brass / Bronze / Gold ramp & Outlines
    ("#060507", "outline_black"),  # 27
    ("#180f07", "metal_deep"),     # 28
    ("#2c1809", "brass_shadow"),   # 29
    ("#48290c", "brass_dark"),     # 30
    ("#6b3f11", "brass_base"),     # 31
    ("#945917", "brass_mid"),      # 32
    ("#bc761f", "brass_warm"),     # 33
    ("#df992a", "brass_light"),    # 34
    ("#f5bd3e", "brass_bright"),   # 35
    ("#fde062", "gold_hi"),        # 36
    ("#fff498", "gold_shine"),     # 37
    ("#fffde0", "gold_white"),     # 38
    # 39..44: Iron / Blued Steel / Dial faces
    ("#141922", "iron_dark"),      # 39
    ("#242d3d", "iron_mid"),       # 40
    ("#3d4b61", "iron_light"),     # 41
    ("#617492", "iron_bright"),    # 42
    ("#94a8cb", "iron_hi"),        # 43
    ("#d0ddf2", "iron_white"),     # 44
    # 45..51: Arcane Cyan / Core Radiance / Runes
    ("#092434", "rune_darkest"),   # 45
    ("#10455d", "rune_dark"),      # 46
    ("#197391", "rune_mid"),       # 47
    ("#27adc7", "rune_bright"),    # 48
    ("#3eecd9", "cyan_glow"),      # 49
    ("#87fff1", "cyan_bright"),    # 50
    ("#f0ffff", "cyan_white"),     # 51
    # 52..56: Gem: Ruby / Crimson
    ("#2c0610", "ruby_deep"),      # 52
    ("#580d20", "ruby_dark"),      # 53
    ("#981836", "ruby_mid"),       # 54
    ("#e0345b", "ruby_bright"),    # 55
    ("#ffa3b8", "ruby_hi"),        # 56
    # 57..61: Gem: Amethyst / Royal Violet
    ("#1f082e", "amethyst_deep"),  # 57
    ("#451264", "amethyst_dark"),  # 58
    ("#7823a8", "amethyst_mid"),   # 59
    ("#b04de6", "amethyst_bright"),# 60
    ("#e6a3ff", "amethyst_hi"),    # 61
    # 62..66: Gem: Emerald / Prismatic Jade
    ("#072215", "emerald_deep"),   # 62
    ("#0f4c2e", "emerald_dark"),   # 63
    ("#1c8753", "emerald_mid"),    # 64
    ("#3ac983", "emerald_bright"), # 65
    ("#9cfcc6", "emerald_hi"),     # 66
    # 67..71: Gem: Sapphire / Celestial Azure
    ("#081532", "sapphire_deep"),  # 67
    ("#10306c", "sapphire_dark"),  # 68
    ("#2054ad", "sapphire_mid"),   # 69
    ("#4789e6", "sapphire_bright"),# 70
    ("#b0d2ff", "sapphire_hi"),    # 71
]

COLOR_INDEX = {name: i for i, (hex_code, name) in enumerate(PALETTE)}

buf = np.full((H, W), COLOR_INDEX["bg_void"], dtype=np.int32)

def set_px(x, y, col_name):
    if 0 <= x < W and 0 <= y < H:
        buf[y, x] = COLOR_INDEX[col_name]

def get_px(x, y):
    if 0 <= x < W and 0 <= y < H:
        return buf[y, x]
    return -1

def draw_line(x0, y0, x1, y1, col_name):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        set_px(x, y, col_name)
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

# ------------------------------------------------------------------------------
# COORDINATE RE-CENTERING:
# The center of the instrument is raised to (128, 92)
# The outer ring has radius R=82
# Bottom of instrument meridian ring + cradle is at y = 92 + 82 + 6 = 180
# Top of pedestal is at y = 208
# This creates a clear 28-pixel LEVITATING GAP full of arcane energy!
# ------------------------------------------------------------------------------
CX, CY = 128, 92
R_OUTER = 82
R_INNER = 75

# ------------------------------------------------------------------------------
# 1. BACKGROUND ARCHITECTURE: Gothic Hall, Vaults, Archway, Stars, Moon, Pillars
# ------------------------------------------------------------------------------
print("Drawing background architecture...")

# Wall stone courses
for y in range(H):
    for x in range(W):
        # Default stone wall
        course = y // 12
        is_joint_h = (y % 12 == 0) and (y < 205)
        is_joint_v = ((x + (course % 2) * 18) % 36 == 0) and (y < 205)
        if is_joint_h or is_joint_v:
            buf[y, x] = COLOR_INDEX["stone_darkest"]
        else:
            # Subtle stone noise / shading
            col = "stone_dark" if (x * 7 + y * 13) % 5 == 0 else "stone_shadow"
            if y < 35:
                col = "stone_darkest" if (x + y) % 3 == 0 else "stone_dark"
            buf[y, x] = COLOR_INDEX[col]

# Gothic pointed arch window
# Left arch center at (212, 130), Right arch center at (44, 130), radius = 168
arch_left_cx, arch_left_cy = 212, 130
arch_right_cx, arch_right_cy = 44, 130
arch_r = 168

for y in range(H):
    for x in range(W):
        d_left = math.hypot(x - arch_left_cx, y - arch_left_cy)
        d_right = math.hypot(x - arch_right_cx, y - arch_right_cy)
        if (d_left <= arch_r) and (d_right <= arch_r) and (y <= 130) and (44 <= x <= 212):
            # Inside night sky
            dist_to_peak = math.hypot(x - 128, y - 8)
            if dist_to_peak < 60:
                col = "sky_dark"
            elif dist_to_peak < 110:
                col = "sky_mid"
            else:
                col = "sky_dark"
            # Cosmic nebula
            neb = math.sin(x * 0.07 + y * 0.04) * math.cos(y * 0.08 - x * 0.03)
            if neb > 0.35:
                col = "sky_nebula"
            buf[y, x] = COLOR_INDEX[col]

# Astrological plate coordinate grid in the sky (faint celestial lines)
for r_grid in [35, 60, 85, 110]:
    for deg in range(0, 360, 4):
        rad = math.radians(deg)
        gx = int(round(CX + r_grid * math.cos(rad)))
        gy = int(round(CY + r_grid * 0.6 * math.sin(rad)))
        if 48 <= gx <= 208 and 14 <= gy <= 126:
            if buf[gy, gx] in (COLOR_INDEX["sky_dark"], COLOR_INDEX["sky_mid"], COLOR_INDEX["sky_nebula"]):
                set_px(gx, gy, "rune_darkest")

# Arch carved stone trim / moulding
for y in range(8, 131):
    dy = y - 130
    if arch_r*arch_r >= dy*dy:
        dx = math.sqrt(arch_r*arch_r - dy*dy)
        lx = int(round(212 - dx))
        rx = int(round(44 + dx))
        if 44 <= lx <= 128:
            for w in range(-2, 3):
                col = "stone_bright" if w == 0 else ("stone_hi" if w == -1 else "stone_darkest")
                set_px(lx + w, y, col)
                set_px(rx - w, y, col)

# Stars & Constellations
star_data = [
    (56, 24, True), (70, 40, False), (62, 70, True), (84, 28, False),
    (92, 54, False), (106, 22, True), (120, 42, False), (136, 26, False),
    (150, 52, False), (164, 20, True), (172, 44, False), (196, 32, True),
    (184, 72, False), (76, 86, False), (108, 76, False), (146, 82, False),
    (178, 90, False), (196, 54, False), (58, 104, False), (200, 100, False)
]
for sx, sy, is_big in star_data:
    set_px(sx, sy, "star_bright" if is_big else "star_dim")
    if is_big:
        set_px(sx + 1, sy, "star_dim")
        set_px(sx - 1, sy, "star_dim")
        set_px(sx, sy + 1, "star_dim")
        set_px(sx, sy - 1, "star_dim")

# Crescent Moon at (184, 32)
moon_cx, moon_cy = 184, 32
for my in range(moon_cy - 7, moon_cy + 8):
    for mx in range(moon_cx - 7, moon_cx + 8):
        d1 = math.hypot(mx - moon_cx, my - moon_cy)
        d2 = math.hypot(mx - (moon_cx - 3.5), my - (moon_cy - 1.5))
        if d1 <= 6.5:
            if d2 > 5.0:
                set_px(mx, my, "gold_hi" if d1 < 5.8 else "gold_shine")
            elif d2 <= 5.0 and (mx + my) % 2 == 0:
                set_px(mx, my, "sky_nebula")

# Massive Pillars with carved capitals (Left: x=8..38, Right: x=218..248)
for y in range(0, 205):
    for x in range(8, 39):
        rel = (x - 8) / 30.0
        if rel < 0.15: col = "stone_darkest"
        elif rel < 0.35: col = "stone_dark"
        elif rel < 0.7: col = "stone_mid"
        elif rel < 0.9: col = "stone_light"
        else: col = "stone_shadow"
        # Flutes
        if x in (14, 20, 26, 32): col = "stone_darkest"
        # Capital at y=76..90
        if 76 <= y <= 90:
            if y % 4 == 0: col = "stone_bright"
            elif y % 4 == 1: col = "stone_hi"
            else: col = "stone_darkest"
        # Base plinth at y=192..205
        if 192 <= y <= 205:
            if y == 192 or y == 204: col = "stone_bright"
            elif (x - 8) < 4 or (38 - x) < 4: col = "stone_darkest"
        set_px(x, y, col)
        
    for x in range(218, 249):
        rel = (248 - x) / 30.0
        if rel < 0.15: col = "stone_darkest"
        elif rel < 0.35: col = "stone_dark"
        elif rel < 0.7: col = "stone_mid"
        elif rel < 0.9: col = "stone_light"
        else: col = "stone_shadow"
        if x in (224, 230, 236, 242): col = "stone_darkest"
        if 76 <= y <= 90:
            if y % 4 == 0: col = "stone_bright"
            elif y % 4 == 1: col = "stone_hi"
            else: col = "stone_darkest"
        if 192 <= y <= 205:
            if y == 192 or y == 204: col = "stone_bright"
            elif (x - 218) < 4 or (248 - x) < 4: col = "stone_darkest"
        set_px(x, y, col)

# Wall sconces with floating cyan will-o'-wisps
for sx, sy in [(23, 115), (233, 115)]:
    # Iron mount
    draw_line(sx - 3, sy + 6, sx + 3, sy + 1, "iron_dark")
    draw_line(sx, sy + 1, sx, sy - 2, "iron_light")
    draw_line(sx - 2, sy - 2, sx + 2, sy - 2, "brass_light")
    # Cyan magical flame
    set_px(sx, sy - 5, "cyan_white")
    set_px(sx, sy - 6, "cyan_bright")
    set_px(sx - 1, sy - 5, "cyan_glow")
    set_px(sx + 1, sy - 5, "cyan_glow")
    set_px(sx, sy - 4, "cyan_glow")

# Floor flagstones at y=202..255
print("Drawing floor flagstones...")
for y in range(202, H):
    for x in range(W):
        dist_y = y - 202
        is_joint_row = (dist_y % 11 == 0)
        # Perspective grid from vanishing point (128, 140)
        v_offset = (dist_y // 11) * 7
        is_joint_col = ((x - 128) % 24 == (v_offset % 24))
        
        if is_joint_row or is_joint_col:
            buf[y, x] = COLOR_INDEX["floor_joint"]
        else:
            # Ambient radial glow from instrument above
            d_center = math.hypot(x - 128, (y - 215) * 1.6)
            if d_center < 45:
                col = "floor_hi" if (x + y) % 3 == 0 else "floor_light"
            elif d_center < 75:
                col = "floor_light" if (x + y) % 2 == 0 else "floor_mid"
            else:
                col = "floor_mid" if (x + y) % 3 == 0 else "floor_dark"
            buf[y, x] = COLOR_INDEX[col]

# ------------------------------------------------------------------------------
# 2. STONE PEDESTAL (Base at y=212..252, centered at x=128)
# Highly detailed ancient carved plinth with glowing runes & transmutation basin!
# ------------------------------------------------------------------------------
print("Drawing stone pedestal...")

# Tier 3 (Bottom Plinth): y=240..252, rx=74, ry=12
for y in range(240, 253):
    for x in range(128 - 75, 128 + 76):
        dx = (x - 128) / 75.0
        dy = (y - 242) / 10.0
        if dx*dx + (dy*dy if y < 242 else 0) <= 1.0:
            rel = (x - (128 - 75)) / 150.0
            if rel < 0.15 or rel > 0.85: col = "ped_shadow"
            elif rel < 0.4: col = "ped_mid"
            elif rel < 0.75: col = "ped_light"
            else: col = "ped_shadow"
            if y == 252 or abs(dx) > 0.98: col = "outline_black"
            set_px(x, y, col)

# Tier 2 (Middle Octagonal Tier): y=226..240, rx=62, ry=10
for y in range(226, 241):
    for x in range(128 - 63, 128 + 64):
        dx = (x - 128) / 63.0
        dy = (y - 228) / 9.0
        if dx*dx + (dy*dy if y < 228 else 0) <= 1.0:
            rel = (x - (128 - 63)) / 126.0
            if rel < 0.15 or rel > 0.85: col = "ped_shadow"
            elif rel < 0.45: col = "ped_mid"
            elif rel < 0.8: col = "ped_light"
            else: col = "ped_shadow"
            # Carved trefoils / runes along Tier 2
            if y == 233 and (x % 8 in (1, 2, 3)):
                col = "gold_hi" if (x % 16 < 8) else "cyan_bright"
            if y == 240 or abs(dx) > 0.98: col = "ped_base"
            set_px(x, y, col)

# Tier 1 (Top Plinth): y=212..226, rx=52, ry=8
for y in range(212, 227):
    for x in range(128 - 53, 128 + 54):
        dx = (x - 128) / 53.0
        dy = (y - 214) / 7.0
        if dx*dx + (dy*dy if y < 214 else 0) <= 1.0:
            rel = (x - (128 - 53)) / 106.0
            if rel < 0.15 or rel > 0.85: col = "ped_shadow"
            elif rel < 0.45: col = "ped_mid"
            elif rel < 0.8: col = "ped_light"
            else: col = "ped_shadow"
            if y == 226 or abs(dx) > 0.98: col = "ped_base"
            set_px(x, y, col)

# Pedestal Top Basin & Transmutation Circle (y=206..215, rx=50, ry=8)
for py in range(206, 216):
    for px in range(128 - 51, 128 + 52):
        dx = (px - 128) / 50.0
        dy = (py - 211) / 7.0
        d2 = dx*dx + dy*dy
        if d2 <= 1.0:
            if d2 > 0.85:
                # Top beveled rim
                col = "ped_hi" if py <= 211 else "ped_shadow"
            elif d2 > 0.72:
                col = "outline_black"
            else:
                # Concave basin containing glowing magical circle
                r_rel = math.sqrt(d2)
                col = "ped_base"
                # Outer glowing ring of the seal
                if abs(r_rel - 0.58) < 0.06:
                    col = "cyan_bright"
                elif abs(r_rel - 0.42) < 0.05:
                    col = "gold_hi"
                elif abs(r_rel - 0.25) < 0.05:
                    col = "cyan_white"
                # Hexagram / star rays
                angle = math.atan2(dy, dx)
                if abs(math.sin(angle * 6)) > 0.88 and r_rel < 0.58:
                    col = "cyan_glow"
            set_px(px, py, col)

# ------------------------------------------------------------------------------
# 3. LEVITATION GAP & ARCANE ENERGY FIELD (y=176..207)
# Distinct 30-pixel height gap showing true levitation!
# ------------------------------------------------------------------------------
print("Drawing levitation energy stream...")
for y in range(176, 208):
    for x in range(128 - 42, 128 + 43):
        # Multiple energetic lightning filaments leaping upward
        for beam_cx, phase in [(114, 0.0), (122, 1.2), (128, 2.4), (134, 3.6), (142, 4.8)]:
            # Zig-zag lightning
            offset = int(math.sin(y * 0.45 + phase) * 2.2 + math.cos(y * 0.9 - phase) * 1.1)
            lx = beam_cx + offset
            dist_x = abs(x - lx)
            if dist_x == 0:
                col = "cyan_white" if y % 2 == 0 else "cyan_bright"
                set_px(x, y, col)
            elif dist_x == 1:
                if (x + y) % 2 == 0:
                    set_px(x, y, "cyan_glow")

# Floating magical glyphs in the gap
lev_runes = [(110, 186), (146, 184), (118, 196), (138, 195), (128, 180), (104, 198), (152, 197)]
for rx, ry in lev_runes:
    set_px(rx, ry, "cyan_white")
    set_px(rx - 1, ry, "cyan_bright")
    set_px(rx + 1, ry, "cyan_bright")
    set_px(rx, ry - 1, "cyan_glow")
    set_px(rx, ry + 1, "cyan_bright")
    set_px(rx - 1, ry + 1, "cyan_glow")

# Floating weightless stone fragments orbiting in the gap
shards = [(100, 182, 3), (156, 178, 4), (144, 200, 2), (112, 202, 3), (128, 174, 2)]
for sx, sy, sr in shards:
    for dy in range(-sr, sr + 1):
        for dx in range(-sr, sr + 1):
            if abs(dx) + abs(dy) <= sr:
                col = "ped_hi" if dy < 0 else "ped_shadow"
                if abs(dx) + abs(dy) == sr:
                    col = "outline_black"
                set_px(sx + dx, sy + dy, col)

# ------------------------------------------------------------------------------
# 4. MASSIVE BRASS ASTROLABE-ORRERY
# Center: (128, 92)
# ------------------------------------------------------------------------------
print("Drawing Astrolabe-Orrery...")

def ellipse_dist(px, py, cx, cy, a, b, tilt_deg):
    rad = math.radians(-tilt_deg)
    cos_r = math.cos(rad)
    sin_r = math.sin(rad)
    tx = (px - cx) * cos_r - (py - cy) * sin_r
    ty = (px - cx) * sin_r + (py - cy) * cos_r
    r_norm = math.sqrt((tx / a)**2 + (ty / b)**2)
    angle = math.atan2(ty, tx)
    return r_norm, tx, ty, angle

# Defined 5 nested gimbal rings at dramatic 3D angles
RINGS = [
    {
        "name": "zodiac_band",
        "a": 76, "b": 32, "tilt": -22, "w": 6.5,
        "teeth": True, "runes": True, "type": "brass"
    },
    {
        "name": "colure_scale",
        "a": 70, "b": 36, "tilt": 38, "w": 6.0,
        "teeth": False, "runes": False, "type": "silver"
    },
    {
        "name": "precession_ring",
        "a": 60, "b": 26, "tilt": -55, "w": 5.0,
        "teeth": True, "runes": True, "type": "brass"
    },
    {
        "name": "equator_ring",
        "a": 52, "b": 17, "tilt": 0, "w": 5.0,
        "teeth": True, "runes": False, "type": "brass"
    },
    {
        "name": "gyro_ring",
        "a": 42, "b": 17, "tilt": 70, "w": 4.5,
        "teeth": False, "runes": True, "type": "gold"
    },
]

def render_ring_pixel(px, py, ring, half):
    r_norm, tx, ty, angle = ellipse_dist(px, py, CX, CY, ring["a"], ring["b"], ring["tilt"])
    if half == "back" and ty >= 0: return None
    if half == "front" and ty < 0: return None
    
    r_px = r_norm * ring["a"]
    half_w = ring["w"] / 2.0
    dist = abs(r_px - ring["a"])
    
    if dist > half_w + 1.1:
        return None
    
    # Crisp black silhouette outline
    if dist > half_w:
        return "outline_black"
    
    # Gear teeth on the outer perimeter
    if ring["teeth"] and (r_px > ring["a"] + half_w - 1.6):
        num_teeth = 36 if ring["a"] > 65 else 24
        cog = math.sin(angle * num_teeth)
        if cog < 0.15:
            return "outline_black" if dist > half_w - 0.7 else "brass_dark"
            
    # Glowing arcane runes engraved along the center line of the ring
    if ring["runes"] and dist < 1.0:
        freq = 30 if ring["a"] > 60 else 20
        rune_p1 = math.sin(angle * freq)
        rune_p2 = math.cos(angle * freq * 2.8)
        if rune_p1 > 0.35 and rune_p2 > 0.0:
            return "cyan_white" if rune_p1 > 0.8 else "cyan_bright"
        elif rune_p1 > 0.15:
            return "cyan_glow"
            
    # 3D Bevel Lighting
    inside = (r_px < ring["a"])
    if inside:
        # Rim facing the blazing central core: intense gold highlight!
        if dist > half_w - 0.9:
            return "brass_shadow"
        elif dist > half_w - 1.8:
            return "gold_shine"
        else:
            return "gold_hi"
    else:
        # Outside rim
        if ring["type"] == "silver":
            # Vernier steel scale
            if dist < 1.0 and int(angle * 32) % 2 == 0:
                return "iron_white"
            return "iron_bright" if py < CY else "iron_mid"
        elif ring["type"] == "gold":
            return "gold_shine" if py < CY else "gold_hi"
        else:
            return "brass_light" if py < CY else "brass_mid"

# ------------------------------------------------------------------------------
# OUTER MERIDIAN CIRCLE (Radius R=82 to 75)
# ------------------------------------------------------------------------------
def draw_outer_meridian_ring():
    for py in range(CY - R_OUTER - 4, CY + R_OUTER + 5):
        for px in range(CX - R_OUTER - 4, CX + R_OUTER + 5):
            d = math.hypot(px - CX, py - CY)
            if (R_INNER - 0.5) <= d <= (R_OUTER + 1.5):
                # Black outlines on both inner and outer edge
                if d >= R_OUTER + 0.5 or d <= R_INNER + 0.5:
                    set_px(px, py, "outline_black")
                elif d >= R_OUTER - 1.2:
                    # Outer bevel highlight
                    set_px(px, py, "gold_hi" if py < CY else "brass_mid")
                elif d <= R_INNER + 1.8:
                    # Inner bevel highlight (catching core light!)
                    set_px(px, py, "gold_shine")
                else:
                    # Main ring face with engraved degree graduations & glowing runes
                    angle = math.atan2(py - CY, px - CX)
                    deg = math.degrees(angle) % 360
                    # Glowing arcane zodiac runes in clusters every 30 degrees
                    rune_zone = abs((deg % 30) - 15) < 5.0
                    if rune_zone and abs(d - 78.5) < 0.9:
                        rune_sig = math.sin(deg * 3.2) * math.cos(deg * 6.4)
                        if rune_sig > 0.1:
                            set_px(px, py, "cyan_white" if rune_sig > 0.4 else "cyan_bright")
                            continue
                        elif rune_sig > -0.2:
                            set_px(px, py, "cyan_glow")
                            continue

                    # Major 15-degree ticks
                    if abs(deg % 15) < 0.9:
                        set_px(px, py, "outline_black")
                    # Minor 5-degree ticks
                    elif abs(deg % 5) < 0.7:
                        set_px(px, py, "brass_dark")
                    else:
                        set_px(px, py, "brass_warm" if py < CY else "brass_mid")

# Top Suspension & Bottom Pivot Cradle
def draw_outer_mounts():
    # Top suspension crown & shackle at (128, CY - R_OUTER)
    top_y = CY - R_OUTER
    for sy in range(top_y - 12, top_y):
        for sx in range(120, 137):
            d = math.hypot(sx - 128, sy - (top_y - 7))
            if 3.5 <= d <= 6.5:
                set_px(sx, sy, "gold_hi" if sy < top_y - 7 else "brass_dark")
            elif d > 6.5 and d <= 7.5:
                set_px(sx, sy, "outline_black")
    # Fleur-de-lis / spearhead finial
    for dy in range(0, 7):
        hw = dy // 2
        for dx in range(-hw, hw + 1):
            col = "gold_shine" if dx == 0 else ("gold_hi" if dx < 0 else "brass_mid")
            set_px(128 + dx, top_y + dy - 1, col)
            set_px(128 - hw - 1, top_y + dy - 1, "outline_black")
            set_px(128 + hw + 1, top_y + dy - 1, "outline_black")

    # Bottom Cradle Mount at (128, CY + R_OUTER) = (128, 174)
    # Clear of pedestal! Pedestal top is at 206, so this floats 32 pixels above!
    bot_y = CY + R_OUTER
    for y in range(bot_y - 2, bot_y + 12):
        for x in range(112, 145):
            dx = x - 128
            dy = y - bot_y
            if abs(dx) <= 5 + dy * 0.4:
                col = "gold_hi" if dx < 0 else "brass_mid"
                if abs(dx) >= 4 + dy * 0.4:
                    col = "outline_black"
                set_px(x, y, col)
    # Heavy pivot stud at (128, bot_y + 4)
    for dy in range(-3, 4):
        for dx in range(-3, 4):
            if dx*dx + dy*dy <= 8:
                set_px(128 + dx, bot_y + 4 + dy, "gold_shine" if dx <= 0 and dy <= 0 else "brass_dark")
            elif dx*dx + dy*dy <= 15:
                set_px(128 + dx, bot_y + 4 + dy, "outline_black")

# Draw back of rings & outer meridian
print("Drawing back half of rings...")
for ring in RINGS:
    for py in range(CY - ring["a"] - 5, CY + ring["a"] + 6):
        for px in range(CX - ring["a"] - 5, CX + ring["a"] + 6):
            col = render_ring_pixel(px, py, ring, "back")
            if col is not None:
                set_px(px, py, col)

draw_outer_meridian_ring()
draw_outer_mounts()

# ------------------------------------------------------------------------------
# 5. DETAILED GEAR TRAINS & ALCHEMICAL DIALS
# ------------------------------------------------------------------------------
print("Drawing gear trains and dials...")

def draw_spur_gear(gx, gy, r, teeth, spoke_count, is_brass=True):
    r_body = r - 2.5
    for y in range(gy - r - 2, gy + r + 3):
        for x in range(gx - r - 2, gx + r + 3):
            d = math.hypot(x - gx, y - gy)
            angle = math.atan2(y - gy, x - gx)
            tooth_mod = math.sin(angle * teeth)
            r_outer = r_body + (2.5 if tooth_mod > 0.0 else 0.0)
            
            if d <= r_outer + 0.9:
                if d > r_outer:
                    set_px(x, y, "outline_black")
                elif d > r_body:
                    if tooth_mod > 0.4:
                        set_px(x, y, "gold_hi" if is_brass else "iron_hi")
                    elif tooth_mod > 0.0:
                        set_px(x, y, "brass_mid" if is_brass else "iron_light")
                    else:
                        set_px(x, y, "brass_dark" if is_brass else "iron_mid")
                elif d > r_body - 2.5:
                    set_px(x, y, "gold_hi" if (y < gy and is_brass) else ("brass_warm" if is_brass else "iron_light"))
                elif d > 4.5:
                    # Spokes
                    spoke_angle = (angle + math.pi) % (2 * math.pi / spoke_count) - (math.pi / spoke_count)
                    if abs(spoke_angle) < (0.35 / (d * 0.12)):
                        set_px(x, y, "gold_shine" if is_brass else "iron_bright")
                elif d > 2.0:
                    set_px(x, y, "brass_dark" if is_brass else "iron_mid")
                else:
                    is_hi = (x <= gx and y <= gy)
                    set_px(x, y, "gold_shine" if is_hi else "outline_black")

# Left Gear Train:
# Gear 1: (88, 114, r=15, teeth=14, brass)
draw_spur_gear(88, 114, 15, 14, 4, is_brass=True)
# Meshed Gear 2: (72, 106, r=9, teeth=8, iron)
draw_spur_gear(72, 106, 9, 8, 3, is_brass=False)
# Meshed Gear 3: (62, 118, r=7, teeth=7, brass)
draw_spur_gear(62, 118, 7, 7, 3, is_brass=True)

# Linkage arms & brackets
draw_line(88, 114, 72, 106, "brass_dark")
draw_line(72, 106, 52, 98, "brass_warm")
draw_line(72, 107, 52, 99, "outline_black")

# Right Alchemical Astrological Dial:
# Gear driving the dial: (182, 104, r=10, teeth=10)
draw_spur_gear(182, 104, 10, 10, 4, is_brass=True)

# Dial at (168, 116, R=16)
def draw_alchemical_dial(dx, dy, r):
    for y in range(dy - r - 2, dy + r + 3):
        for x in range(dx - r - 2, dx + r + 3):
            d = math.hypot(x - dx, y - dy)
            if d <= r + 1.0:
                if d > r:
                    set_px(x, y, "outline_black")
                elif d > r - 2.0:
                    # Brass bezel
                    set_px(x, y, "gold_hi" if (y < dy or x < dx) else "brass_dark")
                elif d > r - 3.0:
                    set_px(x, y, "outline_black")
                elif d > 4.0:
                    # Dial face
                    angle = math.atan2(y - dy, x - dx)
                    deg = math.degrees(angle) % 360
                    if abs(deg % 30) < 3.0:
                        set_px(x, y, "gold_hi")
                    elif abs(deg % 10) < 1.8:
                        set_px(x, y, "iron_hi")
                    elif abs(d - 9.0) < 0.8:
                        set_px(x, y, "cyan_bright")
                    else:
                        set_px(x, y, "iron_dark")
                else:
                    set_px(x, y, "gold_shine" if x <= dx and y <= dy else "brass_shadow")
    # Dial hands
    # Sun pointer (-40 deg)
    for step in range(3, r - 3):
        rad = math.radians(-40)
        px = int(round(dx + step * math.cos(rad)))
        py = int(round(dy + step * math.sin(rad)))
        set_px(px, py, "gold_shine" if step == r - 4 else "gold_hi")
    # Dragon tail pointer (135 deg)
    for step in range(3, r - 4):
        rad = math.radians(135)
        px = int(round(dx + step * math.cos(rad)))
        py = int(round(dy + step * math.sin(rad)))
        set_px(px, py, "cyan_glow")

draw_alchemical_dial(168, 116, 16)

# Top Astronomical Tourbillon & Balance Wheel Escapement at (128, 36)
print("Drawing tourbillon escapement...")
# 1. Beveled support bracket & vertical drive arbor
for y in range(43, 51):
    set_px(127, y, "gold_hi")
    set_px(128, y, "gold_shine")
    set_px(129, y, "brass_dark")
    set_px(126, y, "outline_black")
    set_px(130, y, "outline_black")

# 2. Openwork balance wheel (R = 9.5)
bw_cx, bw_cy = 128, 34
for y in range(bw_cy - 11, bw_cy + 12):
    for x in range(bw_cx - 11, bw_cx + 12):
        d = math.hypot(x - bw_cx, y - bw_cy)
        angle = math.atan2(y - bw_cy, x - bw_cx)
        if 8.0 <= d <= 10.5:
            if d >= 10.0 or d <= 8.3:
                set_px(x, y, "outline_black")
            else:
                # Rim of balance wheel with regulating inertia screws
                is_screw = abs(math.sin(angle * 8)) > 0.85
                if is_screw:
                    set_px(x, y, "gold_shine")
                else:
                    set_px(x, y, "gold_hi" if y < bw_cy else "brass_warm")
        elif 2.5 < d < 8.0:
            # 3 slender curved spokes
            spoke_angle = (angle + 0.3) % (2 * math.pi / 3.0) - (math.pi / 3.0)
            if abs(spoke_angle) < (0.32 / (d * 0.14)):
                set_px(x, y, "gold_hi")
            else:
                # Spiral hairspring (blued steel & cyan glow)
                spiral_r = 3.0 + (angle % (2 * math.pi)) * 0.7
                if abs(d - spiral_r) < 0.55:
                    set_px(x, y, "cyan_bright" if d < 5.5 else "iron_bright")
        elif d <= 2.5:
            # Center ruby cap jewel and gold setting
            if d <= 1.2:
                set_px(x, y, "ruby_bright" if x <= bw_cx else "ruby_deep")
            else:
                set_px(x, y, "gold_shine" if x <= bw_cx and y <= bw_cy else "brass_dark")

# Scrolled filigree balance cock brackets flanking the balance wheel
for bx, sgn in [(128 - 14, -1), (128 + 14, 1)]:
    # Curving brass scroll
    draw_line(128, 44, bx, 40, "brass_mid")
    draw_line(bx, 40, bx + sgn * 2, 34, "gold_hi")
    draw_line(bx + sgn * 2, 34, 128 + sgn * 8, 30, "brass_light")
    set_px(bx + sgn * 2, 34, "gold_shine")

# Astrolabe Rete Tracery (Swooping openwork gothic flame web)
print("Drawing astrolabe rete...")
for t_deg in range(-70, 75, 3):
    rad = math.radians(t_deg)
    rx = int(round(CX + 50 * math.cos(rad)))
    ry = int(round(CY - 28 + 34 * math.sin(rad)))
    if (rx + ry) % 2 == 0:
        set_px(rx, ry, "gold_hi")
        if t_deg in (-46, -12, 24, 60):
            tip_x = int(round(rx + 7 * math.cos(rad - 0.4)))
            tip_y = int(round(ry + 7 * math.sin(rad - 0.4)))
            draw_line(rx, ry, tip_x, tip_y, "gold_shine")
            set_px(tip_x, tip_y, "cyan_white")

# ------------------------------------------------------------------------------
# 6. CENTRAL RADIANT CORE (Center: 128, 92)
# ------------------------------------------------------------------------------
print("Drawing central radiant core...")

# Translucent spherical energy aura
for y in range(CY - 30, CY + 31):
    for x in range(CX - 30, CX + 31):
        d = math.hypot(x - CX, y - CY)
        if d <= 28:
            if d > 22:
                if (x + y) % 3 == 0: set_px(x, y, "rune_darkest")
            elif d > 16:
                if (x + y) % 2 == 0: set_px(x, y, "rune_dark")
            elif d > 11:
                set_px(x, y, "rune_mid")

# Swirling double-helix magical plasma ribbons orbiting the singularity
for t_step in range(0, 360, 3):
    rad = math.radians(t_step)
    # Helix 1
    r_h1 = 12.0 + 5.0 * math.cos(rad * 2.0)
    hx1 = int(round(CX + r_h1 * math.cos(rad)))
    hy1 = int(round(CY + r_h1 * 0.45 * math.sin(rad) + 4.0 * math.sin(rad * 2.0)))
    set_px(hx1, hy1, "cyan_white" if math.sin(rad) > 0 else "cyan_bright")
    set_px(hx1, hy1 + 1, "cyan_glow")
    # Helix 2 (offset phase)
    r_h2 = 12.0 + 5.0 * math.cos(rad * 2.0 + math.pi)
    hx2 = int(round(CX + r_h2 * math.cos(rad + math.pi)))
    hy2 = int(round(CY + r_h2 * 0.45 * math.sin(rad + math.pi) - 4.0 * math.sin(rad * 2.0)))
    set_px(hx2, hy2, "cyan_bright" if math.sin(rad + math.pi) > 0 else "rune_bright")

# Core Gyroscope Brass Wire Cage (Radius = 18)
for deg in range(0, 360, 2):
    rad = math.radians(deg)
    ex = int(round(CX + 18 * math.cos(rad)))
    ey = int(round(CY + 7 * math.sin(rad)))
    set_px(ex, ey, "gold_hi" if ey < CY else "brass_dark")
    vx = int(round(CX + 9 * math.cos(rad)))
    vy = int(round(CY + 18 * math.sin(rad)))
    set_px(vx, vy, "gold_shine" if vx < CX else "brass_warm")
    tx = int(round(CX + 16 * math.cos(rad) - 5 * math.sin(rad)))
    ty = int(round(CY + 5 * math.cos(rad) + 16 * math.sin(rad)))
    set_px(tx, ty, "gold_hi")

# Radiant Core corona & 8 directional energy spikes
ray_angles = [0, 45, 90, 135, 180, 225, 270, 315]
for angle_deg in ray_angles:
    rad = math.radians(angle_deg)
    ray_len = 26 if (angle_deg % 90 == 0) else 20
    for step in range(4, ray_len):
        rx = int(round(CX + step * math.cos(rad)))
        ry = int(round(CY + step * math.sin(rad)))
        if step < 9: col = "cyan_white"
        elif step < 16: col = "cyan_bright"
        elif step < ray_len - 3: col = "cyan_glow"
        else: col = "rune_bright"
        set_px(rx, ry, col)
        if step < 11 and (angle_deg % 90 == 0):
            set_px(rx + 1, ry, "cyan_glow")
            set_px(rx - 1, ry, "cyan_glow")

# Core Blazing Singularity (r <= 6.5)
for y in range(CY - 7, CY + 8):
    for x in range(CX - 7, CX + 8):
        d = math.hypot(x - CX, y - CY)
        if d <= 3.2:
            set_px(x, y, "cyan_white")
        elif d <= 5.0:
            set_px(x, y, "cyan_bright")
        elif d <= 6.8:
            set_px(x, y, "cyan_glow")

# ------------------------------------------------------------------------------
# 7. DRAW FRONT HALVES OF RINGS
# ------------------------------------------------------------------------------
print("Drawing front half of rings...")
for ring in RINGS:
    for py in range(CY - ring["a"] - 5, CY + ring["a"] + 6):
        for px in range(CX - ring["a"] - 5, CX + ring["a"] + 6):
            col = render_ring_pixel(px, py, ring, "front")
            if col is not None:
                set_px(px, py, col)

# ------------------------------------------------------------------------------
# 8. ORBITING CRYSTAL SPHERES & CURVED ARMILLARY ARMS
# ------------------------------------------------------------------------------
print("Drawing orbiting crystal spheres...")

def draw_crystal_sphere(sx, sy, r, gem_type, has_ring=False, arm_start=(CX, CY)):
    # Elegant curved brass orbital arm with gear teeth / filigree
    ax0, ay0 = arm_start
    # Quadratic Bézier curve from (ax0, ay0) to (sx, sy)
    ctrl_x = (ax0 + sx) // 2 + (12 if sy > CY else -12)
    ctrl_y = (ay0 + sy) // 2 + (10 if sx < CX else -10)
    
    steps = 28
    for i in range(steps):
        t = i / float(steps)
        # B(t) = (1-t)^2 P0 + 2(1-t)t P1 + t^2 P2
        bx = int(round((1 - t)**2 * ax0 + 2 * (1 - t) * t * ctrl_x + t**2 * sx))
        by = int(round((1 - t)**2 * ay0 + 2 * (1 - t) * t * ctrl_y + t**2 * sy))
        # 2-pixel wide arm with highlight and outline
        set_px(bx, by, "gold_hi" if by < sy else "brass_warm")
        set_px(bx + 1, by, "brass_dark")
        set_px(bx - 1, by, "outline_black")
        set_px(bx, by + 1, "outline_black")
        # Miniature counter-cogs along the arm
        if i % 6 == 0:
            set_px(bx + 2, by, "gold_shine")

    # Ornate curved U-shaped filigree mounting cup (conforms to sphere curve!)
    for angle_deg in range(25, 156, 5):
        rad = math.radians(angle_deg)
        cup_r = r + 1.2
        cx_cup = int(round(sx + cup_r * math.cos(rad)))
        cy_cup = int(round(sy + cup_r * math.sin(rad)))
        set_px(cx_cup, cy_cup, "gold_hi")
        # Outer shadow rim
        cx_out = int(round(sx + (cup_r + 1.0) * math.cos(rad)))
        cy_out = int(round(sy + (cup_r + 1.0) * math.sin(rad)))
        set_px(cx_out, cy_out, "brass_dark")
        cx_black = int(round(sx + (cup_r + 2.0) * math.cos(rad)))
        cy_black = int(round(sy + (cup_r + 2.0) * math.sin(rad)))
        set_px(cx_black, cy_black, "outline_black")
    
    # Bottom mount pivot jewel / finial
    set_px(sx, sy + r + 3, "gold_shine")
    set_px(sx, sy + r + 4, "brass_dark")
    set_px(sx - 1, sy + r + 3, "outline_black")
    set_px(sx + 1, sy + r + 3, "outline_black")
    set_px(sx, sy + r + 5, "outline_black")

    colors = {
        "amethyst": ["amethyst_deep", "amethyst_dark", "amethyst_mid", "amethyst_bright", "amethyst_hi"],
        "ruby": ["ruby_deep", "ruby_dark", "ruby_mid", "ruby_bright", "ruby_hi"],
        "emerald": ["emerald_deep", "emerald_dark", "emerald_mid", "emerald_bright", "emerald_hi"],
        "sapphire": ["sapphire_deep", "sapphire_dark", "sapphire_mid", "sapphire_bright", "sapphire_hi"],
        "pearl": ["stone_shadow", "stone_mid", "iron_light", "iron_hi", "gold_white"]
    }[gem_type]

    # Core direction
    dx_core = CX - sx
    dy_core = CY - sy
    core_dist = math.hypot(dx_core, dy_core)
    nx_core = dx_core / core_dist if core_dist > 0 else 0
    ny_core = dy_core / core_dist if core_dist > 0 else 0

    for y in range(sy - r - 2, sy + r + 3):
        for x in range(sx - r - 2, sx + r + 3):
            d = math.hypot(x - sx, y - sy)
            if d <= r + 0.8:
                if d > r:
                    set_px(x, y, "outline_black")
                else:
                    nz = math.sqrt(max(0.0, 1.0 - (d / r)**2))
                    nx = (x - sx) / r
                    ny = (y - sy) / r
                    
                    dot_core = nx * nx_core + ny * ny_core + nz * 0.3
                    dot_top = -ny * 0.4 + nz * 0.5
                    intensity = dot_core * 0.65 + dot_top * 0.35
                    
                    if intensity < -0.3: col = colors[0]
                    elif intensity < 0.0: col = colors[1]
                    elif intensity < 0.4: col = colors[2]
                    elif intensity < 0.75: col = colors[3]
                    else: col = colors[4]
                        
                    # Crisp specular glint facing radiant core
                    spec = (nx * nx_core + ny * ny_core)
                    if spec > 0.65 and nz > 0.5 and d < r * 0.65:
                        col = "cyan_white" if gem_type in ("sapphire", "emerald") else colors[4]
                    
                    set_px(x, y, col)

    if has_ring:
        rx_ring, ry_ring = r + 8, (r + 8) // 3
        tilt = -16
        for deg in range(0, 360, 2):
            rad = math.radians(deg)
            lx = rx_ring * math.cos(rad)
            ly = ry_ring * math.sin(rad)
            rot_rad = math.radians(tilt)
            px = int(round(sx + lx * math.cos(rot_rad) - ly * math.sin(rot_rad)))
            py = int(round(sy + lx * math.sin(rot_rad) + ly * math.cos(rot_rad)))
            is_in_front = (ly > 0)
            d_to_sphere = math.hypot(px - sx, py - sy)
            if is_in_front or d_to_sphere > r:
                set_px(px, py, "gold_hi" if is_in_front else "brass_dark")
                set_px(px, py + 1, "outline_black" if is_in_front else "brass_shadow")

# 1. Royal Amethyst Saturn at (198, 64), R=9
draw_crystal_sphere(198, 64, 9, "amethyst", has_ring=True, arm_start=(172, 78))

# 2. Crimson Ruby at (56, 76), R=8
draw_crystal_sphere(56, 76, 8, "ruby", has_ring=False, arm_start=(76, 88))

# 3. Arcane Emerald at (178, 142), R=7
draw_crystal_sphere(178, 142, 7, "emerald", has_ring=False, arm_start=(150, 130))

# 4. Azure Sapphire with Moonlet at (76, 48), R=6
draw_crystal_sphere(76, 48, 6, "sapphire", has_ring=False, arm_start=(96, 60))
# Tiny golden moonlet
for dy in range(-2, 3):
    for dx in range(-2, 3):
        if dx*dx + dy*dy <= 4:
            set_px(86 + dx, 42 + dy, "gold_shine" if dx <= 0 else "brass_dark")
        elif dx*dx + dy*dy <= 8:
            set_px(86 + dx, 42 + dy, "outline_black")

# 5. Pearlescent Moon at (96, 142), R=6
draw_crystal_sphere(96, 142, 6, "pearl", has_ring=False, arm_start=(112, 128))

# ------------------------------------------------------------------------------
# 9. FINAL TOUCHES: Specular Sparkles & Magic Motes
# ------------------------------------------------------------------------------
sparkles = [
    (138, 62), (118, 66), (142, 110), (114, 108), (156, 86), (96, 96),
    (128, 56), (128, 128), (188, 52), (64, 60), (168, 156), (86, 152)
]
for spx, spy in sparkles:
    set_px(spx, spy, "cyan_white")
    if (spx + spy) % 2 == 0:
        set_px(spx + 1, spy, "cyan_glow")
        set_px(spx - 1, spy, "cyan_glow")
        set_px(spx, spy + 1, "cyan_glow")
        set_px(spx, spy - 1, "cyan_glow")

# ------------------------------------------------------------------------------
# TRANSFER BUFFER TO CANVAS
# ------------------------------------------------------------------------------
print("Transferring to canvas...")
c = new_canvas(W, H, name="arcane_orrery")

palette_indices = []
for hex_code, name in PALETTE:
    idx = c.color(hex_code, name=name)
    palette_indices.append(idx)

for y in range(H):
    for x in range(W):
        col_idx = buf[y, x]
        c.set(x, y, palette_indices[col_idx])

print("Canvas completed successfully!")
print(f"Colors used: {c.stats()['colors_used']}")
view(c)
finish(c)
