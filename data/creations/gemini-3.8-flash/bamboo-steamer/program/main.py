import math
from pixelbench_api import *

def build_masterpiece_steamer():
    c = new_canvas(32, 32, name="steamer")

    # -------------------------------------------------------------
    # Palette definition (Total: 27 colors <= 86 limit)
    # -------------------------------------------------------------
    # Bamboo tones (Warm natural golden bamboo)
    C_OUT        = "#261203"  # Deepest contour
    C_BAMBOO_D3  = "#4a2408"  # Deep shadow
    C_BAMBOO_D2  = "#733e14"  # Dark shadow
    C_BAMBOO_D1  = "#995a20"  # Mid-dark wood
    C_BAMBOO_MID = "#bd7a2b"  # Base bamboo tone
    C_BAMBOO_L1  = "#dc9c44"  # Light bamboo tone
    C_BAMBOO_L2  = "#eebc6a"  # Highlight wood
    C_BAMBOO_HI  = "#fbe09b"  # Bright wood highlight
    C_BAMBOO_MAX = "#fff2cf"  # Specular shine

    # Steamer Interior Cavity
    C_IN_SHADOW  = "#180a02"  # Deep cavity
    C_IN_WALL    = "#361b06"  # Inner bamboo rim shadow
    C_IN_RIM     = "#5c300e"  # Inner rim wood

    # Cabbage Leaf Liner (Natural savory dim sum greens)
    C_LEAF_SHAD  = "#11260c"  # Deepest shadow under dumplings
    C_LEAF_D2    = "#1c3c15"  # Leaf crease
    C_LEAF_MID   = "#2e5e22"  # Leaf base green
    C_LEAF_L1    = "#488534"  # Leaf light
    C_LEAF_L2    = "#68aa4a"  # Leaf frill / rib

    # Dumplings (Xiaolongbao - authentic pleated soup dumplings)
    C_D_CONTACT  = "#7a6045"  # Contact shadow on leaf
    C_D_SHAD_D   = "#94785b"  # Base shadow
    C_D_SHAD_M   = "#bfa588"  # Underside shadow
    C_D_CREASE   = "#d8c2a4"  # Pleat furrow / fold shadow
    C_D_CREAM    = "#eee2d0"  # Dumpling skin midtone
    C_D_LIGHT    = "#faf4e8"  # Dumpling pale skin
    C_D_WHITE    = "#ffffff"  # Pleat ridge highlight
    C_D_KNOT     = "#b06e32"  # Pinched twist apex
    C_D_SCALLION = "#3b7322"  # Scallion speck

    # Steam (Airy, misty, delicate rising steam)
    C_STEAM_1    = "#ffffff"  # Crisp core
    C_STEAM_2    = "#f2f8fc"  # Pale misty vapor
    C_STEAM_3    = "#d8ecf6"  # Soft edge
    C_STEAM_4    = "#b2daf0"  # Faint translucent tail

    # -------------------------------------------------------------
    # 1. LID (tilted open, propped open at back)
    # Tilted at -16 degrees, resting on left rim, propped high on right.
    # -------------------------------------------------------------
    angle = math.radians(-16)
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    cx, cy = 15.5, 7.5
    rx, ry = 11.2, 6.4

    for y in range(0, 16):
        for x in range(3, 29):
            tx = x - cx
            ty = y - cy
            lx = tx * cos_a + ty * sin_a
            ly = -tx * sin_a + ty * cos_a
            
            d = (lx / rx)**2 + (ly / ry)**2
            if d <= 1.0:
                # Woven herringbone/bamboo texture
                weave = (int(round(lx * 0.85 + ly * 0.85)) + int(round(lx * 0.85 - ly * 0.85))) % 2
                shade_val = -lx * 0.2 - ly * 0.35
                
                if d > 0.80:
                    c.set(x, y, C_BAMBOO_L2 if shade_val > 0 else C_BAMBOO_MID)
                else:
                    if weave == 0:
                        c.set(x, y, C_BAMBOO_L2 if shade_val > 0 else C_BAMBOO_L1)
                    else:
                        c.set(x, y, C_BAMBOO_L1 if shade_val > 0 else C_BAMBOO_MID)
            elif d <= 1.25:
                # Clean outline of lid
                if y <= 13 or (x > 21 and y <= 14):
                    c.set(x, y, C_OUT)

    # Lid handle (woven bamboo loop in center of dome)
    hx, hy = int(round(cx)), int(round(cy))
    c.set(hx - 2, hy - 1, C_OUT)
    c.set(hx - 1, hy - 2, C_OUT)
    c.set(hx,     hy - 2, C_OUT)
    c.set(hx + 1, hy - 2, C_OUT)
    c.set(hx + 2, hy - 1, C_OUT)
    c.set(hx - 1, hy - 1, C_BAMBOO_HI)
    c.set(hx,     hy - 1, C_BAMBOO_HI)
    c.set(hx + 1, hy - 1, C_BAMBOO_L2)
    c.set(hx - 1, hy,     C_BAMBOO_D3)
    c.set(hx,     hy,     C_OUT)
    c.set(hx + 1, hy,     C_BAMBOO_D3)

    # -------------------------------------------------------------
    # 2. STEAMER BASKET INTERIOR & CAVITY
    # -------------------------------------------------------------
    # Back rim of the basket:
    for x in range(4, 28):
        nx = (x - 15.5) / 11.5
        if abs(nx) <= 1.0:
            dy = 4.8 * math.sqrt(1.0 - nx*nx)
            y_back = int(round(17.0 - dy))
            c.set(x, y_back - 1, C_OUT)
            c.set(x, y_back, C_BAMBOO_MID if x < 16 else C_BAMBOO_D1)
            c.set(x, y_back + 1, C_IN_RIM)

    # Interior cavity & cabbage leaf liner:
    for y in range(14, 22):
        for x in range(5, 27):
            nx_in = (x - 15.5) / 9.8
            ny_in = (y - 17.0) / 3.6
            d_in = nx_in*nx_in + ny_in*ny_in
            
            if d_in <= 1.0:
                if y == 14:
                    c.set(x, y, C_IN_SHADOW)
                else:
                    lx_n = (x - 15.5) / 9.0
                    ly_n = (y - 17.6) / 2.8
                    df = lx_n*lx_n + ly_n*ly_n
                    
                    if df <= 1.0:
                        is_edge = df > 0.75
                        is_rib = (x * 2 + y) % 4 == 0
                        if is_edge:
                            c.set(x, y, C_LEAF_L2 if (x + y) % 2 == 0 else C_LEAF_L1)
                        elif is_rib:
                            c.set(x, y, C_LEAF_L1)
                        else:
                            c.set(x, y, C_LEAF_MID)
                    else:
                        c.set(x, y, C_LEAF_D2)

    # -------------------------------------------------------------
    # 3. THREE DUMPLINGS (Xiaolongbao)
    # -------------------------------------------------------------
    # Dumpling 1: Center-Back (cx=15.5, cy=14.5)
    # Dumpling 2: Front-Left (cx=9.5, cy=18.0)
    # Dumpling 3: Front-Right (cx=21.5, cy=18.0)

    # --- Dumpling 1 (Center-Back) ---
    for sx, sy in [(14, 17), (15, 17), (16, 17), (17, 17)]:
        c.set(sx, sy, C_LEAF_SHAD)

    c.set(15, 13, C_D_KNOT)
    c.set(16, 13, C_D_SCALLION)
    c.set(13, 14, C_D_SHAD_M)
    c.set(14, 14, C_D_WHITE)
    c.set(15, 14, C_D_CREASE)
    c.set(16, 14, C_D_WHITE)
    c.set(17, 14, C_D_CREAM)
    c.set(18, 14, C_D_SHAD_M)
    c.set(13, 15, C_D_CREAM)
    c.set(14, 15, C_D_WHITE)
    c.set(15, 15, C_D_LIGHT)
    c.set(16, 15, C_D_WHITE)
    c.set(17, 15, C_D_LIGHT)
    c.set(18, 15, C_D_SHAD_D)
    c.set(13, 16, C_D_SHAD_M)
    c.set(14, 16, C_D_LIGHT)
    c.set(15, 16, C_D_CREAM)
    c.set(16, 16, C_D_LIGHT)
    c.set(17, 16, C_D_SHAD_M)
    c.set(18, 16, C_D_SHAD_D)
    c.set(14, 17, C_D_CONTACT)
    c.set(15, 17, C_D_CONTACT)
    c.set(16, 17, C_D_CONTACT)
    c.set(17, 17, C_D_CONTACT)

    # --- Dumpling 2 (Front-Left) ---
    for sx, sy in [(8, 20), (9, 20), (10, 20), (11, 20)]:
        c.set(sx, sy, C_LEAF_SHAD)

    c.set(9,  16, C_D_CREAM)
    c.set(10, 16, C_D_KNOT)
    c.set(11, 16, C_D_SCALLION)
    c.set(8,  17, C_D_CREAM)
    c.set(9,  17, C_D_WHITE)
    c.set(10, 17, C_D_CREASE)
    c.set(11, 17, C_D_WHITE)
    c.set(12, 17, C_D_SHAD_M)
    c.set(7,  18, C_D_SHAD_M)
    c.set(8,  18, C_D_WHITE)
    c.set(9,  18, C_D_LIGHT)
    c.set(10, 18, C_D_WHITE)
    c.set(11, 18, C_D_LIGHT)
    c.set(12, 18, C_D_SHAD_M)
    c.set(7,  19, C_D_SHAD_D)
    c.set(8,  19, C_D_LIGHT)
    c.set(9,  19, C_D_CREAM)
    c.set(10, 19, C_D_LIGHT)
    c.set(11, 19, C_D_SHAD_M)
    c.set(12, 19, C_D_SHAD_D)
    c.set(8,  20, C_D_CONTACT)
    c.set(9,  20, C_D_CONTACT)
    c.set(10, 20, C_D_CONTACT)
    c.set(11, 20, C_D_CONTACT)

    # --- Dumpling 3 (Front-Right) ---
    for sx, sy in [(20, 20), (21, 20), (22, 20), (23, 20)]:
        c.set(sx, sy, C_LEAF_SHAD)

    c.set(21, 16, C_D_KNOT)
    c.set(22, 16, C_D_SCALLION)
    c.set(23, 16, C_D_CREAM)
    c.set(20, 17, C_D_CREAM)
    c.set(21, 17, C_D_WHITE)
    c.set(22, 17, C_D_CREASE)
    c.set(23, 17, C_D_WHITE)
    c.set(24, 17, C_D_SHAD_M)
    c.set(19, 18, C_D_CREAM)
    c.set(20, 18, C_D_WHITE)
    c.set(21, 18, C_D_LIGHT)
    c.set(22, 18, C_D_WHITE)
    c.set(23, 18, C_D_SHAD_M)
    c.set(24, 18, C_D_SHAD_D)
    c.set(19, 19, C_D_SHAD_M)
    c.set(20, 19, C_D_LIGHT)
    c.set(21, 19, C_D_CREAM)
    c.set(22, 19, C_D_SHAD_M)
    c.set(23, 19, C_D_SHAD_D)
    c.set(20, 20, C_D_CONTACT)
    c.set(21, 20, C_D_CONTACT)
    c.set(22, 20, C_D_CONTACT)
    c.set(23, 20, C_D_CONTACT)

    # Leaf ripple in center:
    c.set(13, 20, C_LEAF_MID)
    c.set(14, 20, C_LEAF_L1)
    c.set(15, 20, C_LEAF_L2)
    c.set(16, 20, C_LEAF_L1)
    c.set(17, 20, C_LEAF_MID)
    c.set(18, 20, C_LEAF_D2)
    c.set(14, 21, C_LEAF_D2)
    c.set(15, 21, C_LEAF_MID)
    c.set(16, 21, C_LEAF_D2)

    # -------------------------------------------------------------
    # 4. BASKET FRONT WALL & RIM
    # -------------------------------------------------------------
    for x in range(4, 28):
        nx = (x - 15.5) / 11.5
        dy = 4.8 * math.sqrt(max(0.0, 1.0 - nx*nx))
        y_top = int(round(17.0 + dy))
        y_bot = int(round(23.0 + dy))

        for y in range(y_top, y_bot + 1):
            if x == 4 or x == 27:
                c.set(x, y, C_OUT)
            elif y == y_top:
                if x < 8:
                    c.set(x, y, C_BAMBOO_L1)
                elif x < 15:
                    c.set(x, y, C_BAMBOO_MAX)
                elif x < 21:
                    c.set(x, y, C_BAMBOO_HI)
                else:
                    c.set(x, y, C_BAMBOO_L1)
            elif y == y_top + 1:
                if x < 8:
                    c.set(x, y, C_BAMBOO_MID)
                elif x < 18:
                    c.set(x, y, C_BAMBOO_L2)
                elif x < 23:
                    c.set(x, y, C_BAMBOO_L1)
                else:
                    c.set(x, y, C_BAMBOO_D1)
            elif y == y_bot:
                c.set(x, y, C_OUT)
            elif y == y_bot - 1:
                c.set(x, y, C_BAMBOO_D2 if x > 18 else C_BAMBOO_D1)
            else:
                if y == y_top + 3:
                    c.set(x, y, C_BAMBOO_D2 if x > 17 else C_BAMBOO_D1)
                elif (x == 7 or x == 8) and (y == y_top + 2 or y == y_top + 4):
                    c.set(x, y, C_OUT)
                elif x < 8:
                    c.set(x, y, C_BAMBOO_MID)
                elif x < 17:
                    c.set(x, y, C_BAMBOO_L1 if y % 2 == 0 else C_BAMBOO_L2)
                elif x < 23:
                    c.set(x, y, C_BAMBOO_MID)
                else:
                    c.set(x, y, C_BAMBOO_D1)

    # Bottom shadow
    for x in range(7, 25):
        nx = (x - 15.5) / 10.0
        if abs(nx) <= 1.0:
            dy = 4.8 * math.sqrt(max(0.0, 1.0 - ((x - 15.5)/11.5)**2))
            y_base = int(round(23.0 + dy))
            if y_base + 1 < 32:
                c.set(x, y_base + 1, C_OUT)

    # -------------------------------------------------------------
    # 5. RISING STEAM (Delicate wisps drifting into open air)
    # -------------------------------------------------------------
    # Right plume: Billowing gracefully from the lifted lid gap into the sky
    steam_right = [
        (26, 12, C_STEAM_3),
        (27, 11, C_STEAM_2), (28, 11, C_STEAM_4),
        (27, 10, C_STEAM_1), (28, 10, C_STEAM_3),
        (28, 9,  C_STEAM_1), (29, 9,  C_STEAM_3),
        (28, 8,  C_STEAM_1),
        (27, 7,  C_STEAM_2), (28, 7,  C_STEAM_2),
        (26, 6,  C_STEAM_2), (27, 6,  C_STEAM_3),
        (26, 5,  C_STEAM_2),
        (26, 4,  C_STEAM_3),
        (27, 3,  C_STEAM_3),
        (28, 2,  C_STEAM_2), (29, 2, C_STEAM_4),
        (28, 1,  C_STEAM_3),
        (29, 0,  C_STEAM_4),
    ]
    for sx, sy, sc in steam_right:
        c.set(sx, sy, sc)

    # Left plume: Delicate wisp curling up along left side in open air
    steam_left = [
        (3,  10, C_STEAM_3),
        (2,  9,  C_STEAM_2), (3, 9, C_STEAM_3),
        (2,  8,  C_STEAM_1),
        (3,  7,  C_STEAM_1), (4, 7, C_STEAM_3),
        (3,  6,  C_STEAM_2),
        (4,  5,  C_STEAM_2),
        (5,  4,  C_STEAM_3),
        (5,  3,  C_STEAM_2), (6, 3, C_STEAM_4),
        (6,  2,  C_STEAM_3),
        (7,  1,  C_STEAM_3),
        (8,  0,  C_STEAM_4),
    ]
    for sx, sy, sc in steam_left:
        c.set(sx, sy, sc)

    stats = c.stats()
    print("Final stats:", stats)
    view(c)
    finish(c)

build_masterpiece_steamer()
