import random
from pixelbench_api import new_canvas, finish, view

def generate_dirt():
    palette = [
        "#3c2818", # 0
        "#4b331f", # 1
        "#5c4028", # 2
        "#6b4b30", # 3
        "#7a5738", # 4
        "#886341", # 5
        "#966e4a", # 6
        "#a47952", # 7
    ]
    
    random.seed(999)
    grid = [[0]*16 for _ in range(16)]
    
    for y in range(16):
        for x in range(16):
            r = random.random()
            if r < 0.05: v = 1
            elif r < 0.15: v = 2
            elif r < 0.40: v = 3
            elif r < 0.65: v = 4
            elif r < 0.85: v = 5
            elif r < 0.95: v = 6
            else: v = 7
            grid[y][x] = v
            
    # Add grouping
    for _ in range(2):
        new_grid = [[0]*16 for _ in range(16)]
        for y in range(16):
            for x in range(16):
                if random.random() < 0.4:
                    nx = (x + random.choice([-1, 0, 1])) % 16
                    ny = (y + random.choice([-1, 0, 1])) % 16
                    new_grid[y][x] = grid[ny][nx]
                else:
                    new_grid[y][x] = grid[y][x]
        grid = new_grid
        
    # Add shadow under highlights
    for y in range(16):
        for x in range(16):
            if grid[y][x] >= 6:
                if random.random() < 0.8:
                    sy = (y + 1) % 16
                    if grid[sy][x] > 2:
                        grid[sy][x] = max(0, grid[y][x] - 5)

    c = new_canvas(16, 16)
    for y in range(16):
        for x in range(16):
            c.set(x, y, palette[grid[y][x]])
            
    return c

if __name__ == "__main__":
    c = generate_dirt()
    view(c)
    finish(c)
