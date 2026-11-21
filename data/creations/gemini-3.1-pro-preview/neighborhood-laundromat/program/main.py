from pixelbench_api import new_canvas, finish

def draw_laundromat():
    c = new_canvas(64, 64)
    
    # Palette definition
    ceiling = c.color('#D0D8E0')
    light_glow = c.color('#E8F0F8')
    light_bright = c.color('#FFFFFF')
    
    wall_dark = c.color('#7A8B98')
    wall_col = c.color('#8A9BA8')
    wall_light = c.color('#9AAFC0')
    
    floor1 = c.color('#C8D0D8')
    floor2 = c.color('#B0B8C0')
    shadow = c.color('#9098A0')
    
    mach_body = c.color('#F0F4F8')
    mach_shade = c.color('#D0D8E0')
    mach_outline = c.color('#405060')
    mach_panel = c.color('#304050')
    mach_door = c.color('#8090A0')
    mach_glass = c.color('#203040')
    mach_glass_ref = c.color('#6080A0')
    btn_red = c.color('#E04040')
    btn_green = c.color('#40E040')
    
    table_top = c.color('#E0E8F0')
    table_edge = c.color('#A0B0C0')
    table_leg = c.color('#708090')
    
    basket_col = c.color('#40A0B0')
    basket_dark = c.color('#207080')
    cloth1 = c.color('#E07090')
    cloth2 = c.color('#D0C050')
    
    clock_rim = c.color('#203040')
    clock_face = c.color('#F0F4F8')
    
    # Ceiling
    c.rect(0, 0, 64, 5, ceiling)
    # Lights
    c.rect(8, 1, 16, 2, light_glow)
    c.rect(9, 1, 14, 1, light_bright)
    c.rect(36, 1, 16, 2, light_glow)
    c.rect(37, 1, 14, 1, light_bright)
    
    # Wall
    c.rect(0, 5, 64, 37, wall_dark)
    c.rect(0, 5, 64, 23, wall_col)
    c.rect(0, 5, 64, 11, wall_light)
    
    # Pipes
    pipe_col = c.color('#607080')
    c.rect(18, 5, 1, 37, pipe_col)
    c.rect(33, 5, 1, 37, pipe_col)
    
    # Baseboard
    c.rect(0, 42, 64, 2, c.color('#506070'))
    
    # Floor
    c.rect(0, 44, 64, 20, floor1)
    for y in range(44, 64, 4):
        for x in range(0, 64, 8):
            offset = 4 if (y // 4) % 2 == 1 else 0
            c.rect(x + offset, y, 4, 4, floor2)
            
    # Shadows
    c.rect(4, 45, 44, 2, shadow)
    
    # Sign
    c.rect(18, 3, 28, 8, c.color('#C0D8E8'))
    c.rect(18, 3, 28, 1, c.color('#FFFFFF'))
    c.text(20, 4, "WASH", c.color('#105080'), font="5x7")
    
    # Machines
    for col in range(3):
        for row in range(2):
            mx = 4 + col * 15
            my = 12 + row * 17
            
            # Machine outline
            c.rect(mx, my, 14, 16, mach_outline)
            # Machine body
            c.rect(mx+1, my+1, 12, 14, mach_body)
            # shading and highlight
            c.rect(mx+1, my+14, 12, 1, mach_shade)
            c.rect(mx+12, my+1, 1, 14, mach_shade)
            c.rect(mx+1, my+1, 12, 1, c.color('#FFFFFF'))
            c.rect(mx+1, my+1, 1, 14, c.color('#FFFFFF'))
            
            # Control panel
            c.rect(mx+1, my+1, 12, 3, mach_panel)
            c.rect(mx+1, my+1, 12, 1, c.color('#405060'))
            c.set(mx+2, my+2, btn_red)
            c.set(mx+4, my+2, btn_green)
            c.rect(mx+8, my+2, 4, 1, c.color('#A0E0FF'))
            
            # Door
            c.circle(mx+6, my+9, 4, mach_door)
            c.circle(mx+6, my+9, 3, mach_glass)
            c.circle(mx+6, my+9, 2, c.color('#102030'))
            
            # Clothes inside
            if (col + row) % 2 == 0:
                c.rect(mx+5, my+8, 3, 2, c.color('#A04060'))
                c.rect(mx+4, my+10, 4, 2, c.color('#4060A0'))
                
            # Glass reflection
            c.line(mx+5, my+7, mx+7, my+7, mach_glass_ref)
            c.set(mx+4, my+8, mach_glass_ref)
            
            # Hinge and handle
            c.set(mx+2, my+9, c.color('#607080'))
            c.set(mx+10, my+9, c.color('#C0D0E0'))

    # Detergent bottle on machine 1
    det_col = c.color('#FF6020')
    det_cap = c.color('#2040C0')
    c.rect(6, 7, 5, 5, det_col)
    c.rect(7, 5, 3, 2, det_cap)
    c.rect(5, 8, 1, 3, det_col)
    
    # Folding Table
    tx, ty = 49, 32
    c.rect(tx+1, ty+2, 2, 13, table_leg)
    c.rect(tx+7, ty+2, 2, 13, table_leg)
    c.rect(tx, 46, 4, 1, c.color('#506070'))
    c.rect(tx+6, 46, 4, 1, c.color('#506070'))
    c.rect(tx, ty, 10, 3, table_edge)
    c.rect(tx, ty, 10, 2, table_top)
    c.rect(tx+1, ty, 8, 1, c.color('#FFFFFF'))
    c.rect(tx, 47, 4, 1, shadow)
    c.rect(tx+6, 47, 4, 1, shadow)
    
    # Laundry Basket
    bx, by = 49, 25
    c.rect(bx+1, by-2, 8, 4, cloth1)
    c.rect(bx+4, by-3, 5, 4, cloth2)
    c.rect(bx+2, by-2, 2, 1, c.color('#FF90B0'))
    c.rect(bx+5, by-3, 2, 1, c.color('#FFF070'))
    
    c.rect(bx, by, 10, 7, basket_col)
    c.rect(bx+1, by+6, 8, 1, basket_dark)
    for hy in range(by+1, by+6, 2):
        for hx in range(bx+1, bx+9, 2):
            c.set(hx, hy, basket_dark)
            
    # Poster
    c.rect(50, 4, 10, 6, mach_outline)
    c.rect(51, 5, 8, 4, mach_body)
    c.rect(52, 6, 6, 1, btn_red)
    c.rect(52, 8, 4, 1, mach_shade)
    c.set(57, 8, c.color('#4080FF'))
    
    # Clock
    cx, cy = 55, 15
    c.circle(cx, cy, 4, clock_rim)
    c.circle(cx, cy, 3, clock_face)
    c.line(cx, cy, cx, cy-2, clock_rim)
    c.line(cx, cy, cx+1, cy, clock_rim)
    c.line(cx, cy, cx-1, cy+1, c.color('#E04040'))
    c.set(cx, cy-3, clock_rim)
    c.set(cx, cy+3, clock_rim)
    c.set(cx-3, cy, clock_rim)
    c.set(cx+3, cy, clock_rim)
    
    # Trash can
    c.rect(60, 37, 4, 9, c.color('#708090'))
    c.rect(60, 36, 4, 1, c.color('#304050'))
    c.set(61, 36, c.color('#D0E0F0'))
    c.set(62, 36, c.color('#A0B0C0'))
    c.rect(60, 46, 4, 1, shadow)

    return c

c = draw_laundromat()
finish(c)
