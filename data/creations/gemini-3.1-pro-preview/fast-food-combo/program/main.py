from pixelbench_api import new_canvas, finish

def draw():
    c = new_canvas(64, 64)
    out = c.color('#1a100c')
    
    # Colors
    carton_red = c.color('#e61919')
    fry_c1 = c.color('#ffcc00')
    fry_c2 = c.color('#e6a800')
    nugget_c = c.color('#d98c21')
    nugget_hl = c.color('#f2b34c')
    bun_c = c.color('#e69938')
    bun_hl = c.color('#ffb85c')
    meat_c = c.color('#593315')
    cheese_c = c.color('#ffcc00')
    lettuce_c = c.color('#33cc33')
    
    # Tray
    c.rect(4, 8, 56, 48, out)
    c.rect(5, 9, 54, 46, c.color('#9c9a92'))
    c.rect(6, 10, 52, 44, c.color('#d6d3c8'))
    c.line(6, 53, 57, 53, c.color('#ffffff'))
    c.line(57, 10, 57, 53, c.color('#ffffff'))
    c.line(6, 10, 57, 10, c.color('#b0ada4'))
    c.line(6, 10, 6, 53, c.color('#b0ada4'))
    
    # Tray paper liner
    liner_c1 = c.color('#ffffff')
    liner_c2 = c.color('#f0e6d8')
    c.rect(7, 11, 50, 42, liner_c1)
    for i in range(7, 57, 4):
        for j in range(11, 53, 4):
            if ((i - 7) // 4 + (j - 11) // 4) % 2 == 0:
                w = min(4, 57 - i)
                h = min(4, 53 - j)
                if w > 0 and h > 0:
                    c.rect(i, j, w, h, liner_c2)
                    
    # Shadows
    shadow_c = c.color('#d1c7b8')
    cx, cy = 14, 16
    fx, fy = 46, 16
    bx, by = 24, 38
    sx, sy = 54, 46
    c.ellipse(cx+2, cy+16, 7, 3, shadow_c)
    c.ellipse(fx+2, fy+14, 8, 3, shadow_c)
    c.ellipse(bx+2, by+8, 12, 4, shadow_c)
    c.ellipse(46, 44, 10, 5, shadow_c)
    c.ellipse(sx+1, sy+2, 6, 2, shadow_c)
    
    # 1. Cola
    cup = new_canvas(64, 64)
    cup.ellipse(cx, cy+16, 6, 2, c.color('#d62828'))
    cup.poly([(cx-7, cy), (cx+7, cy), (cx+6, cy+16), (cx-6, cy+16)], c.color('#d62828'))
    cup.poly([(cx+2, cy), (cx+7, cy), (cx+6, cy+16), (cx+1, cy+16)], c.color('#b31b1b'))
    cup.poly([(cx-5, cy), (cx-2, cy), (cx-2, cy+16), (cx-4, cy+16)], c.color('#e64c4c'))
    cup.ellipse(cx, cy, 7, 3, c.color('#e0e0e0'))
    cup.ellipse(cx, cy-1, 6, 2, c.color('#ffffff'))
    cup.line(cx-7, cy, cx+7, cy, out)
    cup.outline(out)
    
    straw = new_canvas(64, 64)
    straw.line(cx, cy-1, cx+4, cy-12, c.color('#ff0000'))
    straw.line(cx+1, cy-1, cx+5, cy-12, c.color('#ff0000'))
    straw.outline(out)
    cup.blit(straw, 0, 0)
    cup.set(cx+1, cy-1, out)
    cup.set(cx, cy-1, out)
    c.blit(cup, 0, 0)
    
    # 2. Fries
    fries_layer = new_canvas(64, 64)
    c_back = new_canvas(64, 64)
    c_back.path(f"M {fx-8} {fy-2} Q {fx} {fy-6} {fx+8} {fy-2} L {fx+8} {fy} L {fx-8} {fy} Z", carton_red)
    c_back.outline(out)
    fries_layer.blit(c_back, 0, 0)
    
    fry_layer = new_canvas(64, 64)
    for i in range(14):
        x_off = (i * 37) % 13 - 6
        y_off = (i * 19) % 7 - 10
        fry_layer.rect(fx + x_off, fy + y_off, 3, 10, fry_c1)
        fry_layer.line(fx + x_off + 2, fy + y_off + 1, fx + x_off + 2, fy + y_off + 9, fry_c2)
    fry_layer.outline(out)
    fries_layer.blit(fry_layer, 0, 0)
    
    c_front = new_canvas(64, 64)
    c_front.path(f"M {fx-8} {fy-2} Q {fx} {fy+4} {fx+8} {fy-2} L {fx+6} {fy+14} Q {fx} {fy+16} {fx-6} {fy+14} Z", carton_red)
    c_front.path(f"M {fx} {fy+1} Q {fx+4} {fy+1} {fx+8} {fy-2} L {fx+6} {fy+14} Q {fx+3} {fy+15} {fx} {fy+15} Z", c.color('#b31b1b'))
    c_front.line(fx-7, fy-1, fx-5, fy+13, c.color('#ff4d4d'))
    c_front.outline(out)
    c_front.path(f"M {fx-8} {fy-2} Q {fx} {fy+4} {fx+8} {fy-2}", out, fill=False)
    fries_layer.blit(c_front, 0, 0)
    c.blit(fries_layer, 0, 0)
    
    # 3. Nuggets
    nuggets_layer = new_canvas(64, 64)
    def draw_nugget(x, y):
        n = new_canvas(64, 64)
        n.ellipse(x, y, 4, 3, nugget_c)
        n.ellipse(x-2, y+1, 3, 3, nugget_c)
        n.ellipse(x+2, y-1, 3, 3, nugget_c)
        n.ellipse(x, y-1, 2, 1, nugget_hl)
        n.outline(out)
        nuggets_layer.blit(n, 0, 0)

    draw_nugget(44, 40)
    draw_nugget(50, 38)
    draw_nugget(47, 44)
    draw_nugget(41, 43)
    c.blit(nuggets_layer, 0, 0)
    
    # 4. Dipping Sauce
    sauce_layer = new_canvas(64, 64)
    sauce_layer.ellipse(sx, sy+2, 5, 2, c.color('#ffffff'))
    sauce_layer.poly([(sx-5, sy), (sx+5, sy), (sx+4, sy+2), (sx-4, sy+2)], c.color('#f0f0f0'))
    sauce_layer.ellipse(sx, sy, 5, 2, c.color('#e0e0e0'))
    sauce_layer.ellipse(sx, sy, 4, 1, c.color('#8c1a00'))
    sauce_layer.line(sx-1, sy, sx+1, sy, c.color('#cc2900'))
    sauce_layer.outline(out)
    c.blit(sauce_layer, 0, 0)
    
    # 5. Burger
    burger = new_canvas(64, 64)
    
    bbun = new_canvas(64, 64)
    bbun.ellipse(bx, by+6, 10, 3, bun_c)
    bbun.rect(bx-9, by+4, 19, 3, bun_c)
    bbun.outline(out)
    burger.blit(bbun, 0, 0)
    
    patty = new_canvas(64, 64)
    patty.ellipse(bx, by+4, 11, 3, meat_c)
    patty.rect(bx-10, by+2, 21, 3, meat_c)
    patty.outline(out)
    burger.blit(patty, 0, 0)
    
    cheese = new_canvas(64, 64)
    cheese.poly([(bx-10, by+1), (bx, by+4), (bx+10, by+1), (bx+5, by-1), (bx-5, by-1)], cheese_c)
    cheese.poly([(bx-8, by+2), (bx-6, by+5), (bx-4, by+3)], cheese_c)
    cheese.poly([(bx+4, by+2), (bx+6, by+6), (bx+8, by+2)], cheese_c)
    cheese.outline(out)
    burger.blit(cheese, 0, 0)
    
    lettuce = new_canvas(64, 64)
    for i in range(8):
        lx = bx - 10 + i*3
        ly = by - 1 + (i%2)
        lettuce.circle(lx, ly, 2, lettuce_c)
    lettuce.outline(out)
    burger.blit(lettuce, 0, 0)
    
    tbun = new_canvas(64, 64)
    tbun.ellipse(bx, by-2, 10, 3, bun_c)
    tbun.path(f"M {bx-10} {by-2} C {bx-10} {by-10} {bx+10} {by-10} {bx+10} {by-2} Z", bun_c)
    tbun.path(f"M {bx-6} {by-3} C {bx-6} {by-8} {bx+6} {by-8} {bx+6} {by-3} Z", bun_hl)
    tbun.outline(out)
    
    seed_c = c.color('#fff2cc')
    seeds = [(bx-4, by-6), (bx, by-7), (bx+4, by-5), (bx-2, by-4), (bx+2, by-3)]
    for sdx, sdy in seeds:
        tbun.set(sdx, sdy, seed_c)
        tbun.set(sdx+1, sdy, seed_c)
    
    burger.blit(tbun, 0, 0)
    c.blit(burger, 0, 0)
    
    finish(c)

if __name__ == "__main__":
    draw()
