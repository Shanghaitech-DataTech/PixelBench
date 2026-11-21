import math
from pixelbench_api import *

def render_artwork():
    c = new_canvas(64, 64, "#000000")
    
    # -------------------------------------------------------------------------
    # MASTER PALETTE (Strictly controlled, 42 unique colors, limit 86)
    # -------------------------------------------------------------------------
    # Sky & Distant Mountains
    SKY_MIST     = "#d6e2ec"
    MTN_PALE     = "#98adbf"
    MTN_MID      = "#6b8296"
    MTN_DARK     = "#465c6e"
    MTN_DEEP     = "#2d3d4a"
    SMOKE_PALE   = "#eef4f9"

    # Village & Structures & Stone
    WOOD_DARK    = "#211309"  # deepest shadow, door, wall crevices
    WOOD_MID     = "#3d2414"  # timber wall, dark earth
    WOOD_LIGHT   = "#5c3720"  # sunlit timber, wall stone
    PATH_DARK    = "#7a5a36"  # dirt path shadow
    PATH_LIGHT   = "#a37c4d"  # sunlit dirt path
    STONE_GREY   = "#615c54"  # stone steps/rocks
    WINDOW_GLOW  = "#edd59a"  # warm paper window glow

    # Thatched Roofs & Golden Rice Terraces
    RICE_DARKEST = "#784306"  # cast shadow of walls onto rice
    RICE_DARK    = "#9a5808"  # deep golden grain shadow
    RICE_AMBER   = "#be740b"  # warm rich amber
    RICE_MID     = "#df9313"  # golden ripe grain
    RICE_GOLD    = "#f0ad1c"  # sunlit golden grain
    RICE_BRIGHT  = "#f9c42a"  # bright grain head
    RICE_LIGHT   = "#fde047"  # golden tips, straw highlights
    RICE_PALE    = "#fef9c3"  # sparkling sunlit rice tips
    RICE_TIE     = "#522806"  # sheaf tie band / hat apex

    # Harvested Stubble
    STUBBLE_DARK = "#947b3b"  # cut stubble line
    STUBBLE_MID  = "#bda154"  # harvested ground
    STUBBLE_LIGHT= "#dec97d"  # sunlit cut stalks

    # Vegetation & Bund Grass
    GREEN_DEEP   = "#102919"  # tree shadow
    GREEN_MID    = "#1e5430"  # tree canopy
    GREEN_LIGHT  = "#3b824c"  # sunlit leaves
    GREEN_GOLD   = "#79962a"  # autumn foliage / bright bund grass
    GRASS_BUND   = "#506e23"  # mossy grass along ridges

    # Water & Reflections
    WATER_DEEP   = "#284659"  # water edge shadow
    WATER_MID    = "#4a738f"  # water body
    WATER_SKY    = "#7ba5c4"  # sky reflection / streamlet
    WATER_FOAM   = "#cfe5f5"  # waterfall foam / cloud glint

    # Farmers
    BLUE_DARK    = "#1e3a8a"  # farmer 1 blue coat
    BLUE_LIGHT   = "#3b82f6"  # farmer 1 blue coat light
    RED_DARK     = "#991b1b"  # farmer 2 red tunic
    RED_LIGHT    = "#dc2626"  # farmer 2 red tunic light
    SKIN_TONE    = "#c98a5d"  # skin tone
    SICKLE_SILV  = "#e2e8f0"  # sickle blade
    PANTS_DARK   = "#111827"  # trousers / boots

    # -------------------------------------------------------------------------
    # 1. ELEVATION FIELD & ORGANIC MOUNTAIN CONTOURS
    # -------------------------------------------------------------------------
    def get_elevation(x, y):
        u = x / 63.0
        v = y / 63.0
        
        # Mountain spur curving from left-center across to right-center
        spur_center_x = 0.42 + 0.18 * math.sin(v * math.pi * 0.95)
        dist_spur = u - spur_center_x
        spur_h = 0.28 * math.exp(-(dist_spur**2) / 0.16) * (1.0 - v * 0.3)
        
        # Valley on right side
        valley_h = -0.15 * math.exp(-((u - 0.85)**2) / 0.12) * (0.2 + 0.8 * v)
        
        # Valley on far left
        left_valley = -0.08 * math.exp(-((u - 0.05)**2) / 0.08) * (v * 0.8)
        
        # Organic undulations
        w1 = 0.045 * math.sin(u * 5.5 + v * 3.2)
        w2 = 0.03 * math.sin(u * 10.0 - v * 6.5)
        w3 = 0.02 * math.cos(u * 4.0 + v * 8.5)
        
        base = 1.0 - (0.22 * u + 0.78 * v)
        return base + spur_h + valley_h + left_valley + w1 + w2 + w3

    H = [[get_elevation(x, y) for x in range(64)] for y in range(64)]
    min_h = min(H[y][x] for y in range(64) for x in range(64))
    max_h = max(H[y][x] for y in range(64) for x in range(64))

    N_TIERS = 8
    T = [[0]*64 for _ in range(64)]
    tier_raw = [[0.0]*64 for _ in range(64)]
    for y in range(64):
        for x in range(64):
            norm = (H[y][x] - min_h) / (max_h - min_h + 1e-5)
            val = norm * N_TIERS
            t = int(val)
            t = max(0, min(N_TIERS - 1, t))
            T[y][x] = t
            tier_raw[y][x] = val - t

    # Identify bunds and walls
    is_bund = [[False]*64 for _ in range(64)]
    is_wall = [[False]*64 for _ in range(64)]

    for y in range(64):
        for x in range(64):
            t = T[y][x]
            for dx, dy in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 64 and 0 <= ny < 64:
                    if T[ny][nx] < t:
                        is_bund[y][x] = True
                        is_wall[ny][nx] = True

    # -------------------------------------------------------------------------
    # 2. DRAW BASE TERRACES (Golden Rice Shelves with Layered Values)
    # -------------------------------------------------------------------------
    for y in range(64):
        for x in range(64):
            t = T[y][x]
            frac = tier_raw[y][x] # 1 = near upper wall drop, 0 = near outer bund rim
            
            # Subtle directional grain fleck
            fleck = ((x * 17 + y * 31) ^ (x * 3)) % 100
            
            # Shading inside the shelf:
            if frac > 0.8:
                col = RICE_DARKEST if fleck < 50 else RICE_DARK
            elif frac > 0.55:
                col = RICE_DARK if fleck < 35 else (RICE_AMBER if fleck < 80 else RICE_MID)
            elif frac > 0.25:
                col = RICE_AMBER if fleck < 30 else (RICE_MID if fleck < 75 else RICE_GOLD)
            else:
                col = RICE_GOLD if fleck < 40 else (RICE_BRIGHT if fleck < 85 else RICE_LIGHT)
            
            c.set(x, y, col)

    # -------------------------------------------------------------------------
    # 3. DRAW WALLS AND BUNDS (Stepped Retaining Walls & Footpaths)
    # -------------------------------------------------------------------------
    for y in range(64):
        for x in range(64):
            if is_wall[y][x]:
                # Retaining wall face in shadow
                if (x + y) % 5 == 0:
                    c.set(x, y, WOOD_LIGHT)
                elif (x + y) % 3 == 0:
                    c.set(x, y, WOOD_MID)
                else:
                    c.set(x, y, WOOD_DARK)
            elif is_bund[y][x]:
                # Sunlit bund / walking path
                if (x * 7 + y * 13) % 11 == 0:
                    c.set(x, y, GREEN_GOLD)
                elif (x * 5 + y * 7) % 5 == 0:
                    c.set(x, y, GRASS_BUND)
                elif (x + y) % 2 == 0:
                    c.set(x, y, PATH_LIGHT)
                else:
                    c.set(x, y, PATH_DARK)

    # -------------------------------------------------------------------------
    # 4. HARVESTED PADDY & STACKED RICE SHEAVES (Harvest Season Feature)
    # -------------------------------------------------------------------------
    # Harvested section in Tier 4: x in 30..56, y in 25..36
    for y in range(25, 37):
        for x in range(30, 58):
            if T[y][x] == 4 and not is_bund[y][x] and not is_wall[y][x]:
                # Stubble comb lines running horizontally across the terrace
                if y % 2 == 0:
                    c.set(x, y, STUBBLE_DARK if x % 2 == 0 else STUBBLE_MID)
                else:
                    c.set(x, y, STUBBLE_MID if x % 2 == 0 else STUBBLE_LIGHT)

    # Stacked golden rice sheaves (3x3 neat bundles standing on the stubble)
    sheaf_coords = [
        (34, 27), (40, 27), (46, 28), (52, 28),
        (36, 31), (42, 31), (48, 32), (54, 32),
        (38, 34), (44, 35)
    ]
    for sx, sy in sheaf_coords:
        if 0 <= sx < 62 and 0 <= sy < 62 and T[sy][sx] == 4 and not is_wall[sy][sx] and not is_bund[sy][sx]:
            c.set(sx, sy - 1, RICE_PALE)
            c.set(sx + 1, sy - 1, RICE_LIGHT)
            c.set(sx, sy, RICE_BRIGHT)
            c.set(sx + 1, sy, RICE_TIE)
            c.set(sx, sy + 1, WOOD_DARK)
            c.set(sx + 1, sy + 1, RICE_AMBER)

    # -------------------------------------------------------------------------
    # 5. WATER TERRACE & IRRIGATION STREAMLET (Sky Reflections)
    # -------------------------------------------------------------------------
    # Glassy sky-reflection pool in Tier 1: x in 45..63, y in 48..58
    for y in range(48, 59):
        for x in range(45, 64):
            if T[y][x] == 1 and not is_bund[y][x] and not is_wall[y][x]:
                # Glassy water with smooth horizontal bands reflecting sky & clouds
                if y in [51, 52] and 48 <= x <= 56:
                    # Cloud highlight reflection
                    c.set(x, y, WATER_FOAM if (x % 3 != 0) else WATER_SKY)
                elif y in [49, 50, 53]:
                    c.set(x, y, WATER_SKY if (x % 4 != 0) else WATER_MID)
                elif y in [54, 55]:
                    c.set(x, y, WATER_MID if (x % 3 != 0) else WATER_DEEP)
                else:
                    c.set(x, y, WATER_DEEP)

    # Water streamlet cascading down through terraces on the right
    streamlet = [
        (47, 36), (47, 37), (48, 38), (48, 39), (49, 40), (49, 41),
        (49, 42), (50, 43), (50, 44), (51, 45), (51, 46), (52, 47)
    ]
    for sx, sy in streamlet:
        c.set(sx, sy, WATER_SKY)
        if sx + 1 < 64:
            c.set(sx + 1, sy, WATER_DEEP)
    # Waterfall splashes over the retaining walls
    c.set(47, 37, WATER_FOAM)
    c.set(49, 41, WATER_FOAM)
    c.set(51, 46, WATER_FOAM)

    # -------------------------------------------------------------------------
    # 6. DISTANT MOUNTAIN SILHOUETTE & SKY (y=0..4, clean atmospheric depth)
    # -------------------------------------------------------------------------
    for x in range(64):
        # Distant peak profiles
        p1 = int(1.4 + 0.6 * math.sin(x * 0.12) + 0.3 * math.cos(x * 0.25))
        p2 = int(2.4 + 0.8 * math.sin(x * 0.15 + 1.2))
        p3 = int(3.5 + 0.8 * math.cos(x * 0.18 + 0.5))
        for y in range(0, 5):
            if y < p1:
                c.set(x, y, SKY_MIST)
            elif y < p2:
                c.set(x, y, MTN_PALE)
            elif y < p3:
                c.set(x, y, MTN_MID)
            elif y <= 4 and (x > 33 or y < 3):
                c.set(x, y, MTN_DARK if y == 3 else MTN_DEEP)

    # -------------------------------------------------------------------------
    # 7. VILLAGE ON MOUNTAIN CREST (x=0..34, y=3..12)
    # -------------------------------------------------------------------------
    for y in range(3, 13):
        for x in range(0, 35):
            if x + y * 1.35 < 42:
                # Earthen plateau ground
                if (x * 7 + y * 11) % 7 == 0:
                    c.set(x, y, STONE_GREY)
                elif (x * 5 + y * 13) % 5 == 0:
                    c.set(x, y, GRASS_BUND)
                elif (x + y) % 3 == 0:
                    c.set(x, y, PATH_LIGHT)
                else:
                    c.set(x, y, PATH_DARK)

    # Low stone wall / foundation supporting the village plateau
    for y in range(3, 13):
        for x in range(0, 36):
            if 39 <= x + y * 1.35 < 42:
                c.set(x, y, WOOD_DARK if (x + y) % 2 == 0 else STONE_GREY)

    # Village mountain trees & bamboo (framing the settlement)
    def plant_tree(tx, ty, r, is_autumn=False):
        for dy in range(-r, r + 1):
            for dx in range(-r, r + 1):
                if dx*dx + dy*dy <= r*r:
                    px, py = tx + dx, ty + dy
                    if 0 <= px < 64 and 0 <= py < 64:
                        if dy < 0:
                            col = GREEN_GOLD if is_autumn else (GREEN_LIGHT if (px+py)%2==0 else GREEN_MID)
                        elif dy == 0:
                            col = GREEN_MID if (px+py)%2==0 else GREEN_DEEP
                        else:
                            col = GREEN_DEEP
                        c.set(px, py, col)

    plant_tree(2, 3, 2, False)
    plant_tree(5, 2, 2, True)
    plant_tree(28, 4, 3, False)
    plant_tree(32, 6, 2, True)
    plant_tree(34, 9, 2, False)

    # VILLAGE HOUSES:
    # House 1: Main farmhouse (x=9..17, y=4..10)
    for x in range(11, 16):
        c.set(x, 4, RICE_BRIGHT)
    for x in range(10, 17):
        c.set(x, 5, RICE_GOLD if x < 15 else RICE_AMBER)
    for x in range(9, 18):
        c.set(x, 6, RICE_MID if x < 15 else RICE_DARK)
    for x in range(8, 19):
        c.set(x, 7, WOOD_DARK) # eaves overhang
    for y in range(8, 11):
        for x in range(10, 17):
            c.set(x, y, WOOD_MID)
    for y in range(8, 11):
        c.set(10, y, WOOD_DARK)
        c.set(16, y, WOOD_DARK)
    c.set(13, 9, WOOD_DARK)
    c.set(13, 10, WOOD_DARK)
    c.set(11, 9, WINDOW_GLOW)
    c.set(15, 9, WINDOW_GLOW)
    # Chimney & curling smoke
    c.set(11, 3, SMOKE_PALE)
    c.set(10, 2, SMOKE_PALE)
    c.set(11, 1, SKY_MIST)
    c.set(12, 0, SKY_MIST)

    # House 2: Barn / granary (x=19..25, y=6..11)
    for x in range(21, 25):
        c.set(x, 6, RICE_BRIGHT)
    for x in range(20, 26):
        c.set(x, 7, RICE_GOLD if x < 24 else RICE_AMBER)
    for x in range(19, 27):
        c.set(x, 8, WOOD_DARK)
    for y in range(9, 12):
        for x in range(20, 26):
            c.set(x, y, WOOD_MID)
    for y in range(9, 12):
        c.set(20, y, WOOD_DARK)
        c.set(25, y, WOOD_DARK)
    c.set(22, 10, WOOD_DARK)
    c.set(22, 11, WOOD_DARK)
    c.set(24, 10, WINDOW_GLOW)

    # House 3: Cottage (x=2..7, y=7..12)
    for x in range(3, 7):
        c.set(x, 7, RICE_BRIGHT)
    for x in range(2, 8):
        c.set(x, 8, RICE_GOLD)
    for x in range(1, 9):
        c.set(x, 9, WOOD_DARK)
    for y in range(10, 13):
        for x in range(2, 8):
            c.set(x, y, WOOD_MID)
    c.set(4, 11, WOOD_DARK)
    c.set(4, 12, WOOD_DARK)

    # Village stone/dirt path winding into terrace bunds
    trail = [
        (13, 11), (13, 12), (14, 13), (15, 14), (16, 15), (17, 16),
        (18, 17), (19, 18), (20, 19), (20, 20)
    ]
    for tx, ty in trail:
        c.set(tx, ty, PATH_LIGHT)
        c.set(tx + 1, ty, PATH_DARK)

    # -------------------------------------------------------------------------
    # 8. TWO FARMERS ON NARROW RIDGES
    # -------------------------------------------------------------------------
    # Farmer 1: Carrying pole with two baskets (The Carrier)
    # Walking on ridge at x=24, y=28
    c.set(24, 25, RICE_TIE)       # hat apex
    c.set(23, 26, RICE_LIGHT)     # straw hat
    c.set(24, 26, RICE_LIGHT)
    c.set(25, 26, RICE_GOLD)
    c.set(22, 27, RICE_TIE)       # hat brim
    c.set(23, 27, RICE_LIGHT)
    c.set(24, 27, RICE_BRIGHT)
    c.set(25, 27, RICE_GOLD)
    c.set(26, 27, RICE_TIE)
    # Face & neck
    c.set(24, 28, SKIN_TONE)
    # Indigo Blue Jacket
    c.set(23, 29, BLUE_DARK)
    c.set(24, 29, BLUE_LIGHT)
    c.set(25, 29, BLUE_DARK)
    c.set(24, 30, BLUE_DARK)
    # Legs walking on narrow ridge
    c.set(23, 31, PANTS_DARK)
    c.set(25, 31, PANTS_DARK)
    c.set(23, 32, PANTS_DARK)
    # Bamboo shoulder pole (yoke)
    for px in range(20, 29):
        c.set(px, 28, WOOD_LIGHT if 22 <= px <= 26 else WOOD_MID)
    # Left basket
    c.set(20, 29, WOOD_MID)
    c.set(19, 30, WOOD_LIGHT)
    c.set(20, 30, RICE_PALE)
    c.set(21, 30, RICE_LIGHT)
    c.set(19, 31, WOOD_MID)
    c.set(20, 31, WOOD_DARK)
    c.set(21, 31, WOOD_MID)
    # Right basket
    c.set(28, 29, WOOD_MID)
    c.set(27, 30, RICE_LIGHT)
    c.set(28, 30, RICE_PALE)
    c.set(29, 30, WOOD_LIGHT)
    c.set(27, 31, WOOD_MID)
    c.set(28, 31, WOOD_DARK)
    c.set(29, 31, WOOD_MID)

    # Farmer 2: Harvester with sickle cutting rice (on ridge by harvest patch)
    # Position: x=31, y=34 (right at the boundary of standing rice and cut stubble!)
    c.set(31, 31, RICE_TIE)       # hat apex
    c.set(30, 32, RICE_LIGHT)     # hat
    c.set(31, 32, RICE_BRIGHT)
    c.set(32, 32, RICE_GOLD)
    c.set(29, 33, RICE_TIE)       # brim
    c.set(30, 33, RICE_LIGHT)
    c.set(31, 33, RICE_LIGHT)
    c.set(32, 33, RICE_GOLD)
    c.set(33, 33, RICE_TIE)
    # Face & neck
    c.set(31, 34, SKIN_TONE)
    # Red peasant tunic (bending posture)
    c.set(30, 35, RED_LIGHT)
    c.set(31, 35, RED_DARK)
    c.set(32, 35, RED_DARK)
    c.set(31, 36, RED_DARK)
    # Dark trousers & boots on bund
    c.set(31, 37, PANTS_DARK)
    c.set(32, 37, PANTS_DARK)
    c.set(32, 38, PANTS_DARK)
    # Right arm extending forward with silver sickle
    c.set(29, 35, SKIN_TONE)      # hand
    c.set(28, 34, SICKLE_SILV)    # sickle blade curve
    c.set(28, 35, MTN_PALE)
    # Left hand holding cut golden sheaf
    c.set(33, 34, RICE_PALE)
    c.set(33, 35, RICE_LIGHT)
    c.set(34, 35, RICE_AMBER)

    return c

if __name__ == "__main__":
    canvas = render_artwork()
    stats = canvas.stats()
    print("Stats:", stats["colors_used"], "colors used.")
    view(canvas)
    finish(canvas)
