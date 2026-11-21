import math
import random
from pixelbench_api import new_canvas, flatten, finish

def draw_gnarled_segment(c, x1, y1, x2, y2, w1, w2, bark_colors, segments=3):
    points = [(x1, y1)]
    for i in range(1, segments):
        t = i / segments
        cx = x1 + (x2 - x1) * t + random.uniform(-w1, w1) * 0.2
        cy = y1 + (y2 - y1) * t + random.uniform(-w1, w1) * 0.2
        points.append((cx, cy))
    points.append((x2, y2))
    
    for i in range(segments):
        px1, py1 = points[i]
        px2, py2 = points[i+1]
        cw1 = w1 + (w2 - w1) * (i / segments)
        cw2 = w1 + (w2 - w1) * ((i + 1) / segments)
        
        if i > 0:
            c.circle(int(px1), int(py1), int(cw1), bark_colors[2])
            
        angle = math.atan2(py2 - py1, px2 - px1)
        length = max(1.0, math.hypot(px2 - px1, py2 - py1))
        dx = math.cos(angle + math.pi/2)
        dy = math.sin(angle + math.pi/2)
        
        p_a = (px1 + dx * cw1, py1 + dy * cw1)
        p_b = (px1 - dx * cw1, py1 - dy * cw1)
        p_c = (px2 - dx * cw2, py2 - dy * cw2)
        p_d = (px2 + dx * cw2, py2 + dy * cw2)
        
        c.poly([p_a, p_b, p_c, p_d], bark_colors[2])
        
        area = int(length * (cw1 + cw2) * 0.8)
        for _ in range(area):
            t_line = random.uniform(0, 1)
            lx = px1 + (px2 - px1) * t_line
            ly = py1 + (py2 - py1) * t_line
            lw = cw1 + (cw2 - cw1) * t_line
            offset = random.uniform(-lw, lw) * 0.95
            
            start_x = lx + dx * offset
            start_y = ly + dy * offset
            
            end_t = min(1.0, t_line + random.uniform(0.1, 0.4))
            lx2 = px1 + (px2 - px1) * end_t
            ly2 = py1 + (py2 - py1) * end_t
            end_x = lx2 + dx * offset
            end_y = ly2 + dy * offset
            
            col = random.choice(bark_colors)
            c.line(int(start_x), int(start_y), int(end_x), int(end_y), col)

def draw_branch_recursive(c, x, y, angle, length, width, depth, bark_colors):
    if depth == 0 or width < 1:
        return
    x2 = x + math.cos(angle) * length
    y2 = y + math.sin(angle) * length
    w2 = width * 0.6
    draw_gnarled_segment(c, x, y, x2, y2, width, w2, bark_colors, segments=2)
    
    num_branches = random.randint(1, 3)
    for _ in range(num_branches):
        new_angle = angle + random.uniform(-0.8, 0.8)
        new_length = length * random.uniform(0.6, 0.9)
        draw_branch_recursive(c, x2, y2, new_angle, new_length, w2, depth - 1, bark_colors)

def draw_vines(c, x, y, width, height, moss_colors):
    for _ in range(int(width * 0.8)):
        vx = x + random.uniform(-width, width)
        vy = y + random.uniform(-5, 15)
        vlen = random.uniform(20, height)
        
        cx, cy = vx, vy
        while cy < vy + vlen:
            nxt_y = cy + random.uniform(3, 8)
            nxt_x = cx + random.uniform(-3, 3)
            c.line(int(cx), int(cy), int(nxt_x), int(nxt_y), random.choice(moss_colors))
            if random.random() < 0.3:
                c.circle(int(cx), int(cy), 1, random.choice(moss_colors))
            cx, cy = nxt_x, nxt_y

def draw_moss(c, x, y, r, moss_colors):
    for _ in range(int(r*r*0.5)):
        mx = x + random.uniform(-r, r)
        my = y + random.uniform(-r, r)
        if (mx-x)**2 + (my-y)**2 <= r*r:
            c.set(int(mx), int(my), random.choice(moss_colors))

def draw_foliage(c, x, y, r, moss_colors):
    for _ in range(int(r*r*1.5)):
        fx = x + random.uniform(-r, r)
        fy = y + random.uniform(-r, r)
        if (fx-x)**2 + (fy-y)**2 <= r*r:
            c.circle(int(fx), int(fy), random.randint(1, 2), random.choice(moss_colors))

def main():
    random.seed(42)
    
    bg_color = "#070d07"
    bg_trees = ["#0a140a", "#0f1c0f", "#142614"]
    god_ray_colors = [(220, 255, 220, 12), (220, 255, 220, 18), (220, 255, 220, 24)]
    
    bark_colors = ["#110a05", "#1c1108", "#2c1c0d", "#3b2613", "#4d341a", "#634524"]
    moss_colors = ["#1b3314", "#284d1e", "#376628", "#498035", "#5ca644"]
    eye_colors = ["#003300", "#008000", "#00ff00", "#ccffcc"]
    
    bg = new_canvas(256, 256, bg_color)
    
    for _ in range(40):
        x = random.randint(-20, 256)
        w = random.randint(10, 40)
        col = random.choice(bg_trees)
        bg.rect(x, 0, w, 256, col)
        
    rays_layer = new_canvas(256, 256)
    for _ in range(10):
        x_top = random.randint(-50, 300)
        w_top = random.randint(20, 80)
        x_bot = x_top + random.randint(-150, 150)
        w_bot = w_top + random.randint(40, 150)
        rays_layer.poly([(x_top, 0), (x_top+w_top, 0), (x_bot+w_bot, 256), (x_bot, 256)], random.choice(god_ray_colors))
        
    treant = new_canvas(256, 256)
    
    draw_branch_recursive(treant, 100, 220, math.pi*0.8, 50, 15, 2, bark_colors)
    draw_branch_recursive(treant, 156, 220, math.pi*0.2, 50, 15, 2, bark_colors)
    
    draw_gnarled_segment(treant, 128, 230, 128, 160, 45, 38, bark_colors, segments=3)
    draw_gnarled_segment(treant, 128, 160, 128, 90, 38, 30, bark_colors, segments=3)
    draw_gnarled_segment(treant, 128, 90, 128, 40, 30, 20, bark_colors, segments=2)
    
    draw_branch_recursive(treant, 128, 40, -math.pi/2, 40, 18, 3, bark_colors)
    draw_branch_recursive(treant, 115, 55, -math.pi*0.75, 35, 15, 3, bark_colors)
    draw_branch_recursive(treant, 141, 55, -math.pi*0.25, 35, 15, 3, bark_colors)
    
    draw_gnarled_segment(treant, 95, 100, 50, 130, 22, 18, bark_colors, segments=2)
    draw_gnarled_segment(treant, 50, 130, 20, 180, 18, 12, bark_colors, segments=2)
    draw_branch_recursive(treant, 20, 180, math.pi*0.6, 25, 8, 2, bark_colors)
    draw_branch_recursive(treant, 20, 180, math.pi*0.8, 20, 8, 2, bark_colors)
    
    draw_gnarled_segment(treant, 161, 100, 206, 130, 22, 18, bark_colors, segments=2)
    draw_gnarled_segment(treant, 206, 130, 236, 180, 18, 12, bark_colors, segments=2)
    draw_branch_recursive(treant, 236, 180, math.pi*0.4, 25, 8, 2, bark_colors)
    draw_branch_recursive(treant, 236, 180, math.pi*0.2, 20, 8, 2, bark_colors)
    
    draw_branch_recursive(treant, 128, 210, math.pi*0.6, 60, 20, 2, bark_colors)
    draw_branch_recursive(treant, 128, 210, math.pi*0.4, 60, 20, 2, bark_colors)
    draw_branch_recursive(treant, 128, 220, math.pi*0.5, 40, 25, 1, bark_colors)
    
    draw_foliage(treant, 128, 40, 30, moss_colors)
    draw_foliage(treant, 115, 55, 25, moss_colors)
    draw_foliage(treant, 141, 55, 25, moss_colors)
    
    draw_vines(treant, 50, 130, 20, 70, moss_colors)
    draw_vines(treant, 206, 130, 20, 70, moss_colors)
    draw_vines(treant, 95, 100, 25, 90, moss_colors)
    draw_vines(treant, 161, 100, 25, 90, moss_colors)
    draw_vines(treant, 128, 60, 40, 120, moss_colors)
    
    for _ in range(25):
        mx = 128 + random.randint(-25, 25)
        my = random.randint(80, 210)
        draw_moss(treant, mx, my, random.randint(8, 15), moss_colors)
        
    treant.ellipse(128, 110, 16, 10, "#050302")
    
    treant.circle(120, 110, 8, "#002200")
    treant.circle(136, 110, 8, "#002200")
    treant.circle(120, 110, 5, "#004400")
    treant.circle(136, 110, 5, "#004400")
    
    treant.poly([(115, 107), (124, 110), (120, 113)], eye_colors[2])
    treant.poly([(117, 108), (123, 110), (120, 112)], eye_colors[3])
    treant.poly([(141, 107), (132, 110), (136, 113)], eye_colors[2])
    treant.poly([(139, 108), (133, 110), (136, 112)], eye_colors[3])
    
    treant.outline("#000000")
    
    fg = new_canvas(256, 256)
    for _ in range(12):
        rx = random.randint(10, 246)
        ry = 256
        draw_branch_recursive(fg, rx, ry, -math.pi/2 + random.uniform(-0.6, 0.6), random.uniform(20, 60), random.uniform(8, 18), 2, bark_colors)
        
    for _ in range(8):
        draw_moss(fg, random.randint(20, 236), 245, random.randint(10, 25), moss_colors)
        
    fg.outline("#000000")
    
    for _ in range(40):
        px = random.randint(20, 236)
        py = random.randint(50, 240)
        fg.set(px, py, random.choice([eye_colors[2], eye_colors[3]]))
        
    result = flatten([bg, rays_layer, treant, fg])
    finish(result)

if __name__ == "__main__":
    main()
