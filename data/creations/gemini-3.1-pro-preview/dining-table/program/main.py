from pixelbench_api import new_canvas, view, save, finish

def draw_chair_back(c, x, y):
    # Seat
    c.rect(x, y+11, 10, 10, 'cushion_base')
    c.rect(x, y+11, 10, 10, 'outline', fill=False)
    c.rect(x+1, y+12, 8, 8, 'cushion_hl')
    
    # Backrest
    c.rect(x, y, 10, 12, 'table_light')
    c.rect(x, y, 10, 12, 'outline', fill=False)
    # Wood slats
    c.line(x+3, y+2, x+3, y+9, 'table_dark')
    c.line(x+6, y+2, x+6, y+9, 'table_dark')

def draw_chair_front(c, x, y):
    # Seat (visible behind backrest)
    c.rect(x, y-4, 10, 6, 'cushion_base')
    c.rect(x, y-4, 10, 6, 'outline', fill=False)
    c.rect(x+1, y-3, 8, 4, 'cushion_hl')
    
    # Backrest
    c.rect(x, y, 10, 12, 'table_light')
    c.rect(x, y, 10, 12, 'outline', fill=False)
    # Wood slats
    c.line(x+3, y+2, x+3, y+9, 'table_dark')
    c.line(x+6, y+2, x+6, y+9, 'table_dark')
    
    # Legs
    c.rect(x+1, y+11, 2, 4, 'leg_dark')
    c.rect(x+1, y+11, 2, 4, 'outline', fill=False)
    c.rect(x+7, y+11, 2, 4, 'leg_dark')
    c.rect(x+7, y+11, 2, 4, 'outline', fill=False)

def draw_table(c, x, y, w, h):
    # Front legs
    c.rect(x+1, y+h-2, 4, 12, 'leg_dark')
    c.rect(x+1, y+h-2, 4, 12, 'outline', fill=False)
    c.rect(x+w-5, y+h-2, 4, 12, 'leg_dark')
    c.rect(x+w-5, y+h-2, 4, 12, 'outline', fill=False)
    
    # Table top
    c.rect(x, y, w, h, 'table_base')
    c.rect(x, y, w, h, 'outline', fill=False)
    c.rect(x+1, y+1, w-2, h-2, 'table_light')
    
    # Wood grain details
    c.line(x+3, y+4, x+10, y+4, 'table_med')
    c.line(x+5, y+5, x+12, y+5, 'table_med')
    c.line(x+2, y+12, x+8, y+12, 'table_med')
    
    c.line(x+w-12, y+4, x+w-4, y+4, 'table_med')
    c.line(x+w-14, y+5, x+w-6, y+5, 'table_med')
    c.line(x+w-10, y+12, x+w-3, y+12, 'table_med')
    
    # Top highlight
    c.line(x+2, y+2, x+w-3, y+2, 'table_hl')
    
    # Table edge (thickness)
    c.rect(x, y+h-1, w, 6, 'table_dark')
    c.rect(x, y+h-1, w, 6, 'outline', fill=False)
    
    # Table runner
    runner_x = x + 16
    runner_w = 12
    c.rect(runner_x, y+1, runner_w, h-2, 'runner')
    c.rect(runner_x, y+h, runner_w, 4, 'runner_dark')
    c.line(runner_x, y+1, runner_x, y+h+4, 'outline')
    c.line(runner_x+runner_w-1, y+1, runner_x+runner_w-1, y+h+4, 'outline')

def draw_plate(c, x, y, cup_dx):
    # Plate
    c.ellipse(x, y, 3, 1, 'outline')
    c.ellipse(x, y, 2, 1, 'runner')
    # Cup
    c.rect(x+cup_dx, y-2, 3, 3, 'outline')
    c.rect(x+cup_dx+1, y-1, 1, 1, 'bowl_hl')

def draw_fruit_bowl(c, bx, by):
    # Apple
    c.circle(bx-3, by-1, 2, 'outline')
    c.circle(bx-3, by-1, 1, 'apple')
    
    # Orange
    c.circle(bx+3, by, 2, 'outline')
    c.circle(bx+3, by, 1, 'orange')
    
    # Banana
    c.line(bx-2, by-2, bx+2, by-3, 'outline')
    c.line(bx-1, by-2, bx+1, by-2, 'banana')
    
    # Bowl
    c.ellipse(bx, by+2, 6, 2, 'outline')
    c.ellipse(bx, by+2, 5, 1, 'bowl')
    c.line(bx-2, by+2, bx+2, by+2, 'bowl_hl')

def draw():
    c = new_canvas(64, 64)
    
    # Palette setup
    c.color('#221108', 'outline')
    c.color('#5c3616', 'table_dark')
    c.color('#70431d', 'table_med')
    c.color('#8b5a2b', 'table_base')
    c.color('#a06b3c', 'table_light')
    c.color('#d4a373', 'table_hl')
    
    c.color('#8c2121', 'cushion_base')
    c.color('#b33232', 'cushion_hl')
    c.color('#4a2a10', 'leg_dark')
    
    c.color('#e0e0e0', 'runner')
    c.color('#c0c0c0', 'runner_dark')
    
    c.color('#4a76a8', 'bowl')
    c.color('#7aa0c0', 'bowl_hl')
    c.color('#d03030', 'apple')
    c.color('#f09030', 'orange')
    c.color('#fff050', 'banana')
    
    c.color('#3a5a40', 'rug_dark')
    c.color('#588157', 'rug_light')
    c.color('#2d4a32', 'rug_shadow')
    
    # 1. Rug
    c.rect(4, 10, 56, 52, 'outline')
    c.rect(5, 11, 54, 50, 'rug_dark')
    c.rect(7, 13, 50, 46, 'rug_light')
    # Fringe
    for fx in range(6, 58, 2):
        c.set(fx, 9, 'runner')
        c.set(fx, 62, 'runner')
        
    # Rug inner pattern
    c.rect(10, 16, 44, 40, 'rug_dark', fill=False)
    c.rect(12, 18, 40, 36, 'rug_light', fill=False)
    
    # 2. Table shadow on the rug
    c.rect(10, 46, 44, 6, 'rug_shadow')
    
    # 3. Back chairs
    draw_chair_back(c, 16, 12)
    draw_chair_back(c, 38, 12)
    
    # 4. Table
    draw_table(c, 10, 26, 44, 16)
    
    # 5. Plates and Cups
    draw_plate(c, 20, 29, 4)
    draw_plate(c, 44, 29, -6)
    draw_plate(c, 20, 38, 4)
    draw_plate(c, 44, 38, -6)
    
    # 6. Fruit bowl
    draw_fruit_bowl(c, 32, 33)
    
    # 7. Front chairs
    draw_chair_front(c, 16, 48)
    draw_chair_front(c, 38, 48)
    
    finish(c)

if __name__ == "__main__":
    draw()
