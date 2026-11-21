from pixelbench_api import *

c = new_canvas(32, 32, name="carpet")

palette = {
    "darkred": "#5c1e19",
    "red": "#8a251d",
    "orange": "#c9592a",
    "gold": "#e8a035",
    "cream": "#f2dec4",
    "green": "#4c6b35",
    "dark": "#2e110d"
}

for name, hexcode in palette.items():
    c.color(hexcode, name)

def set_wrap(x, y, color):
    c.set(x % 32, y % 32, color)

centers_main = [(0,0), (16,16)]
centers_edge = [(16,0), (0,16)]
centers_small = [(8,8), (24,8), (8,24), (24,24)]

centers = centers_main + centers_edge + centers_small

for y in range(32):
    for x in range(32):
        min_d = 100
        for cx, cy in centers:
            dx = min(abs(x - cx), 32 - abs(x - cx))
            dy = min(abs(y - cy), 32 - abs(y - cy))
            d = dx + dy
            if d < min_d:
                min_d = d
        
        if min_d == 8:
            if (x % 16 == 0 and y % 16 == 8) or (x % 16 == 8 and y % 16 == 0):
                c.set(x, y, "cream")
            else:
                c.set(x, y, "dark")

def draw_main_diamond(cx, cy):
    for dy in range(-7, 8):
        for dx in range(-7, 8):
            r = abs(dx) + abs(dy)
            if r > 7: continue
            
            color = "red"
            if r == 7:
                color = "gold"
            elif r == 6:
                color = "dark"
            else:
                if dx == 0 and dy == 0:
                    color = "cream"
                elif r == 1:
                    color = "orange"
                elif (dx == 0 and abs(dy) >= 2 and abs(dy) <= 4) or (dy == 0 and abs(dx) >= 2 and abs(dx) <= 4):
                    color = "cream"
                elif abs(dx) == 2 and abs(dy) == 2:
                    color = "green"
                elif r == 4 and abs(dx) > 0 and abs(dy) > 0:
                    color = "dark"
                
            set_wrap(cx + dx, cy + dy, color)

def draw_edge_diamond(cx, cy):
    for dy in range(-7, 8):
        for dx in range(-7, 8):
            r = abs(dx) + abs(dy)
            if r > 7: continue
            
            if r == 7:
                color = "cream"
            elif r == 6:
                color = "dark"
            else:
                if dx == 0 or dy == 0:
                    color = "darkred"
                elif abs(dx) == abs(dy):
                    color = "gold"
                else:
                    color = "green"
            
            if r <= 1:
                color = "dark"
            elif r == 2 and abs(dx) == 1 and abs(dy) == 1:
                color = "cream"
                
            set_wrap(cx + dx, cy + dy, color)

def draw_small_diamond(cx, cy):
    for dy in range(-7, 8):
        for dx in range(-7, 8):
            r = abs(dx) + abs(dy)
            if r > 7: continue
            
            if r == 7:
                color = "orange"
            elif r == 6:
                color = "dark"
            elif r == 5 or r == 4:
                color = "green"
            elif r == 3:
                color = "dark"
            else:
                color = "darkred"
                
            if r <= 2:
                if dx == 0 and dy == 0:
                    color = "cream"
                elif dx == 0 or dy == 0:
                    color = "orange"
                else:
                    color = "dark"
            
            set_wrap(cx + dx, cy + dy, color)

for cx, cy in centers_main:
    draw_main_diamond(cx, cy)
    
for cx, cy in centers_edge:
    draw_edge_diamond(cx, cy)
    
for cx, cy in centers_small:
    draw_small_diamond(cx, cy)

finish(c)
