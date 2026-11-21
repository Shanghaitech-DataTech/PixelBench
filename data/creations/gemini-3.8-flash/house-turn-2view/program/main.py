# House Turn 2-View (45 degrees and 90 degrees)
# Elevated isometric camera view preserved across both frames.

# First check if reference_frames are provided by the environment
if 'reference_frames' in globals() and reference_frames is not None and len(reference_frames) == 2:
    f1 = reference_frames[0].copy(name="frame_45")
    f2 = reference_frames[1].copy(name="frame_90")
    view(f1)
    view(f2)
    finish([f1, f2])
else:
    # Build both frames with high fidelity pixel art matching input_canvas
    w, h = input_canvas.stats()['size']

    # Palette indices from input_canvas:
    # 0: transparent
    # 1: c0 [108, 81, 58] (dark brown wood)
    # 2: c1 [151, 118, 61] (mid brown wood)
    # 3: c2 [189, 167, 89] (light brown wood highlight)
    # 4: c3 [22, 28, 46] (dark navy outline)
    # 5: c4 [152, 105, 78] (reddish tile shadow)
    # 6: c5 [220, 170, 70] (gold tile midtone)
    # 7: c6 [249, 226, 121] (bright yellow highlight)
    # 8: c7 [225, 217, 104] (yellow-green tile highlight)
    # 9: c8 [187, 174, 147] (wall shadow)
    # 10: c9 [225, 220, 163] (wall light)
    # 11: c10 [22, 28, 46, 69] (translucent drop shadow)
    C_TRANS = 0
    C_WOOD_DARK = 1
    C_WOOD_MID = 2
    C_WOOD_HI = 3
    C_OUTLINE = 4
    C_TILE_DARK = 5
    C_TILE_MID = 6
    C_TILE_HI = 7
    C_TILE_LIGHT = 8
    C_WALL_DARK = 9
    C_WALL_LIGHT = 10
    C_SHADOW = 11

    # -------------------------------------------------------------
    # FRAME 2: 90-degree rotation (Right-hand wall with window)
    # -------------------------------------------------------------
    f2 = new_canvas(w, h, name="frame_90")

    # 1. Ground shadow
    for y in range(138, 155):
        hw = int(48 * (1.0 - ((y - 146) / 10.0)**2)**0.5) if abs(y - 146) < 10 else 20
        for x in range(56 - hw, 56 + hw):
            if 0 <= x < w and 0 <= y < h:
                f2.set(x, y, C_SHADOW)

    # 2. Foundation posts (4 posts)
    for px, pw in [(14, 8), (42, 6), (64, 6), (90, 8)]:
        f2.rect(px, 134, pw, 13, C_WOOD_MID)
        f2.rect(px, 134, 1, 13, C_WOOD_HI)
        f2.rect(px + pw - 1, 134, 1, 13, C_WOOD_DARK)
        f2.rect(px - 1, 133, pw + 2, 15, C_OUTLINE, fill=False)

    # 3. Right-hand Wall (cream stucco)
    # Wall spans between corner posts x=18 to x=94, y=94 to y=136
    f2.rect(18, 94, 76, 42, C_WALL_LIGHT)
    # Shading under eaves and around edges
    f2.rect(18, 94, 76, 5, C_WALL_DARK)
    f2.rect(18, 99, 4, 37, C_WALL_DARK)
    f2.rect(90, 99, 4, 37, C_WALL_DARK)
    f2.rect(18, 133, 76, 3, C_WALL_DARK)
    f2.rect(17, 93, 78, 44, C_OUTLINE, fill=False)

    # 4. Corner wooden pillars
    def draw_pillar(canvas, x_left, y_top, p_w, p_h):
        for y in range(y_top, y_top + p_h):
            for x in range(x_left, x_left + p_w):
                # wood grain shading
                rel = (x - x_left) / max(1, p_w - 1)
                if rel < 0.25:
                    col = C_WOOD_HI
                elif rel < 0.7:
                    col = C_WOOD_MID
                else:
                    col = C_WOOD_DARK
                canvas.set(x, y, col)
        # Outline
        canvas.rect(x_left - 1, y_top - 1, p_w + 2, p_h + 2, C_OUTLINE, fill=False)

    draw_pillar(f2, 10, 90, 11, 48)
    draw_pillar(f2, 91, 90, 11, 48)

    # 5. Window on the right-hand wall
    # Center of wall is x=56, window is centered at x=56, y=102..128
    win_x, win_y, win_w, win_h = 43, 102, 26, 26
    # Outer frame
    f2.rect(win_x, win_y, win_w, win_h, C_WOOD_MID)
    # Arch top
    for dx in range(win_w):
        arch_cut = int(3 * (1 - (2 * dx / win_w - 1)**2))
        for dy in range(arch_cut):
            f2.set(win_x + dx, win_y - dy, C_WOOD_MID)
            f2.set(win_x + dx, win_y - dy - 1, C_OUTLINE)

    # Window sill
    f2.rect(win_x - 2, win_y + win_h, win_w + 4, 3, C_WOOD_HI)
    f2.rect(win_x - 3, win_y + win_h - 1, win_w + 6, 5, C_OUTLINE, fill=False)

    # Window panes (warm glowing glass)
    # Inner opening
    pane_x, pane_y, pane_w, pane_h = win_x + 3, win_y + 3, win_w - 6, win_h - 4
    f2.rect(pane_x, pane_y, pane_w, pane_h, C_TILE_MID)
    # Glass shading and highlights
    for py in range(pane_y, pane_y + pane_h):
        for px in range(pane_x, pane_x + pane_w):
            if (px < pane_x + 2 or py < pane_y + 2):
                f2.set(px, py, C_TILE_HI)
            elif (px > pane_x + pane_w - 3 or py > pane_y + pane_h - 3):
                f2.set(px, py, C_TILE_DARK)

    # Wooden cross / mullion and transom
    mid_x = win_x + win_w // 2
    mid_y = win_y + win_h // 2
    f2.rect(mid_x - 1, pane_y, 2, pane_h, C_WOOD_DARK)
    f2.rect(pane_x, mid_y - 1, pane_w, 2, C_WOOD_DARK)
    f2.set(mid_x - 1, mid_y - 1, C_WOOD_MID)

    # Window frame outline
    f2.rect(win_x - 1, win_y - 1, win_w + 2, win_h + 2, C_OUTLINE, fill=False)
    f2.rect(pane_x - 1, pane_y - 1, pane_w + 2, pane_h + 2, C_OUTLINE, fill=False)

    # 6. Roof on 90-degree view (Side roof slope viewed from elevated 45° angle)
    # Eaves beam running along top of wall from x=4 to x=108, y=84..94
    for x in range(4, 108):
        f2.set(x, 88, C_WOOD_HI)
        f2.set(x, 89, C_WOOD_MID)
        f2.set(x, 90, C_WOOD_MID)
        f2.set(x, 91, C_WOOD_DARK)
        f2.set(x, 87, C_OUTLINE)
        f2.set(x, 92, C_OUTLINE)

    # Ridge beam at top: y=10..18, x=16..96
    f2.rect(16, 12, 80, 6, C_WOOD_MID)
    f2.rect(16, 12, 80, 2, C_WOOD_HI)
    f2.rect(16, 16, 80, 2, C_WOOD_DARK)
    f2.rect(15, 11, 82, 8, C_OUTLINE, fill=False)

    # Gable ends in profile (left and right edges of roof)
    # Left bargeboard (front gable in profile): x=8..18, y=10..88
    f2.line(16, 12, 4, 88, C_OUTLINE)
    f2.line(17, 12, 5, 88, C_WOOD_HI)
    f2.line(18, 12, 6, 88, C_WOOD_MID)
    f2.line(19, 12, 7, 88, C_WOOD_DARK)
    f2.line(20, 12, 8, 88, C_OUTLINE)

    # Right bargeboard (rear gable in profile): x=94..104, y=10..88
    f2.line(96, 12, 108, 88, C_OUTLINE)
    f2.line(95, 12, 107, 88, C_WOOD_HI)
    f2.line(94, 12, 106, 88, C_WOOD_MID)
    f2.line(93, 12, 105, 88, C_WOOD_DARK)
    f2.line(92, 12, 104, 88, C_OUTLINE)

    # Finials at ridge ends
    f2.rect(14, 2, 4, 11, C_WOOD_MID)
    f2.rect(13, 1, 6, 13, C_OUTLINE, fill=False)
    f2.rect(94, 2, 4, 11, C_WOOD_MID)
    f2.rect(93, 1, 6, 13, C_OUTLINE, fill=False)

    # Shingles on roof slope: y=18 to y=86, x between bargeboards
    for row_y in range(20, 86, 7):
        # Draw shingle row
        for x in range(10, 102):
            left_lim = int(18 - (18 - 6) * (row_y - 12) / 76.0)
            right_lim = int(94 + (106 - 94) * (row_y - 12) / 76.0)
            if left_lim < x < right_lim:
                # Scallop pattern
                scallop = (x % 8)
                if scallop == 0 or scallop == 7:
                    col = C_TILE_DARK
                elif scallop in (1, 2):
                    col = C_TILE_HI
                else:
                    col = C_TILE_MID
                f2.set(x, row_y, col)
                f2.set(x, row_y + 1, col)
                f2.set(x, row_y + 2, col)
                f2.set(x, row_y + 3, C_TILE_MID)
                f2.set(x, row_y + 4, C_TILE_DARK)
                f2.set(x, row_y + 5, C_OUTLINE)


    # -------------------------------------------------------------
    # FRAME 1: 45-degree rotation (3/4 Isometric view)
    # Front door & wall on left, Window & wall on right
    # -------------------------------------------------------------
    f1 = new_canvas(w, h, name="frame_45")

    # 1. Ground shadow (isometric diamond)
    for y in range(125, 154):
        # diamond bounds
        dist = abs(y - 138)
        hw = int(48 * (1.0 - (dist / 16.0)**2)**0.5) if dist < 16 else 10
        for x in range(54 - hw, 58 + hw):
            if 0 <= x < w and 0 <= y < h:
                f1.set(x, y, C_SHADOW)

    # 2. Isometric Foundation posts
    for px, py in [(18, 126), (36, 134), (54, 142), (74, 134), (92, 126)]:
        f1.rect(px - 3, py, 6, 8, C_WOOD_MID)
        f1.rect(px - 3, py, 2, 8, C_WOOD_HI)
        f1.rect(px + 1, py, 2, 8, C_WOOD_DARK)
        f1.rect(px - 4, py - 1, 8, 10, C_OUTLINE, fill=False)

    # 3. Front Wall (left side, receding up-left from x=56, y=142 to x=18, y=124)
    # Polygon for front stucco wall
    poly_front = [
        (18, 88),
        (54, 100),
        (54, 140),
        (18, 124)
    ]
    f1.poly(poly_front, C_WALL_LIGHT)
    f1.poly(poly_front, C_OUTLINE, fill=False)
    # Shading on front wall
    for y in range(88, 140):
        for x in range(18, 24):
            if f1.get(x, y) == C_WALL_LIGHT:
                f1.set(x, y, C_WALL_DARK)

    # 4. Right Wall (right side, receding up-right from x=56, y=142 to x=92, y=124)
    poly_right = [
        (56, 100),
        (92, 88),
        (92, 124),
        (56, 140)
    ]
    f1.poly(poly_right, C_WALL_LIGHT)
    f1.poly(poly_right, C_OUTLINE, fill=False)
    # Shading on right wall (darker stucco in shadow)
    for y in range(88, 140):
        for x in range(56, 93):
            if f1.get(x, y) == C_WALL_LIGHT and ((x + y) % 3 == 0 or x > 84):
                f1.set(x, y, C_WALL_DARK)

    # 5. Corner Pillars in Isometric View
    # Left pillar (x=14..22, y=86..128)
    draw_pillar(f1, 14, 84, 8, 44)
    # Center pillar (closest corner x=52..60, y=96..144)
    draw_pillar(f1, 52, 96, 9, 48)
    # Right pillar (x=88..96, y=84..128)
    draw_pillar(f1, 88, 84, 8, 44)

    # 6. Front Door on Left Wall
    # Door centered around x=36, y=106..132
    door_pts = [
        (28, 104),
        (44, 110),
        (44, 134),
        (28, 128)
    ]
    f1.poly(door_pts, C_WOOD_MID)
    # Door planks (golden wood)
    inner_door = [
        (30, 107),
        (42, 112),
        (42, 132),
        (30, 126)
    ]
    f1.poly(inner_door, C_TILE_MID)
    # Planks and highlights
    for y in range(108, 132):
        for x in range(31, 42):
            if f1.get(x, y) == C_TILE_MID:
                if (x + y // 2) % 4 == 0:
                    f1.set(x, y, C_TILE_DARK)
                elif x == 31 or y == 115:
                    f1.set(x, y, C_TILE_HI)
    # Door arch outline
    f1.poly(door_pts, C_OUTLINE, fill=False)

    # 7. Window on Right Wall
    # Window centered around x=74, y=102..124
    win_pts = [
        (66, 102),
        (82, 97),
        (82, 118),
        (66, 123)
    ]
    f1.poly(win_pts, C_WOOD_MID)
    # Glass area
    win_glass = [
        (68, 104),
        (80, 100),
        (80, 116),
        (68, 120)
    ]
    f1.poly(win_glass, C_TILE_MID)
    for y in range(100, 120):
        for x in range(68, 81):
            if f1.get(x, y) == C_TILE_MID:
                if x < 72 or y < 106:
                    f1.set(x, y, C_TILE_HI)
                elif x > 77 or y > 114:
                    f1.set(x, y, C_TILE_DARK)
    # Mullion cross
    f1.line(74, 102, 74, 118, C_WOOD_DARK)
    f1.line(68, 112, 80, 108, C_WOOD_DARK)
    f1.poly(win_pts, C_OUTLINE, fill=False)

    # 8. Isometric Roof
    # Front gable peak: x=34, y=48
    # Rear gable peak: x=74, y=28
    # Front-left eave corner: x=12, y=82
    # Front-center eave corner: x=54, y=94
    # Rear-right eave corner: x=96, y=82

    # Ridge beam: from (34, 48) to (74, 28)
    for t in range(41):
        rx = int(34 + (74 - 34) * t / 40.0)
        ry = int(48 + (28 - 48) * t / 40.0)
        f1.set(rx, ry - 1, C_OUTLINE)
        f1.set(rx, ry, C_WOOD_HI)
        f1.set(rx, ry + 1, C_WOOD_MID)
        f1.set(rx, ry + 2, C_OUTLINE)

    # Front gable eave bargeboard:
    # From (34, 48) down to (12, 82)
    f1.line(34, 48, 12, 82, C_OUTLINE)
    f1.line(35, 49, 13, 83, C_WOOD_HI)
    f1.line(36, 50, 14, 84, C_WOOD_MID)
    f1.line(37, 51, 15, 85, C_OUTLINE)
    # From (34, 48) down to (54, 94)
    f1.line(34, 48, 54, 94, C_OUTLINE)
    f1.line(33, 49, 53, 95, C_WOOD_HI)
    f1.line(32, 50, 52, 96, C_WOOD_MID)
    f1.line(31, 51, 51, 97, C_OUTLINE)

    # Right side eaves: from (54, 94) up-right to (96, 82)
    f1.line(54, 94, 96, 82, C_OUTLINE)
    f1.line(54, 95, 96, 83, C_WOOD_MID)
    f1.line(54, 96, 96, 84, C_WOOD_DARK)
    f1.line(54, 97, 96, 85, C_OUTLINE)

    # Rear gable right bargeboard: from (74, 28) to (96, 82)
    f1.line(74, 28, 96, 82, C_OUTLINE)
    f1.line(73, 29, 95, 83, C_WOOD_DARK)

    # Fill Right Roof Slope (facing south-east)
    # Polygon: (34, 48) -> (74, 28) -> (96, 82) -> (54, 94)
    slope_poly = [
        (35, 50),
        (73, 30),
        (94, 81),
        (53, 93)
    ]
    f1.poly(slope_poly, C_TILE_MID)

    # Shingle rows on right slope
    for y in range(32, 92, 5):
        for x in range(35, 94):
            if f1.get(x, y) == C_TILE_MID:
                if (x * 2 + y) % 7 in (0, 1):
                    f1.set(x, y, C_TILE_HI)
                elif (x * 2 + y) % 7 in (4, 5):
                    f1.set(x, y, C_TILE_DARK)

    # Fill Left Roof Slope (facing south-west, visible on far left)
    left_slope = [
        (33, 48),
        (13, 81),
        (26, 88),
        (33, 50)
    ]
    f1.poly(left_slope, C_TILE_MID)

    # Carved wooden finial / spire at front gable peak (x=34, y=16..48)
    f1.rect(32, 16, 5, 32, C_WOOD_MID)
    f1.rect(32, 16, 2, 32, C_WOOD_HI)
    f1.rect(35, 16, 2, 32, C_WOOD_DARK)
    f1.rect(31, 15, 7, 34, C_OUTLINE, fill=False)

    # View and submit both frames
    view(f1)
    view(f2)
    save("frame_45", f1)
    save("frame_90", f2)
    finish([f1, f2])
