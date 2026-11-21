import math

def draw():
    c = new_canvas(64, 64)
    
    def elevation(x, y):
        z = (63 - y) * 0.18
        dx = x - 32
        z += abs(dx) * 0.12
        z += math.sin(y * 0.08 + x * 0.04) * 1.0
        z += math.sin(y * 0.15 - x * 0.08) * 0.5
        return z + 2
        
    elevations = [[0]*64 for _ in range(64)]
    for y in range(64):
        for x in range(64):
            elevations[y][x] = elevation(x, y)
            
    is_ridge_map = [[False]*64 for _ in range(64)]
    for y in range(64):
        for x in range(64):
            z_xy = math.floor(elevations[y][x])
            is_ridge = False
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 64 and 0 <= ny < 64:
                    if z_xy > math.floor(elevations[ny][nx]):
                        is_ridge = True
                        break
            is_ridge_map[y][x] = is_ridge

    palette = [
        (30, 45, 15),   # 0
        (45, 60, 18),   # 1
        (60, 75, 20),   # 2
        (80, 90, 20),   # 3
        (100, 105, 22), # 4
        (125, 120, 22), # 5
        (150, 135, 22), # 6
        (175, 150, 20), # 7
        (200, 165, 20), # 8
        (220, 180, 22), # 9
        (235, 195, 25), # 10
        (250, 210, 35), # 11
        (255, 220, 50), # 12
        (255, 230, 70), # 13
        (255, 235, 95), # 14
        (250, 240, 120),# 15
        (240, 240, 145),# 16
        (230, 240, 165),# 17
        (220, 235, 185),# 18
        (210, 230, 200) # 19
    ]
    
    for y in range(64):
        for x in range(64):
            if is_ridge_map[y][x]:
                if (x + y) % 2 == 0:
                    color = (100, 70, 30)
                else:
                    color = (80, 60, 25)
                    
                if math.sin(x * 2.1 + y * 3.4) > 0.9:
                    color = (60, 90, 30)
            else:
                l = math.floor(elevations[y][x])
                l = max(0, min(19, l))
                
                noise = math.sin(x * 1.3 + y * 1.7) + math.sin(x * 0.7 - y * 1.1)
                if noise > 1.0:
                    l = min(19, l + 1)
                elif noise < -1.0:
                    l = max(0, l - 1)
                    
                color = palette[l]
            c.set(x, y, color)
            
    # Draw houses
    houses = [
        (12, 6),
        (22, 10),
        (42, 7),
        (52, 11)
    ]
    
    def draw_tree(tx, ty):
        c.set(tx, ty, (40, 80, 30))
        c.set(tx-1, ty+1, (40, 80, 30))
        c.set(tx+1, ty+1, (40, 80, 30))
        c.set(tx, ty+1, (50, 100, 40))
        c.set(tx, ty+2, (30, 60, 20))

    for hx, hy in houses:
        draw_tree(hx - 3, hy + 1)
        draw_tree(hx + 6, hy)
        
        c.rect(hx, hy, 5, 4, (180, 160, 140))
        c.rect(hx, hy, 5, 1, (200, 180, 160))
        c.poly([(hx-1, hy), (hx+2, hy-3), (hx+5, hy)], (140, 60, 40))
        c.rect(hx+2, hy+2, 1, 2, (60, 30, 15))

    # Farmers
    farmers = []
    for y in range(30, 60):
        for x in range(15, 50):
            if is_ridge_map[y][x]:
                if all(math.hypot(x - fx, y - fy) > 20 for fx, fy in farmers):
                    farmers.append((x, y))
                    if len(farmers) == 2:
                        break
        if len(farmers) == 2:
            break
            
    for fx, fy in farmers:
        c.set(fx, fy-2, (240, 220, 120))
        c.line(fx-1, fy-1, fx+1, fy-1, (240, 220, 120))
        c.set(fx, fy, (40, 100, 180))
        c.set(fx, fy+1, (30, 40, 50))
        
    return c

result = draw()
finish(result)
