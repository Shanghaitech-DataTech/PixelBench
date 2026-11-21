import sys
from pixelbench_api import *

def build_slime():
    c = new_canvas(32, 32, name="slime")
    
    PAL = {
        # Contact shadow (thin, subtle base grounding)
        "sh_dark": "#0a1c10",
        "sh_mid": "#102a18",
        
        # Slime body - lush forest jade/emerald
        "s_out": "#081a0e",      # Deepest outline / dark crease
        "s_rim": "#0e2917",      # Outer contour shade
        "s_dark": "#123a1f",     # Core shadow
        "s_shd": "#1a4f2a",      # Body shadow
        "s_mid": "#266b37",      # Base body green
        "s_lit": "#3a8c4c",      # Lit mid green
        "s_bright": "#52b066",   # Luminous green
        "s_glow": "#6ccc7e",     # Translucent subsurface green
        "s_hi": "#92f2a4",       # Highlight green
        "s_sheen": "#caffd4",    # Mint sheen
        "s_white": "#ffffff",    # Specular white glint
        
        # Moss - velvety forest moss (chartreuse / olive)
        "m_dark": "#12260b",
        "m_shd": "#1c3d12",
        "m_mid": "#32611c",
        "m_lit": "#4f8726",
        "m_hi": "#7ab832",
        "m_bright": "#aee843",
        "m_tip": "#e0fa70",
        
        # Tiny forest flower in moss
        "fl_petal": "#fffaf0",
        "fl_shadow": "#cfc2b2",
        "fl_center": "#ffce2b",
        
        # Antlers - warm woody fawn horn
        "w_out": "#1c0e07",
        "w_dark": "#331a0d",
        "w_mid": "#563016",
        "w_lit": "#7e4822",
        "w_hi": "#ab6a36",
        "w_tip": "#d49454",
        "w_leaf": "#48b224",
        "w_leafhi": "#92f03f",
        
        # Mushroom - bright forest toadstool
        "mu_out": "#33050a",
        "mu_dark": "#590811",
        "mu_shd": "#870f1a",
        "mu_mid": "#bd1a24",
        "mu_lit": "#e62b32",
        "mu_bright": "#ff4a4a",
        "mu_hi": "#ff8282",
        "mu_spot": "#fff8f0",
        "mu_spotshd": "#d4c0ae",
        "mu_stem": "#ede1d1",
        "mu_stemshd": "#a89680",
        "mu_stemdark": "#594a3a",
        
        # Glowing Eyes - magical warm amber & brilliant gold
        "e_rim": "#4d2103",      # Deep amber socket outline
        "e_amber": "#b35705",    # Rich amber shade
        "e_gold": "#f28f08",     # Luminous gold iris
        "e_bright": "#ffbd17",   # Brilliant yellow
        "e_core": "#ffe947",     # Hot glowing core
        "e_white": "#ffffff",    # Glint / specular
        "e_halo": "#385814",     # Soft warm glow on green slime
        "e_glowlit": "#587a1a",  # Brighter glow reflection
        
        # Face details: blush & mouth
        "blush_soft": "#804842", # Soft translucent coral blush
        "blush_core": "#c4625a", # Rosy cheek flush
        "blush_hi": "#f0948b",   # Cheek highlight
        "mouth_out": "#081a0e",  # Cute mouth outline
        "mouth_crease": "#123a1f",# Soft upper mouth crease
        "mouth_pink": "#a32640", # Cute cheerful tongue
        "mouth_dark": "#4a0d1a", # Mouth shadow
    }
    
    grid = [[None for _ in range(32)] for _ in range(32)]
    def p(x, y, col):
        if 0 <= x < 32 and 0 <= y < 32:
            grid[y][x] = col

    # ==========================================
    # 1. GROUND CONTACT SHADOW (y=29)
    # Subtle grounding directly under the slime base
    # ==========================================
    for x in range(9, 23):
        p(x, 29, "sh_dark")
    for x in range(11, 21):
        p(x, 29, "sh_mid")

    # ==========================================
    # 2. MUSHROOM ON BACK (y=3..10, x=13..19)
    # ==========================================
    # Mushroom stem (behind head, emerging from moss)
    p(15, 8, "mu_stem");     p(16, 8, "mu_stemshd")
    p(15, 9, "mu_stem");     p(16, 9, "mu_stemshd")
    p(15, 10, "mu_stemshd"); p(16, 10, "mu_stemdark")
    p(14, 9, "mu_stemdark")
    
    # Mushroom cap:
    mu_rows = [
        (3, 14, 17),
        (4, 13, 18),
        (5, 12, 19),
        (6, 12, 19),
        (7, 13, 18),
    ]
    for y, x0, x1 in mu_rows:
        for x in range(x0, x1 + 1):
            p(x, y, "mu_lit")
            
    # Mushroom outline & dark shading
    for x in range(14, 18):
        p(x, 3, "mu_dark")
    p(13, 4, "mu_dark");  p(18, 4, "mu_out")
    p(12, 5, "mu_dark");  p(19, 5, "mu_out")
    p(12, 6, "mu_shd");   p(19, 6, "mu_out")
    for x in range(13, 19):
        p(x, 7, "mu_out")
        
    # Cap shading (light from top-left)
    p(14, 4, "mu_hi");     p(15, 4, "mu_bright"); p(16, 4, "mu_bright")
    p(13, 5, "mu_bright"); p(14, 5, "mu_bright"); p(15, 5, "mu_lit"); p(17, 5, "mu_shd"); p(18, 5, "mu_dark")
    p(13, 6, "mu_lit");    p(14, 6, "mu_lit");    p(17, 6, "mu_shd"); p(18, 6, "mu_dark")
    
    # White mushroom spots (Amanita cluster spots)
    p(14, 4, "mu_spot");   p(15, 4, "mu_spot")
    p(14, 5, "mu_spot");   p(15, 5, "mu_spotshd")
    p(17, 5, "mu_spot");   p(18, 5, "mu_spotshd")
    p(13, 6, "mu_spot")

    # ==========================================
    # 3. ANTLERS (y=4..12)
    # ==========================================
    # Left antler:
    p(10, 12, "w_dark")
    p(10, 11, "w_dark");  p(9, 11, "w_mid")
    p(9, 10, "w_mid");    p(8, 10, "w_lit")
    p(8, 9, "w_hi");      p(9, 9, "w_dark")
    # Left brow tine:
    p(7, 9, "w_lit");     p(6, 9, "w_mid")
    p(5, 8, "w_tip");     p(6, 8, "w_hi")
    p(5, 9, "w_out")
    # Left main beam:
    p(8, 8, "w_hi");      p(9, 8, "w_dark")
    p(7, 7, "w_lit");     p(8, 7, "w_out")
    p(7, 6, "w_tip");     p(8, 6, "w_mid")
    p(7, 5, "w_tip")
    p(8, 4, "w_tip")
    # Tiny green leaf on left antler tip!
    p(6, 5, "w_leaf")
    p(6, 4, "w_leafhi")

    # Right antler:
    p(21, 12, "w_dark")
    p(21, 11, "w_dark");  p(22, 11, "w_mid")
    p(22, 10, "w_mid");   p(23, 10, "w_lit")
    p(23, 9, "w_hi");     p(22, 9, "w_dark")
    # Right brow tine:
    p(24, 9, "w_lit");    p(25, 9, "w_mid")
    p(26, 8, "w_tip");    p(25, 8, "w_hi")
    p(26, 9, "w_out")
    # Right main beam:
    p(23, 8, "w_hi");     p(22, 8, "w_dark")
    p(24, 7, "w_lit");    p(23, 7, "w_out")
    p(24, 6, "w_tip");    p(23, 6, "w_mid")
    p(24, 5, "w_tip")
    p(23, 4, "w_tip")

    # ==========================================
    # 4. SLIME BODY SILHOUETTE & BASE VOLUME
    # ==========================================
    slime_rows = {
        10: (14, 17),
        11: (12, 19),
        12: (11, 20),
        13: (10, 21),
        14: (9, 22),
        15: (8, 23),
        16: (7, 24),
        17: (6, 25),
        18: (6, 25),
        19: (5, 26),
        20: (5, 26),
        21: (4, 27),
        22: (4, 27),
        23: (4, 27),
        24: (4, 27),
        25: (4, 27),
        26: (5, 26),
        27: (6, 25),
        28: (8, 23),
    }

    # Fill base slime
    for y, (x0, x1) in slime_rows.items():
        for x in range(x0, x1 + 1):
            p(x, y, "s_mid")

    # Smooth spherical shading:
    for y, (x0, x1) in slime_rows.items():
        for x in range(x0, x1 + 1):
            if y <= 13:
                p(x, y, "s_lit")
            elif 14 <= y <= 18:
                if x <= 16:
                    p(x, y, "s_lit")
                else:
                    p(x, y, "s_mid")
            elif 19 <= y <= 24:
                # Cheeks and mid body
                if x <= 10:
                    p(x, y, "s_lit")
                elif x >= 21:
                    p(x, y, "s_shd")
                else:
                    p(x, y, "s_mid")
            elif 25 <= y <= 27:
                # Lower belly / skirt
                if x <= 8:
                    p(x, y, "s_mid")
                elif x >= 21:
                    p(x, y, "s_shd")
                else:
                    p(x, y, "s_mid")
            else: # y == 28
                p(x, y, "s_dark")

    # Right side ambient shadow (wraparound spherical shading)
    for y in range(16, 28):
        x_edge = slime_rows[y][1]
        p(x_edge - 1, y, "s_shd")
        if y >= 20:
            p(x_edge - 2, y, "s_shd")
        if y >= 25:
            p(x_edge - 1, y, "s_dark")

    # Translucent gelatinous belly: soft round caustics
    belly_caustics = [
        (14, 24, "s_lit"), (15, 24, "s_lit"), (16, 24, "s_lit"), (17, 24, "s_lit"),
        (13, 25, "s_lit"), (14, 25, "s_bright"), (15, 25, "s_glow"), (16, 25, "s_glow"), (17, 25, "s_bright"), (18, 25, "s_lit"),
        (13, 26, "s_lit"), (14, 26, "s_bright"), (15, 26, "s_glow"), (16, 26, "s_glow"), (17, 26, "s_bright"), (18, 26, "s_lit"),
        (14, 27, "s_lit"), (15, 27, "s_bright"), (16, 27, "s_bright"), (17, 27, "s_lit"),
    ]
    for x, y, col in belly_caustics:
        p(x, y, col)

    # Subsurface bottom rim bounce light (ground reflection on bottom edge)
    for x in range(10, 22):
        p(x, 27, "s_lit")
    for x in range(11, 21):
        p(x, 28, "s_mid")

    # Specular gloss on top-left (crisp curved slime shine):
    p(11, 13, "s_hi");    p(12, 13, "s_sheen");  p(13, 13, "s_white")
    p(12, 14, "s_white"); p(13, 14, "s_sheen");  p(14, 14, "s_hi")
    p(10, 14, "s_bright");p(11, 14, "s_hi")
    p(12, 12, "s_hi");    p(13, 12, "s_bright")
    
    # Secondary squishy bounce reflection on left cheek:
    p(6, 22, "s_lit")
    p(6, 23, "s_bright"); p(7, 23, "s_hi"); p(8, 23, "s_sheen")
    p(6, 24, "s_lit");    p(7, 24, "s_bright")

    # ==========================================
    # 5. MOSS PATTERNS (velvety forest moss + tiny flower!)
    # ==========================================
    moss_head = [
        # Crest / top ridge
        (14, 10, "m_hi"), (15, 10, "m_bright"), (16, 10, "m_tip"), (17, 10, "m_hi"),
        (12, 11, "m_lit"), (13, 11, "m_hi"), (14, 11, "m_bright"), (15, 11, "m_tip"), (16, 11, "m_bright"), (17, 11, "m_hi"), (18, 11, "m_lit"),
        (11, 12, "m_mid"), (12, 12, "m_lit"), (13, 12, "m_hi"), (14, 12, "m_mid"), (15, 12, "m_shd"), (16, 12, "m_mid"), (17, 12, "m_hi"), (18, 12, "m_lit"),
        # Scalloped tufts hanging down forehead
        (12, 13, "m_shd"), (13, 13, "m_mid"), (14, 13, "m_dark"),
        (17, 13, "m_mid"), (18, 13, "m_dark"),
        # Left shoulder drape
        (10, 12, "m_shd"), (10, 13, "m_mid"), (9, 13, "m_lit"),
        (9, 14, "m_hi"), (10, 14, "m_mid"), (8, 14, "m_mid"),
        (8, 15, "m_lit"), (9, 15, "m_bright"), (9, 16, "m_dark"), (8, 16, "m_mid"),
        (7, 16, "m_dark"), (7, 17, "m_lit"), (8, 17, "m_dark"),
        # Right shoulder tuft
        (20, 12, "m_lit"), (20, 13, "m_mid"), (21, 13, "m_dark"),
        # Lower flank moss clump
        (24, 23, "m_shd"), (25, 23, "m_mid"),
        (24, 24, "m_mid"), (25, 24, "m_hi"), (26, 24, "m_lit"),
        (23, 25, "m_dark"), (24, 25, "m_lit"), (25, 25, "m_bright"), (26, 25, "m_hi"),
        (24, 26, "m_dark"), (25, 26, "m_mid"),
    ]
    for x, y, col in moss_head:
        p(x, y, col)

    # Cute 4-pixel white forest blossom nestled in moss near right antler!
    p(19, 11, "fl_petal")
    p(18, 12, "fl_petal"); p(19, 12, "fl_center"); p(20, 12, "fl_petal")
    p(19, 13, "fl_shadow")

    # ==========================================
    # 6. GLOWING EYES (Magical, luminous, expressive)
    # ==========================================
    eye_halos = [
        # Left eye glow bleed
        (10, 16, "e_halo"), (11, 16, "e_glowlit"), (12, 16, "e_glowlit"), (13, 16, "e_halo"),
        (9, 17, "e_halo"),  (14, 17, "e_halo"),
        (9, 18, "e_glowlit"),(14, 18, "e_halo"),
        (9, 19, "e_halo"),  (14, 19, "e_halo"),
        (10, 21, "e_glowlit"),(11, 21, "e_glowlit"),(12, 21, "e_glowlit"),(13, 21, "e_halo"),
        # Right eye glow bleed
        (18, 16, "e_halo"), (19, 16, "e_glowlit"), (20, 16, "e_glowlit"), (21, 16, "e_halo"),
        (17, 17, "e_halo"), (22, 17, "e_halo"),
        (17, 18, "e_halo"), (22, 18, "e_glowlit"),
        (17, 19, "e_halo"), (22, 19, "e_halo"),
        (18, 21, "e_halo"), (19, 21, "e_glowlit"),(20, 21, "e_glowlit"),(21, 21, "e_glowlit"),
    ]
    for x, y, col in eye_halos:
        if grid[y][x] and grid[y][x].startswith("s_"):
            p(x, y, col)

    # Left eye (round capsule shape)
    p(10, 17, "e_rim");   p(11, 17, "e_bright"); p(12, 17, "e_gold");   p(13, 17, "e_rim")
    p(10, 18, "e_bright");p(11, 18, "e_white");  p(12, 18, "e_core");   p(13, 18, "e_gold")
    p(10, 19, "e_gold");  p(11, 19, "e_core");   p(12, 19, "e_gold");   p(13, 19, "e_amber")
    p(10, 20, "e_rim");   p(11, 20, "e_amber");  p(12, 20, "e_amber");  p(13, 20, "e_rim")

    # Right eye (round capsule shape)
    p(18, 17, "e_rim");   p(19, 17, "e_bright"); p(20, 17, "e_gold");   p(21, 17, "e_rim")
    p(18, 18, "e_gold");  p(19, 18, "e_white");  p(20, 18, "e_core");   p(21, 18, "e_bright")
    p(18, 19, "e_amber"); p(19, 19, "e_core");   p(20, 19, "e_gold");   p(21, 19, "e_gold")
    p(18, 20, "e_rim");   p(19, 20, "e_amber");  p(20, 20, "e_amber");  p(21, 20, "e_rim")

    # ==========================================
    # 7. EXPRESSION: ADORABLE OPEN HAPPY MOUTH `:D` & ROSY BLUSH
    # ==========================================
    p(15, 21, "mouth_crease"); p(16, 21, "mouth_crease")
    p(14, 22, "mouth_out")
    p(15, 22, "mouth_pink");   p(16, 22, "mouth_pink")
    p(17, 22, "mouth_out")
    p(15, 23, "mouth_out");    p(16, 23, "mouth_out")

    # Rosy coral cheek blush under outer eyes
    p(7, 20, "blush_soft"); p(8, 20, "blush_core"); p(9, 20, "blush_soft")
    p(7, 21, "blush_soft"); p(8, 21, "blush_hi");   p(9, 21, "blush_core")
    p(22, 20, "blush_soft");p(23, 20, "blush_core");p(24, 20, "blush_soft")
    p(22, 21, "blush_core");p(23, 21, "blush_hi");  p(24, 21, "blush_soft")

    # ==========================================
    # 8. OUTLINES & CLEANUP
    # ==========================================
    for y, (x0, x1) in slime_rows.items():
        if grid[y][x0] and not grid[y][x0].startswith("w_") and not grid[y][x0].startswith("m_"):
            p(x0, y, "s_out")
        if grid[y][x1] and not grid[y][x1].startswith("w_") and not grid[y][x1].startswith("m_"):
            if y <= 16:
                p(x1, y, "s_rim")
            else:
                p(x1, y, "s_out")

    # Ground bottom contact line
    for x in range(8, 24):
        p(x, 28, "s_out")

    # Transfer grid to canvas
    for y in range(32):
        for x in range(32):
            if grid[y][x]:
                c.set(x, y, PAL[grid[y][x]])
                
    view(c)
    finish(c)
    return c

if __name__ == "__main__":
    build_slime()
