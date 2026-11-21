import math
from pixelbench_api import *

c = new_canvas(128, 128)

# Palette strictly <= 86 colors (currently 66 colors)
P = {
    # Deep Purple Night Sky (9)
    "sky_0": "#06010d",
    "sky_1": "#0d041a",
    "sky_2": "#170829",
    "sky_3": "#240e3d",
    "sky_4": "#341554",
    "sky_5": "#491d70",
    "sky_6": "#632894",
    "sky_7": "#8037b8",
    "sky_halo": "#4f2675",

    # Moon & Stars (7)
    "moon_white": "#fffde8",
    "moon_cream": "#fdf3c2",
    "moon_pale":  "#ebd89b",
    "moon_gold":  "#cbb177",
    "moon_shade": "#96816a",
    "moon_dark":  "#5f4d5c",
    "star_white": "#f6ecff",

    # Mist & Fog (6)
    "mist_deep":  "#1e1236",
    "mist_dark":  "#2e1c4e",
    "mist_mid":   "#442c6e",
    "mist_light": "#624494",
    "mist_pale":  "#8667bd",
    "mist_glow":  "#ad91e0",

    # Ancient Tree Bark & Timber (7)
    "bark_black": "#0c0610",
    "bark_deep":  "#1b0e20",
    "bark_dark":  "#2d192f",
    "bark_mid":   "#452844",
    "bark_light": "#613b5d",
    "bark_pale":  "#82547b",
    "bark_rim":   "#56456e",

    # Leaves (Dark Red, Brown, Purple) (10)
    "leaf_black":   "#140316",
    "leaf_deep":    "#240625",
    "leaf_purple":  "#3c0b36",
    "leaf_wine":    "#5c123d",
    "leaf_crimson": "#7d1945",
    "leaf_red":     "#a2264e",
    "leaf_rose":    "#c83d63",
    "leaf_brown":   "#4d2217",
    "leaf_amber":   "#78361e",
    "leaf_gold":    "#a85427",

    # Cottage Stone, Slates & Well Masonry (7)
    "stone_black": "#0e0b16",
    "stone_deep":  "#1a1626",
    "stone_dark":  "#28233a",
    "stone_mid":   "#3c3652",
    "stone_light": "#544d6e",
    "stone_pale":  "#756d91",
    "stone_rim":   "#9d95ba",

    # Moss & Forest Greens (7)
    "moss_shadow": "#07100b",
    "moss_deep":   "#0f2015",
    "moss_dark":   "#1a3522",
    "moss_mid":    "#284f32",
    "moss_light":  "#3e7345",
    "moss_bright": "#609f50",
    "moss_lime":   "#8ec960",

    # Warm Light & Fire Glow (8)
    "fire_white":  "#fffde6",
    "fire_cream":  "#fff294",
    "fire_yellow": "#ffc433",
    "fire_amber":  "#f58416",
    "fire_orange": "#d6500d",
    "fire_red":    "#9c2509",
    "fire_dark":   "#571517",
    "warm_mist":   "#662f3f",

    # Magical Accents (5)
    "magic_cyan_light": "#c2fff7",
    "magic_cyan_mid":   "#46e3cb",
    "magic_cyan_dark":  "#11827d",
    "magic_pink":       "#f05ba6",
    "sparkle":          "#ffffff",
}

for name, hexcode in P.items():
    c.color(hexcode, name)

def pset(x, y, col):
    if 0 <= x < 128 and 0 <= y < 128:
        c.set(x, y, P[col])

def pget(x, y):
    if 0 <= x < 128 and 0 <= y < 128:
        return c.get(x, y)
    return None

# =========================================================================
# 1. SKY, STARS, MOON & HORIZON
# =========================================================================
def draw_sky():
    # Vertical gradient
    gradient = [
        (0,  14, "sky_0", "sky_1"),
        (14, 28, "sky_1", "sky_2"),
        (28, 42, "sky_2", "sky_3"),
        (42, 56, "sky_3", "sky_4"),
        (56, 70, "sky_4", "sky_5"),
    ]
    for y in range(70):
        for y0, y1, c0, c1 in gradient:
            if y0 <= y < y1:
                t = (y - y0) / (y1 - y0)
                for x in range(128):
                    dither = 0.25 if (x % 2 == 0 and y % 2 == 0) else \
                             0.75 if (x % 2 == 1 and y % 2 == 1) else \
                             0.50 if (x % 2 == 1 and y % 2 == 0) else 0.0
                    col = c1 if t > dither else c0
                    pset(x, y, col)
                break

    # Stars
    stars = [
        (8, 7), (44, 6), (72, 9), (88, 5), (114, 11),
        (6, 20), (52, 16), (78, 20), (98, 14), (122, 22),
        (16, 32), (48, 34), (84, 28), (106, 32), (124, 38),
        (10, 44), (22, 52), (40, 48), (116, 46), (66, 12)
    ]
    for sx, sy in stars:
        pset(sx, sy, "star_white")
    
    # 4-point cross stars
    for cx, cy in [(82, 8), (106, 6), (14, 12)]:
        pset(cx, cy, "sparkle")
        pset(cx-1, cy, "star_white")
        pset(cx+1, cy, "star_white")
        pset(cx, cy-1, "star_white")
        pset(cx, cy+1, "star_white")

    # Moon at (28, 20), radius 10.5
    mx, my, mr = 28, 20, 10.5
    
    # Soft concentric halo
    for dy in range(-16, 17):
        for dx in range(-16, 17):
            d = math.hypot(dx, dy)
            if mr < d <= mr + 5.5:
                x, y = int(mx + dx), int(my + dy)
                if d <= mr + 2.5:
                    if (x + y) % 2 == 0:
                        pset(x, y, "sky_halo")
                elif d <= mr + 4.5:
                    if (x * 2 + y) % 3 == 0:
                        pset(x, y, "sky_4")

    # Artisanal Lunar Disc (Authentic lunar seas and highlands)
    for dy in range(-11, 12):
        for dx in range(-11, 12):
            d = math.hypot(dx, dy)
            if d <= mr:
                x, y = int(mx + dx), int(my + dy)
                
                # Mare Imbrium (upper left oval)
                in_imbrium = math.hypot(dx + 3.0, dy + 3.0) < 3.2
                # Oceanus Procellarum (west limb patch)
                in_procellarum = (dx < -1.5 and abs(dy) < 3.5)
                # Mare Serenitatis & Tranquillitatis (central-east patch)
                in_tranquil = math.hypot(dx - 2.5, dy + 0.5) < 2.8
                # Mare Crisium (small discrete oval on east limb)
                in_crisium = math.hypot(dx - 5.5, dy + 1.5) < 1.6
                
                is_maria = in_imbrium or in_procellarum or in_tranquil or in_crisium
                
                if d > mr - 1.2:
                    col = "moon_gold" if (dx > 0 or dy > 0) else "moon_pale"
                elif is_maria:
                    is_deep = math.hypot(dx + 3.0, dy + 3.0) < 1.8 or math.hypot(dx - 2.5, dy + 0.5) < 1.5
                    col = "moon_dark" if is_deep else "moon_shade"
                elif d > mr - 2.8:
                    col = "moon_pale"
                elif math.hypot(dx - 1.0, dy - 4.5) < 1.8: # Tycho crater ray
                    col = "moon_white"
                else:
                    col = "moon_cream"
                pset(x, y, col)

    # Soft clouds drifting across sky
    cloud_strips = [
        (26, 36, 78, "sky_4"),
        (27, 32, 84, "sky_4"),
        (28, 42, 76, "sky_3"),
        (38, 14, 44, "sky_4"),
        (42, 64, 108, "sky_4"),
        (43, 70, 102, "sky_3"),
    ]
    for cy, x0, x1, ccol in cloud_strips:
        for cx in range(x0, x1):
            if (cx + cy) % 2 == 0:
                pset(cx, cy, ccol)

    # Distant forest silhouette
    for x in range(128):
        ry = int(58 + 4 * math.sin(x * 0.06) + 2 * math.cos(x * 0.14))
        for y in range(ry, 70):
            pset(x, y, "sky_2" if (x + y) % 2 == 0 else "sky_1")

# =========================================================================
# 2. FOREST GROUND BASE TERRAIN
# =========================================================================
def draw_ground():
    for y in range(68, 128):
        for x in range(128):
            h = y + math.sin(x * 0.07 + y * 0.05) * 2 + math.cos(x * 0.03) * 2
            if h < 76:
                col = "moss_shadow"
            elif h < 88:
                col = "moss_deep" if (x + y) % 2 == 0 else "moss_shadow"
            elif h < 102:
                col = "moss_dark" if (x + y) % 2 == 0 else "moss_deep"
            elif h < 116:
                col = "moss_mid" if (x * 2 + y) % 3 != 0 else "moss_dark"
            else:
                col = "moss_mid" if (x + y) % 2 == 0 else "moss_light"
            pset(x, y, col)

# =========================================================================
# 3. MIDGROUND FOREST MIST
# =========================================================================
def draw_midground_mist():
    for my, x0, x1, col in [
        (66, 8,  118, "mist_deep"),
        (70, 5,  122, "mist_dark"),
        (74, 12, 114, "mist_mid"),
    ]:
        for x in range(x0, x1):
            wave = math.sin(x * 0.11) * 1.5
            y = int(my + wave)
            if (x + y) % 3 == 0:
                pset(x, y, col)

# =========================================================================
# 4. OLD WOOD-AND-STONE COTTAGE (Whimsical 3/4 Storybook Architecture)
# =========================================================================
def draw_cottage():
    # Architecture:
    # Front Gable on left: x=44..64, y=48..88.
    # Timber frame wattle-and-daub upper story, fieldstone lower foundation.
    # Front door at x=48..56, y=68..88.
    # Massive sloping roof on right: x=64..96, y=26..62.
    # Warm glowing bay window at x=72..86, y=62..77.

    # --- 4.1 CHIMNEY ---
    # Fieldstone chimney on left gable roof: x=48..55, y=16..42
    for cy in range(16, 42):
        for cx in range(48, 56):
            if cy < 18 and (cx == 48 or cx == 55):
                continue
            if cy == 16:
                col = "stone_black"
            elif cy == 17:
                col = "stone_light" if cx % 2 == 0 else "stone_mid"
            elif cx == 48:
                col = "stone_pale" if cy % 3 == 0 else "stone_light"
            elif cx == 55:
                col = "stone_deep"
            elif (cx + cy) % 4 == 0:
                col = "stone_dark"
            elif (cx * 2 + cy) % 3 == 0:
                col = "stone_mid"
            else:
                col = "stone_light"
            if cy >= 34 and (cx + cy) % 3 == 0:
                col = "moss_mid"
            pset(cx, cy, col)

    # Smoke curling gracefully toward the moon
    smoke = [
        (51, 14, 1.2, "mist_pale"),
        (52, 11, 1.8, "mist_light"),
        (50, 8,  2.2, "mist_mid"),
        (46, 5,  2.8, "mist_dark"),
        (40, 4,  3.0, "sky_4"),
        (32, 3,  2.2, "sky_3"),
    ]
    for sx, sy, srad, scol in smoke:
        for dy in range(-int(srad)-1, int(srad)+2):
            for dx in range(-int(srad)-1, int(srad)+2):
                if math.hypot(dx, dy) <= srad:
                    if (dx + dy) % 2 == 0 or srad <= 1.4:
                        pset(int(sx + dx), int(sy + dy), scol)

    # --- 4.2 COTTAGE WALLS ---
    for wy in range(48, 89):
        for wx in range(44, 92):
            if wy >= 75:
                # Lower fieldstone masonry foundation: distinct rounded stones with mortar
                stone_x = (wx - 44) % 6
                stone_y = (wy - 75) % 4
                is_mortar = (stone_x == 0) or (stone_y == 0)
                if is_mortar:
                    col = "stone_black"
                elif stone_y == 1 and stone_x in (1, 2):
                    col = "stone_light" # top stone highlight
                elif stone_y == 3:
                    col = "stone_dark"  # bottom stone shade
                else:
                    col = "stone_mid"
                # Moss on lower stone base
                if wy >= 84 and (wx + wy) % 3 == 0:
                    col = "moss_mid"
            else:
                # Upper story warm plaster
                col = "stone_light" if (wx + wy) % 2 == 0 else "stone_mid"
                # Authentic timber beams on front gable (x <= 64):
                if wx <= 64:
                    is_post = wx in (44, 45, 63, 64)
                    is_beam = wy in (56, 73, 74)
                    diag = (wx - 44 == wy - 56) or (64 - wx == wy - 56)
                    if is_post or is_beam or diag:
                        col = "bark_deep" if (wx + wy) % 3 != 0 else "bark_dark"
                else:
                    # Side wall corner post
                    if wx == 91 or wy in (61, 73, 74):
                        col = "bark_deep"
            pset(wx, wy, col)

    # --- 4.3 MASSIVE STEEP MOSSY ROOF ---
    # Left gable bargeboard (x=41..64):
    for x in range(41, 65):
        t = (64 - x) / 23.0
        eave_y = int(26 + 32 * (t ** 1.08))
        for ry in range(eave_y - 2, eave_y + 4):
            col = "moss_lime" if (x + ry) % 3 == 0 else "moss_bright" if ry <= eave_y else "bark_dark"
            pset(x, ry, col)
        pset(x, eave_y + 4, "bark_black")

    # The vast sloping side roof (x=64..96, y=26..62):
    for rx in range(64, 96):
        t = (rx - 64) / 32.0
        ridge_y = int(26 + 6 * t)
        eave_y = int(58 + 4 * t)
        
        for ry in range(ridge_y, eave_y + 1):
            v = (ry - ridge_y) / float(eave_y - ridge_y)
            
            # Slate and wood base
            if v < 0.2:
                col = "stone_light"
            elif v < 0.5:
                col = "stone_mid"
            elif v < 0.8:
                col = "stone_dark"
            else:
                col = "stone_deep"

            # Rich organic clusters of velvety moss
            moss_n = math.sin(rx * 0.38 + ry * 0.5) + math.cos(rx * 0.2 - ry * 0.4)
            if moss_n > 0.15:
                col = "moss_lime" if (rx + ry) % 3 == 0 else "moss_bright"
            elif moss_n > -0.2:
                col = "moss_light" if (rx + ry) % 2 == 0 else "moss_mid"
            elif moss_n > -0.45:
                col = "moss_dark"

            if ry == ridge_y:
                col = "moss_bright" if rx % 2 == 0 else "stone_pale"

            pset(rx, ry, col)

        # Subtle horizontal shingle courses
        for row in range(ridge_y + 3, eave_y, 4):
            pset(rx, row, "bark_dark" if (rx + row//4) % 4 == 0 else "stone_dark")

        # Overhang eave & shadow
        pset(rx, eave_y, "moss_lime" if rx % 2 == 0 else "moss_bright")
        pset(rx, eave_y + 1, "bark_black")

    # --- 4.4 ATTIC WINDOW ---
    for wy in range(42, 49):
        for wx in range(51, 57):
            if (wx, wy) in [(51, 42), (56, 42)]:
                continue
            if wx in (51, 56) or wy in (42, 48):
                pset(wx, wy, "bark_black")
            elif wx == 53 or wy == 45:
                pset(wx, wy, "bark_deep")
            else:
                pset(wx, wy, "fire_cream" if (wx == 52 and wy == 44) else "fire_yellow")

    # --- 4.5 MAIN WARM PICTURE WINDOW (Warm Hearth Beacon) ---
    for wy in range(61, 78):
        for wx in range(71, 88):
            if wx in (71, 87) or wy in (61, 77):
                pset(wx, wy, "bark_black")
            elif wx == 72 or wy == 62 or wx == 86 or wy == 76:
                pset(wx, wy, "bark_deep")
            else:
                d = math.hypot(wx - 79, wy - 69.5)
                if d < 2.2:
                    col = "fire_white"
                elif d < 4.5:
                    col = "fire_cream"
                elif d < 6.5:
                    col = "fire_yellow"
                elif d < 8.2:
                    col = "fire_amber"
                else:
                    col = "fire_orange"

                if wx == 79 or wy == 69:
                    col = "bark_deep"
                pset(wx, wy, col)

    # Window sill & planter box with trailing vines
    for wx in range(71, 88):
        pset(wx, 78, "bark_mid")
        pset(wx, 79, "bark_dark")
        if wx % 3 == 0:
            pset(wx, 77, "moss_bright")
            pset(wx, 78, "moss_lime")
            pset(wx, 79, "leaf_rose" if wx % 6 == 0 else "moss_light")
        elif wx % 4 == 0:
            pset(wx, 80, "leaf_amber")

    # --- 4.6 FRONT DOOR & PORCH ---
    for dy in range(68, 88):
        for dx in range(48, 57):
            if dy < 72 and (dx == 48 or dx == 56) and dy == 68:
                continue
            if dx in (48, 56) or dy == 68:
                pset(dx, dy, "bark_black")
            elif dx in (51, 53):
                pset(dx, dy, "bark_black")
            else:
                col = "bark_deep" if dy % 4 == 0 else "bark_dark"
                pset(dx, dy, col)
    # Iron door handle
    pset(54, 78, "fire_amber")
    pset(54, 79, "stone_pale")

    # Porch canopy over door
    for px in range(46, 58):
        pset(px, 66, "moss_bright" if px % 2 == 0 else "moss_light")
        pset(px, 67, "bark_black")

    # Hanging Brass Lantern at x=58, y=69..73 (Delicate, NO honeycomb circle!)
    pset(58, 68, "bark_black") # arm
    pset(58, 69, "bark_dark")  # bracket
    pset(58, 70, "fire_white") # filament
    pset(57, 70, "fire_yellow")# glass pane left
    pset(59, 70, "fire_yellow")# glass pane right
    pset(58, 71, "fire_amber") # bottom glass
    pset(58, 72, "bark_black") # base finial
    # Gentle highlight on doorframe post next to lantern
    pset(56, 70, "fire_amber")
    pset(56, 71, "fire_orange")
    pset(56, 72, "fire_dark")

    # --- 4.7 RADIANT WARM LIGHT SPILL ON WALLS & GROUND ---
    for gy in range(62, 98):
        for gx in range(45, 96):
            dw = math.hypot(gx - 79, gy - 70)
            # Ground light pool in front of cottage (x=66..92, y=78..95)
            if 78 <= gy <= 95 and 66 <= gx <= 92:
                curr = pget(gx, gy)
                if curr not in (P["bark_black"], P["fire_white"], P["fire_cream"]):
                    if dw < 5.5:
                        pset(gx, gy, "fire_yellow")
                    elif dw < 8.5 and (gx + gy) % 2 == 0:
                        pset(gx, gy, "fire_amber")
                    elif dw < 11.5 and (gx * 2 + gy) % 3 == 0:
                        pset(gx, gy, "fire_orange")
                    elif dw < 14.0 and (gx + gy * 2) % 4 == 0:
                        pset(gx, gy, "fire_dark")

# =========================================================================
# 5. STONE-SLAB PATH
# =========================================================================
def draw_stone_path():
    slabs = [
        # (cx, cy, rx, ry)
        (52, 89, 4.0, 2.0),
        (48, 93, 4.8, 2.4),
        (43, 98, 5.5, 2.7),
        (38, 104, 6.2, 3.0),
        (32, 111, 7.0, 3.3),
        (26, 118, 7.8, 3.6),
        (20, 125, 8.5, 4.0),
    ]
    for cx, cy, rx, ry in slabs:
        for dy in range(int(-ry), int(ry + 2)):
            for dx in range(int(-rx), int(rx + 1)):
                if (dx/rx)**2 + (dy/ry)**2 <= 1.0:
                    x, y = int(cx + dx), int(cy + dy)
                    is_warm = (cx > 42)
                    
                    if dy == int(ry):
                        col = "stone_black"
                    elif dy < 0 and dx < 0:
                        col = "fire_cream" if (is_warm and cx > 48) else "fire_amber" if is_warm else "stone_pale"
                    elif is_warm and (dx + dy) % 2 == 0:
                        col = "fire_amber" if (dx*2 + dy)%3 == 0 else "fire_orange"
                    elif (dx + dy) % 3 == 0:
                        col = "stone_light"
                    elif (dx * 2 + dy) % 4 == 0:
                        col = "stone_pale"
                    else:
                        col = "stone_mid"
                    pset(x, y, col)
        
        pset(int(cx - rx), int(cy), "moss_bright")
        pset(int(cx + rx), int(cy), "moss_light")

# =========================================================================
# 6. STONE WELL & WOODEN WINCH (Foreground Star Feature)
# =========================================================================
def draw_stone_well():
    # Basin: center (25, 96), rx=10, ry=3.5, height down to y=108.
    
    # Outer cylindrical masonry body
    for by in range(96, 110):
        for bx in range(15, 36):
            dx = bx - 25
            if abs(dx) <= 10:
                seam = (bx % 4 == 0 and by % 3 == 0) or (bx % 4 == 2 and by % 3 == 1)
                
                if seam:
                    col = "stone_black"
                elif dx < -6:
                    col = "stone_pale" if (bx + by) % 2 == 0 else "stone_light"
                elif dx < 1:
                    col = "stone_light" if (bx + by) % 2 == 0 else "stone_mid"
                elif dx > 6:
                    col = "stone_deep" if (bx + by) % 2 == 0 else "stone_dark"
                else:
                    col = "stone_mid" if (bx + by) % 2 == 0 else "stone_dark"

                if by >= 106 or ((bx + by) % 5 == 0 and by > 101):
                    col = "moss_dark" if (bx + by) % 2 == 0 else "moss_mid"

                pset(bx, by, col)

    # Top stone rim ellipse
    for dy in range(-4, 5):
        for dx in range(-11, 12):
            if (dx/10.0)**2 + (dy/3.5)**2 <= 1.0:
                x, y = 25 + dx, 96 + dy
                if (dx/8.0)**2 + (dy/2.2)**2 <= 1.0:
                    # Inside well: magical cyan water reflection!
                    if dy == 1 and abs(dx) < 3:
                        col = "magic_cyan_mid" if dx == 0 else "magic_cyan_dark"
                    elif dy == 2 and dx == 0:
                        col = "magic_cyan_light"
                    else:
                        col = "stone_black"
                else:
                    if dx < -4:
                        col = "stone_rim" if (dx + dy) % 2 == 0 else "stone_pale"
                    elif dx > 5:
                        col = "stone_dark"
                    else:
                        col = "stone_light"
                    if (dx + dy) % 5 == 0:
                        col = "moss_bright"
                pset(x, y, col)

    # Wooden Upright Posts
    for py in range(78, 97):
        pset(16, py, "bark_light" if py % 2 == 0 else "bark_mid")
        pset(17, py, "bark_dark")
        pset(32, py, "bark_mid" if py % 2 == 0 else "bark_dark")
        pset(33, py, "bark_black")

    # Wooden Peaked Canopy over well
    for wx in range(13, 38):
        dist_c = abs(wx - 25)
        ry = int(74 + dist_c * 0.48)
        pset(wx, ry, "moss_lime" if wx % 3 == 0 else "moss_bright")
        pset(wx, ry + 1, "bark_dark")
        pset(wx, ry + 2, "bark_black")

    # Winch Crossbar Axle at y=84
    for ax in range(17, 33):
        pset(ax, 84, "bark_dark")

    # Rope Spool in center: x=22..28, y=83..86
    for sy in range(83, 87):
        for sx in range(22, 29):
            col = "leaf_amber" if (sx + sy) % 2 == 0 else "leaf_brown"
            pset(sx, sy, col)

    # Rope hanging down into well
    for ry in range(87, 95):
        pset(25, ry, "leaf_amber" if ry % 2 == 0 else "moon_gold")

    # Wooden bucket sitting on the rim at (23..27, 91..95)
    for by in range(91, 96):
        for bx in range(23, 28):
            if bx in (23, 27) or by == 95:
                pset(bx, by, "bark_black")
            elif by == 93:
                pset(bx, by, "stone_pale")
            else:
                pset(bx, by, "bark_mid")
    pset(25, 90, "stone_light")

    # Winch crank handle on right post
    pset(34, 84, "stone_rim")
    pset(35, 84, "stone_light")
    pset(35, 85, "stone_rim")
    pset(35, 86, "bark_dark")

# =========================================================================
# 7. ANCIENT TWISTED TREES (Sculpted organic bark, NO stripes)
# =========================================================================
def draw_ancient_trees():
    # --- 7.1 RIGHT ANCIENT TREE ---
    for y in range(56, 128):
        cx = 114 - 6.5 * math.sin((y - 56) * 0.048)
        w = 9.0 + (y - 56) * 0.28
        for x in range(int(cx - w), int(cx + w + 1)):
            if 0 <= x < 128:
                rel_x = (x - (cx - w)) / (2.0 * w)
                
                # Volumetric shading: moonlit rim on left, deep shadow on right
                if rel_x < 0.12:
                    col = "bark_rim" if (x + y) % 2 == 0 else "bark_pale"
                elif rel_x < 0.35:
                    col = "bark_light" if (x + y) % 2 == 0 else "bark_mid"
                elif rel_x < 0.68:
                    col = "bark_mid" if (x + y) % 2 == 0 else "bark_dark"
                elif rel_x < 0.88:
                    col = "bark_dark" if (x + y) % 2 == 0 else "bark_deep"
                else:
                    col = "bark_deep" if (x + y) % 2 == 0 else "bark_black"

                # Organic bark fissures (natural twisting grain, not barcode)
                if (int(x * 0.8 + y * 0.3) % 7 == 0) and rel_x > 0.3:
                    col = "bark_black"

                # Moss on tree base
                if y > 102 and rel_x < 0.4 and (x + y) % 3 == 0:
                    col = "moss_dark" if (x * 2 + y) % 4 == 0 else "moss_mid"

                pset(x, y, col)

    # Gnarled roots crawling across forest floor
    root1 = [(106, 101), (101, 104), (96, 107), (91, 109), (86, 112)]
    for rx, ry in root1:
        for dx in range(-2, 3):
            for dy in range(-1, 2):
                pset(rx+dx, ry+dy, "bark_deep" if dy > 0 else "bark_mid")
                if dy == -1:
                    pset(rx+dx, ry+dy, "moss_light" if rx % 2 == 0 else "bark_light")

    # Tree hollow at (114, 82) with glowing fairy eyes
    for dy in range(-3, 4):
        for dx in range(-2, 3):
            if (dx/2)**2 + (dy/3)**2 <= 1.0:
                pset(114+dx, 82+dy, "bark_black")
    pset(113, 82, "magic_cyan_mid")
    pset(115, 82, "magic_cyan_mid")

    # Major Twisted Branches Arching Over Canvas
    b1_pts = [
        (110, 56, 6.0), (104, 44, 5.0), (96, 32, 4.2), (86, 22, 3.6),
        (74, 16, 3.0), (60, 11, 2.5), (46, 8, 2.0), (32, 7, 1.5)
    ]
    for i in range(len(b1_pts) - 1):
        x0, y0, r0 = b1_pts[i]
        x1, y1, r1 = b1_pts[i+1]
        steps = int(math.hypot(x1 - x0, y1 - y0) * 1.6) + 1
        for s in range(steps + 1):
            t = s / steps
            bx = x0 + (x1 - x0) * t
            by = y0 + (y1 - y0) * t
            br = r0 + (r1 - r0) * t
            for dy in range(-int(br)-1, int(br)+2):
                for dx in range(-int(br)-1, int(br)+2):
                    if math.hypot(dx, dy) <= br:
                        px, py = int(bx + dx), int(by + dy)
                        col = "bark_light" if dy < 0 else "bark_black" if dy > 0 else "bark_mid"
                        pset(px, py, col)

    # Secondary branch
    b2_pts = [(96, 32, 3.0), (88, 40, 2.2), (80, 44, 1.6)]
    for i in range(len(b2_pts) - 1):
        x0, y0, r0 = b2_pts[i]
        x1, y1, r1 = b2_pts[i+1]
        steps = 14
        for s in range(steps + 1):
            t = s / steps
            bx = int(x0 + (x1 - x0) * t)
            by = int(y0 + (y1 - y0) * t)
            pset(bx, by, "bark_mid")
            pset(bx, by + 1, "bark_black")

    # --- 7.2 LEFT ANCIENT TREE ---
    for y in range(30, 92):
        tx = int(3 + 3 * math.sin(y * 0.08))
        for x in range(0, tx + 6):
            if x < 128:
                col = "bark_rim" if x == tx + 5 else "bark_light" if (x+y)%2 == 0 else "bark_mid"
                if x < tx:
                    col = "bark_dark"
                pset(x, y, col)
    
    b_left = [(6, 36, 2.5), (12, 26, 2.2), (18, 17, 1.8), (24, 10, 1.5)]
    for i in range(len(b_left) - 1):
        x0, y0, r0 = b_left[i]
        x1, y1, r1 = b_left[i+1]
        steps = 12
        for s in range(steps + 1):
            t = s / steps
            bx = int(x0 + (x1 - x0) * t)
            by = int(y0 + (y1 - y0) * t)
            pset(bx, by, "bark_rim")
            pset(bx, by + 1, "bark_black")

    # --- 7.3 FOLIAGE (Dark Red, Brown, Purple Leaves) ---
    leaf_clusters = [
        (120, 12, 14, 10, "red"),
        (106, 16, 13, 9,  "crimson"),
        (92, 11,  11, 8,  "wine"),
        (76, 8,   10, 7,  "brown"),
        (58, 6,   9,  5,  "red"),
        (42, 5,   8,  5,  "wine"),
        (114, 30, 12, 8,  "amber"),
        (122, 42, 11, 7,  "purple"),
        (102, 34, 10, 6,  "crimson"),
        (88, 22,  8,  5,  "brown"),
        (10, 10,  10, 7,  "purple"),
        (20, 5,   8,  5,  "wine"),
        (4, 22,   8,  6,  "red"),
    ]

    for cx, cy, rx, ry, theme in leaf_clusters:
        for dy in range(-ry, ry + 1):
            for dx in range(-rx, rx + 1):
                d = (dx/rx)**2 + (dy/ry)**2
                jitter = (math.sin(dx * 1.7 + dy * 1.3) * 0.16)
                if d + jitter <= 1.0:
                    px, py = cx + dx, cy + dy
                    if 0 <= px < 128 and 0 <= py < 128:
                        light = -dx * 0.5 - dy * 0.8
                        
                        if theme == "red":
                            if light > 2.0:   col = "leaf_rose"
                            elif light > 0.5: col = "leaf_red"
                            elif light > -1.2:col = "leaf_crimson"
                            elif light > -2.8:col = "leaf_wine"
                            else:             col = "leaf_black"
                        elif theme == "crimson":
                            if light > 2.0:   col = "leaf_red"
                            elif light > 0.5: col = "leaf_crimson"
                            elif light > -1.2:col = "leaf_wine"
                            elif light > -2.8:col = "leaf_purple"
                            else:             col = "leaf_black"
                        elif theme == "wine":
                            if light > 2.0:   col = "leaf_crimson"
                            elif light > 0.5: col = "leaf_wine"
                            elif light > -1.2:col = "leaf_purple"
                            else:             col = "leaf_deep"
                        elif theme == "amber":
                            if light > 2.0:   col = "leaf_gold"
                            elif light > 0.5: col = "leaf_amber"
                            elif light > -1.2:col = "leaf_brown"
                            else:             col = "leaf_deep"
                        elif theme == "brown":
                            if light > 2.0:   col = "leaf_amber"
                            elif light > 0.5: col = "leaf_brown"
                            elif light > -1.2:col = "leaf_deep"
                            else:             col = "leaf_black"
                        else:
                            if light > 2.0:   col = "leaf_wine"
                            elif light > 0.5: col = "leaf_purple"
                            elif light > -1.2:col = "leaf_deep"
                            else:             col = "leaf_black"

                        pset(px, py, col)

    # Falling leaves
    drift_leaves = [
        (84, 24, "leaf_rose"), (72, 22, "leaf_gold"), (56, 18, "leaf_red"),
        (92, 48, "leaf_rose"), (102, 54, "leaf_amber"), (46, 38, "leaf_crimson"),
        (22, 42, "leaf_wine"), (34, 62, "leaf_gold"), (42, 78, "leaf_rose"),
    ]
    for lx, ly, lcol in drift_leaves:
        pset(lx, ly, lcol)
        pset(lx + 1, ly, "leaf_wine" if "leaf" in lcol else "leaf_brown")
        pset(lx, ly + 1, "leaf_black")

# =========================================================================
# 8. GROUND FLORA & GLOWING MUSHROOMS
# =========================================================================
def draw_ground_flora():
    grass_spots = [
        (12, 102), (18, 114), (42, 118), (52, 108), (62, 98),
        (72, 104), (82, 112), (94, 116), (102, 122), (118, 124),
        (8, 118), (28, 112), (48, 122), (68, 115), (88, 124)
    ]
    for gx, gy in grass_spots:
        pset(gx, gy, "moss_lime" if gx % 2 == 0 else "moss_bright")
        pset(gx-1, gy+1, "moss_light")
        pset(gx+1, gy+1, "moss_mid")
        pset(gx, gy+2, "moss_dark")

    # Glowing Magical Mushrooms
    mushrooms = [
        (98, 108, "magic_cyan_mid", 2),
        (101, 106, "magic_cyan_light", 3),
        (104, 109, "magic_cyan_mid", 2),
        (10, 108, "magic_pink", 2),
        (12, 106, "magic_cyan_light", 3),
        (34, 114, "magic_cyan_mid", 2),
        (45, 101, "magic_pink", 2),
    ]
    for mx, my, mcol, msz in mushrooms:
        pset(mx, my+1, "moon_cream")
        pset(mx, my+2, "stone_black")
        if msz == 3:
            pset(mx-1, my, mcol)
            pset(mx, my, "magic_cyan_light" if mcol != "magic_pink" else "magic_pink")
            pset(mx+1, my, mcol)
            pset(mx, my-1, mcol)
            pset(mx, my+2, "magic_cyan_dark")
        else:
            pset(mx, my, mcol)
            pset(mx+1, my, mcol)

# =========================================================================
# 9. DELICATE GROUND MIST & FAIRY PARTICLES
# =========================================================================
def draw_ground_mist_and_fairies():
    # Ethereal ground mist ribbons
    mist_wisps = [
        (80,  62, 112, "mist_dark", "warm_mist"),
        (86,  68, 118, "mist_mid",  "warm_mist"),
        (94,  82, 122, "mist_mid",  "warm_mist"),
        (104, 52, 96,  "mist_light","warm_mist"),
        (114, 48, 110, "mist_mid",  "warm_mist"),
    ]
    for my, x0, x1, c_cool, c_warm in mist_wisps:
        for x in range(x0, x1):
            wave = math.sin(x * 0.14) * 1.4
            y = int(my + wave)
            if 0 <= y < 128:
                if 14 <= x <= 36 and 78 <= y <= 112:
                    continue # protect well
                curr = pget(x, y)
                if curr in [P["fire_white"], P["fire_cream"], P["fire_yellow"], P["fire_amber"],
                            P["magic_cyan_light"], P["magic_cyan_mid"], P["magic_pink"],
                            P["stone_light"], P["stone_pale"], P["stone_rim"]]:
                    continue

                if (x + y * 2) % 4 == 0:
                    dw = math.hypot(x - 79, y - 70)
                    is_warm = (dw < 22 and 60 <= x <= 95)
                    col = c_warm if is_warm else c_cool
                    pset(x, y, col)

    # Fairy Fireflies / Glowing Motes
    fireflies = [
        (22, 74, "magic_cyan_light"), (38, 80, "magic_cyan_mid"), (16, 90, "magic_cyan_light"),
        (66, 60, "fire_cream"), (54, 70, "fire_amber"), (86, 82, "fire_yellow"),
        (92, 92, "magic_cyan_light"), (106, 90, "magic_cyan_mid"), (112, 72, "magic_cyan_light"),
        (76, 34, "magic_cyan_mid"), (88, 26, "star_white"), (48, 50, "magic_pink"),
        (28, 100, "magic_cyan_light"), (64, 110, "fire_yellow"), (98, 112, "magic_cyan_mid")
    ]
    for fx, fy, fcol in fireflies:
        pset(fx, fy, fcol)
        halo = "mist_pale" if "cyan" in fcol else "fire_orange" if "fire" in fcol else "mist_light"
        if (fx + fy) % 2 == 0:
            pset(fx + 1, fy, halo)

# =========================================================================
# RUN PIPELINE
# =========================================================================
draw_sky()
draw_ground()
draw_midground_mist()
draw_cottage()
draw_stone_path()
draw_stone_well()
draw_ancient_trees()
draw_ground_flora()
draw_ground_mist_and_fairies()

print("Stats:", c.stats())
finish(c)
view(c)
