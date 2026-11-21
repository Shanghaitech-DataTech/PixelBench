from pixelbench_api import new_canvas, flatten, finish
import random

random.seed(42)

def draw_scene():
    bg = new_canvas(128, 128, name="bg")
    
    # Sky
    sky_colors = ["#120822", "#1a0b2e", "#241042", "#2d1656"]
    for y in range(128):
        if y < 32: color = sky_colors[0]
        elif y < 64: color = sky_colors[1]
        elif y < 96: color = sky_colors[2]
        else: color = sky_colors[3]
        bg.rect(0, y, 128, 1, color)
        
    # Stars
    for _ in range(15):
        sx = random.randint(0, 128)
        sy = random.randint(0, 60)
        bg.set(sx, sy, "#8c7b9e")
        
    # Moon
    moon_base = "#fffae6"
    moon_crater = "#e6d5a1"
    bg.circle(95, 25, 13, "#fff0b3")
    bg.circle(95, 25, 10, moon_base)
    bg.circle(92, 22, 2, moon_crater)
    bg.circle(97, 27, 3, moon_crater)
    bg.circle(94, 29, 2, moon_crater)

    # Distant trees
    bg_tree_color = "#150824"
    for i in range(16):
        tx = i * 9 + random.randint(-4, 4)
        ty = 70 + random.randint(-5, 5)
        bg.poly([(tx, ty), (tx-5, ty+50), (tx+5, ty+50)], bg_tree_color)

    # Mist layer 1
    mist1 = new_canvas(128, 128, name="mist1")
    for i in range(15):
        mx = random.randint(0, 128)
        my = random.randint(65, 85)
        mr = random.randint(20, 35)
        mist1.ellipse(mx, my, mr, mr//3, "#2a1b3d")

    # Ground
    ground = new_canvas(128, 128, name="ground")
    ground.rect(0, 90, 128, 38, "#1a1625")
    ground.ellipse(64, 90, 80, 10, "#1a1625")
    ground.ellipse(30, 95, 50, 8, "#201a2b")
    ground.ellipse(100, 92, 40, 12, "#171421")
    
    for _ in range(60):
        gx = random.randint(0, 128)
        gy = random.randint(90, 128)
        ground.rect(gx, gy, random.randint(2, 4), 1, "#15121e")
    
    # Cottage
    cottage = new_canvas(128, 128, name="cottage")
    cottage_wall = "#5c5466"
    cottage_wall_dark = "#423c4a"
    cottage_wood = "#3d2817"
    roof_base = "#1f3322"
    roof_mid = "#2b472e"
    roof_light = "#3e6643"
    
    # Walls
    cottage.rect(34, 60, 40, 40, cottage_wall)
    
    # Stone texture
    for _ in range(50):
        sx = random.randint(34, 72)
        sy = random.randint(60, 98)
        cottage.rect(sx, sy, random.randint(2,4), random.randint(1,2), cottage_wall_dark)
        
    # Wood beams
    cottage.rect(34, 60, 40, 2, cottage_wood)
    cottage.rect(34, 98, 40, 2, cottage_wood)
    cottage.rect(34, 60, 2, 40, cottage_wood)
    cottage.rect(72, 60, 2, 40, cottage_wood)
    
    # Door
    cottage.rect(40, 75, 12, 25, cottage_wood)
    cottage.rect(40, 75, 12, 2, "#26190e")
    cottage.rect(40, 85, 12, 2, "#26190e")
    cottage.circle(49, 87, 1, "#111111")
    
    # Window
    window_glow = "#ff9900"
    window_core = "#ffeb99"
    cottage.rect(58, 72, 10, 10, window_glow)
    cottage.rect(60, 74, 6, 6, window_core)
    cottage.rect(62, 72, 2, 10, cottage_wood) # mullion
    cottage.rect(58, 76, 10, 2, cottage_wood) # transom
    
    # Chimney
    cottage.rect(62, 25, 8, 25, cottage_wall_dark)
    cottage.rect(61, 23, 10, 3, cottage_wall)
    
    # Roof
    cottage.poly([(24, 60), (54, 20), (84, 60)], roof_base)
    
    # Roof moss/texture
    for _ in range(150):
        rx = random.randint(24, 84)
        ry = random.randint(20, 60)
        if ry >= 60 - (rx-24)*1.33 and ry >= 60 - (84-rx)*1.33:
            cottage.rect(rx, ry, random.randint(1,3), 1, random.choice([roof_mid, roof_light]))

    # Dormer base
    cottage.rect(49, 38, 10, 12, cottage_wall)
    cottage.poly([(47, 38), (54, 28), (61, 38)], roof_base)
    cottage.rect(50, 35, 2, 1, roof_mid)
    cottage.rect(55, 32, 2, 1, roof_light)
    cottage.rect(51, 42, 6, 6, window_glow)
    cottage.rect(53, 44, 2, 2, window_core)

    # Base grass
    for _ in range(20):
        gx = random.randint(32, 74)
        gy = random.randint(98, 102)
        cottage.rect(gx, gy, 1, random.randint(2, 4), "#1d2b1f")

    # Stone well
    well_x, well_y = 95, 85
    well_color = "#6b6b6b"
    well_dark = "#4d4d4d"
    cottage.ellipse(well_x, well_y-8, 10, 3, "#222222")
    cottage.rect(well_x - 10, well_y - 8, 21, 12, well_color)
    cottage.ellipse(well_x, well_y + 4, 10, 3, well_color)
    cottage.ellipse(well_x, well_y - 8, 10, 3, well_color, fill=False)
    
    for _ in range(15):
        wx = well_x - 10 + random.randint(0, 18)
        wy = well_y - 6 + random.randint(0, 10)
        cottage.rect(wx, wy, 2, 1, well_dark)
        
    # Well winch
    cottage.rect(well_x - 8, well_y - 25, 2, 20, cottage_wood)
    cottage.rect(well_x + 6, well_y - 25, 2, 20, cottage_wood)
    cottage.rect(well_x - 10, well_y - 27, 20, 2, cottage_wood)
    cottage.rect(well_x - 12, well_y - 30, 24, 4, roof_base)
    cottage.rect(well_x - 6, well_y - 18, 12, 3, "#26190e")
    cottage.rect(well_x, well_y - 18, 1, 14, "#d4c3a3")
    cottage.rect(well_x - 2, well_y - 4, 5, 4, cottage_wood)

    # Stone-slab path
    path_color = "#5c6661"
    path_light = "#76827c"
    path_polys = [
        [(45, 101), (53, 101), (51, 105), (43, 105)],
        [(48, 107), (58, 107), (55, 112), (45, 112)],
        [(53, 114), (66, 114), (63, 120), (50, 120)],
        [(62, 122), (78, 122), (75, 128), (58, 128)]
    ]
    for p in path_polys:
        cottage.poly(p, path_color)
        cottage.poly([(p[0][0]+1, p[0][1]+1), (p[1][0]-1, p[1][1]+1), 
                (p[2][0]-1, p[2][1]-1), (p[3][0]+1, p[3][1]-1)], path_light)

    # Light spill layer
    light = new_canvas(128, 128, name="light")
    light.poly([(50, 82), (68, 82), (85, 115), (35, 115)], "#ff990022")

    # Trees layer
    trees = new_canvas(128, 128, name="trees")
    tree_color = "#1f111a"
    tree_highlight = "#2c1a26"
    
    # Left tree
    trees.path("M -10 128 L 25 128 C 20 100 15 80 20 50 C 25 40 30 30 35 20 C 30 18 20 25 10 40 C 0 60 -5 80 -10 100 Z", tree_color)
    trees.path("M 15 70 C 25 60 35 50 45 40 C 40 38 30 48 10 65 Z", tree_color)
    trees.path("M 20 50 C 35 45 45 35 55 25 C 50 22 40 35 25 40 Z", tree_color)
    trees.ellipse(10, 100, 8, 4, tree_color)
    trees.ellipse(25, 98, 6, 3, tree_color)
    # Highlights
    trees.line(10, 128, 5, 80, tree_highlight)
    trees.line(11, 128, 6, 80, tree_highlight)
    trees.line(8, 70, 15, 45, tree_highlight)
    
    # Right tree
    trees.path("M 138 128 L 105 128 C 110 100 115 80 110 50 C 105 40 100 30 95 20 C 100 18 110 25 120 40 C 130 60 135 80 138 100 Z", tree_color)
    trees.path("M 115 70 C 105 60 95 50 85 40 C 90 38 100 48 120 65 Z", tree_color)
    trees.path("M 110 50 C 95 45 85 35 75 25 C 80 22 90 35 105 40 Z", tree_color)
    trees.ellipse(115, 100, 8, 4, tree_color)
    trees.ellipse(100, 98, 6, 3, tree_color)
    # Highlights
    trees.line(115, 128, 122, 80, tree_highlight)
    trees.line(116, 128, 123, 80, tree_highlight)
    trees.line(110, 70, 100, 45, tree_highlight)

    leaf_colors = ["#4a1528", "#5e1c34", "#381628", "#452213", "#2c112e"]
    
    # Cluster leaves left
    for _ in range(7):
        cx = random.randint(-5, 55)
        cy = random.randint(-5, 55)
        for _ in range(15):
            lx = cx + random.randint(-12, 12)
            ly = cy + random.randint(-12, 12)
            trees.circle(lx, ly, random.randint(3, 6), random.choice(leaf_colors))
            
    # Cluster leaves right
    for _ in range(7):
        cx = random.randint(95, 135)
        cy = random.randint(-5, 55)
        for _ in range(15):
            lx = cx + random.randint(-12, 12)
            ly = cy + random.randint(-12, 12)
            if (lx - 95)**2 + (ly - 25)**2 > 20**2: # Keep away from moon
                trees.circle(lx, ly, random.randint(3, 6), random.choice(leaf_colors))

    # Foreground details
    for _ in range(60):
        gx = random.randint(0, 128)
        gy = random.randint(100, 128)
        trees.rect(gx, gy, 1, random.randint(2, 5), "#1d2b1f")

    # Fireflies
    for _ in range(8):
        fx = random.randint(10, 118)
        fy = random.randint(80, 120)
        trees.circle(fx, fy, 1, "#ccff66")
        trees.set(fx, fy, "#ffffff")

    # Smoke layer
    smoke = new_canvas(128, 128, name="smoke")
    smoke.circle(66, 18, 3, "#555555")
    smoke.circle(68, 12, 4, "#444444")
    smoke.circle(72, 5, 5, "#333333")

    # Foreground mist
    mist2 = new_canvas(128, 128, name="mist2")
    for i in range(15):
        mx = random.randint(0, 128)
        my = random.randint(110, 128)
        mr = random.randint(20, 40)
        mist2.ellipse(mx, my, mr, mr//4, "#241733")

    # Composite
    final = flatten([bg, mist1, ground, cottage, light, trees, smoke, mist2])
    
    finish(final)

if __name__ == "__main__":
    draw_scene()
