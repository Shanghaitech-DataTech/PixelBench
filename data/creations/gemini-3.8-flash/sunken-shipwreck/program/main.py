from pixelbench_api import *

def render_scene():
    c = new_canvas(64, 64)

    # =============================================================
    # 1. WATER BACKGROUND & SMOOTH GRADIENT
    # =============================================================
    # 7 distinct ocean depth bands
    w_cols = [
        '#16607a',  # 0: shallow surface water (0..6)
        '#12526b',  # 1: upper ocean (7..13)
        '#0f445b',  # 2: upper mid (14..21)
        '#0c374b',  # 3: mid ocean (22..30)
        '#092b3c',  # 4: lower mid (31..40)
        '#061f2d',  # 5: deep water (41..51)
        '#04141f',  # 6: ocean floor abyss (52..63)
    ]

    c.rect(0, 0,  64, 7,  w_cols[0])
    c.rect(0, 7,  64, 7,  w_cols[1])
    c.rect(0, 14, 64, 8,  w_cols[2])
    c.rect(0, 22, 64, 9,  w_cols[3])
    c.rect(0, 31, 64, 10, w_cols[4])
    c.rect(0, 41, 64, 11, w_cols[5])
    c.rect(0, 52, 64, 12, w_cols[6])

    # Smooth 2-row dither transitions between water layers
    dither_transitions = [
        (6,  7,  w_cols[0], w_cols[1]),
        (13, 14, w_cols[1], w_cols[2]),
        (21, 22, w_cols[2], w_cols[3]),
        (30, 31, w_cols[3], w_cols[4]),
        (40, 41, w_cols[4], w_cols[5]),
        (51, 52, w_cols[5], w_cols[6]),
    ]
    for y0, y1, col_top, col_bot in dither_transitions:
        for x in range(64):
            # Row y0: top color with 25% bottom color
            if (x + y0 * 2) % 4 == 0:
                c.set(x, y0, col_bot)
            # Row y1: bottom color with 25% top color
            if (x + y1 * 2) % 4 == 0:
                c.set(x, y1, col_top)

    # -------------------------------------------------------------
    # 1.2 SUNBEAMS / CAUSTIC LIGHT SHAFTS (Clean diagonal beams)
    # -------------------------------------------------------------
    # Classic, crisp crepuscular light shafts
    # Shaft 1: from top left (x=6..14) angled down-right
    # Shaft 2: from center top (x=24..34) angled down-right
    # Shaft 3: from top right (x=46..52) angled down-right
    beam_hi  = '#1f7998'  # light ray top
    beam_mid = '#176480'  # light ray mid
    beam_low = '#124f67'  # light ray deep

    def draw_sunbeam(x_top, width, max_y):
        for y in range(max_y):
            # slope: advance 1 px right every 2 px down
            xc = x_top + int(y * 0.52)
            col = beam_hi if y < 15 else (beam_mid if y < 30 else beam_low)
            w = width + int(y * 0.08)
            for dx in range(-w // 2, w // 2 + 1):
                x = xc + dx
                if 0 <= x < 64:
                    # Solid center, dithered edges
                    dist = abs(dx)
                    if dist < w // 2:
                        c.set(x, y, col)
                    elif (x + y) % 2 == 0:
                        c.set(x, y, col)

    draw_sunbeam(10, 5, 36)
    draw_sunbeam(27, 6, 44)
    draw_sunbeam(48, 4, 28)

    # =============================================================
    # 2. SEABED / BACKGROUND SAND DUNES
    # =============================================================
    s_rim   = '#b8a876'  # highlighted sand rim
    s_light = '#9c8c5e'  # light sand
    s_mid   = '#756740'  # mid sand body
    s_dark  = '#544829'  # shadow sand
    s_deep  = '#332a15'  # deep sand crevice

    bg_sand = [
        51, 51, 52, 52, 53, 53, 54, 54, 55, 55,
        56, 56, 56, 55, 55, 54, 54, 53, 52, 52,
        51, 51, 50, 50, 50, 51, 51, 52, 52, 53,
        53, 54, 54, 54, 53, 53, 52, 51, 51, 50,
        50, 49, 49, 50, 50, 51, 51, 52, 52, 53,
        53, 54, 54, 55, 55, 55, 56, 56, 56, 57,
        57, 58, 58, 58
    ]
    for x in range(64):
        sy = bg_sand[x]
        c.set(x, sy, s_light)
        for y in range(sy + 1, 64):
            d = y - sy
            if d <= 2:
                c.set(x, y, s_mid)
            elif d <= 5:
                c.set(x, y, s_dark)
            else:
                c.set(x, y, s_deep)

    # =============================================================
    # 3. SUNKEN SHIPWRECK
    # =============================================================
    # Ship Palette:
    w_rim   = '#9e8564'  # sunlit wood highlight
    w_hi    = '#7e6649'  # weathered wood plank light
    w_mid   = '#5c4832'  # main wood body
    w_dark  = '#3e2e1e'  # wood shadow
    w_deep  = '#261b11'  # rotted timber / deep crevice
    w_hole  = '#120c07'  # pitch black interior cavity

    algae_hi = '#4a693d'  # algae/moss highlight
    algae_lo = '#2b3f23'  # algae dark

    # 3.1 Dark Interior Cavity (Hold of the ship)
    for y in range(36, 54):
        xs = max(18, int(15 + (54 - y) * 0.4))
        xe = min(48, int(47 - (54 - y) * 0.3))
        for x in range(xs, xe + 1):
            c.set(x, y, w_hole)

    # 3.2 Distant Back-Side Ribs (silhouetted across the interior hold)
    back_ribs = [
        (22, 35, 43),
        (27, 31, 40),
        (32, 28, 38),
        (37, 26, 35),
        (42, 26, 34),
    ]
    for rx, yt, yb in back_ribs:
        for y in range(yt, yb):
            c.set(rx, y, w_deep)
            c.set(rx + 1, y, w_dark)
        c.set(rx, yt - 1, w_dark)

    # 3.3 Snapped Main Mast and Rigging
    # Angled back to the left: base at (31, 42) up-left to splinter at (18, 15)
    mast_pts = [
        (31, 42), (31, 41), (30, 40), (30, 39),
        (29, 38), (29, 37), (28, 36), (28, 35),
        (27, 34), (27, 33), (26, 32), (26, 31),
        (25, 30), (25, 29), (24, 28), (24, 27),
        (23, 26), (23, 25), (22, 24), (22, 23),
        (21, 22), (21, 21), (20, 20), (20, 19),
        (19, 18), (19, 17), (18, 16)
    ]
    for mx, my in mast_pts:
        c.set(mx, my, w_rim)
        c.set(mx + 1, my, w_hi)
        c.set(mx + 2, my, w_dark)
        if my in (33, 34, 23, 24):
            c.set(mx, my, algae_hi)
            c.set(mx + 1, my, algae_lo)

    # Jagged splintered top
    c.set(18, 15, w_rim)
    c.set(17, 14, w_rim)
    c.set(19, 16, w_mid)

    # Mast Cross-Trees / Crows Nest remnant platform at (23, 27):
    for dx in range(-2, 4):
        c.set(24 + dx, 27, w_rim)
        c.set(24 + dx, 28, w_dark)

    # Broken Yardarm (tilted cross spar)
    yardarm_pts = [
        (14, 31), (15, 31), (16, 30), (17, 30),
        (18, 29), (19, 29), (20, 28), (21, 28),
        (22, 27), (23, 27), (24, 26), (25, 26),
        (26, 25), (27, 25), (28, 24), (29, 24),
        (30, 23), (31, 23), (32, 22), (33, 22)
    ]
    for yx, yy in yardarm_pts:
        c.set(yx, yy, w_rim)
        c.set(yx, yy + 1, w_dark)
    # Algae patches on spar
    c.set(17, 31, algae_hi)
    c.set(17, 32, algae_lo)
    c.set(29, 25, algae_hi)

    # Rotted rope trailing down in a catenary curve
    c_rope = '#4d3d29'
    rope_tip = [(14, 32), (14, 33), (15, 34), (15, 35), (16, 36), (17, 37), (18, 38), (19, 39)]
    for rx, ry in rope_tip:
        c.set(rx, ry, c_rope)

    # 3.4 Foreground Hull Planking
    hull_rows = [
        (35, 47, 52),
        (36, 44, 53),
        (37, 41, 53),
        (38, 36, 53),
        (39, 32, 52),
        (40, 27, 51),
        (41, 23, 50),
        (42, 19, 49),
        (43, 16, 48),
        (44, 15, 47),
        (45, 14, 46),
        (46, 14, 45),
        (47, 14, 44),
        (48, 15, 43),
        (49, 16, 42),
        (50, 18, 40),
        (51, 20, 38),
        (52, 22, 35),
    ]
    for y, xl, xr in hull_rows:
        for x in range(xl, xr + 1):
            is_seam = (y % 3 == 0)
            is_rim  = (x == xr or y == 35 or (y == 36 and x >= 50))
            if is_rim:
                c.set(x, y, w_rim)
            elif is_seam:
                c.set(x, y, w_dark)
            elif (y % 3 == 1):
                c.set(x, y, w_hi if x > 38 else w_mid)
            else:
                c.set(x, y, w_mid if x > 38 else w_dark)

    # 3.5 Rotted Gaps / Holes in Hull Planks
    hull_breaches = [
        (25, 44, 6, 4),
        (33, 42, 7, 5),
        (21, 47, 4, 3),
        (42, 41, 5, 3),
    ]
    for bx, by, bw, bh in hull_breaches:
        for y in range(by, by + bh):
            for x in range(bx, bx + bw):
                c.set(x, y, w_hole)
        # Jagged splintered edges
        c.set(bx - 1, by + 1, w_hi)
        c.set(bx + bw, by + 1, w_rim)
        c.set(bx + bw + 1, by + 2, w_hi)
        c.set(bx + 1, by - 1, w_dark)
        c.set(bx + bw - 1, by + bh, w_dark)

    # Hidden Treasure Inside the Breach (x=27..29, y=45..46)!
    # An ancient treasure chest resting in the dark bilge:
    c.set(27, 46, '#755524') # chest wood
    c.set(28, 46, '#d4a839') # gold chest rim
    c.set(29, 46, '#ffe169') # bright gold coin shine!
    c.set(27, 47, '#4a3414')
    c.set(28, 47, '#755524')
    c.set(29, 47, '#d4a839')

    # Barnacles / sea encrustation on hull
    barnacles = [
        (16, 46), (17, 45), (15, 48), (20, 49),
        (38, 48), (39, 47), (43, 46), (44, 47),
        (49, 41), (50, 40)
    ]
    for bx, by in barnacles:
        c.set(bx, by, '#cbd5e1')
        c.set(bx + 1, by, '#64748b')

    # Algae streaks on hull
    algae_patches = [
        (18, 44), (19, 44), (18, 45),
        (23, 49), (24, 49), (24, 50),
        (30, 48), (31, 48), (31, 49),
        (44, 44), (45, 44), (45, 45),
    ]
    for ax, ay in algae_patches:
        c.set(ax, ay, algae_hi)
        c.set(ax, ay + 1, algae_lo)

    # Porthole (Oxidized iron/bronze frame with dark glass)
    porthole = [
        (47, 37, '#475569'), (48, 37, '#64748b'),
        (46, 38, '#475569'), (47, 38, '#0f172a'), (48, 38, '#0f172a'), (49, 38, '#94a3b8'),
        (46, 39, '#334155'), (47, 39, '#0f172a'), (48, 39, '#0f172a'), (49, 39, '#475569'),
        (47, 40, '#334155'), (48, 40, '#334155'),
    ]
    for px, py, pcol in porthole:
        c.set(px, py, pcol)

    # 3.6 Prominent Curved Ribs (Frames arching up like a skeleton)
    ribs = [
        [(21, 46), (21, 45), (20, 44), (20, 43), (20, 42), (19, 41), (19, 40), (19, 39)],
        [(26, 43), (26, 42), (25, 41), (25, 40), (25, 39), (24, 38), (24, 37), (24, 36), (23, 35), (23, 34)],
        [(31, 41), (31, 40), (31, 39), (30, 38), (30, 37), (30, 36), (29, 35), (29, 34), (29, 33), (28, 32), (28, 31)],
        [(36, 40), (36, 39), (36, 38), (35, 37), (35, 36), (35, 35), (34, 34), (34, 33), (34, 32), (34, 31), (33, 30), (33, 29)],
        [(41, 38), (41, 37), (41, 36), (40, 35), (40, 34), (40, 33), (39, 32), (39, 31), (39, 30), (39, 29), (39, 28)],
        [(46, 36), (46, 35), (45, 34), (45, 33), (45, 32), (44, 31), (44, 30)],
    ]
    for rib in ribs:
        for idx, (rx, ry) in enumerate(rib):
            c.set(rx, ry, w_rim)
            c.set(rx + 1, ry, w_mid)
            c.set(rx + 2, ry, w_dark)
        top_x, top_y = rib[-1]
        c.set(top_x, top_y - 1, w_rim)
        if top_y % 2 == 1:
            c.set(top_x, top_y + 2, algae_hi)
            c.set(top_x + 1, top_y + 2, algae_lo)

    # 3.7 Bow & Shattered Bowsprit
    bow_stem = [(51, 34), (52, 33), (52, 32), (53, 31), (53, 30), (54, 29)]
    for bx, by in bow_stem:
        c.set(bx, by, w_rim)
        c.set(bx + 1, by, w_hi)
        c.set(bx + 2, by, w_dark)

    bowsprit = [(55, 28), (56, 27), (57, 26), (58, 25), (59, 24)]
    for sx, sy in bowsprit:
        c.set(sx, sy, w_rim)
        c.set(sx, sy + 1, w_dark)
    c.set(60, 24, w_rim)
    c.set(59, 23, w_hi)

    # 3.8 Rusty Anchor and Chain
    r_hi   = '#a15835'
    r_mid  = '#6e3820'
    r_dark = '#3d1c0e'

    # Hawsehole on bow at (51, 36)
    c.set(51, 36, '#1a1009')
    c.set(52, 36, '#2d1c12')

    # Interlocking heavy chain links leading to the anchor
    chain_links = [
        # (x, y, w, h)
        (52, 37, 2, 1),
        (53, 38, 1, 2),
        (53, 40, 2, 1),
        (54, 41, 1, 2),
        (54, 43, 2, 1),
        (55, 44, 1, 2),
        (55, 46, 2, 1),
    ]
    for cx, cy, cw, ch in chain_links:
        for dy in range(ch):
            for dx in range(cw):
                c.set(cx + dx, cy + dy, r_hi if (dx + dy) % 2 == 0 else r_mid)

    # Large Rusty Admiralty Anchor lying tilted against the seabed (x=55..61, y=47..56)
    # Ring top
    c.set(56, 47, r_hi)
    c.set(57, 47, r_mid)
    # Stock (wooden/iron cross-bar near top)
    for x in range(54, 60):
        c.set(x, 49, r_hi if x <= 56 else r_mid)
        c.set(x, 50, r_dark)
    # Shank (thick shaft angling down-right)
    anchor_shank = [(57, 48), (57, 49), (58, 50), (58, 51), (59, 52), (59, 53)]
    for sx, sy in anchor_shank:
        c.set(sx, sy, r_hi)
        c.set(sx + 1, sy, r_dark)
    # Crown & Flukes (curved arms of the anchor)
    anchor_flukes = [
        (55, 53, r_hi),
        (56, 54, r_hi),  (57, 54, r_mid),
        (58, 55, r_mid), (59, 55, r_dark),
        (60, 54, r_mid), (61, 53, r_hi)
    ]
    for fx, fy, fcol in anchor_flukes:
        c.set(fx, fy, fcol)

    # =============================================================
    # 4. FOREGROUND SAND DUNES (Burying the hull & anchor)
    # =============================================================
    fg_sand = [
        55, 55, 56, 56, 57, 57, 58, 58, 58, 59,
        59, 60, 60, 59, 58, 57, 56, 55, 54, 53, # burying the stern
        53, 54, 54, 55, 55, 56, 56, 57, 57, 58,
        58, 57, 56, 55, 54, 53, 53, 54, 54, 55, # mound near mid-keel
        55, 56, 56, 57, 57, 58, 58, 58, 57, 56,
        55, 55, 55, 55, 56, 56, 56, 56, 57, 57, # sand under bow
        57, 58, 58, 59
    ]
    for x in range(64):
        sy = fg_sand[x]
        c.set(x, sy, s_rim)
        for y in range(sy + 1, 64):
            d = y - sy
            if d == 1:
                c.set(x, y, s_light)
            elif d <= 3:
                c.set(x, y, s_mid)
            elif d <= 6:
                c.set(x, y, s_dark)
            else:
                c.set(x, y, s_deep)

    # Sand ripple lines
    ripples = [
        (6,  59, 8,  s_rim),
        (22, 57, 7,  s_light),
        (37, 56, 9,  s_rim),
        (44, 60, 11, s_light),
        (16, 61, 14, s_mid),
    ]
    for rx, ry, rw, rcol in ripples:
        for dx in range(rw):
            if 0 <= rx + dx < 64 and ry < 64:
                c.set(rx + dx, ry, rcol)

    # Scattered seashells & pebbles
    shells = [
        (13, 61, '#ffeed4', '#d9b897'),
        (49, 61, '#ffeed4', '#d9b897'),
        (25, 60, '#5a626a', '#333a42'),
        (58, 59, '#5a626a', '#333a42'),
    ]
    for sx, sy, shi, slo in shells:
        c.set(sx, sy, shi)
        c.set(sx + 1, sy, slo)

    # Starfish on the sand at (30, 59)
    c.set(30, 59, '#ff4a36')
    c.set(29, 59, '#d12e1b')
    c.set(31, 59, '#d12e1b')
    c.set(30, 58, '#ff7a6b')
    c.set(30, 60, '#9e1a0b')

    # =============================================================
    # 5. SEAWEED & CORAL ACCENTS
    # =============================================================
    # 5.1 Giant Kelp Forest (Left edge)
    k_bright = '#68d67f'
    k_hi     = '#41ab5a'
    k_mid    = '#257a3e'
    k_dark   = '#144c26'

    kelp_stipe = [
        (4, 15), (4, 16), (3, 17), (3, 18), (3, 19), (4, 20), (4, 21),
        (5, 22), (5, 23), (5, 24), (4, 25), (4, 26), (3, 27), (3, 28),
        (3, 29), (4, 30), (5, 31), (5, 32), (6, 33), (6, 34), (5, 35),
        (4, 36), (3, 37), (2, 38), (2, 39), (3, 40), (4, 41), (5, 42),
        (5, 43), (5, 44), (4, 45), (3, 46), (2, 47), (2, 48), (3, 49),
        (4, 50), (4, 51), (4, 52), (3, 53), (3, 54), (3, 55), (3, 56)
    ]
    for kx, ky in kelp_stipe:
        c.set(kx, ky, k_hi)
        c.set(kx + 1, ky, k_mid)
        c.set(kx + 2, ky, k_dark)

    kelp_blades = [
        (2, 19, [(1, 18), (0, 17)]),
        (2, 27, [(1, 26), (0, 25), (1, 24)]),
        (1, 37, [(0, 36), (0, 35)]),
        (1, 46, [(0, 45), (0, 44)]),
        (6, 23, [(7, 22), (8, 22), (9, 21)]),
        (7, 33, [(8, 32), (9, 32), (10, 31)]),
        (6, 42, [(7, 41), (8, 41), (8, 40)]),
        (5, 50, [(6, 49), (7, 49)]),
    ]
    for bx, by, pts in kelp_blades:
        c.set(bx, by, k_bright)
        for px, py in pts:
            if 0 <= px < 64:
                c.set(px, py, k_hi)
                c.set(px, py + 1, k_dark)

    # Kelp 2 behind stern
    kelp2 = [
        (9, 27), (9, 28), (8, 29), (8, 30), (7, 31), (7, 32),
        (8, 33), (9, 34), (9, 35), (9, 36), (8, 37), (8, 38),
        (7, 39), (7, 40), (8, 41), (8, 42), (9, 43), (9, 44),
        (8, 45), (8, 46), (8, 47), (8, 48), (8, 49), (8, 50)
    ]
    for kx, ky in kelp2:
        c.set(kx, ky, k_mid)
        c.set(kx + 1, ky, k_dark)

    # Kelp on the right
    kelp_right = [
        (62, 32), (61, 33), (61, 34), (62, 35), (63, 36),
        (63, 37), (62, 38), (61, 39), (61, 40), (62, 41),
        (62, 42), (61, 43), (61, 44), (62, 45), (62, 46)
    ]
    for kx, ky in kelp_right:
        if kx < 64:
            c.set(kx, ky, k_bright)
            if kx + 1 < 64:
                c.set(kx + 1, ky, k_mid)

    # 5.2 Corals
    # A) Pink/Magenta Branching Staghorn Coral (x=9..19, y=46..55)
    cp_hi   = '#ffa1be'
    cp_mid  = '#e04875'
    cp_dark = '#9e1e4a'
    cp_deep = '#5e0d29'

    staghorn_coral = [
        (14, 54, cp_deep), (15, 54, cp_deep),
        (14, 53, cp_dark), (15, 53, cp_dark),
        (13, 52, cp_mid),  (14, 52, cp_mid),  (15, 52, cp_dark),
        (12, 51, cp_mid),  (13, 51, cp_mid),
        (11, 50, cp_hi),   (12, 50, cp_mid),
        (10, 49, cp_hi),   (11, 49, cp_mid),
        (10, 48, cp_hi),   (9,  47, cp_hi),
        (11, 47, cp_hi),   (11, 46, cp_hi),
        (14, 51, cp_mid),  (15, 51, cp_dark),
        (14, 50, cp_hi),   (15, 50, cp_mid),
        (14, 49, cp_hi),   (14, 48, cp_hi),
        (16, 52, cp_mid),  (17, 51, cp_mid),
        (17, 50, cp_hi),   (18, 50, cp_mid),
        (18, 49, cp_hi),   (19, 48, cp_hi),
        (16, 49, cp_hi),   (16, 48, cp_hi),
    ]
    for cx, cy, ccol in staghorn_coral:
        c.set(cx, cy, ccol)

    # B) Orange Tube Sponges near bow / anchor (x=46..52, y=45..51)
    co_rim  = '#ffb56b'
    co_hi   = '#f57427'
    co_mid  = '#bd4911'
    co_dark = '#752806'
    co_hole = '#331002'

    tube_sponges = [
        (48, 45, co_hole), (49, 45, co_rim),
        (48, 46, co_hi),   (49, 46, co_rim),  (50, 46, co_mid),
        (48, 47, co_hi),   (49, 47, co_mid),  (50, 47, co_dark),
        (48, 48, co_mid),  (49, 48, co_mid),  (50, 48, co_dark),
        (48, 49, co_dark), (49, 49, co_dark), (50, 49, co_dark),
        (46, 47, co_hole), (47, 47, co_rim),
        (46, 48, co_hi),   (47, 48, co_rim),
        (46, 49, co_mid),  (47, 49, co_mid),
        (46, 50, co_dark), (47, 50, co_dark),
        (51, 48, co_hole), (52, 48, co_rim),
        (51, 49, co_hi),   (52, 49, co_dark),
        (51, 50, co_dark), (52, 50, co_dark),
    ]
    for sx, sy, scol in tube_sponges:
        c.set(sx, sy, scol)

    # C) Vibrant Yellow/Lime Sea Anemone Cluster (x=33..39, y=53..57)
    ca_hi   = '#f7e752'
    ca_mid  = '#c9b828'
    ca_dark = '#7a6e12'

    anemone = [
        (36, 57, ca_dark), (37, 57, ca_dark),
        (35, 56, ca_dark), (36, 56, ca_mid),  (37, 56, ca_mid),  (38, 56, ca_dark),
        (34, 55, ca_mid),  (35, 55, ca_hi),   (36, 55, ca_mid),  (37, 55, ca_hi),   (38, 55, ca_mid),
        (34, 54, ca_hi),   (35, 53, ca_hi),   (36, 54, ca_hi),   (37, 53, ca_hi),   (38, 54, ca_hi),
        (39, 54, ca_mid),  (33, 55, ca_mid),
    ]
    for ax, ay, acol in anemone:
        c.set(ax, ay, acol)

    # D) Purple Sea Fan Coral (x=22..26, y=52..56)
    cpu_hi   = '#d594f7'
    cpu_mid  = '#9c4ec7'
    cpu_dark = '#5e2580'

    sea_fan = [
        (24, 56, cpu_dark), (25, 56, cpu_dark),
        (24, 55, cpu_mid),  (25, 55, cpu_dark),
        (23, 54, cpu_mid),  (24, 54, cpu_mid),  (25, 54, cpu_mid), (26, 54, cpu_dark),
        (22, 53, cpu_hi),   (23, 53, cpu_mid),  (24, 53, cpu_hi),  (25, 53, cpu_mid), (26, 53, cpu_hi),
        (22, 52, cpu_hi),   (24, 52, cpu_hi),   (26, 52, cpu_hi),
    ]
    for px, py, pcol in sea_fan:
        c.set(px, py, pcol)

    # =============================================================
    # 6. DYNAMIC SCHOOL OF FISH SWIMMING PAST
    # =============================================================
    f_white = '#ffffff'
    f_cyan  = '#38eff2'
    f_teal  = '#12a4a8'
    f_dark  = '#095e63'
    f_fin   = '#ffa834'
    f_finhi = '#ffd066'

    # Large fish (5 px wide)
    def draw_large_fish(x, y):
        c.set(x,     y,     f_white)
        c.set(x + 1, y,     f_cyan)
        c.set(x + 2, y,     f_cyan)
        c.set(x + 1, y - 1, f_cyan)
        c.set(x + 1, y + 1, f_teal)
        c.set(x + 2, y + 1, f_dark)
        c.set(x + 3, y,     f_fin)
        c.set(x + 4, y - 1, f_finhi)
        c.set(x + 4, y + 1, f_fin)

    # Medium fish (4 px wide)
    def draw_med_fish(x, y):
        c.set(x,     y,     f_white)
        c.set(x + 1, y,     f_cyan)
        c.set(x + 1, y + 1, f_teal)
        c.set(x + 2, y,     f_cyan)
        c.set(x + 3, y,     f_fin)
        c.set(x + 3, y - 1, f_finhi)

    # Tiny fish (3 px wide)
    def draw_small_fish(x, y):
        c.set(x,     y, f_white)
        c.set(x + 1, y, f_cyan)
        c.set(x + 2, y, f_fin)

    # Beautiful arched school swooping across the upper water
    school = [
        # Large foreground fish
        ('L', 36, 12),  # leading point
        ('L', 42,  9),
        ('L', 43, 15),
        ('L', 49, 11),
        ('L', 50, 17),
        ('L', 56, 13),
        # Medium fish
        ('M', 32, 10),
        ('M', 46,  7),
        ('M', 54,  8),
        ('M', 56, 18),
        ('M', 58, 11),
        # Small distant fish
        ('S', 26,  9),
        ('S', 29,  7),
        ('S', 48,  4),
        ('S', 58,  5),
    ]
    for ftype, fx, fy in school:
        if ftype == 'L':
            draw_large_fish(fx, fy)
        elif ftype == 'M':
            draw_med_fish(fx, fy)
        else:
            draw_small_fish(fx, fy)

    # =============================================================
    # 7. BUBBLE TRAILS & PARTICLES
    # =============================================================
    b_white = '#effdff'
    b_cyan  = '#7ee0f5'
    b_mid   = '#3ba2bd'

    bubble_trail = [
        (32, 40, 2),
        (31, 35, 1),
        (33, 29, 2),
        (32, 23, 1),
        (30, 18, 1),
        (31, 12, 2),
        (29,  6, 1),
        (28,  2, 1),
        (48, 33, 1),
        (49, 27, 1),
        (47, 21, 1),
        (6,  20, 1),
        (5,  13, 1),
    ]
    for bx, by, sz in bubble_trail:
        if sz == 1:
            c.set(bx, by, b_white)
        else:
            c.set(bx,     by,     b_white)
            c.set(bx + 1, by,     b_cyan)
            c.set(bx,     by + 1, b_cyan)
            c.set(bx + 1, by + 1, b_mid)

    marine_snow = [
        (15, 12), (18, 26), (22, 11), (39, 22), (52, 23), (12, 38)
    ]
    for mx, my in marine_snow:
        c.set(mx, my, '#287d9c')

    return c

c = render_scene()
finish(c)
view(c)
