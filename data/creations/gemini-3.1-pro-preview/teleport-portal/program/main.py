import math
import random
from pixelbench_api import new_canvas, finish, view

random.seed(42)

def draw_portal():
    c = new_canvas(48, 48)
    
    # Palette
    c.color('#00000000', 'bg')
    c.color('#1a0033', 'darkest_purple')
    c.color('#360066', 'dark_purple')
    c.color('#5c0099', 'purple')
    c.color('#8a00e6', 'light_purple')
    c.color('#b84dff', 'pinkish')
    c.color('#e699ff', 'light_pink')
    c.color('#ffffff', 'white')

    cx, cy = 23.5, 23.5

    for y in range(48):
        for x in range(48):
            dx = x - cx
            dy = y - cy
            r = math.hypot(dx, dy)
            
            if r > 23:
                continue
                
            theta = math.atan2(dy, dx)
            
            # Vortex parameters
            arms = 3
            spiral = (theta * arms - r * 0.6) % (2 * math.pi)
            arm_dist = min(spiral, 2 * math.pi - spiral)
            
            intensity = 1.0 - (r / 22.0)
            intensity -= arm_dist * 0.3
            intensity += random.uniform(-0.1, 0.1)
            
            if intensity > 0.85:
                col = 'white'
            elif intensity > 0.7:
                col = 'light_pink'
            elif intensity > 0.5:
                col = 'pinkish'
            elif intensity > 0.3:
                col = 'light_purple'
            elif intensity > 0.15:
                col = 'purple'
            elif intensity > 0.0:
                col = 'dark_purple'
            elif intensity > -0.2:
                col = 'darkest_purple'
            else:
                col = 'bg'
                
            if r < 3:
                col = 'white'
            elif r < 5 and col in ['bg', 'darkest_purple', 'dark_purple']:
                col = 'light_pink'
                
            # Glowing halo
            if 19 < r <= 23:
                halo_intensity = (r - 19) / 4.0
                if halo_intensity > 0.75:
                    halo_col = 'darkest_purple'
                elif halo_intensity > 0.5:
                    halo_col = 'dark_purple'
                elif halo_intensity > 0.25:
                    halo_col = 'purple'
                else:
                    halo_col = 'light_purple'
                
                if col == 'bg':
                    col = halo_col
                elif col in ['darkest_purple', 'dark_purple'] and halo_col in ['purple', 'light_purple']:
                    col = halo_col

            if col != 'bg':
                c.set(x, y, col)
                
    # Add some floating energy particles
    for _ in range(40):
        r = random.uniform(4, 24)
        theta = random.uniform(0, 2 * math.pi)
        px = int(cx + r * math.cos(theta))
        py = int(cy + r * math.sin(theta))
        if 0 <= px < 48 and 0 <= py < 48:
            if random.random() < 0.3:
                c.set(px, py, 'white')
            elif random.random() < 0.6:
                c.set(px, py, 'light_pink')
            else:
                c.set(px, py, 'pinkish')

    return c

c = draw_portal()
view(c)
finish(c)
