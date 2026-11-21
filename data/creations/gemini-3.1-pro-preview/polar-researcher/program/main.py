from pixelbench_api import new_canvas, flatten, save, view, finish

def draw_researcher():
    c = new_canvas(48, 48)
    
    # Colors
    outline = '#1a1a24'
    parka_base = '#d94816'
    parka_light = '#f26d24'
    parka_dark = '#a62d08'
    
    fur_base = '#e8e9eb'
    fur_light = '#ffffff'
    
    pants_base = '#2b4162'
    pants_light = '#46638a'
    pants_dark = '#17253d'
    
    boot_base = '#3b312b'
    boot_dark = '#1f1915'
    
    goggle_frame = '#222222'
    goggle_lens = '#0077b6'
    goggle_refl1 = '#90e0ef'
    goggle_refl2 = '#ffffff'
    
    case_base = '#8b939c'
    case_light = '#b0b7bd'
    case_dark = '#5e656e'
    case_accent = '#f2d338'
    
    glove_base = '#222222'
    skin = '#f5c3a4'
    wind_color = '#c8cdd4'

    # 1. Back arm (Left arm)
    c.poly([(26, 16), (28, 20), (18, 24), (12, 28), (10, 26), (16, 20)], parka_dark)
    c.circle(11, 27, 3, glove_base)

    # 2. Back leg (Left leg)
    c.poly([(22, 26), (24, 30), (16, 36), (10, 43), (6, 41), (12, 32)], pants_dark)
    c.poly([(4, 42), (12, 42), (12, 46), (2, 46)], boot_dark)

    # 3. Front leg (Right leg)
    c.poly([(22, 26), (26, 26), (32, 34), (34, 43), (29, 43), (27, 34)], pants_base)
    c.poly([(24, 26), (26, 26), (32, 34), (32, 43), (29, 43), (28, 34)], pants_light)
    c.poly([(28, 42), (34, 42), (38, 46), (28, 46)], boot_base)

    # 4. Torso
    c.circle(28, 18, 6, parka_base)
    c.circle(23, 26, 5, parka_base)
    c.circle(27, 25, 4, parka_base)
    c.poly([(22, 18), (34, 18), (28, 26), (18, 26)], parka_base)
    
    # Shading on Torso
    c.circle(28, 18, 4, parka_light)
    c.poly([(24, 18), (32, 18), (28, 24), (20, 24)], parka_light)
    
    # Shadow under hood
    c.circle(26, 20, 4, parka_dark)

    # 5. Sample Case
    c.rect(29, 31, 8, 2, case_dark) # Handle
    c.rect(27, 33, 14, 10, case_base)
    c.rect(27, 33, 14, 2, case_light)
    c.rect(27, 41, 14, 2, case_dark)
    c.rect(29, 33, 2, 10, case_accent)
    c.rect(37, 33, 2, 10, case_accent)
    c.rect(33, 35, 2, 2, case_light) # latch

    # 6. Front arm (Right arm)
    c.poly([(26, 18), (30, 18), (34, 24), (36, 32), (32, 32), (30, 24)], parka_base)
    c.poly([(27, 18), (30, 18), (34, 24), (35, 32), (33, 32), (31, 24)], parka_light)
    c.circle(34, 32, 3, glove_base)

    # 7. Hood
    c.circle(26, 14, 7, parka_base)
    c.circle(25, 14, 5, parka_light)
    
    # 8. Back fur
    for x, y, r in [(32, 12, 5), (30, 8, 4), (29, 17, 4), (27, 6, 3), (26, 19, 3), (24, 5, 2), (23, 20, 2)]:
        c.circle(x, y, r, fur_base)
        
    # 9. Face
    c.rect(33, 9, 4, 6, skin)
    c.rect(37, 10, 1, 4, skin)
    
    # 10. Goggles
    c.rect(34, 10, 5, 4, goggle_frame)
    c.rect(35, 11, 4, 2, goggle_lens)
    c.set(36, 11, goggle_refl2)
    c.set(37, 11, goggle_refl1)
    c.set(37, 12, goggle_refl1)

    # 11. Front fur
    c.circle(33, 6, 3, fur_light)
    c.circle(32, 17, 3, fur_light)
    c.circle(30, 4, 2, fur_light)
    c.circle(29, 19, 2, fur_light)
    c.circle(27, 5, 2, fur_light)
    c.circle(26, 20, 2, fur_light)
    c.circle(24, 6, 1, fur_light)
    c.circle(23, 20, 1, fur_light)
    
    # 12. Outline
    c.outline(outline)

    # 13. Wind lines
    c.line(42, 10, 46, 10, wind_color)
    c.line(40, 20, 44, 20, wind_color)
    c.line(44, 30, 47, 30, wind_color)
    c.line(2, 15, 8, 15, wind_color)
    c.line(5, 25, 10, 25, wind_color)
    
    view(c)
    finish(c)

if __name__ == "__main__":
    draw_researcher()