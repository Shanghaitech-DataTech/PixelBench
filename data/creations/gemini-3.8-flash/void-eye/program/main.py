import math
from pixelbench_api import new_canvas, flatten, view, finish

def draw_void_eye_boss():
    c = new_canvas(64, 64, name="void_eye")
    
    # =========================================================================
    # 1. COLOR PALETTE
    # =========================================================================
    # Soft Hover Shadow
    C_SHD_EDGE = (10, 4, 20, 35)
    C_SHD_MID  = (10, 3, 18, 75)
    C_SHD_CORE = (8, 2, 16, 125)
    C_SHD_DEEP = (6, 1, 12, 175)

    # Outlines / Deep Crevices
    C_BLACK     = (10, 4, 18)      # Deepest silhouette
    C_VOID_DARK = (18, 7, 32)
    
    # Body Flesh / Carapace (Deep void purple)
    C_FLESH_D4   = (26, 10, 46)
    C_FLESH_D3   = (42, 16, 72)
    C_FLESH_D2   = (65, 25, 106)
    C_FLESH_D1   = (94, 37, 146)
    C_FLESH_MID  = (128, 52, 192)
    C_FLESH_HI   = (164, 82, 236)
    C_FLESH_PEAK = (204, 136, 255)
    C_FLESH_TINT = (236, 196, 255)
    
    # Sleek Void Chitin Horns (Obsidian with bone tips)
    C_HORN_DARK  = (16, 8, 26)
    C_HORN_D1    = (35, 18, 52)
    C_HORN_MID   = (68, 38, 96)
    C_HORN_HI    = (118, 76, 156)
    C_HORN_PEAK  = (182, 146, 218)
    C_HORN_WHITE = (245, 236, 255)

    # Sclera (Eyeball white/grey/cosmic lavender)
    C_SCLERA_D4  = (28, 18, 43)
    C_SCLERA_D3  = (48, 34, 69)
    C_SCLERA_D2  = (76, 61, 102)
    C_SCLERA_MID = (114, 98, 143)
    C_SCLERA_LGT = (162, 148, 191)
    C_SCLERA_BRT = (210, 201, 230)
    C_SCLERA_HI  = (245, 241, 252)

    # Sclera Veins (Red-violet corruption)
    C_VEIN_D = (82, 10, 38)
    C_VEIN_M = (140, 20, 68)
    C_VEIN_H = (202, 36, 96)

    # Deep Purple Iris (Lush, multi-layered cosmic violet)
    C_IRIS_LIMBAL = (16, 2, 28)
    C_IRIS_D4     = (28, 4, 46)
    C_IRIS_D3     = (48, 7, 77)
    C_IRIS_D2     = (78, 11, 120)
    C_IRIS_D1     = (114, 19, 168)
    C_IRIS_MID    = (154, 34, 220)
    C_IRIS_VIB    = (190, 56, 250)
    C_IRIS_HI     = (220, 96, 255)
    C_IRIS_PEAK   = (242, 155, 255)

    # Faintly Glowing Pupil (Eerie cyan/teal aura around vertical slit)
    C_PUPIL_BLACK = (5, 2, 8)
    C_GLOW_D4     = (18, 38, 64)
    C_GLOW_D3     = (20, 75, 105)
    C_GLOW_D2     = (25, 125, 148)
    C_GLOW_MID    = (38, 186, 189)
    C_GLOW_BRT    = (68, 237, 220)
    C_GLOW_PALE   = (175, 255, 247)
    C_WHITE       = (255, 255, 255)

    # Tentacle Bioluminescent Suckers & Nodes
    C_SUCKER_RIM  = (155, 36, 130)
    C_SUCKER_HOLE = (42, 8, 38)
    C_SUCKER_GLOW = (255, 85, 184)
    C_SUCKER_BRT  = (255, 175, 225)

    # =========================================================================
    # 2. SMOOTH HOVERING GROUND SHADOW
    # =========================================================================
    # Clear 8-9 pixel elevation gap under tentacles (y<=48), proving hovering
    shadow_rows = [
        (55, [(27, 37, C_SHD_EDGE)]),
        (56, [(24, 40, C_SHD_EDGE), (27, 37, C_SHD_MID)]),
        (57, [(21, 43, C_SHD_EDGE), (24, 40, C_SHD_MID), (27, 37, C_SHD_CORE)]),
        (58, [(19, 45, C_SHD_EDGE), (22, 42, C_SHD_MID), (25, 39, C_SHD_CORE), (28, 36, C_SHD_DEEP)]),
        (59, [(21, 43, C_SHD_EDGE), (24, 40, C_SHD_MID), (27, 37, C_SHD_CORE)]),
        (60, [(24, 40, C_SHD_EDGE), (27, 37, C_SHD_MID)]),
        (61, [(27, 37, C_SHD_EDGE)]),
    ]
    for sy, spans in shadow_rows:
        for x0, x1, scol in spans:
            for sx in range(x0, x1 + 1):
                c.set(sx, sy, scol)

    # =========================================================================
    # 3. SPHERICAL VOID BODY MASS
    # =========================================================================
    cx, cy = 32, 27
    rx, ry = 17.0, 15.0
    
    for y in range(int(cy - ry - 2), int(cy + ry + 3)):
        for x in range(int(cx - rx - 2), int(cx + rx + 3)):
            dx = (x - cx) / rx
            dy = (y - cy) / ry
            d = math.hypot(dx, dy)
            if d <= 1.0:
                nz = math.sqrt(max(0.0, 1.0 - d*d))
                nx, ny = dx, dy
                dot = nx * (-0.55) + ny * (-0.65) + nz * 0.55
                lobe = math.sin(nx * 5.0) * 0.08 + math.cos(ny * 4.0) * 0.06
                val = dot + lobe
                
                if d >= 0.93:
                    col = C_BLACK
                elif val > 0.62:
                    col = C_FLESH_HI
                elif val > 0.38:
                    col = C_FLESH_MID
                elif val > 0.08:
                    col = C_FLESH_D1
                elif val > -0.25:
                    col = C_FLESH_D2
                elif val > -0.55:
                    col = C_FLESH_D3
                else:
                    col = C_FLESH_D4
                    
                if dx < -0.15 and dy < -0.4 and d < 0.85 and val > 0.68:
                    col = C_FLESH_PEAK
                    
                c.set(x, y, col)

    # =========================================================================
    # 4. SLEEK CURVED VOID HORNS / CHITIN CREST (MENACING & WELL-PROPORTIONED)
    # =========================================================================
    def render_chitin_horn(spine, widths):
        fine = []
        for i in range(len(spine) - 1):
            p0, p1 = spine[i], spine[i+1]
            dist = math.hypot(p1[0]-p0[0], p1[1]-p0[1])
            steps = max(3, int(dist * 3))
            for s in range(steps):
                t = s / steps
                x = p0[0] + (p1[0]-p0[0])*t
                y = p0[1] + (p1[1]-p0[1])*t
                idx_w = min(len(widths)-1, int((i + t) * (len(widths) / len(spine))))
                w = widths[idx_w]
                fine.append((x, y, w, (i + t) / (len(spine) - 1)))
        fine.append((spine[-1][0], spine[-1][1], widths[-1], 1.0))
        
        horn_pixels = {}
        for x, y, w, progress in fine:
            ix, iy = int(round(x)), int(round(y))
            iw = max(0, int(round(w)))
            for oy in range(-iw, iw + 1):
                for ox in range(-iw, iw + 1):
                    d = math.hypot(ox, oy)
                    if d <= w:
                        px, py = ix + ox, iy + oy
                        if 0 <= px < 64 and 0 <= py < 64:
                            norm_x = ox / max(0.5, w)
                            norm_y = oy / max(0.5, w)
                            dot = -0.7 * norm_x - 0.7 * norm_y
                            
                            if progress > 0.75: # Bone Tip
                                col = C_HORN_WHITE if dot > -0.2 else C_HORN_PEAK
                            elif progress > 0.45: # Upper Horn
                                if dot > 0.3: col = C_HORN_PEAK
                                elif dot > -0.2: col = C_HORN_HI
                                else: col = C_HORN_MID
                            else: # Chitin Base
                                if dot > 0.3: col = C_HORN_HI
                                elif dot > -0.2: col = C_HORN_MID
                                else: col = C_HORN_D1
                                
                            horn_pixels[(px, py)] = col
                            
        for (px, py), col in horn_pixels.items():
            c.set(px, py, col)
            
        for (px, py) in list(horn_pixels.keys()):
            for n_dx, n_dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = px + n_dx, py + n_dy
                if (nx, ny) not in horn_pixels:
                    if 0 <= nx < 64 and 0 <= ny < 64 and c.get(nx, ny) is None:
                        c.set(nx, ny, C_BLACK)

    # Sleek curved demon horns framing the skull
    horn_l = [(26, 17), (23, 14), (20, 11), (17, 8), (14, 6), (13, 4)]
    render_chitin_horn(horn_l, [2.8, 2.3, 1.8, 1.4, 0.9, 0.5])

    horn_r = [(38, 17), (41, 14), (44, 11), (47, 8), (50, 6), (51, 4)]
    render_chitin_horn(horn_r, [2.8, 2.3, 1.8, 1.4, 0.9, 0.5])

    # Secondary side spikes
    horn_sub_l = [(20, 19), (16, 17), (13, 16), (11, 15)]
    render_chitin_horn(horn_sub_l, [2.0, 1.5, 1.0, 0.5])

    horn_sub_r = [(44, 19), (48, 17), (51, 16), (53, 15)]
    render_chitin_horn(horn_sub_r, [2.0, 1.5, 1.0, 0.5])

    # Center Forehead Crest (Menacing crown point)
    crest_pts = [
        (32, 10, C_BLACK), (32, 11, C_HORN_WHITE), (32, 12, C_HORN_PEAK), (32, 13, C_HORN_HI),
        (31, 11, C_BLACK), (31, 12, C_HORN_WHITE), (31, 13, C_HORN_PEAK), (31, 14, C_HORN_HI),
        (33, 11, C_BLACK), (33, 12, C_HORN_MID), (33, 13, C_HORN_D1), (33, 14, C_HORN_DARK),
        (30, 13, C_BLACK), (30, 14, C_HORN_PEAK), (30, 15, C_HORN_HI),
        (34, 13, C_BLACK), (34, 14, C_HORN_D1), (34, 15, C_HORN_DARK),
        (29, 15, C_BLACK), (35, 15, C_BLACK),
    ]
    for cx_p, cy_p, cc_p in crest_pts:
        c.set(cx_p, cy_p, cc_p)

    # =========================================================================
    # 5. SHORT TENTACLES (WRITHING, SUSPENDED IN MID-AIR)
    # =========================================================================
    def render_tentacle(pts, is_front=True):
        fine = []
        for i in range(len(pts) - 1):
            p0, p1 = pts[i], pts[i+1]
            dist = math.hypot(p1[0]-p0[0], p1[1]-p0[1])
            steps = max(3, int(dist * 3))
            for s in range(steps):
                t = s / steps
                x = p0[0] + (p1[0]-p0[0])*t
                y = p0[1] + (p1[1]-p0[1])*t
                r = p0[2] + (p1[2]-p0[2])*t
                fine.append((x, y, r))
        fine.append(pts[-1])
        
        for x, y, r in fine:
            ix, iy = int(round(x)), int(round(y))
            ir = max(1, int(round(r)))
            for dy in range(-ir - 1, ir + 2):
                for dx in range(-ir - 1, ir + 2):
                    d = math.hypot(dx, dy)
                    if d <= r:
                        px, py = ix + dx, iy + dy
                        if 0 <= px < 64 and 0 <= py < 64:
                            norm_x = dx / max(0.5, r)
                            norm_y = dy / max(0.5, r)
                            dot = -0.6 * norm_x - 0.7 * norm_y
                            
                            dist_b = math.hypot(px - 32, py - 27)
                            if dist_b < 18:
                                dot -= (18 - dist_b) * 0.07
                                
                            if d >= r - 0.6:
                                col = C_BLACK
                            elif dot > 0.45:
                                col = C_FLESH_HI if is_front else C_FLESH_MID
                            elif dot > 0.1:
                                col = C_FLESH_MID if is_front else C_FLESH_D1
                            elif dot > -0.25:
                                col = C_FLESH_D1 if is_front else C_FLESH_D2
                            elif dot > -0.55:
                                col = C_FLESH_D2 if is_front else C_FLESH_D3
                            else:
                                col = C_FLESH_D3 if is_front else C_FLESH_D4
                            c.set(px, py, col)
                            
        stride = max(4, len(fine) // 4)
        for i in range(stride, len(fine) - 2, stride):
            sx, sy, sr = fine[i]
            p_prev = fine[max(0, i-2)]
            p_next = fine[min(len(fine)-1, i+2)]
            tx = p_next[0] - p_prev[0]
            ty = p_next[1] - p_prev[1]
            tl = math.hypot(tx, ty) or 1
            nx, ny = -ty / tl, tx / tl
            to_cx = 32 - sx
            to_cy = 35 - sy
            if (nx * to_cx + ny * to_cy) < 0:
                nx, ny = -nx, -ny
                
            skx = int(round(sx + nx * (sr * 0.75)))
            sky = int(round(sy + ny * (sr * 0.75)))
            if 0 <= skx < 64 and 0 <= sky < 64:
                c.set(skx, sky, C_SUCKER_GLOW if i % (stride*2) == 0 else C_SUCKER_RIM)

    # Background tentacles
    bg_tentacles = [
        [(18, 22, 2.8), (13, 20, 2.4), (9, 19, 2.0), (6, 21, 1.6), (6, 25, 1.2), (9, 28, 0.7)],
        [(46, 22, 2.8), (51, 20, 2.4), (55, 19, 2.0), (58, 21, 1.6), (58, 25, 1.2), (55, 28, 0.7)],
    ]
    for t in bg_tentacles:
        render_tentacle(t, is_front=False)

    # Foreground tentacles (all terminate at y <= 48!)
    fg_tentacles = [
        # Mid-Left Flank
        [(17, 30, 3.2), (11, 32, 2.8), (7, 36, 2.3), (7, 41, 1.8), (10, 44, 1.2), (13, 44, 0.6)],
        # Lower-Left Underbelly
        [(22, 36, 3.2), (18, 40, 2.7), (17, 44, 2.1), (20, 47, 1.3), (23, 48, 0.6)],
        # Inner-Left Underbelly
        [(27, 39, 2.8), (26, 43, 2.2), (28, 46, 1.5), (30, 47, 0.6)],
        # Inner-Right Underbelly
        [(37, 39, 2.8), (38, 43, 2.2), (36, 46, 1.5), (34, 47, 0.6)],
        # Lower-Right Underbelly
        [(42, 36, 3.2), (46, 40, 2.7), (47, 44, 2.1), (44, 47, 1.3), (41, 48, 0.6)],
        # Mid-Right Flank
        [(47, 30, 3.2), (53, 32, 2.8), (57, 36, 2.3), (57, 41, 1.8), (54, 44, 1.2), (51, 44, 0.6)],
    ]
    for t in fg_tentacles:
        render_tentacle(t, is_front=True)

    # =========================================================================
    # 6. EYE APERTURE & SCLERA
    # =========================================================================
    eye_pixels = set()
    for x in range(18, 47):
        t = (x - 32) / 14.0
        if abs(t) <= 1.0:
            base_curve = math.sqrt(max(0.0, 1.0 - t*t))
            scowl_dip = (1.0 - abs(t)) * 1.2
            y_top = 27 - (9.2 * base_curve - scowl_dip)
            y_bot = 27 + (8.2 * base_curve)
            for y in range(int(math.ceil(y_top)), int(math.floor(y_bot)) + 1):
                eye_pixels.add((x, y))

    # Render Sclera
    for (x, y) in eye_pixels:
        dx = (x - 32) / 14.0
        dy = (y - 27) / 8.5
        d = math.hypot(dx, dy)
        nz = math.sqrt(max(0.0, 1.0 - min(1.0, d*d)))
        dot = dx * (-0.4) + dy * (-0.6) + nz * 0.7
        
        t = (x - 32) / 14.0
        base_curve = math.sqrt(max(0.0, 1.0 - t*t))
        scowl_dip = (1.0 - abs(t)) * 1.2
        y_top_edge = 27 - (9.2 * base_curve - scowl_dip)
        dist_from_lid = y - y_top_edge
        
        if dist_from_lid <= 1.4:
            col = C_SCLERA_D4
        elif dist_from_lid <= 2.6:
            col = C_SCLERA_D3
        elif dist_from_lid <= 3.8 or dot < 0.0:
            col = C_SCLERA_D2
        elif dot < 0.3:
            col = C_SCLERA_MID
        elif dot < 0.6:
            col = C_SCLERA_LGT
        elif dot < 0.82:
            col = C_SCLERA_BRT
        else:
            col = C_SCLERA_HI
            
        c.set(x, y, col)

    # Branching organic veins on Sclera
    vein_branches = [
        (19, 27, C_VEIN_H), (20, 27, C_VEIN_H), (21, 26, C_VEIN_M),
        (22, 26, C_VEIN_M), (23, 25, C_VEIN_M), (24, 25, C_VEIN_D),
        (21, 27, C_VEIN_M), (22, 28, C_VEIN_D), (23, 28, C_VEIN_D),
        (20, 28, C_VEIN_D), (24, 26, C_VEIN_D),
        (45, 27, C_VEIN_H), (44, 27, C_VEIN_H), (43, 26, C_VEIN_M),
        (42, 26, C_VEIN_M), (41, 25, C_VEIN_M), (40, 25, C_VEIN_D),
        (43, 27, C_VEIN_M), (42, 28, C_VEIN_D), (41, 28, C_VEIN_D),
        (44, 28, C_VEIN_D), (40, 26, C_VEIN_D),
        (28, 22, C_VEIN_D), (29, 23, C_VEIN_M),
        (36, 22, C_VEIN_D), (35, 23, C_VEIN_M),
        (28, 32, C_VEIN_D), (29, 31, C_VEIN_M),
        (36, 32, C_VEIN_D), (35, 31, C_VEIN_M),
    ]
    for vx, vy, vc in vein_branches:
        if (vx, vy) in eye_pixels:
            c.set(vx, vy, vc)

    # =========================================================================
    # 7. DEEP PURPLE IRIS
    # =========================================================================
    iris_cx, iris_cy = 32.0, 27.0
    iris_r = 7.8
    
    for y in range(int(iris_cy - iris_r - 1), int(iris_cy + iris_r + 2)):
        for x in range(int(iris_cx - iris_r - 1), int(iris_cx + iris_r + 2)):
            if (x, y) not in eye_pixels:
                continue
            dx = x - iris_cx
            dy = y - iris_cy
            dist = math.hypot(dx, dy)
            if dist <= iris_r:
                angle = math.atan2(dy, dx)
                fiber = math.sin(angle * 10.0) * 0.14 + math.sin(angle * 20.0) * 0.08
                val = dist / iris_r + fiber
                
                if y <= 23: val += 0.35
                elif y <= 25: val += 0.15
                    
                if dist >= iris_r - 0.8:
                    col = C_IRIS_LIMBAL
                elif val > 0.82:
                    col = C_IRIS_D3
                elif val > 0.65:
                    col = C_IRIS_D2
                elif val > 0.48:
                    col = C_IRIS_D1
                elif val > 0.32:
                    col = C_IRIS_MID
                elif val > 0.18:
                    col = C_IRIS_VIB
                else:
                    col = C_IRIS_HI
                    
                c.set(x, y, col)

    # =========================================================================
    # 8. FAINTLY GLOWING PUPIL
    # =========================================================================
    for dy in range(-5, 6):
        for dx in range(-4, 5):
            px = int(iris_cx + dx)
            py = int(iris_cy + dy)
            if (px, py) not in eye_pixels:
                continue
            
            metric = abs(dx) * 2.0 + abs(dy) * 0.7
            if metric <= 4.8:
                if metric > 3.4:
                    col = C_GLOW_D4
                elif metric > 2.3:
                    col = C_GLOW_D3
                elif metric > 1.4:
                    col = C_GLOW_D2
                elif metric > 0.8:
                    col = C_GLOW_MID
                else:
                    col = C_GLOW_BRT
                c.set(px, py, col)

    # Slit void core with glowing pulse
    c.set(32, 23, C_PUPIL_BLACK)
    c.set(32, 24, C_PUPIL_BLACK)
    c.set(32, 25, C_GLOW_PALE)
    c.set(32, 26, C_WHITE)      # Faint glowing epicenter
    c.set(32, 27, C_GLOW_PALE)
    c.set(32, 28, C_PUPIL_BLACK)
    c.set(32, 29, C_PUPIL_BLACK)
    
    # Eerie cyan aura bleed around slit
    c.set(31, 26, C_GLOW_BRT)
    c.set(33, 26, C_GLOW_BRT)
    c.set(31, 27, C_GLOW_MID)
    c.set(33, 27, C_GLOW_MID)

    # =========================================================================
    # 9. CORNEA SPECULAR GLOSS
    # =========================================================================
    c.set(28, 23, C_WHITE)
    c.set(29, 23, C_WHITE)
    c.set(28, 24, C_WHITE)
    c.set(29, 24, C_GLOW_PALE)
    c.set(30, 23, C_SCLERA_HI)
    c.set(27, 24, C_SCLERA_LGT)
    
    c.set(36, 30, C_IRIS_HI)
    c.set(37, 30, C_IRIS_VIB)

    # =========================================================================
    # 10. HEAVY EYELID RIDGES & MENACING BROW
    # =========================================================================
    for x in range(17, 48):
        t = (x - 32) / 14.0
        if abs(t) <= 1.05:
            base_curve = math.sqrt(max(0.0, 1.0 - min(1.0, t*t)))
            scowl_dip = (1.0 - min(1.0, abs(t))) * 1.2
            y_top = int(round(27 - (9.2 * base_curve - scowl_dip)))
            y_bot = int(round(27 + (8.2 * base_curve)))
            
            # Upper eyelid ridge
            c.set(x, y_top, C_BLACK)
            c.set(x, y_top - 1, C_FLESH_D3 if x % 2 == 0 else C_FLESH_D2)
            c.set(x, y_top - 2, C_FLESH_MID if (23 <= x <= 41) else C_FLESH_D1)
            if y_top - 3 >= 14 and (25 <= x <= 39):
                c.set(x, y_top - 3, C_FLESH_HI if (27 <= x <= 37) else C_FLESH_MID)
                
            # Lower eyelid ridge
            c.set(x, y_bot, C_BLACK)
            c.set(x, y_bot + 1, C_FLESH_D3)
            c.set(x, y_bot + 2, C_FLESH_D4)

    # Socket corners
    c.set(17, 27, C_BLACK)
    c.set(16, 27, C_FLESH_D3)
    c.set(47, 27, C_BLACK)
    c.set(48, 27, C_FLESH_D3)

    # Deep brow wrinkles (center forehead)
    c.set(31, 16, C_BLACK)
    c.set(32, 16, C_BLACK)
    c.set(31, 15, C_FLESH_D3)
    c.set(32, 15, C_FLESH_D3)
    c.set(30, 15, C_FLESH_HI)
    c.set(33, 15, C_FLESH_MID)

    # =========================================================================
    # 11. SUBTLE DRIFTING VOID PARTICLES (BOSS AURA)
    # =========================================================================
    particles = [
        (10, 11, C_GLOW_BRT), (11, 12, C_GLOW_D3),
        (53, 11, C_GLOW_BRT), (52, 12, C_GLOW_D3),
        (6, 29, C_GLOW_D2),
        (57, 29, C_GLOW_D2),
        (14, 51, C_IRIS_HI),
        (49, 51, C_IRIS_HI),
    ]
    for px, py, col in particles:
        if 0 <= px < 64 and 0 <= py < 64 and c.get(px, py) is None:
            c.set(px, py, col)

    print(c.stats_text())
    view(c)
    finish(c)

if __name__ == "__main__":
    draw_void_eye_boss()
