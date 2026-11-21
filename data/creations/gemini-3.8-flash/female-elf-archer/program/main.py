from pixelbench_api import new_canvas, view, finish

def draw_elf_archer_v5():
    c = new_canvas(64, 64)

    # -------------------------------------------------------------------------
    # COHESIVE PALETTE (<86 colors, currently 44 colors)
    # -------------------------------------------------------------------------
    P = {
        ".": None,

        # Ground Shadow
        "gs1": "#121a1538",
        "gs2": "#0f161268",

        # Skin (Fair porcelain elven skin)
        "sk0": "#fff5ee",  # specular highlight
        "sk1": "#fde4d2",  # light skin
        "sk2": "#f4c6a6",  # warm peach midtone
        "sk3": "#cc8b6e",  # soft shadow
        "sk4": "#96543d",  # crease shadow
        "bls": "#f09285",  # rosy blush
        "lip": "#d95b50",  # lips

        # Eyes (Luminous Anime Emerald)
        "ew":   "#eef5f1",  # sclera
        "eg0":  "#7df7bf",  # bright mint catchlight/reflection
        "eg1":  "#34d68b",  # emerald bright
        "eg2":  "#158a50",  # rich emerald mid
        "eg3":  "#0c4a29",  # deep pine
        "ep":   "#102016",  # dark pupil & lash
        "w0":   "#ffffff",  # pure white catchlight

        # Hair (Long Vibrant Emerald Hair)
        "h0":  "#bcfcd8",  # hair gloss sheen
        "h1":  "#6be695",  # vibrant light emerald
        "h2":  "#28b35a",  # forest green base
        "h3":  "#167a3a",  # deep green shadow
        "h4":  "#0d4820",  # dark shadow
        "h5":  "#06240e",  # deepest crease / outline

        # Outfit (Light Green Archer Tunic & Skirt)
        "c0":  "#e4faea",  # highlight
        "c1":  "#9cebb0",  # light sage / mint
        "c2":  "#51c97a",  # light green base
        "c3":  "#288544",  # green shadow
        "c4":  "#145027",  # deep fold shadow

        # Cream / White Trim & Blouse
        "cr0": "#ffffff",  # white
        "cr1": "#efe9de",  # cream base
        "cr2": "#b8b2a3",  # cream shadow

        # Gold Metal (Trim, Buckles, Earring, Embroidery)
        "g0":  "#fff691",  # gold shine
        "g1":  "#e6b82c",  # polished gold
        "g2":  "#946a10",  # gold shadow

        # Brown Leather (Corset, Belt, Boots, Quiver, Vambraces)
        "l0":  "#d89d6e",  # leather highlight
        "l1":  "#946035",  # warm chestnut brown
        "l2":  "#5f3719",  # leather shadow
        "l3":  "#361a08",  # deep leather

        # Wood (Bow)
        "wd0": "#e4b082",  # wood highlight
        "wd1": "#ab7546",  # polished wood
        "wd2": "#6e4322",  # dark wood
        "wd3": "#3e230e",  # wood shadow

        # Arrows
        "ash": "#c4a272",  # wood shaft
        "afw": "#f2f6f2",  # white feather
        "afr": "#d8382b",  # crimson feather
        "afd": "#781810",  # dark feather

        # Soft Outlines
        "ol_d": "#0e1310",
        "ol_h": "#072010",
        "ol_c": "#10381e",
        "ol_l": "#221106",
        "ol_s": "#5a2b1c",
    }

    def px(x, y, key):
        if 0 <= x < 64 and 0 <= y < 64 and key != ".":
            c.set(x, y, P[key])

    def hline(y, x0, x1, key):
        for x in range(x0, x1 + 1):
            px(x, y, key)

    # -------------------------------------------------------------------------
    # 1. GROUND SHADOW (Grounded standing pose)
    # -------------------------------------------------------------------------
    for x in range(23, 44):
        px(x, 60, "gs1")
    for x in range(25, 42):
        px(x, 59, "gs1")
        px(x, 61, "gs1")
    for x in range(26, 33):
        px(x, 60, "gs2")
    for x in range(34, 41):
        px(x, 60, "gs2")

    # -------------------------------------------------------------------------
    # 2. BOW (SLUNG ON BACK) - Elegant Wooden Recurve Bow
    # -------------------------------------------------------------------------
    # Upper limb: arcs from behind left shoulder (x=23, y=21) up to tip at (x=15, y=4)
    bow_upper_coords = [
        (15, 4), (15, 5), (16, 6), (16, 7), (17, 8), (17, 9),
        (18, 10), (18, 11), (19, 12), (19, 13), (20, 14), (20, 15),
        (21, 16), (21, 17), (22, 18), (22, 19), (23, 20), (23, 21),
    ]
    for idx, (bx, by) in enumerate(bow_upper_coords):
        if idx == 0:
            px(bx, by, "g0")
            px(bx + 1, by, "g1")
        elif idx == 1:
            px(bx, by, "g1")
            px(bx + 1, by, "g2")
        else:
            px(bx - 1, by, "wd0")
            px(bx, by, "wd1")
            px(bx + 1, by, "wd2")

    # Lower limb: contiguous smooth curve down behind right hip/skirt to (20, 54)
    bow_lower_coords = [
        (24, 36), (24, 37), (23, 38), (23, 39),
        (22, 40), (22, 41), (21, 42), (21, 43),
        (20, 44), (20, 45), (19, 46), (19, 47),
        (18, 48), (18, 49), (18, 50), (19, 51),
        (19, 52), (20, 53), (20, 54),
    ]
    for idx, (bx, by) in enumerate(bow_lower_coords):
        if idx >= len(bow_lower_coords) - 2:
            px(bx, by, "g1")
            px(bx + 1, by, "g2")
        else:
            px(bx - 1, by, "wd0")
            px(bx, by, "wd1")
            px(bx + 1, by, "wd2")

    # -------------------------------------------------------------------------
    # 3. QUIVER & ARROWS ON BACK
    # -------------------------------------------------------------------------
    # Quiver tube angled behind left shoulder (x=21..25, y=13..24)
    for qy in range(13, 24):
        px(21, qy, "l0")
        px(22, qy, "l1")
        px(23, qy, "l1")
        px(24, qy, "l2")
        px(25, qy, "l3")
    # Quiver top gold rim:
    hline(13, 21, 25, "g1")
    px(22, 13, "g0")
    px(21, 14, "g2")

    # Arrows sticking out of quiver:
    # Arrow 1:
    c.line(22, 12, 19, 5, P["ash"])
    px(18, 5, "afw")
    px(19, 5, "afr")
    px(20, 5, "afw")
    px(18, 6, "afw")
    px(19, 6, "afr")
    px(20, 6, "afw")
    px(19, 7, "afd")

    # Arrow 2:
    c.line(23, 12, 22, 4, P["ash"])
    px(21, 4, "afw")
    px(22, 4, "afr")
    px(23, 4, "afw")
    px(21, 5, "afw")
    px(22, 5, "afr")
    px(23, 5, "afw")
    px(22, 6, "afd")

    # Arrow 3:
    c.line(24, 12, 25, 5, P["ash"])
    px(24, 5, "afw")
    px(25, 5, "afr")
    px(26, 5, "afw")
    px(24, 6, "afw")
    px(25, 6, "afr")
    px(26, 6, "afw")
    px(25, 7, "afd")

    # -------------------------------------------------------------------------
    # 4. LONG GREEN HAIR (BACK CASCADE - Flowing on both sides down to y=42)
    # -------------------------------------------------------------------------
    # Left back hair cascade (behind left shoulder & hip):
    back_hair_left = [
        (14, 25, 30),
        (15, 24, 30),
        (16, 23, 31),
        (17, 23, 31),
        (18, 22, 31),
        (19, 22, 30),
        (20, 22, 30),
        (21, 22, 29),
        (22, 22, 29),
        (23, 22, 28),
        (24, 22, 28),
        (25, 22, 28),
        (26, 22, 27),
        (27, 22, 27),
        (28, 22, 27),
        (29, 22, 27),
        (30, 22, 27),
        (31, 22, 27),
        (32, 22, 27),
        (33, 22, 26),
        (34, 22, 26),
        (35, 23, 26),
        (36, 23, 26),
        (37, 23, 25),
        (38, 23, 25),
        (39, 24, 25),
        (40, 24, 25),
        (41, 24, 25),
    ]
    for hy, hx0, hx1 in back_hair_left:
        for hx in range(hx0, hx1 + 1):
            if hx == hx0:
                col = "h3"
            elif hx == hx0 + 1:
                col = "h2"
            elif hx < hx1:
                col = "h3"
            else:
                col = "h4"
            px(hx, hy, col)
        px(hx0 - 1, hy, "ol_h")

    # Right back hair cascade (behind right shoulder & hip, extending down to y=42!):
    back_hair_right = [
        (15, 37, 41),
        (16, 37, 42),
        (17, 37, 42),
        (18, 38, 43),
        (19, 38, 43),
        (20, 39, 43),
        (21, 39, 43),
        (22, 39, 43),
        (23, 39, 42),
        (24, 39, 42),
        (25, 39, 42),
        (26, 39, 42),
        (27, 39, 42),
        (28, 39, 42),
        (29, 39, 42),
        (30, 39, 41),
        (31, 39, 41),
        (32, 39, 41),
        (33, 39, 41),
        (34, 39, 41),
        (35, 39, 41),
        (36, 39, 41),
        (37, 38, 40),
        (38, 38, 40),
        (39, 38, 40),
        (40, 38, 39),
        (41, 38, 39),
    ]
    for hy, hx0, hx1 in back_hair_right:
        for hx in range(hx0, hx1 + 1):
            if hx == hx1:
                col = "h4"
            elif hx == hx1 - 1:
                col = "h3"
            elif hx == hx0 + 1:
                col = "h1"
            else:
                col = "h2"
            px(hx, hy, col)
        px(hx1 + 1, hy, "ol_h")

    # -------------------------------------------------------------------------
    # 5. LEGS & ARCHER BOOTS (Standing Pose in 3/4 View)
    # -------------------------------------------------------------------------
    # Thighs (y=38..46): Fair porcelain skin
    for ty in range(38, 47):
        # Left thigh (near, straight: x=28..31)
        hline(ty, 28, 31, "sk1")
        px(28, ty, "sk2")
        px(31, ty, "sk2")
        # Right thigh (far, angled: x=34..37)
        hline(ty, 34, 37, "sk2")
        px(34, ty, "sk3")
        px(37, ty, "sk3")
    for ty in range(38, 44):
        px(31, ty, "sk3")
        px(32, ty, ".")
        px(33, ty, ".")
        px(34, ty, "sk3")

    # --- Archer Boots (y=47..59) ---
    # Left boot turnover cuff (y=47..48):
    hline(47, 27, 32, "l0")
    hline(48, 27, 32, "l1")
    px(27, 47, "l2")
    px(32, 47, "l2")
    px(27, 48, "l3")
    px(32, 48, "l3")
    px(29, 47, "g0")
    px(29, 48, "g1")

    # Right boot cuff:
    hline(47, 34, 38, "l1")
    hline(48, 34, 38, "l2")
    px(34, 47, "l2")
    px(38, 47, "l3")
    px(36, 47, "g1")

    # Left Boot Shaft & Calf (y=49..55):
    boot_left = [
        (49, 27, 32),
        (50, 27, 32),
        (51, 27, 32),
        (52, 27, 31),
        (53, 28, 31),
        (54, 28, 31),
        (55, 28, 31),
    ]
    for by, bx0, bx1 in boot_left:
        for bx in range(bx0, bx1 + 1):
            if bx == bx0:
                col = "l1"
            elif bx == bx0 + 1:
                col = "l0"
            elif bx < bx1:
                col = "l1"
            else:
                col = "l2"
            px(bx, by, col)
        px(bx0 - 1, by, "ol_l")
        px(bx1 + 1, by, "ol_l")

    # Left Foot & Toe (y=56..59):
    for by in range(56, 59):
        bx0 = 26 if by == 58 else 27
        bx1 = 32
        for bx in range(bx0, bx1 + 1):
            if bx <= 28:
                col = "l0" if by < 58 else "l1"
            elif bx < 31:
                col = "l1"
            else:
                col = "l2"
            px(bx, by, col)
        px(bx0 - 1, by, "ol_l")
        px(bx1 + 1, by, "ol_l")
    hline(59, 26, 32, "l3")

    # Right Boot Shaft & Calf (y=49..55):
    boot_right = [
        (49, 34, 38),
        (50, 34, 38),
        (51, 34, 38),
        (52, 34, 38),
        (53, 34, 37),
        (54, 34, 37),
        (55, 34, 37),
    ]
    for by, bx0, bx1 in boot_right:
        for bx in range(bx0, bx1 + 1):
            if bx == bx0:
                col = "l2"
            elif bx == bx0 + 1:
                col = "l1"
            elif bx < bx1:
                col = "l2"
            else:
                col = "l3"
            px(bx, by, col)
        px(bx0 - 1, by, "ol_l")
        px(bx1 + 1, by, "ol_l")

    # Right Foot & Toe (y=56..59):
    for by in range(56, 59):
        bx0 = 34
        bx1 = 39 if by == 58 else 38
        for bx in range(bx0, bx1 + 1):
            if bx < 36:
                col = "l1"
            elif bx < 38:
                col = "l2"
            else:
                col = "l3"
            px(bx, by, col)
        px(bx0 - 1, by, "ol_l")
        px(bx1 + 1, by, "ol_l")
    hline(59, 34, 39, "l3")

    # -------------------------------------------------------------------------
    # 6. LIGHT GREEN OUTFIT (Flared Skirt, Corset, Bodice, Belt, Quiver Strap)
    # -------------------------------------------------------------------------

    # --- Flared Archer Skirt / Tunic Bottom (y=31..38) ---
    skirt_data = [
        (31, 27, 35),
        (32, 26, 36),
        (33, 26, 36),
        (34, 25, 37),
        (35, 25, 38),
        (36, 24, 38),
        (37, 24, 39),
        (38, 23, 39),
    ]
    for sy, sx0, sx1 in skirt_data:
        for sx in range(sx0, sx1 + 1):
            u = (sx - sx0) / max(1, sx1 - sx0)
            if u < 0.15:
                col = "c3"
            elif u < 0.45:
                col = "c1" if sy < 35 else "c2"
            elif u < 0.7:
                col = "c2"
            elif u < 0.88:
                col = "c3"
            else:
                col = "c4"
            px(sx, sy, col)
        px(sx0 - 1, sy, "ol_c")
        px(sx1 + 1, sy, "ol_c")

    # Skirt folds / pleat highlights:
    for sy in range(32, 38):
        px(28, sy, "c0")
        px(29, sy, "c1")
        px(33, sy, "c1")
        px(34, sy, "c3")

    # Scalloped gold hem:
    for sx in range(24, 40):
        if sx % 2 == 0:
            px(sx, 38, "g0")
        else:
            px(sx, 38, "g1")
    hline(39, 24, 39, "g1")
    px(28, 39, "g0")
    px(29, 39, "g0")

    # --- Leather Underbust Corset (y=26..31) ---
    for cy in range(26, 31):
        cx0 = 27 if cy >= 28 else 28
        cx1 = 35 if cy >= 28 else 34
        for cx in range(cx0, cx1 + 1):
            if cx <= cx0 + 1:
                col = "l2"
            elif cx < 31:
                col = "l0" if cy < 28 else "l1"
            elif cx < 34:
                col = "l1"
            else:
                col = "l2"
            px(cx, cy, col)
        px(cx0 - 1, cy, "ol_l")
        px(cx1 + 1, cy, "ol_l")

    # Corset front laces:
    for ly in range(26, 30):
        px(30, ly, "cr1")
        px(31, ly, "l3")

    # Leather Belt with Golden Buckle (y=30..31):
    hline(30, 26, 36, "l1")
    hline(31, 26, 36, "l2")
    px(30, 30, "g0")
    px(31, 30, "g0")
    px(32, 30, "g1")
    px(30, 31, "g1")
    px(31, 31, "g2")
    px(32, 31, "g2")

    # Pouch:
    for py in range(31, 34):
        px(35, py, "l0")
        px(36, py, "l1")
        px(37, py, "l2")
    px(36, 32, "g0")

    # --- Light Green Tunic Bodice (y=21..25) ---
    for ty in range(21, 26):
        tx0 = 25 - (ty - 21) // 2
        tx1 = 36 + (ty - 21) // 2
        for tx in range(tx0, tx1 + 1):
            if tx < 27:
                col = "c2"
            elif tx < 32:
                col = "c1" if ty < 24 else "c2"
            elif tx < 35:
                col = "c2"
            else:
                col = "c3"
            px(tx, ty, col)
        px(tx0 - 1, ty, "ol_c")
        px(tx1 + 1, ty, "ol_c")

    px(28, 22, "c0")
    px(29, 22, "c0")
    px(28, 23, "c1")
    px(29, 23, "c1")

    # White collar & neckline:
    hline(19, 30, 32, "cr0")
    hline(20, 29, 33, "cr1")
    hline(21, 29, 33, "cr2")
    px(31, 21, "g1")

    # Quiver Strap across Chest:
    for sx, sy in [(25, 21), (26, 22), (27, 23), (28, 24),
                  (29, 25), (30, 26), (31, 27), (32, 28)]:
        px(sx, sy, "l0")
        px(sx + 1, sy, "l2")
    px(28, 24, "g0")
    px(29, 24, "g1")

    # --- Arms & Hands ---
    # Left Arm:
    for sy in range(21, 25):
        px(22, sy, "ol_c")
        px(23, sy, "c1")
        px(24, sy, "c2")
        px(25, sy, "c3")
    for vy in range(25, 30):
        px(22, vy, "ol_l")
        px(23, vy, "l0")
        px(24, vy, "l1")
        px(25, vy, "ol_l")
    px(23, 27, "g0")
    px(23, 30, "sk1")
    px(24, 30, "sk0")
    px(23, 31, "sk1")
    px(24, 31, "sk2")
    px(24, 32, "sk3")

    # Right Arm:
    for sy in range(21, 25):
        px(37, sy, "c2")
        px(38, sy, "c3")
        px(39, sy, "ol_c")
    for vy in range(25, 30):
        px(37, vy, "l1")
        px(38, vy, "l2")
        px(39, vy, "ol_l")
    px(38, 27, "g1")
    px(37, 30, "sk1")
    px(38, 30, "sk2")
    px(37, 31, "sk1")
    px(38, 31, "sk3")

    # -------------------------------------------------------------------------
    # 7. HEAD, FACE & POINTED ELF EARS
    # -------------------------------------------------------------------------

    # --- Neck (y=18..19) ---
    hline(18, 30, 32, "sk1")
    hline(19, 30, 32, "sk2")
    px(30, 18, "sk3")
    px(32, 18, "sk3")
    px(30, 19, "sk3")
    px(32, 19, "sk4")

    # --- Face Base (y=8..18) ---
    face_map = [
        (8,  29, 34),
        (9,  28, 35),
        (10, 27, 36),
        (11, 27, 36),
        (12, 27, 36),
        (13, 27, 36),
        (14, 28, 35),
        (15, 28, 35),
        (16, 29, 34),
        (17, 30, 33),
        (18, 31, 32),
    ]
    for fy, fx0, fx1 in face_map:
        hline(fy, fx0, fx1, "sk1")

    # Jawline and cheek contours
    px(27, 11, "sk2")
    px(27, 12, "sk2")
    px(27, 13, "sk3")
    px(28, 14, "sk3")
    px(28, 15, "sk3")
    px(29, 16, "sk3")
    px(30, 17, "sk3")
    px(31, 18, "sk4")
    px(32, 18, "sk4")

    px(36, 11, "sk2")
    px(36, 12, "sk3")
    px(36, 13, "sk3")
    px(35, 14, "sk3")
    px(35, 15, "sk3")
    px(34, 16, "ol_s")
    px(33, 17, "ol_s")

    # Forehead highlight
    px(31, 9, "sk0")
    px(32, 9, "sk0")

    # Soft blush on cheeks
    px(28, 15, "bls")
    px(29, 15, "bls")
    px(34, 15, "bls")
    px(35, 15, "bls")

    # --- POINTED ELF EARS (Dramatic, Long & Elegant!) ---
    # Left Ear: sweeping up-left from side of head at x=27 to tip at x=19, y=9
    ear_left = [
        (19, 9, "sk0"),
        (20, 9, "sk0"), (20, 10, "sk1"),
        (21, 10, "sk0"), (21, 11, "sk1"),
        (22, 10, "sk0"), (22, 11, "sk1"), (22, 12, "sk2"),
        (23, 11, "sk1"), (23, 12, "bls"), (23, 13, "sk3"),
        (24, 11, "sk1"), (24, 12, "bls"), (24, 13, "sk2"), (24, 14, "sk3"),
        (25, 12, "sk1"), (25, 13, "sk2"), (25, 14, "sk3"), (25, 15, "sk4"),
        (26, 12, "sk1"), (26, 13, "sk2"), (26, 14, "sk3"), (26, 15, "ol_s"),
    ]
    for ex, ey, ecol in ear_left:
        px(ex, ey, ecol)
    px(25, 15, "g0")
    px(25, 16, "g1")

    # Right Ear: sweeping up-right from x=36 to tip at x=43, y=10
    ear_right = [
        (43, 10, "sk0"),
        (42, 10, "sk0"), (42, 11, "sk1"),
        (41, 11, "sk1"), (41, 12, "sk2"),
        (40, 11, "sk1"), (40, 12, "bls"), (40, 13, "sk3"),
        (39, 12, "sk1"), (39, 13, "sk2"), (39, 14, "sk4"),
        (38, 12, "sk1"), (38, 13, "sk2"), (38, 14, "sk3"),
        (37, 13, "sk1"), (37, 14, "sk3"),
    ]
    for ex, ey, ecol in ear_right:
        px(ex, ey, ecol)

    # --- Facial Features (Expressive Anime/RPG Eyes, Nose, Mouth) ---
    # Eyebrows:
    px(28, 10, "h4")
    px(29, 10, "h4")
    px(30, 10, "h3")
    px(34, 10, "h3")
    px(35, 10, "h4")

    # Left Eye (near eye, x=28..31, y=12..14):
    # Lash:
    px(27, 12, "ep")
    px(28, 12, "ep")
    px(29, 12, "ep")
    px(30, 12, "ep")
    px(31, 12, "ep")
    # Upper Eye:
    px(28, 13, "ew")    # white sclera on outer corner
    px(29, 13, "w0")    # sharp specular catchlight!
    px(30, 13, "ep")    # deep dark pupil
    px(31, 13, "ew")    # white sclera on inner corner
    # Lower Eye:
    px(28, 14, "sk2")   # soft outer lid
    px(29, 14, "eg2")   # emerald iris base
    px(30, 14, "eg0")   # bright mint reflection shine
    px(31, 14, "sk2")   # soft inner lid

    # Right Eye (far eye, 3/4 turn, x=33..36, y=12..14):
    px(33, 12, "ep")
    px(34, 12, "ep")
    px(35, 12, "ep")
    px(36, 12, "ep")
    # Upper Eye:
    px(33, 13, "w0")    # catchlight!
    px(34, 13, "ep")    # dark pupil
    px(35, 13, "ew")    # sclera
    # Lower Eye:
    px(33, 14, "eg2")   # emerald
    px(34, 14, "eg0")   # bright mint reflection
    px(35, 14, "sk2")

    # Nose:
    px(32, 15, "sk0")
    px(33, 15, "sk3")

    # Mouth:
    px(31, 17, "lip")
    px(32, 17, "lip")
    px(31, 18, "sk3")

    # -------------------------------------------------------------------------
    # 8. FRONT HAIR (Crown, Lush Bangs, Flowing Locks)
    # -------------------------------------------------------------------------

    # Crown & Hair Volume (y=4..8):
    crown_map = [
        (4,  29, 34),
        (5,  27, 36),
        (6,  26, 37),
        (7,  25, 38),
        (8,  25, 38),
    ]
    for hy, hx0, hx1 in crown_map:
        for hx in range(hx0, hx1 + 1):
            if hy == 4:
                col = "h1" if hx in (31, 32) else "h2"
            elif hy == 5:
                col = "h0" if hx in (30, 31, 32) else ("h1" if hx in (29, 33) else "h2")
            elif hy == 6:
                col = "h0" if hx in (29, 30, 31, 32) else ("h1" if hx < 35 else "h3")
            elif hy == 7:
                col = "h1" if hx in (28, 29, 30) else ("h2" if hx < 34 else "h3")
            else:
                col = "h2" if hx < 31 else ("h3" if hx < 36 else "h4")
            px(hx, hy, col)
        px(hx0 - 1, hy, "ol_h")
        px(hx1 + 1, hy, "ol_h")

    # Glossy sheen shine on hair:
    hline(5, 30, 32, "h0")
    px(31, 5, "w0")

    # Bangs framing the face:
    # Left Bang:
    px(27, 8, "h1")
    px(28, 8, "h0")
    px(29, 8, "h1")
    px(27, 9, "h2")
    px(28, 9, "h1")
    px(27, 10, "h3")
    px(28, 10, "h2")
    px(28, 11, "h3")

    # Center-left Bang:
    px(30, 8, "h1")
    px(30, 9, "h2")
    px(30, 10, "h2")
    px(30, 11, "h3")

    # Center Bang:
    px(31, 8, "h1")
    px(32, 8, "h0")
    px(31, 9, "h2")
    px(32, 9, "h1")
    px(31, 10, "h2")
    px(32, 10, "h3")
    px(32, 11, "h4")

    # Right Bang:
    px(34, 8, "h2")
    px(35, 8, "h3")
    px(34, 9, "h3")
    px(35, 9, "h4")
    px(34, 10, "h3")
    px(35, 10, "h4")
    px(34, 11, "h4")

    # --- Front Side Locks ---
    # Left Lock (cascading down in front of left shoulder):
    left_lock = [
        (26, 11, "h1"), (27, 11, "h2"),
        (26, 12, "h0"), (27, 12, "h1"),
        (25, 13, "h1"), (26, 13, "h2"),
        (25, 14, "h0"), (26, 14, "h1"),
        (24, 15, "h1"), (25, 15, "h2"),
        (24, 16, "h1"), (25, 16, "h2"),
        (23, 17, "h0"), (24, 17, "h1"),
        (23, 18, "h1"), (24, 18, "h2"),
        (22, 19, "h0"), (23, 19, "h1"),
        (22, 20, "h1"), (23, 20, "h2"),
        (22, 21, "h2"), (23, 21, "h3"),
        (23, 22, "h3"),
        (23, 23, "h4"),
    ]
    for lx, ly, lcol in left_lock:
        px(lx, ly, lcol)
        px(lx - 1, ly, "ol_h")

    # Right Lock (cascading down past right shoulder):
    right_lock = [
        (36, 11, "h2"), (37, 11, "h3"),
        (36, 12, "h2"), (37, 12, "h3"),
        (37, 13, "h2"), (38, 13, "h3"),
        (37, 14, "h2"), (38, 14, "h3"),
        (37, 15, "h1"), (38, 15, "h2"),
        (37, 16, "h1"), (38, 16, "h2"),
        (38, 17, "h1"), (39, 17, "h2"),
        (38, 18, "h2"), (39, 18, "h3"),
        (38, 19, "h2"), (39, 19, "h3"),
        (39, 20, "h3"),
        (39, 21, "h4"),
    ]
    for lx, ly, lcol in right_lock:
        px(lx, ly, lcol)
        px(lx + 1, ly, "ol_h")

    print(c.stats())
    return c

c = draw_elf_archer_v5()
view(c)
finish(c)
