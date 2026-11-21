from pixelbench_api import *

c_in = input_canvas
w, h = c_in.stats()['size']

max_x = [-1] * h
for y in range(h):
    for x in range(w-1, -1, -1):
        if c_in.get(x, y) != 0:
            max_x[y] = x
            break

depth = 80

def draw_house(canvas, projection, offset_x, offset_y):
    # Draw right face (back to front)
    for pz in range(depth, -1, -1):
        for y in range(h):
            px = max_x[y]
            if px == -1: continue
            
            if projection == "45":
                screen_x = offset_x + px + pz
                screen_y = offset_y + y + int(0.5 * px) - int(0.5 * pz)
            else:
                # 90 degree view
                screen_x = offset_x + pz
                screen_y = offset_y + y - int(0.5 * px)
                
            col = c_in.get(px, y)
            
            is_roof = y < 115
            
            if not is_roof:
                # Wall
                if pz < 4 or pz > depth - 4:
                    col = 2 # c1
                elif y > 150:
                    col = 2 # c1
                elif y > 145:
                    col = 9 # c8
                else:
                    col = 10 # c9
                    
                # Window
                if 30 <= pz <= 50 and 125 <= y <= 145:
                    if pz in (30, 31, 49, 50) or y in (125, 126, 144, 145):
                        col = 2
                    elif 39 <= pz <= 40 or 134 <= y <= 135:
                        col = 2
                    else:
                        col = 4
            else:
                # Roof
                if pz < 4 or pz > depth - 4:
                    col = 2 # c1
                elif y < 35 and px < 80:
                    # Wooden beam side
                    col = 1 # c0
                    if pz % 16 < 2 or y % 12 < 2:
                        col = 2 # c1
                else:
                    # Shingle pattern
                    grid_y = y // 6
                    offset_pattern = 4 if (grid_y % 2 == 1) else 0
                    
                    is_edge_z = ((pz + offset_pattern) % 8 < 2)
                    is_edge_y = (y % 6 < 2)
                    
                    if is_edge_z or is_edge_y:
                        col = 3 # c2
                    else:
                        val = (pz * 13 + y * 7) % 10
                        if val < 2:
                            col = 6 # c5
                        elif val < 5:
                            col = 7 # c6
                        else:
                            col = 8 # c7
                            
            canvas.set(screen_x, screen_y, col)
            canvas.set(screen_x, screen_y+1, col)
            canvas.set(screen_x+1, screen_y, col)
            canvas.set(screen_x+1, screen_y+1, col)

    if projection == "45":
        # Draw front face
        for px in range(w):
            for y in range(h):
                col = c_in.get(px, y)
                if col != 0:
                    screen_x = offset_x + px
                    screen_y = offset_y + y + int(0.5 * px)
                    canvas.set(screen_x, screen_y, col)
                    canvas.set(screen_x+1, screen_y, col)
                    canvas.set(screen_x, screen_y+1, col)
                    canvas.set(screen_x+1, screen_y+1, col)

f1 = new_canvas(300, 300, name="frame1")
f2 = new_canvas(300, 300, name="frame2")

draw_house(f1, "45", 50, 60)
draw_house(f2, "90", 110, 140)

finish([f1, f2])
