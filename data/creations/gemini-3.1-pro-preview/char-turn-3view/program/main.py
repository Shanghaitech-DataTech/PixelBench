import pixelbench_api
from pixelbench_api import input_canvas, finish

def make_frame1():
    c = input_canvas.copy()
    
    # Shift bangs right by 2
    s_bangs = c.select(22, 28, 22, 8)
    s_bangs.copy_to(24, 28, c)
    c.rect(22, 28, 2, 8, 4) 
    
    # Shift face right by 4
    s_face = c.select(19, 36, 28, 9)
    s_face.copy_to(23, 36, c)
    c.rect(19, 36, 4, 9, 7) # left cheek
    c.line(50, 36, 50, 44, 1) # right face outline
    
    # Shift chest right by 4
    s_chest = c.select(20, 45, 26, 12)
    s_chest.copy_to(24, 45, c)
    c.rect(20, 45, 4, 3, 7) # left neck
    c.rect(20, 48, 4, 9, 18) # left dress
    c.line(49, 45, 49, 56, 1) # right chest outline
    
    return c

def make_frame2(f1):
    c = f1.copy()
    c.mirror("h")
    return c

def make_frame3():
    c = input_canvas.copy()
    w, h = 66, 119
    
    # Symmetrical base (mirror left to right)
    for y in range(h):
        for x in range(33):
            c.set(65 - x, y, c.get(x, y))
            
    # Cover face and neck with hair
    for y in range(25, 52):
        for x in range(14, 52):
            p = c.get(x, y)
            if p in [7, 8, 9, 10, 11, 12, 13, 14, 15]: 
                val = (x // 2 + y // 4) % 3 + 1
                hair_colors = [2, 3, 4, 5]
                c.set(x, y, hair_colors[val])

    # Cover remaining V-neck with dress
    for y in range(48, 60):
        for x in range(20, 46):
            p = c.get(x, y)
            if p in [7, 8, 9, 10, 14, 15]:
                if 28 <= x <= 38:
                    c.set(x, y, 18)
                else:
                    c.set(x, y, 17)
                
    return c

def main():
    f1 = make_frame1()
    f2 = make_frame2(f1)
    f3 = make_frame3()
    
    finish([f1, f2, f3])

if __name__ == "__main__":
    main()
