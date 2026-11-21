from pixelbench_api import *

def tint_red(c_hex):
    r = int(c_hex[1:3], 16)
    g = int(c_hex[3:5], 16)
    b = int(c_hex[5:7], 16)
    r = (r + 255) // 2
    g = g // 2
    b = b // 2
    return f"#{r:02x}{g:02x}{b:02x}ff"

def main():
    f1 = new_canvas(50, 50, name="f1")
    f1.blit(input_canvas, 6, 10)
    
    c2_base = new_canvas(37, 33)
    c2_base.blit(input_canvas, 0, 0)
    
    for y in range(16, 19):
        for x in range(17, 20):
            c2_base.set(x, y, 6)
    for y in range(15, 17):
        for x in range(17, 20):
            c2_base.set(x, y, 1)
            
    c2_base.rect(15, 20, 7, 6, 5)
    c2_base.rect(16, 21, 5, 4, 1)
    c2_base.rect(16, 21, 5, 1, 6)
    c2_base.rect(16, 24, 5, 1, 6)
    
    sel = c2_base.select(0, 0, 37, 33)
    rot_sel = sel.rotate(20, algorithm="rotsprite")
    preview = rot_sel.preview()
    
    f2 = new_canvas(50, 50, name="f2")
    f2.blit(preview, 6, 2)
    
    f3 = f2.copy(name="f3")
    
    pal = input_canvas.palette()
    color_map = {}
    for entry in pal:
        idx = entry['index']
        rgba = entry['rgba']
        if rgba == (0, 0, 0, 0):
            continue
        hex_str = f"#{rgba[0]:02x}{rgba[1]:02x}{rgba[2]:02x}ff"
        red_hex = tint_red(hex_str)
        color_map[idx] = f3.color(red_hex)
        
    w, h = f3.stats()['size']
    for y in range(h):
        for x in range(w):
            p = f3.get(x, y)
            if p != 0 and p in color_map:
                f3.set(x, y, color_map[p])
                
    finish([f1, f2, f3])
    
main()