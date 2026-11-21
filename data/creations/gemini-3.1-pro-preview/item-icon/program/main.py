import pixelbench_api as pb

def make_compass():
    outline = '#1a140a'
    gold_dark = '#5c3a21'
    gold_mid = '#8a5c2a'
    gold_base = '#b88633'
    gold_light = '#e6b840'
    gold_high = '#ffe073'

    blue_dark = '#0f2b5c'
    blue_mid = '#1a4c99'
    blue_base = '#2b73d9'
    blue_light = '#5ca3ff'
    blue_high = '#b3d9ff'

    dial_dark = '#5c4a3d'
    dial_mid = '#8a735c'
    dial_light = '#b89f82'
    dial_high = '#e6ccab'

    c_out = pb.new_canvas(32, 32)
    c_base = pb.new_canvas(32, 32)
    c_gold = pb.new_canvas(32, 32)
    c_dial = pb.new_canvas(32, 32)
    c_crystal = pb.new_canvas(32, 32)

    # 1. Thick Outlines
    c_out.circle(15, 5, 5, outline)
    c_out.circle(15, 17, 14, outline)
    c_out.circle(15, 5, 1, 'transparent')

    # 2. Base outlines
    c_base.circle(15, 5, 4, outline)
    c_base.circle(15, 17, 13, outline)
    c_base.circle(15, 5, 2, 'transparent')

    # 3. Gold Casing
    c_gold.circle(15, 5, 3, gold_dark)
    c_gold.circle(15, 4, 2, gold_light)
    c_gold.circle(15, 5, 2, outline)
    c_gold.circle(15, 5, 1, 'transparent')

    # Outer casing base
    c_gold.circle(15, 17, 12, gold_dark)
    c_gold.circle(15, 17, 11, gold_base)
    
    # Outer casing highlight
    c_gold.circle(14, 16, 10, gold_light)
    c_gold.circle(14, 16, 9, gold_high)
    
    # Inner rim base
    c_gold.circle(15, 17, 9, gold_dark)
    
    # Inner rim highlight
    c_gold.circle(16, 18, 8, gold_base)

    # Engraved markings
    c_gold.set(15, 6, outline)
    c_gold.set(15, 7, gold_high)
    c_gold.set(15, 27, outline)
    c_gold.set(15, 28, gold_high)
    c_gold.set(25, 17, outline)
    c_gold.set(26, 17, gold_high)
    c_gold.set(5, 17, outline)
    c_gold.set(6, 17, gold_high)

    c_gold.set(22, 10, outline)
    c_gold.set(23, 11, gold_high)
    c_gold.set(8, 10, outline)
    c_gold.set(9, 11, gold_high)
    c_gold.set(22, 24, outline)
    c_gold.set(23, 25, gold_high)
    c_gold.set(8, 24, outline)
    c_gold.set(9, 25, gold_high)

    # 4. Dial
    c_dial.circle(15, 17, 8, outline)
    c_dial.circle(15, 17, 7, dial_dark)
    c_dial.circle(15, 17, 6, dial_mid)
    c_dial.circle(15, 17, 5, dial_light)
    c_dial.circle(15, 17, 4, dial_high)

    # Diagonal arrows (behind)
    c_dial.poly([(15, 17), (15, 15), (19, 13)], gold_base)
    c_dial.poly([(15, 17), (17, 17), (19, 13)], gold_mid)
    
    c_dial.poly([(15, 17), (15, 15), (11, 13)], gold_base)
    c_dial.poly([(15, 17), (13, 17), (11, 13)], gold_mid)
    
    c_dial.poly([(15, 17), (17, 17), (19, 21)], gold_base)
    c_dial.poly([(15, 17), (15, 19), (19, 21)], gold_mid)
    
    c_dial.poly([(15, 17), (13, 17), (11, 21)], gold_base)
    c_dial.poly([(15, 17), (15, 19), (11, 21)], gold_mid)

    # Main arrows
    c_dial.poly([(15, 17), (13, 15), (15, 9)], gold_light)
    c_dial.poly([(15, 17), (17, 15), (15, 9)], gold_dark)
    
    c_dial.poly([(15, 17), (17, 15), (23, 17)], gold_light)
    c_dial.poly([(15, 17), (17, 19), (23, 17)], gold_dark)
    
    c_dial.poly([(15, 17), (13, 19), (15, 25)], gold_light)
    c_dial.poly([(15, 17), (17, 19), (15, 25)], gold_dark)
    
    c_dial.poly([(15, 17), (13, 15), (7, 17)], gold_light)
    c_dial.poly([(15, 17), (13, 19), (7, 17)], gold_dark)

    # 5. Blue Crystal
    c_crystal.circle(15, 17, 4, outline)
    c_crystal.circle(15, 17, 3, blue_dark)
    
    c_crystal.poly([(15, 17), (13, 17), (15, 15)], blue_light)
    c_crystal.poly([(15, 17), (15, 15), (17, 17)], blue_base)
    c_crystal.poly([(15, 17), (17, 17), (15, 19)], blue_dark)
    c_crystal.poly([(15, 17), (15, 19), (13, 17)], blue_mid)
    
    c_crystal.set(13, 16, blue_light)
    c_crystal.set(14, 15, blue_light)
    c_crystal.set(16, 15, blue_base)
    c_crystal.set(17, 16, blue_base)
    c_crystal.set(16, 19, blue_dark)
    c_crystal.set(17, 18, blue_dark)
    c_crystal.set(13, 18, blue_mid)
    c_crystal.set(14, 19, blue_mid)

    c_crystal.set(15, 16, blue_high)
    c_crystal.set(14, 16, blue_high)
    c_crystal.set(15, 15, '#ffffff')

    final = pb.flatten([c_out, c_base, c_gold, c_dial, c_crystal])
    return final

final_canvas = make_compass()
pb.finish(final_canvas)
