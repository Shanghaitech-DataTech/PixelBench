from pixelbench_api import *

def build_dim_sum_chef():
    c = new_canvas(32, 32)
    
    pal = {
        '.': None,
        
        # --- Chef Hat (Toque Blanche) ---
        'H1': "#FFFFFF", # Purest white highlight
        'H2': "#EDF2F7", # Light white
        'H3': "#D6DFE8", # Soft shadow
        'H4': "#B0C0D0", # Mid shadow / crease
        'H5': "#7F94A8", # Deep fold shadow
        'H6': "#45596D", # Clean hat outline
        
        # --- Hair ---
        'B1': "#1C1410", # Darkest outline / shadow
        'B2': "#38251C", # Rich dark brown hair
        'B3': "#543A2C", # Hair warm highlight
        
        # --- Skin & Face ---
        'S1': "#FFEADA", # Highlight (nose tip, chin, brow)
        'S2': "#F8C69E", # Skin main tone
        'S3': "#E49E6F", # Skin warm shadow
        'S4': "#B3683E", # Deep shadow / finger separation
        'S5': "#3D1D0D", # Eye pupil / dark brow
        'SR': "#F27878", # Soft rosy blush cheeks
        'SM': "#C95649", # Gentle warm rosy smile tone (reads as friendly smile, not dark moustache)
        'SW': "#FFFFFF", # Eye twinkle shine
        
        # --- Red Neck Scarf / Collar Accent ---
        'C1': "#E53935", # Vibrant red scarf
        'C2': "#B71C1C", # Scarf fold / shadow
        'C3': "#7F0000", # Scarf knot / deep dark
        
        # --- White Chef Coat / Uniform ---
        'J1': "#FFFFFF", # Pure coat white
        'J2': "#EDF2F7", # Light tone
        'J3': "#CBD5E1", # Shadow
        'J4': "#94A3B8", # Deep crease
        'J5': "#475569", # Outline
        
        # --- Apron (Dark Indigo Navy) ---
        'A1': "#384E6B", # Apron pocket trim / highlight
        'A2': "#223348", # Apron main indigo fabric
        'A3': "#172332", # Apron deep shadow
        'A4': "#0E1620", # Apron silhouette outline
        
        # --- Flour Dust on Apron ---
        'F1': "#FFFFFF", # Pure flour speck / dense patch
        'F2': "#E2ECF7", # Flour smudge
        'F3': "#9EBAD6", # Flour powder haze
        'F4': "#57769A", # Faint flour dust veil
        
        # --- Bamboo Steamer Basket ---
        'Y1': "#FAE298", # Bamboo light rim highlight
        'Y2': "#E5B963", # Bamboo golden amber
        'Y3': "#C59239", # Bamboo warm mid
        'Y4': "#96651E", # Bamboo shadow
        'Y5': "#5A380A", # Bamboo dark rim / lattice
        'Y6': "#301D04", # Deep crevice / bottom rim
        'YW': "#754C16", # Bamboo horizontal binding strip tone
        
        # --- Dim Sum Buns (Baozi) ---
        'D1': "#FFFFFF", # Bun top white
        'D2': "#FFF8F0", # Bun fluffy ivory body
        'D3': "#EDE0D0", # Bun soft shading
        'D4': "#D1BBA2", # Bun crease / pleat shadow
        'DR': "#E53935", # Traditional dim sum red dot
        'DG': "#6EA33E", # Lotus leaf bright green
        'Dg': "#3A611B", # Leaf shadow green
        
        # --- Steam ---
        'M1': "#FFFFFF", # Dense steam
        'M2': "#E1EEF7", # Soft steam
        'M3': "#C2DCEB", # Faint steam edge
        
        # --- Pants & Shoes ---
        'P1': "#323842", # Pants main slate
        'P2': "#20242B", # Pants shadow
        'P3': "#13161A", # Pants outline
        'K1': "#26282E", # Shoe leather
        'K2': "#464B54", # Shoe toe highlight
        'K3': "#121315", # Shoe sole
    }
    
    g = [['.' for _ in range(32)] for _ in range(32)]
    
    def set_px(x, y, col):
        if 0 <= x < 32 and 0 <= y < 32:
            g[y][x] = col
            
    def set_sym(x_left, y, col):
        set_px(x_left, y, col)
        set_px(31 - x_left, y, col)
        
    def hline(x0, x1, y, col):
        for x in range(x0, x1 + 1):
            set_px(x, y, col)

    # ==========================================
    # 1. CHEF HAT (Toque) - rows 0 to 6
    # ==========================================
    # Row 0: Top dome curve
    hline(11, 20, 0, 'H6')
    
    # Row 1: Top puff
    set_sym(9, 1, 'H6'); set_sym(10, 1, 'H6')
    hline(11, 20, 1, 'H1')
    
    # Row 2: Upper puff
    set_sym(7, 2, 'H6'); set_sym(8, 2, 'H6')
    hline(9, 22, 2, 'H1')
    set_px(11, 2, 'H2'); set_px(15, 2, 'H3'); set_px(16, 2, 'H3'); set_px(20, 2, 'H3')
    
    # Row 3: Widest puff & vertical pleats
    set_sym(6, 3, 'H6')
    hline(7, 24, 3, 'H1')
    set_px(11, 3, 'H4'); set_px(15, 3, 'H4'); set_px(16, 3, 'H4'); set_px(20, 3, 'H4')
    set_px(12, 3, 'H3'); set_px(17, 3, 'H3'); set_px(21, 3, 'H3')
    set_px(23, 3, 'H2'); set_px(24, 3, 'H3')
    
    # Row 4: Puff body
    set_sym(6, 4, 'H6')
    hline(7, 24, 4, 'H2')
    set_px(7, 4, 'H1'); set_px(8, 4, 'H1'); set_px(9, 4, 'H1')
    set_px(11, 4, 'H5'); set_px(15, 4, 'H5'); set_px(16, 4, 'H5'); set_px(20, 4, 'H5')
    set_px(12, 4, 'H3'); set_px(17, 4, 'H3'); set_px(21, 4, 'H4')
    set_px(23, 4, 'H4'); set_px(24, 4, 'H4')
    
    # Row 5: Gathering into band
    set_sym(7, 5, 'H6')
    hline(8, 23, 5, 'H3')
    set_px(8, 5, 'H1'); set_px(9, 5, 'H2'); set_px(13, 5, 'H2'); set_px(14, 5, 'H2'); set_px(18, 5, 'H2')
    set_px(11, 5, 'H5'); set_px(15, 5, 'H5'); set_px(16, 5, 'H5'); set_px(20, 5, 'H5')
    set_px(21, 5, 'H4'); set_px(22, 5, 'H4'); set_px(23, 5, 'H5')
    
    # Row 6: Hat headband (crisp horizontal chef band)
    set_sym(7, 6, 'H6')
    hline(8, 23, 6, 'H1')
    set_px(19, 6, 'H2'); set_px(20, 6, 'H3'); set_px(21, 6, 'H3'); set_px(22, 6, 'H4'); set_px(23, 6, 'H4')
    
    # Row 7: Headband bottom shadow + Hair framing
    set_sym(7, 7, 'H6')
    hline(8, 23, 7, 'H3')
    set_px(8, 7, 'H2'); set_px(9, 7, 'H2'); set_px(10, 7, 'H2')
    set_px(19, 7, 'H4'); set_px(20, 7, 'H4'); set_px(21, 7, 'H5'); set_px(22, 7, 'H5'); set_px(23, 7, 'H5')

    # ==========================================
    # 2. HAIR & FACE (rows 8 to 13)
    # ==========================================
    # Row 8: Hair bangs and hair silhouette
    set_sym(6, 8, 'B1'); set_sym(7, 8, 'B2'); set_sym(8, 8, 'B3')
    hline(9, 22, 8, 'B2')
    set_px(12, 8, 'B3'); set_px(13, 8, 'B3'); set_px(18, 8, 'B3'); set_px(19, 8, 'B3')
    
    # Row 9: Forehead, eyebrows, side hair
    set_sym(6, 9, 'B1'); set_sym(7, 9, 'B2'); set_sym(8, 9, 'B2')
    hline(9, 22, 9, 'S2')
    # Eyebrows (warm arched dark brows):
    set_px(11, 9, 'B1'); set_px(12, 9, 'B1')
    set_px(19, 9, 'B1'); set_px(20, 9, 'B1')
    # Forehead highlight:
    set_px(15, 9, 'S1'); set_px(16, 9, 'S1')
    
    # Row 10: Eyes, Ears, Nose Bridge
    # Ears:
    set_sym(5, 10, 'B1'); set_sym(6, 10, 'S3'); set_sym(7, 10, 'S2')
    hline(8, 23, 10, 'S2')
    # Left eye: white sparkle at top-left (x=11), dark pupil (x=12)
    set_px(11, 10, 'SW'); set_px(12, 10, 'S5')
    # Right eye: white sparkle at top-left (x=19), dark pupil (x=20)
    set_px(19, 10, 'SW'); set_px(20, 10, 'S5')
    # Nose bridge:
    set_px(15, 10, 'S1'); set_px(16, 10, 'S1')
    
    # Row 11: Eyes bottom, Rosy Cheeks, Cute Nose!
    set_sym(6, 11, 'S4'); set_sym(7, 11, 'S3')
    hline(8, 23, 11, 'S2')
    # Eye bottom pupils:
    set_px(11, 11, 'S5'); set_px(12, 11, 'S5')
    set_px(19, 11, 'S5'); set_px(20, 11, 'S5')
    # Soft rosy blush cheeks:
    set_px(9, 11, 'SR'); set_px(10, 11, 'SR')
    set_px(21, 11, 'SR'); set_px(22, 11, 'SR')
    # Cute button nose:
    set_px(15, 11, 'S3'); set_px(16, 11, 'S3')
    
    # Row 12: Happy smiling mouth & Cheeks
    set_sym(7, 12, 'B1'); set_sym(8, 12, 'S3')
    hline(9, 22, 12, 'S2')
    # Gentle, charming smile:
    set_px(14, 12, 'S2')
    set_px(15, 12, 'SM'); set_px(16, 12, 'SM')
    set_px(17, 12, 'S2')
    
    # Row 13: Clean distinct chin & neck (Skin tone, separating face from scarf!)
    set_sym(8, 13, 'B1')
    hline(9, 22, 13, 'S2')
    # Chin highlight and shadow:
    set_px(15, 13, 'S1'); set_px(16, 13, 'S1')
    set_px(14, 13, 'S3'); set_px(17, 13, 'S3')
    set_px(9, 13, 'S3'); set_px(22, 13, 'S3')

    # ==========================================
    # 3. RED SCARF / COLLAR & SHOULDERS (rows 14-16)
    # ==========================================
    # Row 14: Neckerchief neatly tied at collar & white chef coat shoulders
    set_sym(6, 14, 'J5'); set_sym(7, 14, 'J5')
    hline(8, 23, 14, 'J2')
    # Red scarf neatly tied:
    hline(12, 19, 14, 'C1')
    set_px(12, 14, 'C2'); set_px(19, 14, 'C2')
    set_px(15, 14, 'C3'); set_px(16, 14, 'C3') # Center knot
    # Shoulders white coat highlights:
    set_px(8, 14, 'J1'); set_px(9, 14, 'J1'); set_px(10, 14, 'J1')
    set_px(21, 14, 'J2'); set_px(22, 14, 'J3'); set_px(23, 14, 'J3')
    
    # Row 15: Chest, Apron Bib Top, Sleeves, Steam rising
    set_sym(5, 15, 'J5'); set_sym(6, 15, 'J1'); set_sym(7, 15, 'J2'); set_sym(8, 15, 'J3')
    # Dark indigo apron bib behind buns provides ultimate contrast:
    hline(12, 19, 15, 'A2')
    set_px(12, 15, 'A3'); set_px(19, 15, 'A3') # Apron straps
    set_px(14, 15, 'F3'); set_px(17, 15, 'F4') # Flour flecks on bib
    # Steam rising from the buns!
    set_px(10, 15, 'M2'); set_px(11, 15, 'M1')
    set_px(20, 15, 'M1'); set_px(21, 15, 'M2')
    
    # Row 16: Sleeves, Steam wisps, Back rim of bamboo steamer & Bun Tops
    set_sym(4, 16, 'J5'); set_sym(5, 16, 'J1'); set_sym(6, 16, 'J2'); set_sym(7, 16, 'J3')
    # Indigo apron bib background:
    hline(9, 22, 16, 'A3')
    # Steam curls floating up:
    set_px(9, 16, 'M3'); set_px(10, 16, 'M1'); set_px(11, 16, 'M2')
    set_px(20, 16, 'M2'); set_px(21, 16, 'M1'); set_px(22, 16, 'M3')
    
    # Steamer back inner rim at outer sides:
    set_px(8, 16, 'Y5'); set_px(23, 16, 'Y5')
    
    # 3 Plump Dim Sum Buns peeking up:
    # --- Left Bun top (x=10..12) ---
    set_px(10, 16, 'D1'); set_px(11, 16, 'D1'); set_px(12, 16, 'D2')
    set_px(13, 16, 'D3') # Soft crease between buns
    # --- Center Bun top (x=14..17) ---
    set_px(14, 16, 'D2'); set_px(15, 16, 'D1'); set_px(16, 16, 'D1'); set_px(17, 16, 'D2')
    set_px(18, 16, 'D3') # Soft crease between buns
    # --- Right Bun top (x=19..21) ---
    set_px(19, 16, 'D2'); set_px(20, 16, 'D1'); set_px(21, 16, 'D1')

    # ==========================================
    # 4. BAMBOO STEAMER WITH 3 BUNS & CLEARLY DEFINED HANDS (rows 17 to 22)
    # Clear separation:
    # Hands (skin) | Steamer (bamboo) | Food (buns + leaf) | Sleeves (white)
    # ==========================================
    
    # Row 17:
    # White coat sleeve cuffs:
    set_sym(4, 17, 'J5'); set_sym(5, 17, 'J2'); set_sym(6, 17, 'J3')
    # Flour dust speck on left cuff:
    set_px(5, 17, 'F1')
    # Thumbs resting firmly on top of bamboo rim:
    set_px(7, 17, 'S4'); set_px(8, 17, 'S1') # Left thumb with highlight
    set_px(23, 17, 'S1'); set_px(24, 17, 'S4') # Right thumb with highlight
    # Steamer rim edge:
    set_px(9, 17, 'Y1'); set_px(22, 17, 'Y1')
    
    # 3 Buns in the steamer:
    # --- Left Bun (x=10..12) ---
    set_px(10, 17, 'D1'); set_px(11, 17, 'D2'); set_px(12, 17, 'D3')
    set_px(13, 17, 'D4') # Soft contact crease between buns
    # --- Center Bun (x=14..17) with classic Dim Sum RED DOT! ---
    set_px(14, 17, 'D2'); set_px(15, 17, 'D1'); set_px(16, 17, 'DR'); set_px(17, 17, 'D2')
    set_px(18, 17, 'D4') # Soft contact crease between buns
    # --- Right Bun (x=19..21) ---
    set_px(19, 17, 'D3'); set_px(20, 17, 'D1'); set_px(21, 17, 'D2')

    # Row 18:
    # Sleeve cuffs outline:
    set_sym(4, 18, 'J5'); set_sym(5, 18, 'J4')
    # Hands - index fingers curling over the bamboo rim:
    set_px(6, 18, 'S4'); set_px(7, 18, 'S2'); set_px(8, 18, 'S1')
    set_px(23, 18, 'S1'); set_px(24, 18, 'S2'); set_px(25, 18, 'S4')
    # Steamer front rim & bun bases sitting on green liner:
    set_px(9, 18, 'Y2')
    # Left bun base on green liner:
    set_px(10, 18, 'D2'); set_px(11, 18, 'D3'); set_px(12, 18, 'DG')
    set_px(13, 18, 'DG') # Green leaf liner peeking through
    # Center bun base on green liner:
    set_px(14, 18, 'D3'); set_px(15, 18, 'D2'); set_px(16, 18, 'D3'); set_px(17, 18, 'DG')
    set_px(18, 18, 'DG') # Green leaf liner peeking through
    # Right bun base on green liner:
    set_px(19, 18, 'DG'); set_px(20, 18, 'D2'); set_px(21, 18, 'D3')
    set_px(22, 18, 'Y2')

    # Row 19: Steamer Front Bamboo Wall - Upper Section
    # Hands - middle fingers gripping side:
    set_px(6, 19, 'S4'); set_px(7, 19, 'S2'); set_px(8, 19, 'S3')
    set_px(23, 19, 'S3'); set_px(24, 19, 'S2'); set_px(25, 19, 'S4')
    # Steamer front curved wall (golden bamboo with vertical slat grain):
    set_px(9, 19, 'Y5')
    hline(10, 21, 19, 'Y2')
    # Bamboo vertical slat highlights & shadows:
    set_px(10, 19, 'Y1'); set_px(13, 19, 'Y3'); set_px(14, 19, 'Y1')
    set_px(17, 19, 'Y3'); set_px(18, 19, 'Y1'); set_px(21, 19, 'Y3')
    set_px(22, 19, 'Y5')

    # Row 20: Steamer Middle - Horizontal Rattan Binding Hoop
    # Hands - ring fingers supporting sides:
    set_px(7, 20, 'S4'); set_px(8, 20, 'S3')
    set_px(23, 20, 'S3'); set_px(24, 20, 'S4')
    # Horizontal rattan hoop across middle:
    set_px(9, 20, 'YW')
    hline(10, 21, 20, 'Y3')
    # Wood grain and stitching:
    set_px(10, 20, 'Y2'); set_px(13, 20, 'YW'); set_px(14, 20, 'Y2')
    set_px(17, 20, 'YW'); set_px(18, 20, 'Y2'); set_px(21, 20, 'Y4')
    set_px(22, 20, 'YW')

    # Row 21: Steamer Lower Bamboo Wall
    # Hands - pinky fingers supporting bottom:
    set_px(8, 21, 'S4'); set_px(23, 21, 'S4')
    # Bamboo lower wall (warm shading):
    set_px(9, 21, 'Y5')
    hline(10, 21, 21, 'Y4')
    set_px(10, 21, 'Y3'); set_px(14, 21, 'Y3'); set_px(17, 21, 'Y3'); set_px(21, 21, 'Y5')
    set_px(22, 21, 'Y5')

    # Row 22: Steamer Bottom Circular Rim & Crevice
    # Apron peeking at sides:
    set_sym(6, 22, 'A4'); set_sym(7, 22, 'A2')
    # Steamer bottom hoop:
    set_px(8, 22, 'Y5')
    hline(9, 22, 22, 'Y6')
    set_px(11, 22, 'Y5'); set_px(12, 22, 'Y4'); set_px(19, 22, 'Y5'); set_px(20, 22, 'Y4')
    set_px(23, 22, 'Y5')

    # ==========================================
    # 5. FLOUR-DUSTED APRON (rows 23 to 26)
    # The dark indigo apron is vividly dusted with flour!
    # Flour handprint smudges, powder dusting, and fine white flecks.
    # ==========================================
    # Row 23:
    set_sym(6, 23, 'A4')
    set_px(7, 23, 'A2'); set_px(8, 23, 'A2')
    # Left flour hand-smudge (distinct white & light powder on dark blue):
    set_px(9, 23, 'F2'); set_px(10, 23, 'F1'); set_px(11, 23, 'F1'); set_px(12, 23, 'F3')
    # Center apron fabric with light powder scatter:
    set_px(13, 23, 'A2'); set_px(14, 23, 'F4'); set_px(15, 23, 'A3'); set_px(16, 23, 'F3'); set_px(17, 23, 'A2'); set_px(18, 23, 'A2')
    # Right flour hand-smudge:
    set_px(19, 23, 'F3'); set_px(20, 23, 'F1'); set_px(21, 23, 'F1'); set_px(22, 23, 'F2')
    set_px(23, 23, 'A2'); set_px(24, 23, 'A2'); set_px(25, 23, 'A4')

    # Row 24: Pockets & continuing flour wipe marks
    set_sym(6, 24, 'A4')
    set_px(7, 24, 'A3'); set_px(8, 24, 'A1') # Left pocket rim
    # Left pocket dusted with flour:
    set_px(9, 24, 'F1'); set_px(10, 24, 'F2'); set_px(11, 24, 'F3'); set_px(12, 24, 'F4')
    # Center apron with flour dust:
    set_px(13, 24, 'A2'); set_px(14, 24, 'A3'); set_px(15, 24, 'A2'); set_px(16, 24, 'F4'); set_px(17, 24, 'F3'); set_px(18, 24, 'A2')
    # Right pocket dusted with flour:
    set_px(19, 24, 'F4'); set_px(20, 24, 'F3'); set_px(21, 24, 'F2'); set_px(22, 24, 'F1')
    set_px(23, 24, 'A1'); set_px(24, 24, 'A3'); set_px(25, 24, 'A4')

    # Row 25: Apron lower body & fine powder flecks
    set_sym(6, 25, 'A4')
    set_px(7, 25, 'A3'); set_px(8, 25, 'A2')
    set_px(9, 25, 'F3'); set_px(10, 25, 'A2'); set_px(11, 25, 'F4'); set_px(12, 25, 'A2')
    set_px(13, 25, 'A3'); set_px(14, 25, 'A2'); set_px(15, 25, 'A2'); set_px(16, 25, 'A3'); set_px(17, 25, 'A2'); set_px(18, 25, 'A2')
    set_px(19, 25, 'A2'); set_px(20, 25, 'F4'); set_px(21, 25, 'A2'); set_px(22, 25, 'F3')
    set_px(23, 25, 'A2'); set_px(24, 25, 'A3'); set_px(25, 25, 'A4')

    # Row 26: Apron bottom hem
    set_sym(6, 26, 'A4')
    hline(7, 24, 26, 'A3')
    set_px(7, 26, 'A4'); set_px(15, 26, 'A4'); set_px(16, 26, 'A4'); set_px(24, 26, 'A4')

    # ==========================================
    # 6. PANTS & SHOES (rows 27 to 31)
    # ==========================================
    # Row 27: Dark chef pants legs
    set_px(9, 27, 'P3'); hline(10, 12, 27, 'P1'); set_px(13, 27, 'P2')
    set_px(18, 27, 'P2'); hline(19, 21, 27, 'P1'); set_px(22, 27, 'P3')
    
    # Row 28: Pants cuffs
    set_px(9, 28, 'P3'); hline(10, 12, 28, 'P1'); set_px(13, 28, 'P2')
    set_px(18, 28, 'P2'); hline(19, 21, 28, 'P1'); set_px(22, 28, 'P3')
    
    # Row 29: Shoes top
    set_px(8, 29, 'K3'); set_px(9, 29, 'K2'); hline(10, 12, 29, 'K1'); set_px(13, 29, 'K3')
    set_px(18, 29, 'K3'); hline(19, 21, 29, 'K1'); set_px(22, 29, 'K2'); set_px(23, 29, 'K3')
    
    # Row 30: Shoes body
    set_px(8, 30, 'K3'); hline(9, 12, 30, 'K1'); set_px(13, 30, 'K3')
    set_px(18, 30, 'K3'); hline(19, 22, 30, 'K1'); set_px(23, 30, 'K3')
    
    # Row 31: Shoes bottom sole
    hline(8, 13, 31, 'K3')
    hline(18, 23, 31, 'K3')

    # Paint onto canvas
    for y in range(32):
        for x in range(32):
            char = g[y][x]
            if char in pal and pal[char] is not None:
                c.set(x, y, pal[char])
                
    return c

c = build_dim_sum_chef()
print("Colors used:", len(c.palette()))
view(c)
finish(c)
