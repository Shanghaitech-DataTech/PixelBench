import math
import random
from pixelbench_api import *

def project(x, y, z):
    if z <= 0: z = 0.1
    scale = 100 / z
    px = 64 + x * scale
    py = 48 + y * scale
    return px, py

def draw_poly(c, pts, color):
    proj_pts = []
    for (x, y, z) in pts:
        px, py = project(x, y, z)
        proj_pts.append((int(px), int(py)))
    c.poly(proj_pts, color)

def draw_line(c, p1, p2, color):
    px1, py1 = project(*p1)
    px2, py2 = project(*p2)
    c.line(int(px1), int(py1), int(px2), int(py2), color)

def main():
    bg = new_canvas(128, 128, name="bg")
    
    c_ceil = bg.color("#e0e8f0")
    c_ceil_light = bg.color("#ffffff")
    c_wall = bg.color("#d0e0e8")
    c_wall_dark = bg.color("#b0c8d0")
    c_floor = bg.color("#c0d8e0")
    c_grid = bg.color("#a0c0d0")
    c_pool_wall = bg.color("#90b8c8")
    c_pool_bottom = bg.color("#70a8b8")
    
    # Room boundaries
    draw_poly(bg, [(-40, -30, 200), (40, -30, 200), (40, 20, 200), (-40, 20, 200)], c_wall_dark)
    draw_poly(bg, [(-40, -30, 20), (40, -30, 20), (40, -30, 200), (-40, -30, 200)], c_ceil)
    draw_poly(bg, [(-40, -30, 20), (-40, -30, 200), (-40, 20, 200), (-40, 20, 20)], c_wall)
    draw_poly(bg, [(40, -30, 20), (40, -30, 200), (40, 20, 200), (40, 20, 20)], c_wall)

    # Base floor and grid
    draw_poly(bg, [(-40, 20, 20), (40, 20, 20), (40, 20, 200), (-40, 20, 200)], c_floor)
    for x in range(-40, 41, 4):
        draw_line(bg, (x, 20, 20), (x, 20, 200), c_grid)
    for z in range(20, 201, 8):
        draw_line(bg, (-40, 20, z), (40, 20, z), c_grid)

    # Ceiling lights
    for z in range(40, 200, 40):
        draw_poly(bg, [(-15, -30, z), (15, -30, z), (15, -30, z+10), (-15, -30, z+10)], c_ceil_light)

    # Left wall grid
    for y in range(-30, 21, 4):
        draw_line(bg, (-40, y, 20), (-40, y, 200), c_grid)
    for z in range(20, 201, 8):
        draw_line(bg, (-40, -30, z), (-40, 20, z), c_grid)

    # Right wall grid
    for y in range(-30, 21, 4):
        draw_line(bg, (40, y, 20), (40, y, 200), c_grid)
    for z in range(20, 201, 8):
        draw_line(bg, (40, -30, z), (40, 20, z), c_grid)
        
    # Back wall grid
    for x in range(-40, 41, 4):
        draw_line(bg, (x, -30, 200), (x, 20, 200), c_grid)
    for y in range(-30, 21, 4):
        draw_line(bg, (-40, y, 200), (40, y, 200), c_grid)

    # Pool hole
    draw_poly(bg, [(-20, 28, 40), (20, 28, 40), (20, 28, 180), (-20, 28, 180)], c_pool_bottom)
    draw_poly(bg, [(-20, 20, 180), (20, 20, 180), (20, 28, 180), (-20, 28, 180)], c_pool_wall)
    draw_poly(bg, [(-20, 20, 40), (-20, 20, 180), (-20, 28, 180), (-20, 28, 40)], c_pool_wall)
    draw_poly(bg, [(20, 20, 40), (20, 20, 180), (20, 28, 180), (20, 28, 40)], c_pool_wall)
    
    for x in range(-20, 21, 4):
        draw_line(bg, (x, 28, 40), (x, 28, 180), c_grid)
    for z in range(40, 181, 8):
        draw_line(bg, (-20, 28, z), (20, 28, z), c_grid)

    # Columns
    for z in [180, 140, 100, 60]:
        # Left column
        draw_poly(bg, [(-32, -30, z), (-28, -30, z), (-28, 20, z), (-32, 20, z)], c_wall_dark) # Front
        draw_poly(bg, [(-28, -30, z), (-28, -30, z+8), (-28, 20, z+8), (-28, 20, z)], c_wall) # Side
        for y in range(-30, 21, 4):
            draw_line(bg, (-32, y, z), (-28, y, z), c_grid)
            draw_line(bg, (-28, y, z), (-28, y, z+8), c_grid)
        for cx in range(-32, -27, 2):
            draw_line(bg, (cx, -30, z), (cx, 20, z), c_grid)
        for cz in range(z, z+9, 4):
            draw_line(bg, (-28, -30, cz), (-28, 20, cz), c_grid)
        
        # Right column
        draw_poly(bg, [(28, -30, z), (32, -30, z), (32, 20, z), (28, 20, z)], c_wall_dark) # Front
        draw_poly(bg, [(28, -30, z), (28, -30, z+8), (28, 20, z+8), (28, 20, z)], c_wall) # Side
        for y in range(-30, 21, 4):
            draw_line(bg, (28, y, z), (32, y, z), c_grid)
            draw_line(bg, (28, y, z), (28, y, z+8), c_grid)
        for cx in range(28, 33, 2):
            draw_line(bg, (cx, -30, z), (cx, 20, z), c_grid)
        for cz in range(z, z+9, 4):
            draw_line(bg, (28, -30, cz), (28, 20, cz), c_grid)

    # Girl's legs under water
    lx, ly = project(-1.5, 23, 100)
    bg.line(int(lx), int(ly), int(lx), int(ly+4), bg.color("#ffccaa"))
    rx, ry = project(1.5, 23, 100)
    bg.line(int(rx), int(ry), int(rx), int(ry+4), bg.color("#ffccaa"))

    # Water layer
    water_layer = new_canvas(128, 128, name="water")
    c_water_fill = water_layer.color((140, 210, 235, 200))
    draw_poly(water_layer, [(-20, 22, 40), (20, 22, 40), (20, 22, 180), (-20, 22, 180)], c_water_fill)
    
    # Ring shadow
    c_water_shadow = water_layer.color((100, 160, 180, 200))
    px_ring, py_ring = project(0, 22, 100)
    water_layer.ellipse(int(px_ring), int(py_ring)+2, 6, 2, c_water_shadow)

    c_ripple = water_layer.color((255, 255, 255, 120))
    random.seed(42)
    for _ in range(50):
        rx_pos = random.uniform(-18, 18)
        rz = random.uniform(45, 175)
        rw = random.uniform(2, 6)
        px1, py1 = project(rx_pos, 22, rz)
        px2, py2 = project(rx_pos+rw, 22, rz)
        water_layer.line(int(px1), int(py1), int(px2), int(py2), c_ripple)

    # FG Floor (occludes pool and water)
    fg = new_canvas(128, 128, name="fg")
    c_floor_fg = fg.color("#c0d8e0")
    c_grid_fg = fg.color("#a0c0d0")
    draw_poly(fg, [(-40, 20, 20), (40, 20, 20), (40, 20, 40), (-40, 20, 40)], c_floor_fg)
    for x in range(-40, 41, 4):
        draw_line(fg, (x, 20, 20), (x, 20, 40), c_grid_fg)
    for z in range(20, 41, 8):
        draw_line(fg, (-40, 20, z), (40, 20, z), c_grid_fg)

    # Sprites layer
    sprites = new_canvas(128, 128, name="sprites")
    
    # Water slide
    slide_color = sprites.color("#ffffff")
    slide_shadow = sprites.color("#d0d0d0")
    for i in range(100):
        t = i / 100.0
        x = 30 * (1 - t) + 0 * t + 15 * math.sin(t * math.pi)
        y = -10 * (1 - t) + 22 * t
        z = 180 * (1 - t) + 120 * t
        px, py = project(x, y, z)
        scale = 100 / z
        r = 8 * scale
        sprites.circle(int(px), int(py), int(r), slide_shadow)
        sprites.circle(int(px), int(py-r*0.2), int(r*0.8), slide_color)
        
    for t_val in [0.2, 0.5, 0.8]:
        sx = 30 * (1 - t_val) + 15 * math.sin(t_val * math.pi)
        sy = -10 * (1 - t_val) + 22 * t_val
        sz = 180 * (1 - t_val) + 120 * t_val
        px1, py1 = project(sx, sy, sz)
        px2, py2 = project(sx, 20, sz)
        sprites.line(int(px1), int(py1), int(px2), int(py2), sprites.color("#a0a0a0"))
        sprites.line(int(px1)+1, int(py1), int(px2)+1, int(py2), sprites.color("#c0c0c0"))

    # Girl and ring
    ring_color = sprites.color("#ffdd00")
    skin = sprites.color("#ffccaa")
    hair = sprites.color("#302010")
    swimsuit = sprites.color("#ff4040")

    sprites.ellipse(int(px_ring), int(py_ring), 6, 2, ring_color)
    sprites.ellipse(int(px_ring), int(py_ring), 4, 1, sprites.color("transparent"))
    sprites.rect(int(px_ring)-2, int(py_ring)-4, 5, 5, swimsuit)
    sprites.circle(int(px_ring), int(py_ring)-6, 2, hair)
    sprites.line(int(px_ring)-2, int(py_ring)-3, int(px_ring)-4, int(py_ring)-1, skin)
    sprites.line(int(px_ring)+2, int(py_ring)-3, int(px_ring)+4, int(py_ring)-1, skin)

    final = flatten([bg, water_layer, fg, sprites])
    finish(final)

if __name__ == "__main__":
    main()
