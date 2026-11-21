import math
import random
from pixelbench_api import new_canvas, finish

def draw_burst(c, cx, cy, r_inner, r_outer, points, color, angle_offset=0):
    poly_points = []
    for i in range(points * 2):
        angle = angle_offset + i * math.pi / points
        r = r_outer if i % 2 == 0 else r_inner
        x = cx + math.cos(angle) * r
        y = cy + math.sin(angle) * r
        poly_points.append((int(x), int(y)))
    c.poly(poly_points, color)

def draw_explosion():
    c = new_canvas(64, 64)
    
    # Palette
    white = c.color("#ffffff")
    light_yellow = c.color("#fff59d")
    yellow = c.color("#ffeb3b")
    orange = c.color("#ff9800")
    red = c.color("#f44336")
    dark_red = c.color("#b71c1c")
    
    random.seed(42)
    
    # ---------------------------------------------------------
    # Frame 1: Bright yellow fireball at center of left half (16, 32)
    # ---------------------------------------------------------
    draw_burst(c, 16, 32, 7, 12, 7, orange, 0)
    draw_burst(c, 16, 32, 5, 9, 7, yellow, 0.2)
    draw_burst(c, 16, 32, 3, 6, 7, light_yellow, 0.4)
    c.circle(16, 32, 2, white)
    
    # Organic fiery blobs for Frame 1
    for angle in range(0, 360, 45):
        rad = math.radians(angle + 20)
        x = 16 + int(math.cos(rad) * 9)
        y = 32 + int(math.sin(rad) * 9)
        c.circle(x, y, 1, orange)
        
        x2 = 16 + int(math.cos(rad + 10) * 7)
        y2 = 32 + int(math.sin(rad + 10) * 7)
        c.circle(x2, y2, 1, yellow)
        
    # Extra particles
    particles1 = [
        (10, -8), (-9, 10), (2, 13), (-11, -2), (12, 4), (-3, -12)
    ]
    for dx, dy in particles1:
        c.set(16 + dx, 32 + dy, random.choice([orange, yellow]))
        
    # ---------------------------------------------------------
    # Frame 2: Expanding orange-red blast with sparks at center of right half (48, 32)
    # ---------------------------------------------------------
    draw_burst(c, 48, 32, 9, 14, 9, dark_red, 0.1)
    draw_burst(c, 48, 32, 7, 11, 9, red, 0.3)
    draw_burst(c, 48, 32, 4, 8, 9, orange, 0.5)
    
    # Hollow center
    c.circle(48, 32, 4, dark_red)
    c.circle(48, 32, 2, "transparent")
    
    # Sparks for Frame 2
    for i in range(16):
        angle = i * (2 * math.pi / 16) + random.uniform(-0.2, 0.2)
        r = random.uniform(12, 16)
        sx = 48 + int(math.cos(angle) * r)
        sy = 32 + int(math.sin(angle) * r)
        if 32 <= sx < 64 and 0 <= sy < 64:
            c.set(sx, sy, white)
            tx = 48 + int(math.cos(angle) * (r - 1))
            ty = 32 + int(math.sin(angle) * (r - 1))
            c.set(tx, ty, yellow)
            tx2 = 48 + int(math.cos(angle) * (r - 2))
            ty2 = 32 + int(math.sin(angle) * (r - 2))
            c.set(tx2, ty2, orange)
            
    # Frame 2 smoke puffs
    smoke = [
        (8, 8, 2), (-9, -7, 2), (7, -9, 1), (-8, 6, 1), (10, -2, 1), (-10, 2, 2)
    ]
    for dx, dy, r in smoke:
        c.circle(48 + dx, 32 + dy, r, dark_red)
        
    # Some inner debris
    for i in range(5):
        angle = random.uniform(0, 2 * math.pi)
        r = random.uniform(5, 9)
        x = 48 + int(math.cos(angle) * r)
        y = 32 + int(math.sin(angle) * r)
        c.set(x, y, dark_red)

    finish(c)

if __name__ == "__main__":
    draw_explosion()
