from pixelbench_api import new_canvas, finish

def draw_spark(c, x, y, color, outline_color):
    c.set(x, y, color)
    c.set(x-1, y, outline_color)
    c.set(x+1, y, outline_color)
    c.set(x, y-1, outline_color)
    c.set(x, y+1, outline_color)

def main():
    c = new_canvas(64, 64)

    outline = c.color('#1a1a24')

    fire_dark = c.color('#d9381e')
    fire_mid = c.color('#f26d21')
    fire_light = c.color('#f9a32b')
    fire_core = c.color('#ffdf70')

    ice_dark = c.color('#255487')
    ice_mid = c.color('#3fa0d6')
    ice_light = c.color('#8ae0ff')
    ice_white = c.color('#ffffff')

    heal_dark = c.color('#1e6b3b')
    heal_mid = c.color('#34a853')
    heal_light = c.color('#8cf071')
    heal_white = c.color('#f0fff0')

    bolt_dark = c.color('#b57b00')
    bolt_mid = c.color('#f2b705')
    bolt_light = c.color('#f2d544')
    bolt_white = c.color('#ffffff')

    # FIREBALL (0, 0)
    ox, oy = 0, 0
    c.circle(ox+16, oy+20, 8, fire_dark)
    c.poly([(ox+8, oy+20), (ox+16, oy+2), (ox+24, oy+20)], fire_dark)
    c.poly([(ox+6, oy+22), (ox+8, oy+10), (ox+14, oy+18)], fire_dark)
    c.poly([(ox+26, oy+22), (ox+24, oy+10), (ox+18, oy+18)], fire_dark)
    
    c.circle(ox+16, oy+20, 6, fire_mid)
    c.poly([(ox+10, oy+20), (ox+16, oy+6), (ox+22, oy+20)], fire_mid)
    c.poly([(ox+8, oy+21), (ox+10, oy+14), (ox+13, oy+19)], fire_mid)
    c.poly([(ox+24, oy+21), (ox+22, oy+14), (ox+19, oy+19)], fire_mid)
    
    c.circle(ox+16, oy+20, 4, fire_light)
    c.poly([(ox+12, oy+20), (ox+16, oy+10), (ox+20, oy+20)], fire_light)
    
    c.circle(ox+16, oy+20, 2, fire_core)
    c.poly([(ox+14, oy+20), (ox+16, oy+14), (ox+18, oy+20)], fire_core)

    # ICE SHIELD (32, 0)
    ox, oy = 32, 0
    hex_dark = [(ox+16, oy+2), (ox+28, oy+8), (ox+28, oy+24), (ox+16, oy+30), (ox+4, oy+24), (ox+4, oy+8)]
    c.poly(hex_dark, ice_dark)
    
    hex_mid = [(ox+16, oy+5), (ox+25, oy+10), (ox+25, oy+22), (ox+16, oy+27), (ox+7, oy+22), (ox+7, oy+10)]
    c.poly(hex_mid, ice_mid)
    
    hex_light = [(ox+16, oy+8), (ox+22, oy+12), (ox+22, oy+20), (ox+16, oy+24), (ox+10, oy+20), (ox+10, oy+12)]
    c.poly(hex_light, ice_light)
    
    c.line(ox+16, oy+10, ox+16, oy+22, ice_white)
    c.line(ox+10, oy+13, ox+22, oy+19, ice_white)
    c.line(ox+10, oy+19, ox+22, oy+13, ice_white)
    c.circle(ox+16, oy+16, 2, ice_white)
    
    c.poly([(ox+16, oy+5), (ox+7, oy+10), (ox+10, oy+12), (ox+16, oy+8)], ice_white)
    c.poly([(ox+7, oy+10), (ox+7, oy+22), (ox+10, oy+20), (ox+10, oy+12)], ice_light)

    # HEALING (0, 32)
    ox, oy = 0, 32
    c.rect(ox+11, oy+3, 10, 26, heal_dark)
    c.rect(ox+3, oy+11, 26, 10, heal_dark)
    
    c.rect(ox+13, oy+5, 6, 22, heal_mid)
    c.rect(ox+5, oy+13, 22, 6, heal_mid)
    
    c.rect(ox+14, oy+6, 4, 20, heal_light)
    c.rect(ox+6, oy+14, 20, 4, heal_light)
    
    c.rect(ox+15, oy+7, 2, 18, heal_white)
    c.rect(ox+7, oy+15, 18, 2, heal_white)
    
    c.poly([(ox+16, oy+12), (ox+20, oy+16), (ox+16, oy+20), (ox+12, oy+16)], heal_white)
    
    c.poly([(ox+11, oy+21), (ox+3, oy+23), (ox+1, oy+31), (ox+9, oy+29)], heal_dark)
    c.poly([(ox+9, oy+23), (ox+5, oy+25), (ox+4, oy+29), (ox+8, oy+27)], heal_mid)
    c.poly([(ox+8, oy+24), (ox+6, oy+26), (ox+5, oy+28), (ox+7, oy+27)], heal_light)
    
    c.poly([(ox+21, oy+11), (ox+29, oy+9), (ox+31, oy+1), (ox+23, oy+3)], heal_dark)
    c.poly([(ox+23, oy+9), (ox+27, oy+7), (ox+28, oy+4), (ox+24, oy+5)], heal_mid)
    c.poly([(ox+24, oy+8), (ox+26, oy+6), (ox+27, oy+5), (ox+25, oy+6)], heal_light)

    # LIGHTNING (32, 32)
    ox, oy = 32, 32
    dark = [(ox+24, oy+0), (ox+6, oy+16), (ox+14, oy+16), (ox+10, oy+30), (ox+28, oy+16), (ox+20, oy+16)]
    c.poly(dark, bolt_dark)
    
    mid = [(ox+23, oy+3), (ox+9, oy+15), (ox+15, oy+15), (ox+12, oy+27), (ox+25, oy+17), (ox+19, oy+17)]
    c.poly(mid, bolt_mid)
    
    light = [(ox+22, oy+6), (ox+12, oy+14), (ox+16, oy+14), (ox+14, oy+24), (ox+22, oy+18), (ox+18, oy+18)]
    c.poly(light, bolt_light)
    
    white = [(ox+21, oy+9), (ox+15, oy+13), (ox+17, oy+13), (ox+16, oy+21), (ox+19, oy+19), (ox+17, oy+19)]
    c.poly(white, bolt_white)

    # APPLY OUTLINE
    c.outline(outline)

    # SPARKS
    ox, oy = 0, 0
    draw_spark(c, ox+12, oy+6, fire_mid, outline)
    draw_spark(c, ox+20, oy+8, fire_mid, outline)
    draw_spark(c, ox+16, oy+2, fire_dark, outline)
    draw_spark(c, ox+10, oy+10, fire_light, outline)
    draw_spark(c, ox+22, oy+12, fire_light, outline)

    ox, oy = 0, 32
    draw_spark(c, ox+6, oy+6, heal_light, outline)
    draw_spark(c, ox+26, oy+26, heal_light, outline)
    draw_spark(c, ox+24, oy+20, heal_white, outline)
    draw_spark(c, ox+8, oy+12, heal_white, outline)

    ox, oy = 32, 32
    draw_spark(c, ox+6, oy+6, bolt_white, outline)
    draw_spark(c, ox+26, oy+24, bolt_white, outline)
    draw_spark(c, ox+24, oy+4, bolt_light, outline)
    draw_spark(c, ox+10, oy+26, bolt_light, outline)

    finish(c)

if __name__ == "__main__":
    main()
