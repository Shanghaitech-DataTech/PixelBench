import math
from pixelbench_api import new_canvas, view

def render_icon_set():
    c = new_canvas(64, 64)
    
    # ====================================================
    # 1. FIREBALL (0, 0)
    # ====================================================
    buf1 = [[None for _ in range(32)] for _ in range(32)]
    cx1, cy1 = 12.5, 17.5
    
    # 1. Main blazing sphere head
    for y in range(32):
        for x in range(32):
            dx = x - cx1
            dy = y - cy1
            d = math.sqrt(dx*dx + dy*dy)
            if d <= 7.6:
                if d <= 2.2:
                    buf1[y][x] = '#ffffff'  # white-hot core
                elif d <= 4.0:
                    buf1[y][x] = '#ffea38'  # brilliant yellow
                elif d <= 5.8:
                    buf1[y][x] = '#f88c14'  # hot orange
                else:
                    buf1[y][x] = '#d42010'  # crimson flame

    # 2. Flame Tendrils (curving organically towards top-right)
    # Tongue A (Main upper-right trailing flame):
    pts_a = [
        (15, 13, 4.2), (17, 11, 3.6), (19, 9, 3.0), 
        (21, 7, 2.4), (23, 6, 1.8), (25, 5, 1.2), (27, 4, 0.7)
    ]
    for tx, ty, r in pts_a:
        for y in range(32):
            for x in range(32):
                d = math.sqrt((x-tx)**2 + (y-ty)**2)
                if d <= r:
                    tip_dist = math.sqrt((x-27)**2 + (y-4)**2)
                    if d <= r * 0.4 and tip_dist > 5:
                        if buf1[y][x] != '#ffffff': buf1[y][x] = '#ffea38'
                    elif tip_dist > 3:
                        if buf1[y][x] not in ['#ffffff', '#ffea38']: buf1[y][x] = '#f88c14'
                    else:
                        if buf1[y][x] not in ['#ffffff', '#ffea38', '#f88c14']: buf1[y][x] = '#d42010'

    # Tongue B (Top crest licking up):
    pts_b = [
        (11, 11, 3.6), (12, 8, 2.8), (14, 5, 2.0), (16, 3, 1.3), (17, 2, 0.7)
    ]
    for tx, ty, r in pts_b:
        for y in range(32):
            for x in range(32):
                d = math.sqrt((x-tx)**2 + (y-ty)**2)
                if d <= r:
                    tip_dist = math.sqrt((x-17)**2 + (y-2)**2)
                    if d <= r * 0.35 and tip_dist > 4:
                        if buf1[y][x] != '#ffffff': buf1[y][x] = '#ffea38'
                    elif tip_dist > 2:
                        if buf1[y][x] not in ['#ffffff', '#ffea38']: buf1[y][x] = '#f88c14'
                    else:
                        if buf1[y][x] not in ['#ffffff', '#ffea38', '#f88c14']: buf1[y][x] = '#d42010'

    # Tongue C (Middle-right flame tongue):
    pts_c = [
        (17, 16, 3.8), (20, 16, 3.0), (23, 15, 2.2), (26, 14, 1.4), (28, 14, 0.7)
    ]
    for tx, ty, r in pts_c:
        for y in range(32):
            for x in range(32):
                d = math.sqrt((x-tx)**2 + (y-ty)**2)
                if d <= r:
                    tip_dist = math.sqrt((x-28)**2 + (y-14)**2)
                    if tip_dist > 3:
                        if buf1[y][x] not in ['#ffffff', '#ffea38']: buf1[y][x] = '#f88c14'
                    else:
                        if buf1[y][x] not in ['#ffffff', '#ffea38', '#f88c14']: buf1[y][x] = '#d42010'

    # Tongue D (Lower-right flame curl):
    pts_d = [
        (17, 19, 3.2), (20, 20, 2.4), (23, 21, 1.6), (25, 21, 0.8)
    ]
    for tx, ty, r in pts_d:
        for y in range(32):
            for x in range(32):
                d = math.sqrt((x-tx)**2 + (y-ty)**2)
                if d <= r:
                    if buf1[y][x] is None:
                        buf1[y][x] = '#d42010' if d > r*0.5 else '#f88c14'

    # Internal swirling flame tongues (giving fiery texture)
    for (sx, sy) in [(11, 15), (12, 14), (14, 13), (15, 12), (16, 11)]:
        buf1[sy][sx] = '#ffea38'
    for (sx, sy) in [(10, 18), (11, 19), (12, 20), (13, 21)]:
        if buf1[sy][sx] == '#d42010': buf1[sy][sx] = '#f88c14'

    # Floating ember sparks (drifting in the slipstream)
    embers = [
        (28, 2, '#ffea38'), (25, 1, '#f88c14'), 
        (29, 8, '#ffea38'), (28, 9, '#f88c14'),
        (29, 18, '#f88c14'), (26, 18, '#ffea38'),
        (27, 24, '#f88c14'), (7, 12, '#f88c14'),
        (5, 16, '#f88c14')
    ]
    for ex, ey, col in embers:
        buf1[ey][ex] = col

    # Outline for Fireball
    out_c1 = '#1e0508'
    fire_final = [[buf1[y][x] for x in range(32)] for y in range(32)]
    for y in range(32):
        for x in range(32):
            if buf1[y][x] is None:
                has_col = False
                for dy, dx in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < 32 and 0 <= nx < 32 and buf1[ny][nx] is not None:
                        has_col = True
                        break
                if has_col:
                    fire_final[y][x] = out_c1


    # ====================================================
    # 2. ICE SHIELD (32, 0)
    # ====================================================
    buf2 = [[None for _ in range(32)] for _ in range(32)]
    
    # Symmetrical heater shield mask with crisp crown and tapered bottom
    shield_rows = {
        2: [15, 16],
        3: [15, 16],
        4: [8, 9, 14, 15, 16, 17, 22, 23],
        5: [7, 8, 9, 13, 14, 15, 16, 17, 18, 22, 23, 24],
        6: list(range(6, 26)),
        7: list(range(6, 26)),
        8: list(range(5, 27)),
        9: list(range(5, 27)),
        10: list(range(4, 28)),  # shoulder frost spikes
        11: list(range(4, 28)),
        12: list(range(5, 27)),
        13: list(range(5, 27)),
        14: list(range(6, 26)),
        15: list(range(6, 26)),
        16: list(range(7, 25)),
        17: list(range(8, 24)),
        18: list(range(9, 23)),
        19: list(range(10, 22)),
        20: list(range(11, 21)),
        21: list(range(12, 20)),
        22: list(range(12, 20)),
        23: list(range(13, 19)),
        24: list(range(13, 19)),
        25: list(range(14, 18)),
        26: list(range(14, 18)),
        27: [15, 16],
        28: [15, 16],
        29: [15],  # 1px sharp needle tip at the bottom!
    }

    for y, xs in shield_rows.items():
        min_x, max_x = min(xs), max(xs)
        for x in xs:
            if x <= 15:  # Left facet (facing light)
                if x <= min_x + 1 or y <= 6:
                    buf2[y][x] = '#b8f2fc'  # light frost rim
                elif x <= 11:
                    buf2[y][x] = '#5ebef6'  # vibrant cyan
                else:
                    buf2[y][x] = '#2e7ad6'  # crystal blue mid
            else:  # Right facet (in deep shadow)
                if x >= max_x - 1:
                    buf2[y][x] = '#0e2254'  # dark navy rim
                elif x >= 20:
                    buf2[y][x] = '#163878'  # deep sapphire shadow
                else:
                    buf2[y][x] = '#225eb2'  # crystal blue shadow

    # Center vertical ridge
    for y in range(3, 29):
        if y in shield_rows:
            if 15 in shield_rows[y]:
                buf2[y][15] = '#ffffff' if y in [3, 4, 14, 15, 26, 27, 28, 29] else '#d4f8fe'
            if 16 in shield_rows[y]:
                buf2[y][16] = '#163878'

    # Carved crystalline ice snowflake / 8-pointed star in the center (15.5, 14.5)
    center_y = 14
    # Center diamond
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            if abs(dx) + abs(dy) <= 2:
                buf2[center_y+dy][15+dx] = '#ffffff' if dx <= 0 else '#b8f2fc'
    # Cardinal spikes
    for i in range(3, 6):
        buf2[center_y-i][15] = '#ffffff'
        buf2[center_y+i][15] = '#d4f8fe'
        buf2[center_y][15-i] = '#ffffff'
        buf2[center_y][16+i-1] = '#b8f2fc'
    # Diagonal points
    for i in [2, 3]:
        buf2[center_y-i][15-i] = '#ffffff'
        buf2[center_y-i][16+i] = '#b8f2fc'
        buf2[center_y+i][15-i] = '#d4f8fe'
        buf2[center_y+i][16+i] = '#5ebef6'

    # Elegant glint stars (4-pointed mini stars)
    # Top-left shoulder glint:
    buf2[6][4] = '#ffffff'
    buf2[5][4] = '#b8f2fc'
    buf2[7][4] = '#b8f2fc'
    buf2[6][3] = '#b8f2fc'
    buf2[6][5] = '#b8f2fc'

    # Right side frost glint:
    buf2[8][28] = '#ffffff'
    buf2[8][27] = '#b8f2fc'
    buf2[8][29] = '#b8f2fc'

    # Bottom frost particles:
    buf2[25][9] = '#b8f2fc'
    buf2[26][23] = '#b8f2fc'
    buf2[18][3] = '#b8f2fc'

    # Outline for Ice Shield
    out_c2 = '#081024'
    ice_final = [[buf2[y][x] for x in range(32)] for y in range(32)]
    for y in range(32):
        for x in range(32):
            if buf2[y][x] is None:
                has_col = False
                for dy, dx in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < 32 and 0 <= nx < 32 and buf2[ny][nx] is not None:
                        has_col = True
                        break
                if has_col:
                    ice_final[y][x] = out_c2


    # ====================================================
    # 3. HEALING (0, 32)
    # ====================================================
    buf3 = [[None for _ in range(32)] for _ in range(32)]
    
    # 1. Golden halo ring behind cross: center at (15.5, 15.5), radius 8..11
    for y in range(32):
        for x in range(32):
            d = math.sqrt((x-15.5)**2 + (y-15.5)**2)
            if 8.2 <= d <= 11.2:
                # Top half is bright gold, bottom half is rich amber
                if y <= 15:
                    buf3[y][x] = '#fce850'
                else:
                    buf3[y][x] = '#d49818'

    # 2. Solid Holy Cross
    # Vertical arm: x in [12..19], y in [5..26]
    for y in range(5, 27):
        for x in range(12, 20):
            if x <= 13 or y <= 6:
                buf3[y][x] = '#6ee682'  # mint highlight
            elif x >= 18 or y >= 25:
                buf3[y][x] = '#0e5222'  # deep shadow
            elif x <= 15:
                buf3[y][x] = '#2eb84e'  # rich emerald
            else:
                buf3[y][x] = '#188236'  # mid jade

    # Horizontal arm: y in [12..19], x in [5..26]
    for y in range(12, 20):
        for x in range(5, 27):
            if y <= 13 or x <= 6:
                buf3[y][x] = '#6ee682'
            elif y >= 18 or x >= 25:
                buf3[y][x] = '#0e5222'
            elif y <= 15:
                buf3[y][x] = '#2eb84e'
            else:
                buf3[y][x] = '#188236'

    # Flared ends (templar style caps)
    for y in [4, 27]:
        for x in range(11, 21):
            buf3[y][x] = '#6ee682' if y == 4 else '#0e5222'
    for x in [4, 27]:
        for y in range(11, 21):
            buf3[y][x] = '#6ee682' if x == 4 else '#0e5222'

    # Holy central core: radiant jewel in the center of the cross
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            if abs(dx) + abs(dy) <= 2:
                if abs(dx) + abs(dy) == 0:
                    buf3[15][15] = '#ffffff'
                    buf3[15][16] = '#ffffff'
                    buf3[16][15] = '#ffffff'
                    buf3[16][16] = '#ffffff'
                elif abs(dx) + abs(dy) == 1:
                    buf3[15+dy][15+dx] = '#d4fce2'
                else:
                    buf3[15+dy][15+dx] = '#6ee682'

    # Rising magical healing sparkles (4-pointed golden and mint stars)
    stars = [
        (6, 6, '#fce850', '#ffffff'),
        (25, 6, '#fce850', '#ffffff'),
        (6, 25, '#fce850', '#ffffff'),
        (25, 25, '#fce850', '#ffffff'),
        (15, 2, '#6ee682', '#ffffff'),
        (16, 2, '#6ee682', '#ffffff'),
    ]
    for sx, sy, c_arm, c_mid in stars:
        buf3[sy][sx] = c_mid
        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = sy + dy, sx + dx
            if 0 <= ny < 32 and 0 <= nx < 32:
                buf3[ny][nx] = c_arm

    # Tiny curative motes rising:
    buf3[9][10] = '#d4fce2'
    buf3[10][21] = '#d4fce2'
    buf3[22][10] = '#d4fce2'
    buf3[21][21] = '#d4fce2'

    # Outline for Healing
    out_c3 = '#06180a'
    heal_final = [[buf3[y][x] for x in range(32)] for y in range(32)]
    for y in range(32):
        for x in range(32):
            if buf3[y][x] is None:
                has_col = False
                for dy, dx in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < 32 and 0 <= nx < 32 and buf3[ny][nx] is not None:
                        has_col = True
                        break
                if has_col:
                    heal_final[y][x] = out_c3


    # ====================================================
    # 4. LIGHTNING (32, 32)
    # ====================================================
    buf4 = [[None for _ in range(32)] for _ in range(32)]
    
    # Razor-sharp continuous thunderbolt with sharp acute zag turns:
    # Segment 1: from (26, 2) down-left to (17, 11)
    # Shelf 1: horizontal cutback from (17, 11) to (23, 11)
    # Segment 2: from (23, 11) down-left to (11, 20)
    # Shelf 2: horizontal cutback from (11, 20) to (17, 20)
    # Segment 3: from (17, 20) plunging to needle point at (5, 29)
    light_rows = {
        2: [25, 26],
        3: [24, 25, 26],
        4: [23, 24, 25],
        5: [22, 23, 24],
        6: [21, 22, 23],
        7: [17, 18, 19, 20, 21, 22],  # start branch 1
        8: [14, 15, 16, 17, 19, 20, 21],
        9: [12, 13, 14, 18, 19, 20],
        10: [10, 11, 17, 18, 19],
        11: list(range(16, 25)),       # Acute cutback shelf 1 (16..24)
        12: [15, 16, 21, 22, 23, 24],
        13: [20, 21, 22, 23],
        14: [18, 19, 20, 21],
        15: [17, 18, 19, 20],
        16: [15, 16, 17, 18, 22, 23, 24],  # start branch 2
        17: [13, 14, 15, 16, 24, 25, 26],
        18: [12, 13, 14, 15, 26, 27],
        19: [10, 11, 12, 13],
        20: list(range(9, 19)),        # Acute cutback shelf 2 (9..18)
        21: [8, 9, 15, 16, 17],
        22: [14, 15, 16],
        23: [12, 13, 14],
        24: [10, 11, 12],
        25: [8, 9, 10],
        26: [7, 8, 9],
        27: [6, 7, 8],
        28: [5, 6, 7],
        29: [5, 6],
        30: [5],  # Needle tip!
    }

    # Color the lightning:
    for y, xs in light_rows.items():
        min_x, max_x = min(xs), max(xs)
        mid_x = (min_x + max_x) // 2
        for x in xs:
            if x == mid_x or (max_x - min_x >= 4 and abs(x - mid_x) <= 0.6):
                buf4[y][x] = '#ffffff'  # brilliant white spine
            elif x < mid_x:
                buf4[y][x] = '#fffa50'  # electric yellow leading edge
            else:
                buf4[y][x] = '#40d0f4'  # neon cyan plasma trailing edge

    # Secondary electric crackles / sparks:
    sparks = [
        (8, 11, '#ffffff'), (9, 12, '#40d0f4'),
        (28, 6, '#fffa50'), (27, 7, '#ffffff'),
        (28, 17, '#ffffff'), (29, 18, '#40d0f4'),
        (4, 17, '#fffa50'), (5, 18, '#ffffff'),
        (21, 26, '#ffffff'), (22, 27, '#40d0f4'),
        (10, 27, '#fffa50')
    ]
    for sx, sy, col in sparks:
        if 0 <= sx < 32 and 0 <= sy < 32:
            buf4[sy][sx] = col

    # Outline for Lightning
    out_c4 = '#0c0418'
    light_final = [[buf4[y][x] for x in range(32)] for y in range(32)]
    for y in range(32):
        for x in range(32):
            if buf4[y][x] is None:
                has_col = False
                for dy, dx in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < 32 and 0 <= nx < 32 and buf4[ny][nx] is not None:
                        has_col = True
                        break
                if has_col:
                    light_final[y][x] = out_c4

    # Blit all 4 to the main 64x64 canvas
    for y in range(32):
        for x in range(32):
            if fire_final[y][x] is not None:
                c.set(x, y, fire_final[y][x])
            if ice_final[y][x] is not None:
                c.set(32 + x, y, ice_final[y][x])
            if heal_final[y][x] is not None:
                c.set(x, 32 + y, heal_final[y][x])
            if light_final[y][x] is not None:
                c.set(32 + x, 32 + y, light_final[y][x])

    view(c)
    print("Stats:", c.stats_text())
    return c

if __name__ == '__main__':
    render_icon_set()
