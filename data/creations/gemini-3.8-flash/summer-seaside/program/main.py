import numpy as np
from pixelbench_api import new_canvas, view, finish

def draw_beach_scene():
    c = new_canvas(128, 128, name="summer_seaside")

    # =========================================================================
    # PALETTE DEFINITIONS (Strictly organized, ~55 cohesive colors total)
    # =========================================================================
    # Sky tones
    SKY = [
        "#2367cf", # 0: deep zenith blue
        "#397fe3", # 1: bright summer sky
        "#5698f0", # 2: mid sky
        "#78b4f8", # 3: soft cyan-blue
        "#9ecdfa", # 4: pale sky
        "#c6e4fd", # 5: horizon warm haze
    ]

    # Sun & Warm light
    SUN_CORE = "#ffffff"
    SUN_HI   = "#fffde6"
    SUN_MID  = "#fff199"
    SUN_WARM = "#fed968"
    SUN_GLOW = "#fde68a"

    # Clouds
    CL_WHITE = "#ffffff"
    CL_HI    = "#f3f8fe"
    CL_MID   = "#d8e7fa"
    CL_SHAD  = "#afcaf0"
    CL_DEEP  = "#8eaedb"

    # Birds
    GULL_WHITE= "#ffffff"
    GULL_DARK = "#1e293b"
    GULL_WING = "#475569"
    GULL_BEAK = "#f59e0b"

    # Sea tones (layered from deep blue to teal to aqua)
    SEA = [
        "#113a70", # 0: deep horizon navy
        "#144d8f", # 1: horizon cobalt
        "#1865a8", # 2: deep ocean blue
        "#1b7ebc", # 3: rich ocean blue
        "#1d97cc", # 4: cerulean
        "#22b2d6", # 5: tropical blue
        "#2ec9d2", # 6: turquoise
        "#3fe0d4", # 7: bright teal
        "#67edd8", # 8: shallow crystal aqua
        "#97f6e6", # 9: light surf aqua
    ]
    FOAM_WHITE = "#ffffff"
    FOAM_SOFT  = "#d6fbf5"
    FOAM_SHAD  = "#9eece1"

    # Sand tones
    WET_SAND_DARK = "#926839"
    WET_SAND_MID  = "#ad8048"
    WET_SAND_LGT  = "#c6975a"
    SAND_SUNNY    = "#fce18d"
    SAND_BASE     = "#f5cb68"
    SAND_WARM     = "#e9b54c"
    SAND_SHAD     = "#d29734"
    SAND_DEEP     = "#b57722"

    # Umbrella
    UMB_RED_HI   = "#ff7070"
    UMB_RED_MID  = "#ef3838"
    UMB_RED_DARK = "#c01a1a"
    UMB_RED_DEEP = "#7f1313"
    UMB_WHT_HI   = "#ffffff"
    UMB_WHT_MID  = "#f1f5f9"
    UMB_WHT_SHAD = "#cbd5e1"
    UMB_WHT_DEEP = "#94a3b8"
    POLE_HI      = "#fef08a"
    POLE_MID     = "#ca8a04"
    POLE_DARK    = "#78350f"

    # Towel
    TOWEL_BLU_HI = "#60a5fa"
    TOWEL_BLU    = "#2563eb"
    TOWEL_BLU_SH = "#1d4ed8"
    TOWEL_YEL_HI = "#fef08a"
    TOWEL_YEL    = "#facc15"
    TOWEL_YEL_SH = "#ca8a04"
    TOWEL_WHT    = "#ffffff"
    TOWEL_WHT_SH = "#cbd5e1"

    # Flip-flops
    FLIP_SOLE    = "#ec4899"
    FLIP_SOLE_DK = "#be185d"
    FLIP_SOLE_HI = "#fbcfe8"
    FLIP_STRAP   = "#38bdf8"
    FLIP_STRAP_DK= "#0284c7"

    # Beach ball & details
    BALL_RED     = "#ef4444"
    BALL_BLU     = "#0284c7"
    BALL_YEL     = "#facc15"
    BALL_WHT     = "#ffffff"
    GLASS_WHT    = "#ffffff"
    DRINK_ORANGE = "#f97316"
    DRINK_LEMON  = "#facc15"
    STRAW_RED    = "#ef4444"
    STARFISH     = "#f43f5e"
    STARFISH_HI  = "#fda4af"

    # =========================================================================
    # 1. SKY GRADIENT
    # =========================================================================
    sky_rows = [
        (0, 7, SKY[0]),
        (8, 15, SKY[1]),
        (16, 23, SKY[2]),
        (24, 31, SKY[3]),
        (32, 39, SKY[4]),
        (40, 47, SKY[5]),
    ]
    for y0, y1, col in sky_rows:
        c.rect(0, y0, 128, y1 - y0 + 1, col)

    # Dither transitions
    for band_idx in range(len(sky_rows) - 1):
        y_trans = sky_rows[band_idx][1]
        col_top = sky_rows[band_idx][2]
        col_bot = sky_rows[band_idx + 1][2]
        for x in range(128):
            if (x + y_trans) % 3 == 0:
                c.set(x, y_trans + 1, col_top)
            elif (x + y_trans) % 3 == 1:
                c.set(x, y_trans, col_bot)

    # =========================================================================
    # 2. BRIGHT SUN
    # =========================================================================
    sx, sy = 105, 12
    # Corona glow
    for angle in np.linspace(0, 2*np.pi, 36, endpoint=False):
        for r in range(9, 14):
            if (int(r * 2.5 + angle * 4)) % 3 == 0:
                px = int(round(sx + r * np.cos(angle)))
                py = int(round(sy + r * np.sin(angle)))
                if 0 <= px < 128 and 0 <= py < 128:
                    c.set(px, py, SUN_GLOW if r < 12 else SUN_WARM)

    c.circle(sx, sy, 8, SUN_WARM)
    c.circle(sx, sy, 6, SUN_MID)
    c.circle(sx, sy, 4, SUN_HI)
    c.circle(sx, sy, 2, SUN_CORE)

    # Solar flares
    flares = [
        (-10, 0), (-9, 0), (-8, 0), (8, 0), (9, 0), (10, 0),
        (0, -9), (0, -8), (0, 8), (0, 9),
        (-6, -6), (6, -6), (-6, 6), (6, 6)
    ]
    for dx, dy in flares:
        c.set(sx + dx, sy + dy, SUN_HI)

    # =========================================================================
    # 3. SOFT WHITE CLOUDS
    # =========================================================================
    # Cloud 1: Main fluffy cumulus on left
    cloud_puffs = [
        (16, 21, 7),
        (26, 17, 10),
        (38, 15, 11),
        (51, 19, 9),
        (61, 23, 6),
        (32, 23, 9),
        (44, 24, 8),
        (22, 25, 7),
    ]
    for cx, cy, r in cloud_puffs:
        c.circle(cx, cy + 3, r, CL_DEEP)
    for cx, cy, r in cloud_puffs:
        c.circle(cx, cy + 2, r, CL_SHAD)
    for cx, cy, r in cloud_puffs:
        c.circle(cx, cy + 1, r, CL_MID)
    for cx, cy, r in cloud_puffs:
        c.circle(cx, cy, r, CL_HI)
    for cx, cy, r in cloud_puffs:
        c.circle(cx + 1, cy - 2, max(2, r - 3), CL_WHITE)

    # Cloud 2: Gentle puffy cloud under sun
    c2_puffs = [
        (78, 34, 6),
        (88, 31, 8),
        (99, 32, 7),
        (108, 35, 5),
        (86, 36, 6),
        (96, 36, 6),
    ]
    for cx, cy, r in c2_puffs:
        c.circle(cx, cy + 2, r, CL_SHAD)
    for cx, cy, r in c2_puffs:
        c.circle(cx, cy + 1, r, CL_MID)
    for cx, cy, r in c2_puffs:
        c.circle(cx, cy, r, CL_HI)
    for cx, cy, r in c2_puffs:
        c.circle(cx + 1, cy - 1, max(2, r - 3), CL_WHITE)

    # Cloud 3: Distant low wisp
    c.ellipse(12, 42, 9, 3, CL_MID)
    c.ellipse(13, 41, 7, 2, CL_WHITE)

    # =========================================================================
    # 4. TWO SEAGULLS FLYING IN CLEAR SKY
    # =========================================================================
    # Gull 1 (Close, soaring gracefully) at (73, 15) in open blue sky
    g1 = [
        (-4, 0, GULL_WING), (-3, -1, GULL_WING), (-2, -1, GULL_WING), (-1, 0, GULL_DARK),
        (0, 1, GULL_WHITE), (1, 1, GULL_WHITE), (2, 0, GULL_DARK),
        (3, -1, GULL_WING), (4, -1, GULL_WING), (5, 0, GULL_WING),
        (-3, 0, GULL_WHITE), (-2, 0, GULL_WHITE),
        (3, 0, GULL_WHITE), (4, 0, GULL_WHITE),
        (1, 2, GULL_BEAK)
    ]
    for dx, dy, col in g1:
        c.set(73 + dx, 15 + dy, col)

    # Gull 2 (Distant, gliding slightly lower) at (84, 21) in open blue sky
    g2 = [
        (-3, 0, GULL_WING), (-2, -1, GULL_WING), (-1, 0, GULL_WHITE),
        (0, 1, GULL_WHITE), (1, 0, GULL_WHITE), (2, -1, GULL_WING), (3, 0, GULL_WING),
        (-2, 0, GULL_WHITE), (2, 0, GULL_WHITE)
    ]
    for dx, dy, col in g2:
        c.set(84 + dx, 21 + dy, col)

    # =========================================================================
    # 5. DISTANT SAILBOAT ON HORIZON
    # =========================================================================
    # Horizon is at y = 48
    # Hull
    c.poly([(24, 47), (26, 49), (33, 49), (35, 47)], "#1e3a5f")
    c.line(25, 47, 34, 47, "#ffffff")
    # Mast
    c.line(29, 39, 29, 47, "#475569")
    # Mainsail
    c.poly([(29, 40), (23, 46), (29, 46)], "#ffffff")
    c.line(24, 46, 29, 46, "#cbd5e1")
    # Jib sail
    c.poly([(30, 41), (34, 46), (30, 46)], "#e2e8f0")
    # Red pennant
    c.set(30, 39, "#ef4444")
    c.set(31, 39, "#ef4444")
    # Reflection
    c.set(29, 50, "#ffffff")
    c.line(26, 50, 32, 50, "#38bdf8")

    # =========================================================================
    # 6. SEA (LAYERED FROM DEEP BLUE TO TEAL TO AQUA)
    # =========================================================================
    def shore_y(x):
        return int(73.5 + 8.5 * (x / 127.0) + 1.2 * np.sin(x * 0.07 + 0.5))

    sea_layers = [
        (48, 51, SEA[0]), # Deep horizon navy
        (52, 55, SEA[1]), # Horizon cobalt
        (56, 59, SEA[2]), # Deep ocean
        (60, 63, SEA[3]), # Rich blue
        (64, 67, SEA[4]), # Cerulean
        (68, 71, SEA[5]), # Tropical blue
        (72, 75, SEA[6]), # Turquoise
        (76, 79, SEA[7]), # Bright teal
        (80, 84, SEA[8]), # Shallow aqua
    ]
    for y0, y1, col in sea_layers:
        for y in range(y0, y1 + 1):
            for x in range(128):
                if y <= shore_y(x):
                    c.set(x, y, col)

    # Rhythmic wave crests
    for y, spacing, col in [(50, 9, SEA[1]), (53, 11, SEA[2]), (57, 10, SEA[3]), (61, 12, SEA[4])]:
        for x in range(2, 126, spacing):
            w = 3 + (x % 3)
            c.line(x, y, min(127, x + w), y, col)

    for y, spacing, col in [(64, 14, SEA[5]), (67, 13, SEA[6]), (70, 15, SEA[7])]:
        for x in range(4, 124, spacing):
            w = 5 + (x % 4)
            c.line(x, y, min(127, x + w), y, col)
            c.set(x + w//2, y - 1, SEA[6])

    # =========================================================================
    # 7. BREAKING SURF WAVE & WHITE SEA FOAM ONTO GOLDEN SAND
    # =========================================================================
    for x in range(128):
        sy = shore_y(x)
        c.set(x, sy - 2, SEA[8])
        c.set(x, sy - 1, SEA[9])

    for x in range(128):
        sy = shore_y(x)
        c.set(x, sy - 1, FOAM_SHAD)
        c.set(x, sy, FOAM_WHITE)

        tongue = int(2.0 + 1.6 * np.sin(x * 0.22) + 0.9 * np.cos(x * 0.08))
        for dy in range(1, tongue + 1):
            if dy == tongue:
                c.set(x, sy + dy, FOAM_WHITE if (x % 2 == 0) else FOAM_SOFT)
            else:
                c.set(x, sy + dy, FOAM_WHITE)
        if (x * 13) % 17 < 5:
            c.set(x, sy + tongue + 2, FOAM_WHITE)
        if (x * 7) % 19 < 4:
            c.set(x, sy + tongue + 1, FOAM_SOFT)

    # Foam lacing in shallows
    for x in range(1, 127, 4):
        sy = shore_y(x)
        if (x % 3 != 0):
            c.set(x, sy - 3, FOAM_SOFT)
            c.set(x + 1, sy - 3, FOAM_WHITE)
        if (x % 5 == 0):
            c.set(x, sy - 5, FOAM_SOFT)

    # Glossy wet sand
    for x in range(128):
        sy = shore_y(x)
        tongue = int(2.0 + 1.6 * np.sin(x * 0.22) + 0.9 * np.cos(x * 0.08))
        wet_start = sy + tongue + 1
        c.set(x, wet_start, WET_SAND_DARK)
        c.set(x, wet_start + 1, WET_SAND_MID)
        c.set(x, wet_start + 2, WET_SAND_LGT)
        if (x + 3) % 11 < 3 and x < 95:
            c.set(x, wet_start + 1, "#e0f2fe")

    # =========================================================================
    # 8. GOLDEN SAND BEACH
    # =========================================================================
    for y in range(74, 128):
        for x in range(128):
            sy = shore_y(x)
            tongue = int(2.0 + 1.6 * np.sin(x * 0.22) + 0.9 * np.cos(x * 0.08))
            wet_end = sy + tongue + 3
            if y > wet_end:
                v = (y - 74) / 54.0
                if v < 0.25:
                    col = SAND_SUNNY
                elif v < 0.55:
                    col = SAND_BASE if (x + y) % 3 != 0 else SAND_SUNNY
                elif v < 0.8:
                    col = SAND_BASE if (x + y) % 3 != 0 else SAND_WARM
                else:
                    col = SAND_WARM if (x + y) % 4 != 0 else SAND_SHAD
                c.set(x, y, col)

    # Sand sparkles
    sand_sparkles = [
        (10, 88), (22, 94), (35, 91), (15, 114), (48, 93),
        (8, 105), (116, 94), (122, 112), (18, 124), (54, 124)
    ]
    for px, py in sand_sparkles:
        c.set(px, py, "#fff7cc")
        c.set(px + 1, py + 1, SAND_SHAD)

    # Starfish on sand
    c.set(16, 86, STARFISH_HI)
    c.set(16, 85, STARFISH)
    c.set(16, 87, STARFISH)
    c.set(15, 86, STARFISH)
    c.set(17, 86, STARFISH)
    c.set(14, 88, STARFISH)
    c.set(18, 88, STARFISH)
    c.set(16, 88, SAND_DEEP)

    # Seashells
    c.set(33, 85, "#ffffff")
    c.set(34, 85, "#fed7aa")
    c.set(33, 86, SAND_DEEP)

    c.set(24, 102, "#ffffff")
    c.set(25, 102, "#ffedd5")
    c.set(24, 103, SAND_DEEP)

    # Beach ball on sand near x=18, y=96
    bx, by, br = 18, 96, 5
    c.ellipse(bx - 1, by + 5, 5, 2, SAND_DEEP)
    for y in range(by - br, by + br + 1):
        for x in range(bx - br, bx + br + 1):
            dx = (x - bx) / float(br)
            dy = (y - by) / float(br)
            if dx*dx + dy*dy <= 1.0:
                if dx < -0.4:
                    col = BALL_BLU
                elif dx < 0.0:
                    col = BALL_WHT
                elif dx < 0.4:
                    col = BALL_RED
                else:
                    col = BALL_YEL
                if (x - (bx + 2))**2 + (y - (by - 2))**2 <= 4:
                    col = BALL_WHT
                c.set(x, y, col)
    c.set(bx, by - 5, BALL_WHT)

    # =========================================================================
    # 9. UMBRELLA SHADOW ON SAND
    # =========================================================================
    # Canopy shadow centered around (x=76, y=110), rx=18, ry=7
    for y in range(103, 118):
        for x in range(58, 95):
            dx = (x - 76) / 18.0
            dy = (y - 110) / 7.0
            if dx*dx + dy*dy <= 1.0:
                c.set(x, y, SAND_SHAD if dx*dx + dy*dy > 0.6 else SAND_DEEP)

    # Pole shadow
    c.line(92, 112, 78, 110, SAND_DEEP)
    c.line(91, 112, 78, 111, SAND_DEEP)

    # =========================================================================
    # 10. STRIPED BEACH TOWEL (5 CLEAN LENGTHWISE STRIPES)
    # =========================================================================
    towel_stripes = [
        (TOWEL_BLU, TOWEL_BLU_SH),
        (TOWEL_WHT, TOWEL_WHT_SH),
        (TOWEL_YEL, TOWEL_YEL_SH),
        (TOWEL_WHT, TOWEL_WHT_SH),
        (TOWEL_BLU, TOWEL_BLU_SH),
    ]

    for py in range(98, 123):
        t_left = (py - 98) / 19.0
        x_left = 44 + t_left * (36 - 44)
        x_right = 70 + t_left * (62 - 70)
        
        for px in range(int(round(x_left)), int(round(x_right)) + 1):
            if py < 98 + (px - 44) * (5.0 / 26.0) - 0.5:
                continue
            if py > 117 + (px - 36) * (5.0 / 26.0) + 0.5:
                continue
            
            w_span = max(1.0, x_right - x_left)
            u_towel = (px - x_left) / w_span
            
            stripe_idx = int(np.floor(u_towel * 5.0))
            stripe_idx = max(0, min(4, stripe_idx))
            
            dx_s = (px - 76) / 18.0
            dy_s = (py - 110) / 7.0
            in_shadow = (dx_s*dx_s + dy_s*dy_s) <= 1.0

            s_colors = towel_stripes[stripe_idx]
            col = s_colors[1] if in_shadow else s_colors[0]
            c.set(px, py, col)

    # Rolled head pillow at the top of the towel
    for px in range(45, 69):
        py = int(round(98 + (px - 44) * (5.0 / 26.0)))
        c.set(px, py, TOWEL_WHT)
        c.set(px, py + 1, TOWEL_WHT_SH)

    # White fringe on top and bottom ends of towel
    for px in range(44, 71, 2):
        py = int(round(98 + (px - 44) * (5.0 / 26.0)))
        c.set(px, py - 1, "#ffffff")
    for px in range(36, 63, 2):
        py = int(round(117 + (px - 36) * (5.0 / 26.0)))
        c.set(px, py + 1, "#ffffff")

    # Towel left edge shadow
    for py in range(99, 122):
        t_left = (py - 98) / 19.0
        xl = int(round(44 + t_left * (36 - 44)))
        c.set(xl - 1, py, SAND_DEEP)

    # =========================================================================
    # 11. FLIP-FLOPS (Resting on golden sand beside towel)
    # =========================================================================
    flip1 = [
        (29, 108), (30, 107), (31, 107),
        (29, 109), (30, 109), (31, 109),
        (28, 110), (29, 110), (30, 110), (31, 110),
        (28, 111), (29, 111), (30, 111), (31, 111),
        (29, 112), (30, 112), (31, 112),
        (29, 113), (30, 113), (31, 113),
        (29, 114), (30, 114),
    ]
    for x, y in flip1:
        c.set(x + 1, y + 1, SAND_DEEP)
    for x, y in flip1:
        c.set(x, y, FLIP_SOLE)
    c.set(30, 107, FLIP_SOLE_HI)
    c.set(31, 107, FLIP_SOLE_HI)
    c.set(28, 112, FLIP_SOLE_DK)
    c.set(29, 115, FLIP_SOLE_DK)
    c.set(30, 108, "#ffffff")
    c.set(29, 109, FLIP_STRAP)
    c.set(31, 109, FLIP_STRAP)
    c.set(28, 110, FLIP_STRAP_DK)
    c.set(31, 110, FLIP_STRAP_DK)

    flip2 = [
        (34, 109), (35, 108), (36, 108),
        (34, 110), (35, 110), (36, 110),
        (33, 111), (34, 111), (35, 111), (36, 111),
        (33, 112), (34, 112), (35, 112), (36, 112),
        (34, 113), (35, 113), (36, 113),
        (34, 114), (35, 114), (36, 114),
        (34, 115), (35, 115),
    ]
    for x, y in flip2:
        c.set(x + 1, y + 1, SAND_DEEP)
    for x, y in flip2:
        c.set(x, y, FLIP_SOLE)
    c.set(35, 108, FLIP_SOLE_HI)
    c.set(36, 108, FLIP_SOLE_HI)
    c.set(33, 113, FLIP_SOLE_DK)
    c.set(34, 116, FLIP_SOLE_DK)
    c.set(35, 109, "#ffffff")
    c.set(34, 110, FLIP_STRAP)
    c.set(36, 110, FLIP_STRAP)
    c.set(33, 111, FLIP_STRAP_DK)
    c.set(36, 111, FLIP_STRAP_DK)

    # Tropical drink on towel corner (x=65, y=96)
    c.rect(65, 96, 4, 6, GLASS_WHT)
    c.rect(66, 97, 2, 4, DRINK_ORANGE)
    c.set(66, 98, "#fed7aa")
    c.set(64, 95, DRINK_LEMON)
    c.line(67, 94, 69, 91, STRAW_RED)
    c.set(66, 102, SAND_DEEP)

    # =========================================================================
    # 12. RED-AND-WHITE STRIPED BEACH UMBRELLA
    # =========================================================================
    # Wooden pole running from (94, 76) to (91, 112)
    c.line(94, 76, 91, 112, POLE_MID)
    c.line(95, 76, 92, 112, POLE_DARK)
    c.line(93, 76, 90, 112, POLE_HI)
    # Pole base in sand
    c.set(89, 112, SAND_SUNNY)
    c.set(90, 112, SAND_SUNNY)
    c.set(91, 113, SAND_SHAD)
    c.set(92, 113, SAND_DEEP)

    # Canopy Geometry:
    cx, cy_rim = 94, 76
    rx, ry = 22, 18

    # Function to get the scalloped bottom y for any given x
    def umbrella_bottom_y(px):
        dx = (px - cx) / float(rx)
        base = cy_rim + 1.8 * (1.0 - dx*dx)
        # 6 panels across u in [-1, 1]
        u = dx
        # panel width = 2.0 / 6 = 0.3333
        panel_idx = int(np.floor((u + 1.0) / 0.33333))
        panel_idx = max(0, min(5, panel_idx))
        u_mid = -1.0 + (panel_idx + 0.5) * 0.33333
        dist = abs(u - u_mid)
        scallop_w = 0.33333 / 2.0
        if dist < scallop_w:
            scallop = 2.0 * np.cos(dist * np.pi / (2.0 * scallop_w))
        else:
            scallop = 0.0
        return int(round(base + scallop))

    # Fill every column of the umbrella from top to bottom scalloped rim
    for px in range(cx - rx, cx + rx + 1):
        dx = (px - cx) / float(rx)
        y_top = int(round(cy_rim - ry * np.sqrt(max(0.0, 1.0 - dx*dx))))
        y_bot = umbrella_bottom_y(px)
        
        # Determine panel index from px
        u_val = dx
        panel_idx = int(np.floor((u_val + 1.0) / 0.33333))
        panel_idx = max(0, min(5, panel_idx))
        is_red = (panel_idx % 2 == 0)

        for py in range(y_top, y_bot + 1):
            # Lighting model: sun at top right (105, 12)
            light = dx * 0.55 - (py - 58) / 20.0 * 0.35 + 0.35
            if is_red:
                if light > 0.45:
                    col = UMB_RED_HI
                elif light > 0.05:
                    col = UMB_RED_MID
                elif light > -0.25:
                    col = UMB_RED_DARK
                else:
                    col = UMB_RED_DEEP
            else:
                if light > 0.45:
                    col = UMB_WHT_HI
                elif light > 0.05:
                    col = UMB_WHT_MID
                elif light > -0.25:
                    col = UMB_WHT_SHAD
                else:
                    col = UMB_WHT_DEEP
            
            # Bottom 1px rim outline
            if py == y_bot:
                col = UMB_RED_DEEP if is_red else UMB_WHT_DEEP

            c.set(px, py, col)

    # Crisp vertical rib seams radiating from apex down to rim
    for panel in range(1, 6):
        u_seam = -1.0 + panel * 0.33333
        for y in range(59, 78):
            t = (y - 58) / 20.0
            px = int(round(cx + rx * u_seam * (0.22 + 0.78 * np.sqrt(t))))
            if cx - rx <= px <= cx + rx:
                y_bot = umbrella_bottom_y(px)
                if y < y_bot:
                    c.set(px, y, UMB_RED_DEEP if (panel % 2 == 1) else UMB_WHT_DEEP)

    # Wooden ring / bracket under umbrella where pole connects
    c.rect(93, 78, 3, 2, POLE_DARK)
    c.set(94, 78, POLE_MID)

    # Finial / cap on top apex
    c.set(94, 56, POLE_HI)
    c.set(94, 57, POLE_MID)
    c.set(93, 57, POLE_HI)
    c.set(95, 57, POLE_DARK)
    c.set(94, 58, POLE_DARK)

    print(c.stats_text())
    view(c)
    finish(c)
    return c

if __name__ == "__main__":
    draw_beach_scene()
