import math
from pixelbench_api import *

# Master Cohesive Dawn Palette (55 colors, well under 86 limit)
PAL = {
    # Sky & Sunrise (8)
    "sky_deep": "#1a0f30",
    "sky_indigo": "#2b1842",
    "sky_purple": "#482150",
    "sky_rose": "#742b56",
    "sky_coral": "#a43c53",
    "sky_orange": "#d8603c",
    "sky_gold": "#f19a3b",
    "sky_peach": "#fad06c",
    
    # Sun & Core Glow (2)
    "sun_white": "#fffde8",
    "sun_halo": "#fedf88",
    
    # Far Mountains & Snow (7)
    "mtn_shadow": "#2c1d40",
    "mtn_mid": "#482b52",
    "mtn_lit": "#7a4366",
    "snow_shadow": "#72678e",
    "snow_mid": "#9c8ea6",
    "snow_lit": "#ffd4b8",
    "snow_white": "#fff3e6",
    
    # Mid-range Ridge & Mist (4)
    "ridge_shadow": "#1e162c",
    "ridge_lit": "#3d2842",
    "mist_dark": "#684a65",
    "mist_light": "#aa8197",
    
    # Pine Trees (6)
    "pine_black": "#081012",
    "pine_shadow": "#0e1e1b",
    "pine_dark": "#163229",
    "pine_mid": "#254e3a",
    "pine_lit": "#427246",
    "pine_gold": "#759642",
    
    # Meadow & Terraces (6)
    "grass_dark": "#142416",
    "grass_mid": "#223f20",
    "grass_lit": "#3a5f2a",
    "grass_gold": "#688834",
    "earth_dark": "#1f1510",
    "earth_lit": "#462e1f",
    
    # Wood & Chalets (8)
    "wood_black": "#110a07",
    "wood_shadow": "#271710",
    "wood_mid": "#472918",
    "wood_lit": "#6c3f22",
    "wood_gold": "#965d2f",
    "roof_shadow": "#201220",
    "roof_mid": "#3c2237",
    "roof_lit": "#653856",
    
    # Stone & Cobblestone Path (6)
    "stone_dark": "#1b1920",
    "stone_mid": "#36343e",
    "stone_light": "#565260",
    "stone_lit": "#827682",
    "stone_high": "#b5a3a1",
    "stone_edge": "#d4c2ba",
    
    # Window Glow & Hearth (5)
    "glow_red": "#721f0d",
    "glow_orange": "#b04312",
    "glow_amber": "#dd7e18",
    "glow_yellow": "#f2c232",
    "glow_white": "#fff9b2",
    
    # Chimney Smoke (4)
    "smoke_shadow": "#463c4e",
    "smoke_mid": "#6e5f76",
    "smoke_lit": "#b2919e",
    "smoke_white": "#efd1d8",
    
    # Wildflowers (3)
    "flower_white": "#fff8ea",
    "flower_yellow": "#fcd752",
    "flower_blue": "#8aa2cc",
}

def pset(c, x, y, col):
    if 0 <= x < 128 and 0 <= y < 128:
        c.set(x, y, col)

def draw_art():
    c = new_canvas(128, 128)
    c.rect(0, 0, 128, 128, PAL["sky_deep"])

    # -------------------------------------------------------------
    # 1. SKY GRADIENT & RISING SUN
    # -------------------------------------------------------------
    sky_bands = [
        (0, 6, PAL["sky_deep"], PAL["sky_indigo"]),
        (6, 13, PAL["sky_indigo"], PAL["sky_purple"]),
        (13, 21, PAL["sky_purple"], PAL["sky_rose"]),
        (21, 29, PAL["sky_rose"], PAL["sky_coral"]),
        (29, 38, PAL["sky_coral"], PAL["sky_orange"]),
        (38, 47, PAL["sky_orange"], PAL["sky_gold"]),
        (47, 58, PAL["sky_gold"], PAL["sky_peach"]),
    ]
    for y0, y1, c0, c1 in sky_bands:
        for y in range(y0, y1):
            t = (y - y0) / (y1 - y0)
            for x in range(128):
                if t < 0.25:
                    col = c0
                elif t < 0.5:
                    col = c1 if ((x + y) % 3 == 0) else c0
                elif t < 0.75:
                    col = c1 if ((x + y) % 2 == 0) else c0
                elif t < 0.9:
                    col = c0 if ((x + y) % 3 == 0) else c1
                else:
                    col = c1
                pset(c, x, y, col)

    # Rising Sun at x=86, y=28
    sun_x, sun_y = 86, 28
    for dy in range(-25, 26):
        for dx in range(-32, 33):
            x = sun_x + dx
            y = sun_y + dy
            if 0 <= x < 128 and 0 <= y < 58:
                d = math.sqrt(dx * dx + (dy * 1.25) * (dy * 1.25))
                if d <= 3.8:
                    pset(c, x, y, PAL["sun_white"])
                elif d <= 6.5:
                    pset(c, x, y, PAL["sun_halo"])
                elif d <= 11.0:
                    if d <= 8.5 or (x + y) % 2 == 0:
                        pset(c, x, y, PAL["sun_halo"])
                    else:
                        pset(c, x, y, PAL["sky_peach"])
                elif d <= 17.0:
                    if d <= 13.5 or (x + y) % 2 == 0:
                        pset(c, x, y, PAL["sky_peach"])
                    else:
                        pset(c, x, y, PAL["sky_gold"])
                elif d <= 24.0:
                    if (x + y) % 2 == 0 and d <= 20.0:
                        pset(c, x, y, PAL["sky_gold"])

    # High cirrus dawn clouds (gentle, organic wisps)
    for ox in range(32):
        x = 10 + ox
        y = 14 + int(math.sin(ox * 0.2) * 1.5)
        pset(c, x, y, PAL["sky_peach"] if ox % 2 == 0 else PAL["sun_halo"])
        pset(c, x, y - 1, PAL["sky_rose"])

    for ox in range(28):
        x = 55 + ox
        y = 11 + int(math.sin(ox * 0.25) * 1.2)
        pset(c, x, y, PAL["sun_halo"] if ox % 2 == 0 else PAL["sky_peach"])
        pset(c, x, y - 1, PAL["sky_rose"])

    # -------------------------------------------------------------
    # 2. DISTANT ALPINE MOUNTAINS (Layer 1)
    # -------------------------------------------------------------
    def get_mtn_top(x):
        pts = [
            (-10, 48), (6, 28), (22, 16), (34, 26), (42, 32),
            (48, 24), (60, 33), (68, 28), (78, 17), (92, 28),
            (102, 27), (114, 21), (124, 31), (138, 45)
        ]
        for i in range(len(pts) - 1):
            if pts[i][0] <= x <= pts[i+1][0]:
                x0, y0 = pts[i]
                x1, y1 = pts[i+1]
                t = (x - x0) / (x1 - x0)
                return y0 + t * (y1 - y0)
        return 50.0

    def get_ridge_x(y):
        r1 = 22 + (y - 16) * 0.24
        r3 = 78 - (y - 17) * 0.16
        r4 = 114 - (y - 21) * 0.1
        return r1, r3, r4

    for x in range(128):
        yt = int(round(get_mtn_top(x)))
        for y in range(yt, 58):
            r1, r3, r4 = get_ridge_x(y)
            
            if x < 42:
                is_lit = (x >= r1)
            elif x < 64:
                is_lit = (x >= 48)
            elif x < 100:
                is_lit = (x >= r3)
            else:
                is_lit = (x >= r4)

            dist_top = y - yt
            couloir = int(round(math.sin(x * 1.2) * 2.2 + math.cos(x * 0.6) * 1.8))
            snow_reach = 11 + couloir

            if dist_top <= snow_reach and y < 42:
                if is_lit:
                    if dist_top <= 2 or x in (int(round(r3)), int(round(r1))):
                        col = PAL["snow_white"]
                    elif (x + y) % 4 == 0:
                        col = PAL["snow_white"]
                    else:
                        col = PAL["snow_lit"]
                else:
                    col = PAL["snow_mid"] if (x + y) % 3 == 0 else PAL["snow_shadow"]
            else:
                if is_lit:
                    col = PAL["mtn_lit"] if (x + y) % 2 == 0 else PAL["mtn_mid"]
                else:
                    col = PAL["mtn_mid"] if (x + y) % 3 == 0 else PAL["mtn_shadow"]
            pset(c, x, y, col)

    # -------------------------------------------------------------
    # 3. MID-RANGE MOUNTAIN RIDGE & VALLEY MIST (Layer 2)
    # -------------------------------------------------------------
    def get_mid_ridge(x):
        pts = [
            (-10, 50), (16, 43), (36, 39), (56, 44),
            (74, 38), (94, 41), (114, 36), (138, 45)
        ]
        for i in range(len(pts) - 1):
            if pts[i][0] <= x <= pts[i+1][0]:
                x0, y0 = pts[i]
                x1, y1 = pts[i+1]
                t = (x - x0) / (x1 - x0)
                return y0 + t * (y1 - y0)
        return 44.0

    for x in range(128):
        yt = int(round(get_mid_ridge(x)))
        for y in range(yt, 66):
            is_lit = (x % 14 > 6)
            col = PAL["ridge_lit"] if (is_lit and (x + y) % 2 == 0) else PAL["ridge_shadow"]
            pset(c, x, y, col)

        if x % 3 == 0 and (x % 9 != 0):
            th = 2 + (x % 3)
            for ty in range(th):
                pset(c, x, yt - ty, PAL["pine_black"])
                if ty > 0 and 0 < x < 127:
                    pset(c, x - 1, yt - ty + 1, PAL["pine_black"])
                    pset(c, x + 1, yt - ty + 1, PAL["pine_black"])

    # Morning valley mist ribbons
    for y in range(49, 61):
        for x in range(128):
            wave = math.sin(x * 0.08 + y * 0.4) * 0.5 + math.cos(x * 0.16 - y * 0.2) * 0.4
            band = 1.0 - abs(y - 54) / 6.0
            dens = wave + band
            if dens > 1.1:
                pset(c, x, y, PAL["mist_light"])
            elif dens > 0.7:
                if (x + y) % 2 == 0:
                    pset(c, x, y, PAL["mist_light"])
                elif (x + y) % 3 == 0:
                    pset(c, x, y, PAL["mist_dark"])

    # -------------------------------------------------------------
    # 4. VILLAGE HILLSIDE & MEADOW TERRAIN (Layer 3)
    # -------------------------------------------------------------
    def get_ground_y(x):
        pts = [
            (0, 68), (20, 66), (44, 63), (64, 62),
            (84, 64), (108, 66), (127, 68)
        ]
        for i in range(len(pts) - 1):
            if pts[i][0] <= x <= pts[i+1][0]:
                x0, y0 = pts[i]
                x1, y1 = pts[i+1]
                t = (x - x0) / (x1 - x0)
                return y0 + t * (y1 - y0)
        return 65.0

    for x in range(128):
        gy = int(round(get_ground_y(x)))
        for y in range(gy, 128):
            dy = y - gy
            if dy <= 1:
                pset(c, x, y, PAL["grass_gold"])
            elif dy <= 3:
                pset(c, x, y, PAL["grass_lit"])
            elif y > 100:
                split_x = 55 + int(round(math.sin(y * 0.15) * 6))
                if x < split_x - 12:
                    pset(c, x, y, PAL["grass_dark"] if (x + y * 3) % 7 == 0 else PAL["grass_mid"])
                elif x > split_x + 12:
                    pset(c, x, y, PAL["grass_gold"] if (x + y * 2) % 8 == 0 else PAL["grass_lit"])
                else:
                    pset(c, x, y, PAL["grass_lit"] if (x + y) % 2 == 0 else PAL["grass_mid"])
            else:
                pset(c, x, y, PAL["grass_lit"] if (x * 2 + y * 3) % 9 < 4 else PAL["grass_mid"])

    # Embankments
    for tx in range(12, 38):
        if tx % 4 != 0:
            pset(c, tx, 73, PAL["earth_dark"])
            pset(c, tx, 74, PAL["earth_lit"] if tx % 2 == 0 else PAL["grass_dark"])

    for tx in range(86, 116):
        if tx % 4 != 0:
            pset(c, tx, 76, PAL["earth_dark"])
            pset(c, tx, 77, PAL["earth_lit"] if tx % 2 == 0 else PAL["grass_dark"])

    # -------------------------------------------------------------
    # 5. THE THREE WOODEN CHALETS
    # -------------------------------------------------------------
    def draw_chalet(hx, hy, hw, hh, apex_y,
                    dormer=False, balcony=False,
                    win_left=True, win_right=True,
                    chimney_x=None, door_x=None):
        wall_l = hx
        wall_r = hx + hw
        wall_t = hy
        wall_b = hy + hh
        apex_x = hx + hw // 2
        eaves_overhang = 6
        roof_l = wall_l - eaves_overhang
        roof_r = wall_r + eaves_overhang
        eaves_y = wall_t + 2

        # 1. GABLE WALL (Drawn first)
        for gy in range(apex_y + 4, eaves_y):
            t = (gy - apex_y) / max(1, (eaves_y - apex_y))
            gx0 = int(round(apex_x - t * (apex_x - roof_l))) + 3
            gx1 = int(round(apex_x + t * (roof_r - apex_x))) - 3
            for gx in range(gx0, gx1 + 1):
                plank_phase = (gy - apex_y) % 3
                if plank_phase == 0:
                    pset(c, gx, gy, PAL["wood_gold"] if gx > apex_x else PAL["wood_lit"])
                elif plank_phase == 1:
                    pset(c, gx, gy, PAL["wood_lit"] if gx > apex_x else PAL["wood_mid"])
                else:
                    pset(c, gx, gy, PAL["wood_shadow"])

        for gy in range(apex_y + 4, eaves_y):
            pset(c, apex_x, gy, PAL["wood_shadow"])

        # 2. ROOF BARGEBOARDS & SLOPES (Drawn ON TOP of gable)
        for y in range(apex_y, eaves_y + 1):
            t = (y - apex_y) / max(1, (eaves_y - apex_y))
            rx0 = int(round(apex_x - t * (apex_x - roof_l)))
            rx1 = int(round(apex_x + t * (roof_r - apex_x)))
            
            # Left bargeboard (shadowed, 3px thick)
            for bx in range(rx0, rx0 + 3):
                pset(c, bx, y, PAL["wood_shadow"] if bx == rx0 else PAL["roof_mid"])
            
            # Right bargeboard (sunlit, 3px thick)
            for bx in range(rx1 - 2, rx1 + 1):
                pset(c, bx, y, PAL["wood_gold"] if bx == rx1 else PAL["roof_lit"])

            # Ridge cap
            if y <= apex_y + 3:
                for bx in range(rx0, rx1 + 1):
                    pset(c, bx, y, PAL["roof_lit"] if bx >= apex_x else PAL["roof_mid"])

        # Eaves fascia beam & shadow under eaves
        for rx in range(roof_l, roof_r + 1):
            pset(c, rx, eaves_y, PAL["wood_gold"] if rx >= apex_x else PAL["wood_shadow"])
            if wall_l <= rx < wall_r:
                pset(c, rx, eaves_y + 1, PAL["wood_black"])

        # 3. Dormer window (attic)
        if dormer:
            dw_x = apex_x - 3
            dw_y = wall_t - 5
            for dy in range(dw_y, dw_y + 6):
                for dx in range(dw_x, dw_x + 6):
                    pset(c, dx, dy, PAL["wood_black"])
            for dy in range(dw_y + 1, dw_y + 5):
                for dx in range(dw_x + 1, dw_x + 5):
                    if dy == dw_y + 2 or dx == dw_x + 2:
                        pset(c, dx, dy, PAL["wood_shadow"])
                    else:
                        pset(c, dx, dy, PAL["glow_white"] if (dx == dw_x + 3 and dy == dw_y + 3) else PAL["glow_yellow"])
            pset(c, apex_x - 1, dw_y, PAL["wood_gold"])
            pset(c, apex_x, dw_y, PAL["wood_gold"])

        # 4. Wooden alpine balcony
        if balcony:
            by = wall_t + 2
            bw = hw - 4
            bx0 = wall_l + 2
            for bx in range(bx0, bx0 + bw):
                pset(c, bx, by, PAL["wood_gold"] if bx >= apex_x else PAL["wood_lit"])
                pset(c, bx, by + 3, PAL["wood_shadow"])
                if bx % 2 == 0:
                    pset(c, bx, by + 1, PAL["wood_lit"] if bx >= apex_x else PAL["wood_mid"])
                    pset(c, bx, by + 2, PAL["wood_mid"])
                else:
                    pset(c, bx, by + 1, PAL["wood_black"])
                    pset(c, bx, by + 2, PAL["wood_black"])
            for bx in range(bx0 + 2, bx0 + bw - 2):
                if bx % 3 == 0:
                    pset(c, bx, by + 3, PAL["glow_orange"])
                elif bx % 3 == 1:
                    pset(c, bx, by + 3, PAL["flower_yellow"])

        # 5. Main log walls (Sturdy thick logs, 4px high each)
        start_y = eaves_y + 2
        for wy in range(start_y, wall_b):
            log_phase = (wy - start_y) % 4
            for wx in range(wall_l, wall_r):
                if wx in (wall_l, wall_l + 1):
                    pset(c, wx, wy, PAL["wood_black"] if log_phase == 0 else PAL["wood_shadow"])
                elif wx in (wall_r - 1, wall_r - 2):
                    pset(c, wx, wy, PAL["wood_gold"] if log_phase == 0 else PAL["wood_lit"])
                else:
                    if log_phase == 0:
                        pset(c, wx, wy, PAL["wood_gold"] if wx >= apex_x else PAL["wood_lit"])
                    elif log_phase in (1, 2):
                        pset(c, wx, wy, PAL["wood_lit"] if wx >= apex_x else PAL["wood_mid"])
                    else:
                        pset(c, wx, wy, PAL["wood_shadow"] if wx >= apex_x else PAL["wood_black"])

        # 6. Windows with dark shutters
        if win_left:
            wx0 = wall_l + 3
            wy0 = wall_b - 9
            ww, wh = 6, 6
            for wy in range(wy0, wy0 + wh):
                for wx in range(wx0, wx0 + ww):
                    if wx == wx0 or wx == wx0 + ww - 1 or wy == wy0 or wy == wy0 + wh - 1:
                        pset(c, wx, wy, PAL["wood_black"])
                    elif wx == wx0 + ww // 2 or wy == wy0 + wh // 2:
                        pset(c, wx, wy, PAL["wood_shadow"])
                    else:
                        pset(c, wx, wy, PAL["glow_white"] if (wx == wx0 + 2 and wy == wy0 + 2) else PAL["glow_yellow"])
            for wx in range(wx0 - 1, wx0 + ww + 1):
                pset(c, wx, wy0 + wh, PAL["wood_lit"])

        if win_right:
            wx0 = wall_r - 9
            wy0 = wall_b - 9
            ww, wh = 6, 6
            for wy in range(wy0, wy0 + wh):
                for wx in range(wx0, wx0 + ww):
                    if wx == wx0 or wx == wx0 + ww - 1 or wy == wy0 or wy == wy0 + wh - 1:
                        pset(c, wx, wy, PAL["wood_black"])
                    elif wx == wx0 + ww // 2 or wy == wy0 + wh // 2:
                        pset(c, wx, wy, PAL["wood_shadow"])
                    else:
                        pset(c, wx, wy, PAL["glow_white"] if (wx == wx0 + 4 and wy == wy0 + 2) else PAL["glow_yellow"])
            for wx in range(wx0 - 1, wx0 + ww + 1):
                pset(c, wx, wy0 + wh, PAL["wood_gold"])

        # 7. Door
        if door_x is None:
            door_x = apex_x - 3
        dw, dh = 5, 10
        dy0 = wall_b - dh
        for dy in range(dy0, wall_b):
            for dx in range(door_x, door_x + dw):
                if dx == door_x or dx == door_x + dw - 1 or dy == dy0:
                    pset(c, dx, dy, PAL["wood_black"])
                else:
                    pset(c, dx, dy, PAL["wood_shadow"] if dy % 2 == 0 else PAL["wood_mid"])
        pset(c, door_x + dw - 2, dy0 + 5, PAL["wood_gold"])

        # 8. Stone Foundation
        for fy in range(wall_b, wall_b + 3):
            for fx in range(wall_l - 1, wall_r + 1):
                if (fx + fy * 2) % 3 == 0:
                    pset(c, fx, fy, PAL["stone_dark"])
                elif fx >= apex_x:
                    pset(c, fx, fy, PAL["stone_lit"] if (fx + fy) % 2 == 0 else PAL["stone_mid"])
                else:
                    pset(c, fx, fy, PAL["stone_mid"] if (fx + fy) % 2 == 0 else PAL["stone_dark"])

        # 9. Stone Chimney
        if chimney_x is not None:
            ch_w = 5
            ch_h = 9
            ch_y0 = apex_y - 1
            for cy in range(ch_y0, ch_y0 + ch_h):
                for cx in range(chimney_x, chimney_x + ch_w):
                    if cy == ch_y0:
                        pset(c, cx, cy, PAL["stone_lit"] if cx > chimney_x + 2 else PAL["stone_mid"])
                    elif cy == ch_y0 + 1:
                        pset(c, cx, cy, PAL["stone_dark"])
                    elif cx == chimney_x:
                        pset(c, cx, cy, PAL["stone_dark"])
                    elif cx == chimney_x + ch_w - 1:
                        pset(c, cx, cy, PAL["stone_lit"])
                    else:
                        pset(c, cx, cy, PAL["stone_mid"] if (cx + cy) % 2 == 0 else PAL["stone_dark"])

    # Draw House 1 (Left House): x=14, y=74, w=22, h=13, apex=63
    draw_chalet(hx=14, hy=74, hw=22, hh=13, apex_y=63,
                dormer=False, balcony=False,
                win_left=True, win_right=False,
                chimney_x=17, door_x=28)

    for sy in range(80, 87):
        for sx in range(35, 39):
            if sy == 80:
                pset(c, sx, sy, PAL["wood_shadow"])
            elif (sx + sy) % 2 == 0:
                pset(c, sx, sy, PAL["wood_gold"])
            else:
                pset(c, sx, sy, PAL["wood_mid"])

    # Draw House 3 (Right House): x=92, y=77, w=22, h=15, apex=66
    draw_chalet(hx=92, hy=77, hw=22, hh=15, apex_y=66,
                dormer=False, balcony=False,
                win_left=True, win_right=True,
                chimney_x=108, door_x=103)

    for sy in range(85, 93):
        for sx in range(114, 122):
            if sy == 85:
                pset(c, sx, sy, PAL["wood_gold"])
            elif sx == 121:
                pset(c, sx, sy, PAL["wood_lit"])
            else:
                pset(c, sx, sy, PAL["wood_gold"] if (sx + sy) % 3 == 0 else PAL["wood_mid"])

    # Draw House 2 (CENTER HOUSE - HERO FOCAL POINT):
    # Centered at x=64, w=32, h=20, apex=54
    draw_chalet(hx=48, hy=74, hw=32, hh=20, apex_y=54,
                dormer=True, balcony=True,
                win_left=True, win_right=True,
                chimney_x=53, door_x=62)

    lan_x, lan_y = 60, 82
    pset(c, lan_x, lan_y - 1, PAL["wood_black"])
    pset(c, lan_x, lan_y, PAL["glow_white"])
    pset(c, lan_x, lan_y + 1, PAL["glow_yellow"])
    pset(c, lan_x - 1, lan_y, PAL["glow_amber"])
    pset(c, lan_x + 1, lan_y, PAL["glow_amber"])
    for lx in range(58, 64):
        pset(c, lx, 94, PAL["glow_amber"] if lx % 2 == 0 else PAL["wood_lit"])

    for step_y in range(94, 98):
        sw = 10 + (step_y - 94) * 2
        sx0 = 64 - sw // 2
        for sx in range(sx0, sx0 + sw):
            if step_y == 94:
                pset(c, sx, step_y, PAL["stone_lit"] if sx > 64 else PAL["stone_mid"])
            else:
                pset(c, sx, step_y, PAL["stone_mid"] if (sx + step_y) % 2 == 0 else PAL["stone_dark"])

    # -------------------------------------------------------------
    # 6. STONE PATH (Natural Cobblestone Flagstones)
    # -------------------------------------------------------------
    def draw_flagstone(fx, fy, fw, fh, high_lit=False):
        for y in range(fy, fy + fh):
            for x in range(fx, fx + fw):
                if 0 <= x < 128 and 0 <= y < 128:
                    is_corner = (x == fx or x == fx + fw - 1) and (y == fy or y == fy + fh - 1)
                    if is_corner:
                        pset(c, x, y, PAL["stone_dark"])
                    elif y == fy + fh - 1 or x == fx:
                        pset(c, x, y, PAL["stone_dark"])
                    elif y == fy or x == fx + fw - 1:
                        pset(c, x, y, PAL["stone_edge"] if high_lit else PAL["stone_lit"])
                    else:
                        pset(c, x, y, PAL["stone_high"] if high_lit else PAL["stone_light"])

    def get_path_x_range(y):
        if y < 97: return None
        t = (y - 97) / (127 - 97)
        cx = 64 - math.sin(t * math.pi) * 5
        hw = 5 + t * 9
        return int(cx - hw), int(cx + hw)

    for y in range(97, 128):
        pr = get_path_x_range(y)
        if pr:
            x0, x1 = pr
            for x in range(x0, x1 + 1):
                pset(c, x, y, PAL["stone_dark"] if (x + y) % 3 != 0 else PAL["earth_dark"])

    flagstones = [
        (61, 98, 4, 3, True), (66, 99, 4, 3, False),
        (59, 101, 5, 3, False), (65, 102, 4, 3, True),
        (57, 104, 4, 3, False), (62, 105, 5, 3, False), (68, 105, 4, 3, True),
        (54, 108, 4, 3, True), (59, 108, 5, 3, False), (65, 109, 5, 3, False),
        (53, 111, 5, 3, False), (59, 112, 4, 3, True), (64, 112, 6, 3, False),
        (52, 115, 5, 3, True), (58, 115, 6, 3, False), (65, 116, 5, 3, True),
        (49, 118, 5, 3, False), (55, 119, 5, 3, True), (61, 119, 6, 3, False), (68, 119, 5, 3, False),
        (48, 122, 6, 3, True), (55, 122, 5, 3, False), (61, 123, 6, 3, True), (68, 122, 6, 3, False),
        (47, 125, 6, 3, False), (54, 125, 6, 3, True), (61, 126, 6, 3, False), (68, 125, 7, 3, True),
    ]
    for fx, fy, fw, fh, hl in flagstones:
        draw_flagstone(fx, fy, fw, fh, high_lit=hl)

    for y in range(98, 128):
        pr = get_path_x_range(y)
        if pr:
            x0, x1 = pr
            if y % 3 == 0:
                pset(c, x0, y, PAL["grass_lit"])
                pset(c, x0 - 1, y, PAL["grass_gold"])
            if y % 4 == 0:
                pset(c, x1, y, PAL["grass_gold"])
                pset(c, x1 + 1, y, PAL["grass_lit"])

    # -------------------------------------------------------------
    # 7. PINE TREES (Layered Evergreens)
    # -------------------------------------------------------------
    def draw_pine_tree(tx, ty, th, tw):
        trunk_h = max(3, th // 5)
        for y in range(ty - trunk_h, ty + 1):
            pset(c, tx, y, PAL["wood_black"])
            pset(c, tx + 1, y, PAL["wood_shadow"])
            
        foliage_top = ty - th
        num_tiers = max(3, th // 8)
        tier_h = (th - trunk_h) / num_tiers
        
        for tier in range(num_tiers):
            tier_top = foliage_top + tier * tier_h
            tier_bot = tier_top + tier_h * 1.35
            tier_w = tw * ((tier + 1) / num_tiers)
            
            for y in range(int(round(tier_top)), int(round(tier_bot)) + 1):
                if y > ty - trunk_h + 1: continue
                prog = (y - tier_top) / max(1, (tier_bot - tier_top))
                w = max(1, tier_w * prog)
                rx0 = int(round(tx - w / 2))
                rx1 = int(round(tx + w / 2))
                
                for x in range(rx0, rx1 + 1):
                    is_right = (x > tx)
                    is_bottom = (y >= int(round(tier_bot)) - 1)
                    
                    if is_right:
                        if x == rx1 or is_bottom:
                            pset(c, x, y, PAL["pine_gold"])
                        elif x > tx + w * 0.3:
                            pset(c, x, y, PAL["pine_lit"])
                        else:
                            pset(c, x, y, PAL["pine_mid"])
                    else:
                        if is_bottom or x == rx0:
                            pset(c, x, y, PAL["pine_black"])
                        elif x < tx - w * 0.3:
                            pset(c, x, y, PAL["pine_shadow"])
                        else:
                            pset(c, x, y, PAL["pine_dark"])

    draw_pine_tree(tx=9, ty=76, th=24, tw=10)
    draw_pine_tree(tx=37, ty=74, th=22, tw=9)
    draw_pine_tree(tx=42, ty=80, th=26, tw=11)
    draw_pine_tree(tx=88, ty=76, th=24, tw=10)
    draw_pine_tree(tx=118, ty=76, th=28, tw=12)
    draw_pine_tree(tx=125, ty=84, th=25, tw=11)

    draw_pine_tree(tx=6, ty=126, th=88, tw=22)
    draw_pine_tree(tx=17, ty=118, th=44, tw=15)
    draw_pine_tree(tx=124, ty=126, th=52, tw=17)

    # -------------------------------------------------------------
    # 8. RUSTIC WOODEN FENCES
    # -------------------------------------------------------------
    fence1_posts = [(43, 108), (46, 114), (49, 120), (52, 126)]
    for i in range(len(fence1_posts)):
        px, py = fence1_posts[i]
        for y in range(py - 7, py + 1):
            pset(c, px, y, PAL["wood_gold"] if y == py - 7 else PAL["wood_lit"])
            pset(c, px + 1, y, PAL["wood_shadow"])
        if i < len(fence1_posts) - 1:
            nx, ny = fence1_posts[i + 1]
            for step in range(1, 10):
                t = step / 10.0
                rx = int(round(px + t * (nx - px)))
                ry = int(round(py + t * (ny - py)))
                pset(c, rx, ry - 5, PAL["wood_gold"] if step % 2 == 0 else PAL["wood_lit"])
                pset(c, rx, ry - 2, PAL["wood_mid"])

    fence2_posts = [(82, 97), (86, 98), (90, 99)]
    for i in range(len(fence2_posts)):
        px, py = fence2_posts[i]
        for y in range(py - 5, py + 1):
            pset(c, px, y, PAL["wood_lit"])
        if i < len(fence2_posts) - 1:
            nx, ny = fence2_posts[i + 1]
            for step in range(1, 6):
                t = step / 6.0
                rx = int(round(px + t * (nx - px)))
                ry = int(round(py + t * (ny - py)))
                pset(c, rx, ry - 3, PAL["wood_gold"])

    # -------------------------------------------------------------
    # 9. CHIMNEY SMOKE (AIRY, COZY PIXEL-ART PUFFS)
    # -------------------------------------------------------------
    def draw_soft_smoke_puff(cx, cy, rx, ry, dither_outer=True):
        irx = int(math.ceil(rx))
        iry = int(math.ceil(ry))
        for dy in range(-iry, iry + 1):
            for dx in range(-irx, irx + 1):
                nd = (dx * dx) / (rx * rx) + (dy * dy) / (ry * ry)
                if nd <= 1.0:
                    px = int(round(cx + dx))
                    py = int(round(cy + dy))
                    if 0 <= px < 128 and 0 <= py < 128:
                        if dither_outer and nd > 0.72 and (px + py) % 2 != 0:
                            continue
                        
                        if dx >= 0 and dy <= 0:
                            if nd < 0.4:
                                pset(c, px, py, PAL["smoke_white"])
                            else:
                                pset(c, px, py, PAL["smoke_lit"])
                        elif dx <= 0 and dy >= 0:
                            if nd > 0.6:
                                pset(c, px, py, PAL["smoke_shadow"])
                            else:
                                pset(c, px, py, PAL["smoke_mid"])
                        else:
                            if dy < 0 or dx > 0:
                                pset(c, px, py, PAL["smoke_lit"])
                            else:
                                pset(c, px, py, PAL["smoke_mid"])

    # HERO SMOKE from House 2:
    pset(c, 55, 51, PAL["smoke_mid"])
    pset(c, 55, 50, PAL["smoke_lit"])
    pset(c, 54, 49, PAL["smoke_lit"])
    pset(c, 55, 49, PAL["smoke_white"])
    pset(c, 54, 48, PAL["smoke_white"])

    hero_puffs = [
        (54, 46, 2.2, 1.8),
        (52, 42, 2.8, 2.2),
        (49, 37, 3.6, 2.8),
        (45, 31, 4.4, 3.4),
        (39, 24, 5.4, 4.0),
        (32, 17, 6.4, 4.6),
        (24, 11, 7.2, 5.0),
    ]
    for cx, cy, rx, ry in hero_puffs:
        draw_soft_smoke_puff(cx, cy, rx, ry)

    # Smoke from House 1 (Chimney at x=19, y=56)
    pset(c, 19, 56, PAL["smoke_mid"])
    pset(c, 19, 55, PAL["smoke_lit"])
    house1_puffs = [
        (20, 52, 1.8, 1.5),
        (22, 47, 2.4, 1.9),
        (25, 42, 3.0, 2.3),
        (29, 36, 3.6, 2.8),
    ]
    for cx, cy, rx, ry in house1_puffs:
        draw_soft_smoke_puff(cx, cy, rx, ry)

    # Smoke from House 3 (Chimney at x=110, y=63)
    pset(c, 110, 63, PAL["smoke_mid"])
    pset(c, 110, 62, PAL["smoke_lit"])
    house3_puffs = [
        (111, 59, 1.8, 1.5),
        (113, 54, 2.3, 1.9),
        (116, 49, 2.9, 2.3),
        (120, 44, 3.5, 2.7),
    ]
    for cx, cy, rx, ry in house3_puffs:
        draw_soft_smoke_puff(cx, cy, rx, ry)

    # -------------------------------------------------------------
    # 10. WILDFLOWERS & FOREGROUND DETAILS
    # -------------------------------------------------------------
    flowers = [
        (26, 96, PAL["flower_yellow"]),
        (30, 100, PAL["flower_white"]),
        (35, 103, PAL["flower_yellow"]),
        (40, 110, PAL["flower_blue"]),
        (44, 118, PAL["flower_yellow"]),
        (47, 124, PAL["flower_white"]),
        (72, 106, PAL["flower_white"]),
        (76, 111, PAL["flower_yellow"]),
        (80, 116, PAL["flower_blue"]),
        (85, 120, PAL["flower_yellow"]),
        (92, 104, PAL["flower_white"]),
        (98, 108, PAL["flower_yellow"]),
        (106, 112, PAL["flower_blue"]),
        (114, 116, PAL["flower_yellow"]),
    ]
    for fx, fy, fcol in flowers:
        pset(c, fx, fy, fcol)
        pset(c, fx, fy + 1, PAL["grass_dark"])

    print("Canvas stats:", c.stats())

    view(c)
    finish(c)
    return c

if __name__ == "__main__":
    draw_art()
