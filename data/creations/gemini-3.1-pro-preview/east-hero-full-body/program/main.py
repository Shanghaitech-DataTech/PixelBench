from pixelbench_api import *

def draw():
    # Colors
    c_outline = '#1A1A1A'
    c_robe_base = '#2C3539'
    c_robe_hi = '#455258'
    c_robe_shadow = '#1C2326'
    c_skin = '#E5C298'
    c_skin_hi = '#FFE4C4'
    c_hair = '#111111'
    c_sash = '#8B2500'
    c_sash_hi = '#CD3700'
    c_hat = '#D2B48C'
    c_hat_shadow = '#8B5A2B'
    c_sword_hilt = '#DAA520'
    c_sword_scab = '#2F4F4F'
    c_sword_hi = '#5F9EA0'

    # Background Canvas
    bg = new_canvas(256, 256)
    for i in range(32):
        bg.rect(0, i*8, 256, 8, color=f'#{180-i:02x}{190-i:02x}{210:02x}')

    bg.circle(180, 80, 24, '#C0D0E0')
    bg.circle(180, 80, 20, '#F0F8FF')

    bg.path('M -20 160 L 40 90 L 90 130 L 160 70 L 230 140 L 280 100 L 280 256 L -20 256 Z', '#8098B0')
    bg.path('M -20 190 L 60 130 L 130 180 L 210 110 L 280 160 L 280 256 L -20 256 Z', '#607890')
    bg.path('M -20 220 L 80 160 L 150 210 L 220 150 L 280 200 L 280 256 L -20 256 Z', '#405870')

    # Mist
    bg.path('M -20 215 Q 100 200 150 220 T 280 210 L 280 256 L -20 256 Z', '#B0C0D0')
    bg.path('M -20 225 Q 80 210 180 230 T 280 220 L 280 256 L -20 256 Z', '#C0D0E0')
    for i in range(10):
        bg.rect(0, 236+i*2, 256, 2, color=f'#{192+i*4:02x}{208+i*2:02x}{224+i:02x}')
        
    # Wind streaks
    bg.path('M 180 120 Q 150 125 120 120', '#A0B8D0', fill=False)
    bg.path('M 220 150 Q 190 155 160 150', '#A0B8D0', fill=False)
    bg.path('M 100 90 Q 70 95 40 90', '#A0B8D0', fill=False)

    layers = [bg]

    # Layer 2: Back Hair
    c2 = new_canvas(256, 256)
    c2.path('M 135 60 Q 170 120 140 180 Q 155 120 150 60 Z', c_hair)
    c2.outline(c_outline)
    layers.append(c2)

    # Layer 3: Back Arm
    c3 = new_canvas(256, 256)
    c3.path('M 140 85 Q 175 100 170 130 Q 155 135 145 110 Z', c_robe_shadow)
    c3.path('M 170 130 Q 180 160 165 180 Q 150 150 145 110 Z', c_robe_shadow)
    c3.outline(c_outline)
    layers.append(c3)

    # Layer 4: Back Leg
    c4 = new_canvas(256, 256)
    c4.path('M 145 170 L 155 220 L 175 220 L 160 170 Z', c_robe_shadow)
    c4.path('M 155 205 L 170 205 L 175 220 L 145 220 L 150 210 Z', '#1A1A1A')
    c4.outline(c_outline)
    layers.append(c4)

    # Layer 5: Skirt Back
    c5 = new_canvas(256, 256)
    c5.path('M 110 135 L 150 135 L 130 210 L 80 200 Z', c_robe_shadow)
    c5.outline(c_outline)
    layers.append(c5)

    # Layer 6: Front Leg
    c6 = new_canvas(256, 256)
    c6.path('M 120 170 L 110 225 L 135 225 L 140 170 Z', c_robe_base)
    c6.path('M 115 210 L 130 210 L 130 225 L 100 225 L 105 215 Z', '#1A1A1A')
    c6.path('M 115 210 L 115 225', c_robe_hi, fill=False)
    c6.outline(c_outline)
    layers.append(c6)

    # Layer 7: Face & Neck
    c7 = new_canvas(256, 256)
    c7.path('M 120 80 L 130 80 L 130 95 L 120 95 Z', '#C8A078')
    c7.path('M 115 65 L 135 65 L 135 80 L 125 88 L 115 80 Z', c_skin)
    c7.path('M 115 80 L 125 88 L 135 80', c_skin_hi, fill=False)
    c7.path('M 115 80 Q 125 95 135 80', '#8B5A2B', fill=False)
    c7.outline(c_outline)
    layers.append(c7)

    # Layer 8: Torso
    c8 = new_canvas(256, 256)
    c8.path('M 105 90 L 115 80 L 125 100 L 140 80 L 150 90 L 150 140 L 105 140 Z', c_robe_base)
    c8.path('M 115 80 L 125 100 L 140 80', c_robe_hi, fill=False)
    c8.outline(c_outline)
    layers.append(c8)

    # Layer 9: Skirt Front
    c9 = new_canvas(256, 256)
    c9.path('M 105 135 L 150 135 L 180 215 C 150 220 110 215 80 205 C 95 180 100 150 105 135 Z', c_robe_base)
    c9.path('M 115 135 Q 110 170 85 200 Q 105 170 125 135 Z', c_robe_hi)
    c9.path('M 135 135 Q 140 170 130 210 Q 150 180 145 135 Z', c_robe_hi)
    c9.path('M 125 135 Q 125 180 105 210', c_robe_shadow, fill=False)
    c9.outline(c_outline)
    layers.append(c9)

    # Layer 10: Sash
    c10 = new_canvas(256, 256)
    c10.path('M 103 130 L 152 135 L 150 145 L 101 140 Z', c_sash)
    c10.circle(105, 135, 4, c_sash_hi)
    c10.path('M 105 135 Q 70 160 50 145 Q 75 140 103 130 Z', c_sash_hi)
    c10.path('M 103 140 Q 60 170 40 160 Q 70 150 101 140 Z', c_sash)
    c10.outline(c_outline)
    layers.append(c10)

    # Layer 11: Sword
    c11 = new_canvas(256, 256)
    c11.path('M 88 135 L 70 230 L 78 232 L 96 135 Z', c_sword_scab)
    c11.path('M 88 135 L 70 230', c_sword_hi, fill=False)
    c11.path('M 82 135 L 102 131 L 103 127 L 83 131 Z', c_sword_hilt)
    c11.path('M 88 130 L 85 110 L 93 108 L 96 130 Z', c_robe_shadow)
    c11.circle(84, 105, 4, c_sword_hilt) # Pommel
    c11.outline(c_outline)
    layers.append(c11)

    # Layer 12: Front Arm & Hand
    c12 = new_canvas(256, 256)
    c12.path('M 110 85 L 80 115 L 90 110 L 125 90 Z', c_robe_base)
    c12.path('M 80 115 L 89 106 Q 100 130 85 170 Q 70 150 80 115 Z', c_robe_base)
    c12.path('M 89 106 Q 100 130 85 170', c_robe_hi, fill=False)
    c12.circle(89, 112, 5, c_skin) # Hand
    c12.outline(c_outline)
    layers.append(c12)

    # Layer 13: Front Hair
    c13 = new_canvas(256, 256)
    c13.path('M 110 65 Q 80 85 60 80 Q 85 95 115 80 Z', c_hair)
    c13.path('M 135 65 Q 140 95 155 110 Q 145 85 140 65 Z', c_hair)
    c13.outline(c_outline)
    layers.append(c13)

    # Layer 14: Hat
    c14 = new_canvas(256, 256)
    c14.path('M 60 65 Q 120 85 180 55 Q 150 25 120 15 Q 90 30 60 65 Z', c_hat)
    for i in range(1, 5):
        c14.path(f'M {60 + i*15} {65 - i*5} Q 120 {85 - i*10} {180 - i*10} {55 - i*5}', c_hat_shadow, fill=False)
    c14.outline(c_outline)
    layers.append(c14)

    final = flatten(layers)
    
    fg_mist = new_canvas(256, 256)
    fg_mist.rect(0, 220, 256, 36, '#D0D8E0')
    fg_mist.dither(0, 210, 256, 10, ['#D0D8E0', 'transparent'], pattern='bayer4')
    fg_mist.rect(0, 235, 256, 21, '#E0E8F0')
    fg_mist.dither(0, 225, 256, 10, ['#E0E8F0', 'transparent'], pattern='bayer4')
    
    final = flatten([final, fg_mist])

    finish(final)

draw()
