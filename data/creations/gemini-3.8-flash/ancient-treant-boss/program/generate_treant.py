import numpy as np
import math
import random

def build_treant_art():
    w, h = 256, 256
    
    PALETTE = [
        "#000000",  # 0: unused
        # 1-8: Deep Forest Mist & Fog (dark teal to misty sage)
        "#050b0d",  # 1 deepest background
        "#081417",  # 2
        "#0e1e22",  # 3
        "#152a2e",  # 4
        "#1e383c",  # 5
        "#2a494c",  # 6
        "#3a5d5f",  # 7
        "#4e7676",  # 8 lightest clearing mist
        # 9-16: God Rays / Golden-Green Light Shafts
        "#1b3831",  # 9 deep ray
        "#284e43",  # 10
        "#3a6756",  # 11
        "#50856d",  # 12
        "#6da689",  # 13
        "#90c6a8",  # 14
        "#bce4ce",  # 15 bright ray
        "#e5f8ee",  # 16 ray highlight
        # 17-27: Bark & Wood tones (deep crevice to sunlit rim)
        "#0c0705",  # 17 deepest outline
        "#170f0b",  # 18 dark crevice / deep furrow
        "#241711",  # 19 deep shadow
        "#352219",  # 20 bark shadow
        "#492f23",  # 21 bark mid-dark
        "#5e3e2e",  # 22 bark midtone
        "#764f3c",  # 23 bark mid-light
        "#91634c",  # 24 bark light
        "#ae7b60",  # 25 bark highlight
        "#cb9779",  # 26 sunlit bark
        "#e4b899",  # 27 rim-lit bark peak
        # 28-36: Foliage / Leaves
        "#071108",  # 28 leaf darkest
        "#0e1e10",  # 29 leaf deep
        "#172f19",  # 30 leaf shadow
        "#234324",  # 31 leaf mid
        "#325d33",  # 32 leaf mid-light
        "#467b46",  # 33 leaf light
        "#609e5d",  # 34 leaf bright
        "#82c37c",  # 35 leaf sunlit
        "#ade5a4",  # 36 leaf tip highlight
        # 37-43: Moss & Hanging Vines
        "#10200e",  # 37 moss deep
        "#1a3416",  # 38 moss shadow
        "#294e22",  # 39 moss mid
        "#3e6f32",  # 40 moss bright
        "#5a9846",  # 41 moss vibrant
        "#7ec761",  # 42 moss highlight
        "#abf089",  # 43 moss edge
        # 44-51: Glowing Green Magic / Eyes / Core / Spores
        "#062411",  # 44 glow dark
        "#0b4b21",  # 45 glow mid-dark
        "#137c35",  # 46 glow emerald
        "#1eb54e",  # 47 glow bright
        "#3fe071",  # 48 glow neon green
        "#7fff9c",  # 49 glow lime white
        "#d2ffe0",  # 50 glow core
        "#ffffff",  # 51 pure white core
        # 52-60: Forest Ground / Earth / Mud / Stones
        "#0f0b08",  # 52 earth deepest
        "#1c140e",  # 53 earth dark
        "#2a1e16",  # 54 earth mid
        "#3b2b20",  # 55 earth light
        "#101416",  # 56 rock deepest
        "#1c2225",  # 57 rock dark
        "#2a3337",  # 58 rock mid
        "#3e4a50",  # 59 rock light
        "#58676e",  # 60 rock highlight
        # 61-66: Mushrooms & Shelf Fungi & Magic Flora
        "#682914",  # 61 bracket fungus dark red-brown
        "#9c441c",  # 62 bracket fungus orange-brown
        "#c96e38",  # 63 bracket fungus rim
        "#13a669",  # 64 glowing mushroom cyan-green
        "#3be29f",  # 65 glowing mushroom bright
        "#a2ffd9",  # 66 glowing mushroom cap highlight
    ]

    grid = np.zeros((h, w), dtype=np.int32)
    obj_mask = np.zeros((h, w), dtype=np.int32)

    # 1. Atmospheric Forest Background & Clearing
    for y in range(h):
        for x in range(w):
            gy = y / 210.0
            gx = (x - 128) / 128.0
            fog = 2.4 + gy * 4.2 - (gx * gx) * 1.6
            n = math.sin(x * 0.04 + y * 0.02) * 0.6 + math.cos(y * 0.05 - x * 0.03) * 0.5
            grid[y, x] = max(1, min(7, int(fog + n)))

    # Distant Giant Trees
    for tx, tw, base_col in [(16, 24, 2), (44, 18, 3), (80, 15, 3), (176, 15, 3), (212, 18, 3), (244, 24, 2)]:
        for y in range(210):
            cur_tx = tx + int(math.sin(y * 0.025 + tx) * 2)
            x0 = cur_tx - tw // 2
            x1 = cur_tx + tw // 2
            for x in range(max(0, x0), min(w, x1)):
                d = abs(x - cur_tx) / (tw / 2.0)
                grid[y, x] = base_col if d < 0.8 else max(1, base_col - 1)

    # 2. Dramatic Volumetric God Rays
    ray_defs = [(15, 34, 1.45, 1.0), (55, 40, 1.55, 1.25), (105, 44, 1.65, 1.15), (155, 36, 1.60, 0.95)]
    bayer = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]
    for rx0, r_w, slope, intensity_mul in ray_defs:
        for y in range(230):
            cx = rx0 + y / slope
            ix0 = max(0, int(cx - r_w))
            ix1 = min(w, int(cx + r_w))
            for x in range(ix0, ix1):
                dist = abs(x - cx) / float(r_w)
                if dist < 1.0:
                    ray_val = (1.0 - dist * dist) * (1.0 - y / 280.0) * intensity_mul
                    d_thresh = bayer[y % 4][x % 4] / 16.0
                    if ray_val > d_thresh * 0.55:
                        cur = grid[y, x]
                        boost = int(ray_val * 5.0)
                        if boost > 0:
                            grid[y, x] = min(15, 9 + boost + (cur % 2))

    # Overhanging top canopy
    for y in range(38):
        for x in range(w):
            hang = 16 + int(math.sin(x * 0.07) * 7 + math.cos(x * 0.13) * 5 + math.sin(x * 0.02) * 9)
            if y < hang:
                dy = hang - y
                grid[y, x] = 28 if dy > 11 else (29 if dy > 5 else (30 if dy > 2 else 31))

    # 3. Ground & Ancient Megaliths
    for y in range(195, h):
        for x in range(w):
            gh = 214 + int(math.sin(x * 0.04) * 6 + math.cos(x * 0.08) * 3)
            if y >= gh:
                obj_mask[y, x] = 1
                dy = y - gh
                if dy == 0:
                    grid[y, x] = 38
                elif dy < 3:
                    grid[y, x] = 37
                elif dy < 8:
                    grid[y, x] = 54
                elif dy < 16:
                    grid[y, x] = 53
                else:
                    grid[y, x] = 52

    for y in range(178, 242):
        tx0 = 10 + int((240 - y) * 0.12)
        tx1 = tx0 + 22 - int((240 - y) * 0.06)
        for x in range(tx0, tx1):
            if 0 <= x < w:
                obj_mask[y, x] = 1
                edge = min(x - tx0, tx1 - 1 - x)
                top = y - 178
                if edge == 0 or top == 0:
                    grid[y, x] = 56
                elif x < tx0 + 6:
                    grid[y, x] = 60
                elif x < tx0 + 13:
                    grid[y, x] = 59
                else:
                    grid[y, x] = 58
                if top < 4 and x > tx0 + 1:
                    grid[y, x] = 40 if edge > 1 else 38

    for y in range(184, 242):
        tx0 = 224 - int((240 - y) * 0.08)
        tx1 = tx0 + 20
        for x in range(tx0, tx1):
            if 0 <= x < w:
                obj_mask[y, x] = 1
                edge = min(x - tx0, tx1 - 1 - x)
                top = y - 184
                if edge == 0 or top == 0:
                    grid[y, x] = 56
                elif x < tx0 + 6:
                    grid[y, x] = 59
                elif x < tx0 + 13:
                    grid[y, x] = 58
                else:
                    grid[y, x] = 57
                if top < 3:
                    grid[y, x] = 39

    # 4. Volumetric Limb Renderer
    def draw_organic_branch(pts_radii):
        for i in range(len(pts_radii) - 1):
            p0, p1 = pts_radii[i], pts_radii[i + 1]
            x0, y0, r0 = p0
            x1, y1, r1 = p1
            dist = math.hypot(x1 - x0, y1 - y0)
            steps = max(1, int(dist * 2.5))
            for s in range(steps + 1):
                t = s / float(steps)
                cx = x0 + t * (x1 - x0)
                cy = y0 + t * (y1 - y0)
                cr = r0 + t * (r1 - r0)
                ir = int(math.ceil(cr))
                for dy in range(-ir, ir + 1):
                    py = int(cy + dy)
                    if 0 <= py < h:
                        dx_max = math.sqrt(max(0.0, cr * cr - dy * dy))
                        px0 = max(0, int(cx - dx_max))
                        px1 = min(w - 1, int(cx + dx_max))
                        for px in range(px0, px1 + 1):
                            obj_mask[py, px] = 2
                            rel_x = (px - cx) / cr
                            nz = math.sqrt(max(0.0, 1.0 - rel_x * rel_x))
                            diff = max(0.0, -rel_x * 0.72 + nz * 0.58)
                            l_val = 0.28 + diff * 0.92
                            grain = math.sin(rel_x * 7.5 + cy * 0.18)
                            if grain < -0.42:
                                c = 18
                            elif l_val < 0.45:
                                c = 19
                            elif l_val < 0.65:
                                c = 20
                            elif l_val < 0.85:
                                c = 21
                            elif l_val < 1.05:
                                c = 22
                            elif l_val < 1.25:
                                c = 23
                            elif l_val < 1.45:
                                c = 24
                            else:
                                c = 25
                            grid[py, px] = c

    # 5. Continuous Trunk & Chest
    def get_torso_half_width(y):
        if y < 65:
            return 22.0 + (y - 45) * 0.2
        elif y < 98:
            t = (y - 65) / 33.0
            return 26.0 + t * 24.0
        elif y < 130:
            return 50.0 - (y - 98) * 0.22
        elif y < 155:
            t = (y - 130) / 25.0
            return 43.0 - t * 5.0
        elif y <= 185:
            t = (y - 155) / 30.0
            return 38.0 + t * 14.0
        return 0.0

    for py in range(50, 186):
        hw = get_torso_half_width(py)
        if hw > 0:
            x_min = int(round(128 - hw))
            x_max = int(round(128 + hw))
            for px in range(x_min, x_max + 1):
                obj_mask[py, px] = 2
                u = (px - 128) / hw
                nz = math.sqrt(max(0.0, 1.0 - u * u))
                diffuse = max(0.0, -u * 0.72 + nz * 0.55)
                light = 0.26 + diffuse * 0.95

                furrow_val = 0.0
                for fu in [-0.74, -0.44, -0.18, 0.18, 0.44, 0.74]:
                    cur_fu = fu + math.sin(py * 0.11 + fu * 5.0) * 0.06
                    if 72 <= py <= 112:
                        fade = 1.0 - abs(py - 92) / 20.0
                        cur_fu += (0.15 if fu > 0 else -0.15) * fade
                    dist_f = abs(u - cur_fu)
                    if dist_f < 0.045:
                        furrow_val = -0.4
                    elif dist_f < 0.08 and u < cur_fu:
                        furrow_val = max(furrow_val, 0.22)

                final_light = light + furrow_val
                if furrow_val < -0.3:
                    c = 18
                elif final_light < 0.38:
                    c = 19
                elif final_light < 0.55:
                    c = 20
                elif final_light < 0.72:
                    c = 21
                elif final_light < 0.90:
                    c = 22
                elif final_light < 1.10:
                    c = 23
                elif final_light < 1.30:
                    c = 24
                elif final_light < 1.50:
                    c = 25
                else:
                    c = 26
                grid[py, px] = c

    # 6. High Hunched Shoulders & Arms
    # Left Arm
    draw_organic_branch([(108, 76, 20), (84, 68, 22), (58, 64, 24), (40, 88, 22), (32, 126, 18)])
    draw_organic_branch([(32, 126, 18), (38, 152, 16), (46, 172, 14)])
    draw_organic_branch([(46, 172, 14), (44, 184, 12)])
    draw_organic_branch([(50, 184, 6), (62, 198, 4.5), (74, 216, 2)])
    draw_organic_branch([(46, 186, 6), (50, 206, 4.5), (54, 230, 2)])
    draw_organic_branch([(40, 186, 6), (34, 206, 4.5), (28, 232, 2)])
    draw_organic_branch([(34, 184, 5), (22, 198, 4.0), (14, 220, 2)])

    # Right Arm
    draw_organic_branch([(148, 76, 20), (172, 68, 22), (198, 64, 24), (216, 88, 22), (224, 124, 18)])
    draw_organic_branch([(224, 124, 18), (218, 150, 16), (210, 170, 14)])
    draw_organic_branch([(210, 170, 14), (212, 182, 12)])
    draw_organic_branch([(206, 182, 6), (192, 196, 4.5), (180, 214, 2)])
    draw_organic_branch([(210, 184, 6), (206, 206, 4.5), (202, 230, 2)])
    draw_organic_branch([(216, 184, 6), (222, 206, 4.5), (226, 232, 2)])
    draw_organic_branch([(222, 182, 5), (234, 198, 4.0), (244, 220, 2)])

    # 7. Roots Rising from Ground
    draw_organic_branch([(82, 175, 18), (62, 195, 16), (46, 218, 14), (32, 238, 11), (20, 248, 6)])
    draw_organic_branch([(106, 182, 17), (96, 205, 15), (88, 226, 13), (80, 248, 9)])
    draw_organic_branch([(150, 182, 17), (160, 205, 15), (168, 226, 13), (176, 248, 9)])
    draw_organic_branch([(174, 175, 18), (194, 195, 16), (210, 218, 14), (224, 238, 11), (236, 248, 6)])
    draw_organic_branch([(88, 226, 11), (105, 238, 7), (116, 245, 4)])
    draw_organic_branch([(168, 226, 11), (150, 238, 7), (138, 245, 4)])
    draw_organic_branch([(46, 218, 11), (58, 236, 7), (68, 245, 4)])
    draw_organic_branch([(210, 218, 11), (196, 236, 7), (184, 245, 4)])
    draw_organic_branch([(128, 185, 12), (128, 212, 8), (128, 235, 4)])

    # 8. Antler Horns
    draw_organic_branch([(120, 56, 9), (105, 40, 7.5), (88, 26, 6), (72, 14, 4), (60, 8, 2)])
    draw_organic_branch([(105, 40, 5), (96, 50, 3.5), (88, 58, 2)])
    draw_organic_branch([(88, 26, 4.5), (76, 32, 3), (66, 38, 1.8)])

    draw_organic_branch([(136, 56, 9), (151, 40, 7.5), (168, 26, 6), (184, 14, 4), (196, 8, 2)])
    draw_organic_branch([(151, 40, 5), (160, 50, 3.5), (168, 58, 2)])
    draw_organic_branch([(168, 26, 4.5), (180, 32, 3), (190, 38, 1.8)])

    draw_organic_branch([(128, 56, 8), (128, 30, 5.5), (122, 14, 3), (118, 6, 1.8)])
    draw_organic_branch([(128, 30, 4.5), (136, 16, 3), (142, 8, 1.8)])

    # 9. Menacing Ancient Wooden Face & Glowing Green Eyes
    for py in range(72, 115):
        for px in range(106, 150):
            dx = (px - 128) / 19.0
            dy = (py - 93) / 20.0
            if dx * dx + dy * dy < 1.0:
                dist = math.hypot(dx, dy)
                grid[py, px] = 18 if dist < 0.75 else (19 if dist < 0.95 else 20)

    # Gnarled wooden forehead overhang above eye cavity
    for px in range(112, 145):
        # Deep cast shadow over the top of the eye hollow
        grid[77, px] = 17
        grid[78, px] = 18

    # Glowing Green Eyes in Trunk (Large, piercing, menacing emerald/lime glow)
    for eye_cx, eye_cy, is_left in [(119, 85, True), (137, 85, False)]:
        for dy in range(-7, 8):
            for dx in range(-8, 9):
                px = eye_cx + dx
                py = eye_cy + dy
                if 0 <= px < w and 0 <= py < h:
                    slant_dx = dx + (dy * 0.45 if is_left else -dy * 0.45)
                    dist = math.hypot(slant_dx, dy * 1.5)
                    if dist < 1.2:
                        grid[py, px] = 51 # pure white core
                        obj_mask[py, px] = 5
                    elif dist < 2.2:
                        grid[py, px] = 50 # glow core lime
                        obj_mask[py, px] = 5
                    elif dist < 3.4:
                        grid[py, px] = 49 # lime white
                        obj_mask[py, px] = 5
                    elif dist < 4.8:
                        grid[py, px] = 48 # neon green
                        obj_mask[py, px] = 5
                    elif dist < 6.2:
                        grid[py, px] = 47 # bright emerald
                    elif dist < 8.5:
                        if grid[py, px] in (18, 19, 20):
                            grid[py, px] = 46
                        elif grid[py, px] in (21, 22):
                            grid[py, px] = 45

    # Glowing ethereal wisps floating upwards from eyes
    random.seed(888)
    for _ in range(28):
        wx = random.randint(114, 142)
        wy = random.randint(64, 83)
        dist_eye = min(math.hypot(wx - 119, wy - 85), math.hypot(wx - 137, wy - 85))
        if 2.5 < dist_eye < 15:
            grid[wy, wx] = random.choice([47, 48, 49])
            obj_mask[wy, wx] = 5

    # Menacing wide snarling jagged wooden maw
    for py in range(97, 114):
        for px in range(112, 145):
            # Jagged crevasse profile
            jag = math.sin((px - 128) * 0.8) * 2.0
            if abs(py - 105 - jag) < 4.5:
                grid[py, px] = 17 # deep dark maw

    # Splinter wooden fangs
    teeth_top = [(116, 100), (120, 102), (124, 103), (128, 104), (132, 103), (136, 102), (140, 100)]
    for tx, ty in teeth_top:
        grid[ty, tx] = 24
        grid[ty - 1, tx] = 23
    teeth_bottom = [(118, 110), (122, 108), (126, 107), (130, 107), (134, 108), (138, 110)]
    for tx, ty in teeth_bottom:
        grid[ty, tx] = 24
        grid[ty + 1, tx] = 23

    # Inner green magical light leaking through maw
    for px in range(120, 137):
        grid[105, px] = 46
        grid[106, px] = 47
    grid[105, 128] = 49
    grid[105, 129] = 49
    grid[106, 128] = 48

    # Cascading Spanish moss and root beard hanging from jaw
    tendril_roots = [
        (112, 108, 132, -1.8), (116, 110, 145, -1.2), (120, 111, 156, -0.5),
        (124, 112, 162, 0.0), (128, 112, 164, 0.2), (132, 112, 160, 0.6),
        (136, 111, 148, 1.2), (140, 110, 138, 1.6), (144, 108, 126, 2.0)
    ]
    for sx, sy, max_y, sway in tendril_roots:
        cur_x = float(sx)
        for cy in range(sy, max_y):
            cur_x += sway * 0.06 + math.sin(cy * 0.22 + sx) * 0.22
            ix = int(round(cur_x))
            if 0 <= ix < w and 0 <= cy < h:
                prog = (cy - sy) / float(max_y - sy)
                grid[cy, ix] = 41 if prog > 0.7 else (40 if prog > 0.3 else 39)
                obj_mask[cy, ix] = 4
                if ix + 1 < w and grid[cy, ix + 1] not in (40, 41, 42, 47, 48, 49, 50, 51):
                    grid[cy, ix + 1] = 38

    # 10. Crown Foliage (Ancient Oak Canopy)
    def paint_leaf_canopy(cx, cy, rx, ry):
        for dy in range(-ry, ry + 1):
            py = cy + dy
            if 0 <= py < h:
                dx_limit = rx * math.sqrt(max(0.0, 1.0 - (dy / float(ry)) ** 2))
                ix0 = max(0, int(cx - dx_limit))
                ix1 = min(w - 1, int(cx + dx_limit))
                for px in range(ix0, ix1 + 1):
                    scallop = math.sin(px * 0.55 + py * 0.4) * 0.18 + math.cos(px * 0.3 - py * 0.6) * 0.12
                    norm_r = math.hypot((px - cx) / float(rx), dy / float(ry)) + scallop
                    if norm_r < 1.0:
                        obj_mask[py, px] = 3
                        lx = (px - (cx - rx)) / (2.0 * rx)
                        ly = (py - (cy - ry)) / (2.0 * ry)
                        sun = (1.0 - lx) * 0.65 + (1.0 - ly) * 0.75
                        tex = ((px * 3 ^ py * 5) % 5) * 0.08
                        t_val = sun + tex
                        if t_val > 1.22:
                            c = 36
                        elif t_val > 1.02:
                            c = 35
                        elif t_val > 0.82:
                            c = 34
                        elif t_val > 0.64:
                            c = 33
                        elif t_val > 0.44:
                            c = 32
                        elif t_val > 0.24:
                            c = 31
                        else:
                            c = 30
                        grid[py, px] = c

    for bcx, bcy, brx, bry in [
        (128, 22, 26, 14), (104, 20, 22, 13), (152, 20, 22, 13),
        (80, 16, 18, 10), (176, 16, 18, 10), (60, 12, 14, 8), (196, 12, 14, 8),
        (128, 38, 22, 9), (100, 42, 15, 8), (156, 42, 15, 8),
    ]:
        paint_leaf_canopy(bcx, bcy, brx, bry)

    # 11. Remove dotted block - clean bark
    pass

    # 12. Hanging Vines
    vines = [
        (32, 90, 36, 0.8), (42, 94, 48, -0.6), (50, 92, 30, 0.4),
        (24, 130, 44, -1.2), (32, 134, 54, 0.9), (42, 160, 32, 0.7),
        (208, 90, 34, -0.7), (218, 94, 46, 1.0), (226, 128, 48, -0.9),
        (216, 134, 38, 0.6), (204, 160, 32, -0.5),
        (116, 186, 26, 0.4), (124, 187, 34, -0.3), (132, 187, 30, 0.5), (140, 186, 24, -0.4),
    ]
    for vx, vy, vlen, vsway in vines:
        cur_vx = float(vx)
        for s in range(vlen):
            py = vy + s
            cur_vx += math.sin(py * 0.16 + vx) * 0.32 + vsway * 0.05
            px = int(round(cur_vx))
            if 0 <= px < w and 0 <= py < h:
                prog = s / float(vlen)
                col = 41 if prog > 0.6 else 40
                grid[py, px] = col
                obj_mask[py, px] = 4
                if s % 8 == 0:
                    ldir = 1 if (s // 8) % 2 == 0 else -1
                    if 0 <= px + ldir < w:
                        grid[py, px + ldir] = 42
                        if 0 <= py + 1 < h:
                            grid[py + 1, px + ldir] = 39

    # Mushrooms
    for mx, my, mw, mh in [
        (70, 236, 5, 3), (76, 238, 4, 3), (62, 241, 6, 4),
        (106, 243, 5, 3), (148, 243, 5, 3), (174, 237, 5, 3),
        (182, 239, 6, 4), (190, 242, 4, 2), (24, 239, 5, 3), (236, 239, 5, 3),
    ]:
        for dy in range(mh, mh + 4):
            if 0 <= my + dy < h:
                grid[my + dy, mx] = 50
        for dy in range(-mh//2, mh//2 + 1):
            for dx in range(-mw//2, mw//2 + 1):
                px = mx + dx
                py = my + dy
                if 0 <= px < w and 0 <= py < h:
                    grid[py, px] = 66 if dy == -mh//2 else (65 if dy == 0 else 64)
        for g_dy in range(-3, 5):
            for g_dx in range(-5, 6):
                gx = mx + g_dx
                gy = my + g_dy
                if 0 <= gx < w and 0 <= gy < h:
                    if math.hypot(g_dx, g_dy) < 4.2 and grid[gy, gx] in (52, 53, 54, 56, 57):
                        grid[gy, gx] = 44

    # Ferns
    for fx, fy, num_fronds, fdir in [
        (14, 219, 5, -1), (26, 223, 6, 1), (60, 233, 5, -1), (114, 239, 6, 1),
        (142, 239, 6, -1), (196, 233, 5, 1), (228, 225, 6, -1), (244, 221, 5, 1),
    ]:
        for frond in range(num_fronds):
            angle = -0.32 - frond * 0.24
            flen = 10 + (frond % 3) * 3
            for step in range(flen):
                cur_fx = fx + int(math.cos(angle) * step * fdir * 1.2)
                cur_fy = fy - int(math.sin(-angle) * step * 0.7)
                if 0 <= cur_fx < w and 0 <= cur_fy < h:
                    prog = step / float(flen)
                    grid[cur_fy, cur_fx] = 42 if prog > 0.7 else (41 if prog > 0.3 else 39)
                    if step % 2 == 0 and step > 2 and 0 <= cur_fx + fdir < w:
                        grid[cur_fy, cur_fx + fdir] = 40

    # 13. Crisp Dark Outlines
    outline_mask = np.zeros((h, w), dtype=bool)
    for py in range(h):
        for px in range(w):
            if obj_mask[py, px] in (2, 3, 4):
                for ny, nx in [(py-1, px), (py+1, px), (py, px-1), (py, px+1)]:
                    if 0 <= ny < h and 0 <= nx < w:
                        if obj_mask[ny, nx] in (0, 1):
                            outline_mask[py, px] = True
                            break
                    else:
                        outline_mask[py, px] = True
                        break

    for py in range(h):
        for px in range(w):
            if outline_mask[py, px] and obj_mask[py, px] != 5:
                grid[py, px] = 17

    # Internal separation lines
    for py in range(98, 175):
        cur_x = int(58 - (py - 95) * 0.58) if py < 135 else int(34 + (py - 135) * 0.3)
        for ox in range(cur_x + 9, cur_x + 13):
            if 0 <= ox < w and obj_mask[py, ox] == 2 and obj_mask[py, ox - 2] == 2 and (ox + py) % 4 != 0:
                grid[py, ox] = 17

    for py in range(98, 175):
        cur_x = int(198 + (py - 95) * 0.68) if py < 130 else int(224 - (py - 130) * 0.4)
        for ox in range(cur_x - 13, cur_x - 9):
            if 0 <= ox < w and obj_mask[py, ox] == 2 and obj_mask[py, ox + 2] == 2 and (ox + py) % 4 != 0:
                grid[py, ox] = 17

    for py in range(184, 218):
        for px in [42, 50, 60]:
            if 0 <= px < w and obj_mask[py, px] == 2:
                grid[py, px] = 17
        for px in [196, 206, 218]:
            if 0 <= px < w and obj_mask[py, px] == 2:
                grid[py, px] = 17

    # God-Ray Rim Lighting on Sunlit Left Contours
    for py in range(8, 225):
        for px in range(w):
            if obj_mask[py, px] in (2, 3) and not outline_mask[py, px]:
                if px < 130:
                    if obj_mask[py, px] == 3:
                        grid[py, px] = 36
                        if px + 1 < w and obj_mask[py, px + 1] == 3:
                            grid[py, px + 1] = 35
                    elif obj_mask[py, px] == 2:
                        grid[py, px] = 27
                        if px + 1 < w and obj_mask[py, px + 1] == 2 and grid[py, px + 1] != 17:
                            grid[py, px + 1] = 26
                break

    # 14. Floating Glowing Spores & Dust Motes
    random.seed(999)
    for _ in range(55):
        sx = random.randint(10, 245)
        sy = random.randint(18, 235)
        if obj_mask[sy, sx] not in (2, 3):
            ray_dist = min(
                abs(sx - (15 + sy / 1.45)),
                abs(sx - (55 + sy / 1.55)),
                abs(sx - (105 + sy / 1.65))
            )
            if ray_dist < 26:
                spore_col = random.choice([14, 15, 48, 49, 50])
                grid[sy, sx] = spore_col
                if spore_col in (49, 50) and sx + 1 < w:
                    grid[sy, sx + 1] = 47

    return grid, PALETTE
