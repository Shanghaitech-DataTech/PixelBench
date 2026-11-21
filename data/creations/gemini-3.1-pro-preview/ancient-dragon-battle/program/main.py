from pixelbench_api import new_canvas, flatten, finish

def draw_scene():
    # 1. Sky
    sky = new_canvas(256, 256, name="sky")
    
    sky_top = sky.color('#2a0845')
    sky_mid1 = sky.color('#6441A5')
    sky_mid2 = sky.color('#cc5333')
    sky_low = sky.color('#f5af19')
    
    sky.rect(0, 0, 256, 64, sky_top)
    sky.rect(0, 64, 256, 64, sky_mid1)
    sky.dither(0, 54, 256, 20, [sky_top, sky_mid1])
    sky.rect(0, 128, 256, 64, sky_mid2)
    sky.dither(0, 118, 256, 20, [sky_mid1, sky_mid2])
    sky.rect(0, 192, 256, 64, sky_low)
    sky.dither(0, 182, 256, 20, [sky_mid2, sky_low])
    
    # Sun
    sky.circle(150, 125, 28, sky.color('#ff8c00'))
    sky.circle(150, 125, 20, sky.color('#ffea00'))
    sky.circle(150, 125, 14, sky.color('#ffffff'))
    
    # 2. Mountains
    mountains = new_canvas(256, 256, name="mountains")
    mountain_back = mountains.color('#1f1c2c')
    mountain_front = mountains.color('#111119')
    
    mountains.poly([(0, 160), (40, 130), (80, 150), (120, 110), (170, 140), (220, 120), (256, 150), (256, 256), (0, 256)], mountain_back)
    mountains.poly([(0, 180), (50, 150), (100, 170), (160, 130), (210, 160), (256, 140), (256, 256), (0, 256)], mountain_front)
    
    # 3. Ground
    ground = new_canvas(256, 256, name="ground")
    ground_col = ground.color('#2a1a10')
    ground_dark = ground.color('#1a0f08')
    ground.rect(0, 200, 256, 56, ground_dark)
    ground.rect(0, 200, 256, 10, ground_col)
    ground.dither(0, 210, 256, 20, [ground_col, ground_dark], pattern="bayer4")
    
    # 4. Castle
    castle = new_canvas(256, 256, name="castle")
    castle_base = castle.color('#2b2b2b')
    castle_dark = castle.color('#1a1a1a')
    castle_light = castle.color('#3c3c3c')
    
    # Main block
    castle.rect(20, 120, 100, 120, castle_base)
    # Left tower
    castle.rect(10, 90, 30, 150, castle_base)
    # Right tower
    castle.rect(100, 80, 30, 160, castle_base)
    # Keep (center high)
    castle.rect(40, 70, 50, 50, castle_base)
    
    # Crenellations
    for x in range(20, 120, 10):
        castle.rect(x, 110, 5, 10, castle_base)
    for x in range(10, 40, 10):
        castle.rect(x, 80, 5, 10, castle_base)
    for x in range(100, 130, 10):
        castle.rect(x, 70, 5, 10, castle_base)
    for x in range(40, 90, 10):
        castle.rect(x, 60, 5, 10, castle_base)
        
    # Details & Shading
    castle.rect(10, 90, 5, 150, castle_light)
    castle.rect(100, 80, 5, 160, castle_light)
    castle.rect(40, 70, 5, 50, castle_light)
    castle.rect(20, 120, 100, 5, castle_dark)
    
    # Castle Gate
    gate_col = castle.color('#3e2723')
    castle.rect(60, 200, 20, 40, gate_col)
    castle.ellipse(70, 200, 10, 10, gate_col)
    port_col = castle.color('#757575')
    for px in range(62, 80, 4):
        castle.rect(px, 195, 2, 45, port_col)
    for py in range(200, 240, 6):
        castle.rect(60, py, 20, 2, port_col)
    
    # Windows
    window_col = castle.color('#ff8c00')
    for wx, wy in [(18, 110), (18, 140), (18, 170), (112, 100), (112, 130), (112, 160), (55, 90), (65, 90)]:
        castle.rect(wx, wy, 8, 12, castle_dark)
        castle.rect(wx+1, wy+1, 6, 10, window_col)
        castle.rect(wx+2, wy+2, 4, 8, castle.color('#ffd700'))
        
    # Banners
    banner_red = castle.color('#d32f2f')
    banner_gold = castle.color('#fbc02d')
    castle.rect(20, 100, 10, 30, banner_red)
    castle.rect(22, 100, 6, 25, banner_gold)
    castle.rect(110, 90, 10, 30, banner_red)
    castle.rect(112, 90, 6, 25, banner_gold)
    castle.rect(60, 80, 10, 20, banner_red)
        
    # Rampart Knights
    armor_col = castle.color('#9e9e9e')
    shield_col = castle.color('#b71c1c')
    spear_col = castle.color('#dddddd')
    
    for x in range(22, 118, 14):
        if x > 35 and x < 95:
            castle.rect(x, 104, 4, 6, armor_col)
            castle.rect(x+1, 101, 2, 3, armor_col)
            castle.rect(x+4, 100, 1, 12, spear_col)
            castle.rect(x-1, 105, 3, 5, shield_col)

    for x in range(42, 88, 12):
        castle.rect(x, 54, 4, 6, armor_col)
        castle.rect(x+1, 51, 2, 3, armor_col)
        castle.rect(x+4, 50, 1, 12, spear_col)
        castle.rect(x-1, 55, 3, 5, shield_col)
        
    castle.outline(castle.color('#000000'))
    
    # 5. Army & Siege Towers
    army = new_canvas(256, 256, name="army")
    wood_dark = army.color('#3e2723')
    wood_light = army.color('#5d4037')
    
    # Tower 1
    army.rect(180, 110, 40, 110, wood_dark)
    army.rect(180, 110, 5, 110, wood_light)
    army.rect(215, 110, 5, 110, wood_light)
    army.rect(180, 110, 40, 5, army.color('#111111'))
    army.rect(185, 140, 30, 4, wood_light)
    army.rect(185, 170, 30, 4, wood_light)
    army.rect(185, 200, 30, 4, wood_light)
    
    # Tower 2
    army.rect(130, 130, 30, 80, wood_dark)
    army.rect(130, 130, 4, 80, wood_light)
    army.rect(156, 130, 4, 80, wood_light)
    army.rect(130, 130, 30, 4, army.color('#111111'))
    army.rect(134, 155, 22, 3, wood_light)
    army.rect(134, 180, 22, 3, wood_light)
    
    # Shields on towers
    for ty in range(120, 200, 15):
        army.rect(178, ty, 2, 8, shield_col)
        if ty < 190:
            army.rect(128, ty+10, 2, 6, shield_col)
    
    # Ladder
    ladder_col = army.color('#8d6e63')
    army.line(90, 210, 70, 120, ladder_col)
    army.line(95, 210, 75, 120, ladder_col)
    for i in range(15):
        lx = int(90 - (i * (20/15)))
        ly = int(210 - (i * (90/15)))
        army.line(lx, ly, lx+5, ly, ladder_col)
        
    armor_dark = army.color('#616161')
    # Soldiers on ladder
    for i in range(3, 12, 3):
        lx = int(90 - (i * (20/15)))
        ly = int(210 - (i * (90/15)))
        army.rect(lx, ly-5, 4, 6, armor_dark)
        army.rect(lx+1, ly-8, 2, 3, armor_col)
    
    # Soldiers in formation
    for y in range(215, 256, 7):
        for x in range(30, 256, 8):
            if 45 < x < 95 and 210 < y < 245:
                continue
            ox = x + (y % 4)
            army.rect(ox, y, 3, 5, armor_dark)
            army.rect(ox+1, y-2, 2, 2, armor_col)
            army.rect(ox+3, y-5, 1, 9, spear_col)
            army.rect(ox-1, y+1, 2, 4, shield_col)
            
    # Battering Ram
    ram_wood = army.color('#4e342e')
    ram_metal = army.color('#9e9e9e')
    army.poly([(55, 215), (85, 215), (90, 230), (50, 230)], ram_wood)
    army.rect(55, 230, 30, 10, army.color('#271c19'))
    army.rect(50, 233, 10, 4, ram_metal)
    
    # Wheels
    wheel_col = army.color('#111111')
    army.circle(60, 240, 3, wheel_col)
    army.circle(80, 240, 3, wheel_col)
    army.circle(190, 220, 5, wheel_col)
    army.circle(210, 220, 5, wheel_col)
    army.circle(135, 210, 4, wheel_col)
    army.circle(150, 210, 4, wheel_col)
            
    army.outline(army.color('#000000'))
    
    # 6. Dragon
    dragon = new_canvas(256, 256, name="dragon")
    d_body = dragon.color('#113322')
    d_wing = dragon.color('#0a1e14')
    d_belly = dragon.color('#225533')
    d_eye = dragon.color('#ff0000')
    
    # Far wing
    dragon.path("M 155 55 Q 130 -10 70 0 Q 110 30 130 50 Z", d_wing)
    dragon.path("M 155 55 Q 120 10 70 0", dragon.color('#050f0a'), fill=False)
    # Body
    dragon.ellipse(160, 60, 26, 14, d_body)
    dragon.ellipse(160, 64, 20, 8, d_belly)
    # Neck
    dragon.path("M 145 60 Q 115 45 105 72 Q 125 78 145 68 Z", d_body)
    # Head
    dragon.ellipse(100, 75, 12, 7, d_body)
    dragon.rect(90, 74, 14, 6, d_body)
    # Eye
    dragon.set(98, 75, d_eye)
    dragon.set(99, 75, d_eye)
    # Horns
    dragon.path("M 105 72 L 95 62 L 110 70 Z", dragon.color('#555555'))
    dragon.path("M 103 73 L 93 65 L 107 71 Z", dragon.color('#444444'))
    # Tail
    dragon.path("M 175 60 Q 210 50 240 80 Q 210 70 175 68 Z", d_body)
    # Spikes on back
    for i in range(130, 210, 8):
        dragon.poly([(i, 52 + (i-130)//3), (i-4, 45 + (i-130)//3), (i+4, 49 + (i-130)//3)], dragon.color('#555555'))
    # Near wing
    dragon.path("M 165 60 Q 190 -20 250 -5 Q 220 35 190 60 Z", d_wing)
    dragon.path("M 165 60 Q 210 0 250 -5", dragon.color('#050f0a'), fill=False)
    # Legs
    dragon.path("M 150 65 L 140 85 L 135 85 L 145 68 Z", d_body)
    dragon.path("M 170 65 L 165 88 L 170 88 L 175 68 Z", d_body)
    # Claws
    dragon.rect(133, 85, 4, 2, dragon.color('#aaaaaa'))
    dragon.rect(165, 88, 5, 2, dragon.color('#aaaaaa'))
    
    dragon.outline(dragon.color('#000000'))
    
    # 7. FX (Fire, Smoke, Arrows, Embers)
    fx = new_canvas(256, 256, name="fx")
    fire_y = fx.color('#ffff00')
    fire_o = fx.color('#ff8800')
    fire_r = fx.color('#ff0000')
    smoke_d = fx.color('#222222')
    smoke_l = fx.color('#444444')
    
    # Dragon Fire
    fx.path("M 90 77 Q 60 90 30 120 Q 70 120 85 85 Z", fire_o)
    fx.path("M 87 78 Q 60 95 35 115 Q 70 110 83 82 Z", fire_y)
    fx.path("M 85 79 Q 65 98 40 110 Q 65 105 80 80 Z", fx.color('#ffffff'))
    
    # Castle Fires
    for fx_x, fx_y in [(25, 120), (45, 120), (85, 120), (105, 80), (115, 80), (15, 90), (35, 90), (50, 70), (70, 70), (60, 100)]:
        fx.circle(fx_x, fx_y, 10, fire_r)
        fx.circle(fx_x+2, fx_y-3, 7, fire_o)
        fx.circle(fx_x+1, fx_y-5, 4, fire_y)
        
    # Smoke plumes
    for sx, sy in [(25, 110), (105, 70), (50, 60), (15, 80)]:
        for i in range(8):
            rad = 8 + i*2
            fx.circle(sx - i*2, sy - i*10, rad, smoke_d)
            fx.circle(sx - i*2 - 2, sy - i*10 - 2, rad-2, smoke_l)
            
    # Arrows
    arrow_col = fx.color('#ffffff')
    for i in range(40):
        ax = 30 + (i * 27) % 200
        ay = 100 + (i * 13) % 100
        fx.line(ax, ay, ax-4, ay-4, arrow_col)
    for i in range(20):
        ax = 40 + (i * 31) % 100
        ay = 90 + (i * 17) % 60
        fx.line(ax, ay, ax+4, ay-3, arrow_col)
        
    # Embers
    for i in range(60):
        ex = (i * 47) % 256
        ey = (i * 73) % 256
        if ey > 50 and ey < 200:
            fx.set(ex, ey, fire_o)
            if i % 2 == 0:
                fx.set(ex+1, ey, fire_y)
                
    # Flatten everything
    result = flatten([sky, mountains, ground, castle, army, dragon, fx])
    finish(result)

draw_scene()
