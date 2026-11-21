from pixelbench_api import *

c = new_canvas(64, 64)

outline = "#303030"
bg = "#1A1A1A"

battery_w = 12
battery_h = 24
y = 21

fills = [
    ("#4CAF50", "#81C784", "#388E3C", 22), 
    ("#FFB300", "#FFCA28", "#FF8F00", 13), 
    ("#E53935", "#EF5350", "#C62828", 5),  
    ("#4CAF50", "#81C784", "#388E3C", 11)  
]

bolt_pattern = [
    "  ##  ",
    " ###  ",
    " ###  ",
    "###   ",
    "######",
    "  ### ",
    "  ### ",
    "  ##  ",
    "  ##  ",
    "   #  "
]

for i in range(4):
    x = 2 + i * 16
    
    c.rect(x+3, y-3, 6, 3, outline)
    c.rect(x+4, y-2, 4, 2, "#9E9E9E")
    c.rect(x+4, y-2, 1, 2, "#E0E0E0") 
    
    c.rect(x, y, battery_w, battery_h, outline)
    
    c.set(x, y, None)
    c.set(x+11, y, None)
    c.set(x, y+23, None)
    c.set(x+11, y+23, None)
    
    c.rect(x+1, y+1, 10, 22, bg)
    c.rect(x+1, y+1, 10, 2, "#0A0A0A") 
    
    base, high, shad, fill_h = fills[i]
    y_fill = y + 1 + 22 - fill_h
    
    c.rect(x+1, y_fill, 10, fill_h, base)
    c.rect(x+1, y_fill, 2, fill_h, high)
    c.rect(x+1, y_fill, 10, 1, high)
    c.rect(x+9, y_fill, 2, fill_h, shad)
    
    if i == 3:
        offset_x = x + 3
        offset_y = y + 7
        
        for r, row in enumerate(bolt_pattern):
            for c_idx, char in enumerate(row):
                if char == '#':
                    c.set(offset_x + c_idx + 1, offset_y + r + 1, "#00000088")
        
        for r, row in enumerate(bolt_pattern):
            for c_idx, char in enumerate(row):
                if char == '#':
                    c.set(offset_x + c_idx, offset_y + r, "#FFEB3B")
                    
    c.rect(x+7, y+2, 2, 20, "#FFFFFF1A")
    
finish(c)
