import numpy as np
from pixelbench_api import *

def create_sky_pirate():
    c = new_canvas(64, 64)
    
    # 36-color palette
    P = {
        '.': None,
        
        # Outlines & dark accents
        'K': '#140c18', # Deepest dark / eyelashes / pupil
        'B': '#0b162c', # Dark navy coat outline
        
        # Skin tones
        's0': '#fff6f0', # Highlight
        's1': '#fedccb', # Base skin
        's2': '#f0a88c', # Soft shade
        's3': '#c77058', # Deep shadow (under chin/jaw)
        'sb': '#f88888', # Cute cheek blush
        'sm': '#6e1820', # Smirk line
        'sp': '#de4c58', # Lip tint
        
        # Hair (Golden Honey / Amber Blonde)
        'h0': '#fff8be', # Hair shine
        'h1': '#fad45c', # Hair light
        'h2': '#d9992e', # Hair midtone
        'h3': '#9a5c18', # Hair shade
        'h4': '#5a300a', # Deep hair undercut
        'h5': '#381c06', # Darkest hair contour
        
        # Eyes & Glass (Sky Cyan / Teal)
        'e0': '#ffffff', # Specular glint
        'e1': '#d8f6fc', # Glass/sclera light
        'e2': '#9ec2d4', # Sclera shadow
        'e3': '#36eed6', # Bright glowing cyan
        'e4': '#14a89f', # Mid teal
        'e5': '#0c5c64', # Dark teal
        
        # Goggles Brass & Gold Accents
        'g0': '#fff9c4', # Brass specular
        'g1': '#ecc044', # Brass light
        'g2': '#b07a1c', # Brass mid
        'g3': '#6d420a', # Brass shadow
        'g4': '#3a1e04', # Brass dark rim
        
        # Leather
        'l0': '#7a4224',
        'l1': '#4a2412',
        'l2': '#261006',
        
        # Red Scarf (Vibrant Crimson)
        'r0': '#ff7884', # Highlight fold
        'r1': '#e63246', # Rich crimson
        'r2': '#af172a', # Scarf mid
        'r3': '#720b18', # Scarf shadow
        'r4': '#3c0309', # Deepest crease
        
        # Navy Coat (Deep Indigo / Navy)
        'c0': '#6a94c6', # Rim light / seam
        'c1': '#3e6594', # Coat light
        'c2': '#243a5e', # Coat navy base
        'c3': '#15243e', # Coat shadow
        
        # Inner shirt
        'w0': '#ffffff',
        'w1': '#ded7cb',
        'w2': '#9e9484',
    }

    grid = [['.' for _ in range(64)] for _ in range(64)]

    def set_p(x, y, col):
        if 0 <= x < 64 and 0 <= y < 64:
            grid[y][x] = col

    def fill_poly(pts, col):
        pts = np.array(pts, dtype=float)
        min_y = max(0, int(np.floor(np.min(pts[:, 1]))))
        max_y = min(63, int(np.ceil(np.max(pts[:, 1]))))
        n = len(pts)
        for y in range(min_y, max_y + 1):
            nodes = []
            for i in range(n):
                j = (i + 1) % n
                y1 = pts[i, 1]
                y2 = pts[j, 1]
                x1 = pts[i, 0]
                x2 = pts[j, 0]
                if (y1 <= y < y2) or (y2 <= y < y1):
                    x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                    nodes.append(x)
            nodes.sort()
            for i in range(0, len(nodes), 2):
                if i + 1 < len(nodes):
                    x_start = max(0, int(np.round(nodes[i])))
                    x_end = min(63, int(np.round(nodes[i+1])))
                    for x in range(x_start, x_end + 1):
                        set_p(x, y, col)

    # ==========================================
    # 1. BACK HAIR (Dynamic wind-swept flowing mane)
    # ==========================================
    # Top plume:
    fill_poly([(30, 8), (42, 3), (53, 4), (60, 8), (56, 11), (45, 9), (34, 10)], 'h3')
    fill_poly([(32, 7), (42, 4), (52, 5), (57, 8), (48, 8), (36, 9)], 'h2')
    fill_poly([(36, 6), (43, 4), (50, 6), (44, 7)], 'h1')
    fill_poly([(39, 4), (45, 4)], 'h0')

    # Main upper sweep:
    fill_poly([(34, 10), (48, 8), (58, 10), (63, 14), (58, 17), (47, 14), (34, 15)], 'h4')
    fill_poly([(35, 11), (48, 9), (57, 11), (61, 14), (56, 16), (46, 13), (35, 14)], 'h3')
    fill_poly([(36, 12), (48, 10), (55, 12), (58, 14), (52, 14), (44, 12)], 'h2')
    fill_poly([(38, 11), (47, 10), (52, 12)], 'h1')

    # Mid hair sweep:
    fill_poly([(33, 15), (47, 14), (57, 16), (63, 20), (57, 23), (46, 19), (33, 20)], 'h4')
    fill_poly([(34, 16), (47, 15), (56, 17), (61, 20), (55, 22), (45, 18), (34, 19)], 'h3')
    fill_poly([(35, 17), (46, 16), (54, 18), (57, 20), (51, 20), (43, 17)], 'h2')
    fill_poly([(38, 17), (46, 16), (51, 18)], 'h1')

    # Lower hair sweep:
    fill_poly([(32, 19), (45, 19), (55, 22), (61, 27), (54, 29), (44, 25), (32, 25)], 'h5')
    fill_poly([(33, 20), (45, 20), (54, 23), (58, 26), (53, 28), (43, 24), (33, 24)], 'h4')
    fill_poly([(34, 21), (44, 21), (51, 24), (55, 26), (49, 26), (41, 23)], 'h3')
    fill_poly([(36, 22), (43, 22), (48, 25)], 'h2')

    # Deep hair under-shadow behind neck:
    fill_poly([(31, 24), (42, 25), (51, 30), (55, 34), (49, 35), (39, 30), (31, 29)], 'h5')
    fill_poly([(32, 25), (41, 26), (49, 31), (52, 33), (47, 33), (38, 29)], 'h4')
    fill_poly([(33, 26), (40, 27), (46, 31)], 'h3')

    # Wisps at outer tips:
    set_p(61, 7, 'h2')
    set_p(62, 8, 'h3')
    set_p(63, 13, 'h2')
    set_p(62, 15, 'h4')
    set_p(63, 19, 'h3')
    set_p(62, 21, 'h4')
    set_p(60, 28, 'h4')
    set_p(55, 34, 'h5')

    # ==========================================
    # 2. TORSO & COAT (Base)
    # ==========================================
    # Left shoulder & sleeve:
    fill_poly([(8, 63), (8, 55), (13, 50), (19, 47), (24, 48), (22, 63)], 'c2')
    fill_poly([(9, 54), (13, 50), (18, 48), (17, 51), (12, 54), (9, 57)], 'c1')
    fill_poly([(11, 51), (15, 49), (16, 50), (12, 53)], 'c0') # rim highlight
    fill_poly([(8, 58), (11, 55), (13, 56), (12, 63), (8, 63)], 'c3')
    fill_poly([(8, 61), (10, 58), (10, 63)], 'B')

    # Right shoulder:
    fill_poly([(33, 47), (43, 49), (50, 53), (52, 63), (32, 63)], 'c2')
    fill_poly([(42, 50), (49, 54), (52, 63), (47, 63), (45, 56), (39, 52)], 'c3')
    fill_poly([(48, 56), (51, 59), (52, 63), (48, 63)], 'B')

    # Chest & inner shirt:
    fill_poly([(22, 45), (34, 45), (33, 63), (22, 63)], 'c2')
    # Shirt V-opening
    fill_poly([(26, 43), (31, 43), (30, 53), (27, 53)], 'w1')
    fill_poly([(27, 43), (30, 43), (29, 51), (28, 51)], 'w0')
    set_p(28, 52, 'w2')
    set_p(29, 52, 'w2')
    # Gold compass pendant at shirt
    set_p(28, 51, 'g1')
    set_p(29, 51, 'g0')

    # Coat lapels / V-opening
    fill_poly([(22, 45), (26, 51), (25, 63), (21, 63)], 'c3')
    fill_poly([(34, 45), (30, 51), (31, 63), (35, 63)], 'c3')
    
    # Left shoulder epaulette (brass trim)
    fill_poly([(12, 51), (16, 49), (17, 50), (13, 52)], 'g1')
    set_p(13, 50, 'g0')
    set_p(15, 49, 'g0')
    set_p(12, 52, 'g2')

    # Polished brass buttons (2x2 clusters)
    # Button 1 (top-left)
    set_p(23, 54, 'g0')
    set_p(24, 54, 'g1')
    set_p(23, 55, 'g2')
    set_p(24, 55, 'g3')
    # Button 2 (bottom-left)
    set_p(22, 60, 'g0')
    set_p(23, 60, 'g1')
    set_p(22, 61, 'g2')
    set_p(23, 61, 'g3')
    # Button 3 (top-right)
    set_p(31, 53, 'g0')
    set_p(32, 53, 'g1')
    set_p(31, 54, 'g2')
    set_p(32, 54, 'g3')
    # Button 4 (bottom-right)
    set_p(32, 59, 'g0')
    set_p(33, 59, 'g1')
    set_p(32, 60, 'g2')
    set_p(33, 60, 'g3')

    # Popped Coat Collars:
    # Left collar
    fill_poly([(15, 43), (19, 38), (22, 42), (19, 47), (15, 45)], 'c3')
    fill_poly([(16, 42), (19, 38), (21, 41), (18, 45)], 'c1')
    set_p(19, 38, 'c0')
    set_p(20, 39, 'c0')
    set_p(21, 40, 'c0')

    # Right collar
    fill_poly([(33, 40), (37, 37), (39, 41), (35, 45)], 'c3')
    fill_poly([(34, 40), (37, 37), (38, 40)], 'c1')
    set_p(37, 37, 'c0')

    # ==========================================
    # 3. NECK & HEAD BASE
    # ==========================================
    # Neck: compact, neatly nestled into scarf
    fill_poly([(25, 34), (32, 33), (33, 38), (25, 38)], 's3')
    fill_poly([(26, 34), (31, 34), (32, 37), (27, 37)], 's2')

    # Face base:
    face_pts = [
        (23, 17), (29, 15), (35, 17), (37, 21), (37, 28),
        (34, 32), (29, 35), (24, 36), (21, 33), (20, 30), (20, 28), (21, 25), (22, 21)
    ]
    fill_poly(face_pts, 's1')

    # Forehead tone
    fill_poly([(24, 18), (30, 16), (34, 18), (33, 22), (25, 22)], 's1')
    # Soft forehead shadow under bangs:
    for x in range(24, 33):
        if grid[19][x] == 's1':
            set_p(x, 19, 's2')

    # Soft cheeks
    fill_poly([(21, 27), (27, 26), (27, 32), (22, 33)], 's1')
    fill_poly([(28, 27), (35, 26), (35, 31), (30, 33)], 's1')
    
    # Soft jaw contour only at bottom edge:
    for x in range(24, 30): set_p(x, 35, 's2')
    set_p(30, 34, 's2')
    set_p(31, 33, 's2')
    set_p(32, 32, 's2')

    # Chin tip definition:
    set_p(23, 35, 's1')
    set_p(24, 35, 's1')
    set_p(24, 36, 's2')
    set_p(25, 36, 's3')

    # Neat Anime Ear:
    fill_poly([(35, 26), (37, 26), (37, 30), (35, 30)], 's2')
    set_p(36, 27, 's3')
    # Gold Hoop Earring:
    set_p(37, 29, 'g1')
    set_p(37, 30, 'g0')
    set_p(36, 30, 'g2')

    # Cute Cheek Blush:
    set_p(22, 27, 'sb')
    set_p(23, 27, 'sb')
    set_p(25, 27, 'sb')
    set_p(26, 27, 'sb')
    
    set_p(31, 27, 'sb')
    set_p(32, 27, 'sb')
    set_p(33, 27, 'sb')

    # ==========================================
    # 4. FACIAL FEATURES (Crisp, expressive anime!)
    # ==========================================
    # Nose: cute, clear 3/4 anime profile!
    set_p(20, 29, 's2')
    set_p(20, 30, 's3') # nose tip definition
    set_p(21, 29, 's0') # nose highlight
    set_p(21, 30, 's1')

    # Confident Smirk Mouth:
    set_p(24, 33, 'sm')
    set_p(25, 33, 'sp')
    set_p(26, 33, 'sm')
    set_p(27, 32, 'sm') # smug upturned corner!
    set_p(25, 34, 's2') # lower lip soft shadow

    # --- LEFT EYE (Near eye, viewer's left) ---
    # Eyebrow: sharp, confident anime brow
    set_p(22, 20, 'h3')
    set_p(23, 19, 'h4')
    set_p(24, 18, 'h4')
    set_p(25, 18, 'h4')
    set_p(26, 19, 'h3')
    set_p(27, 20, 'h3')

    # Upper lash line
    set_p(22, 22, 'K')
    set_p(23, 22, 'K')
    set_p(24, 21, 'K')
    set_p(25, 21, 'K')
    set_p(26, 21, 'K')
    set_p(27, 21, 'K')
    set_p(28, 22, 'K')
    set_p(29, 21, 'K') # cat-eye flick!

    # Sclera
    set_p(23, 23, 'e2')
    set_p(24, 23, 'e1')
    set_p(27, 23, 'e1')
    set_p(28, 23, 'e1')
    set_p(28, 24, 'e2')

    # Iris & Pupil
    set_p(24, 24, 'e0') # Specular sparkle!
    set_p(25, 22, 'K')  # Pupil top
    set_p(26, 22, 'e5')
    set_p(25, 23, 'K')  # Pupil center
    set_p(26, 23, 'e4')
    set_p(25, 24, 'e3') # Bright glowing cyan bottom
    set_p(26, 24, 'e3')
    set_p(27, 24, 'e4')
    set_p(25, 25, 'e4')
    set_p(26, 25, 'e3')

    # Lower eyelid
    set_p(25, 26, 's2')
    set_p(26, 26, 's3')
    set_p(27, 25, 'K')

    # --- RIGHT EYE (Far eye, in 3/4 perspective) ---
    # Eyebrow:
    set_p(31, 19, 'h3')
    set_p(32, 18, 'h4')
    set_p(33, 18, 'h4')
    set_p(34, 19, 'h3')

    # Upper lash line
    set_p(31, 21, 'K')
    set_p(32, 21, 'K')
    set_p(33, 21, 'K')
    set_p(34, 21, 'K')
    set_p(35, 22, 'K')

    # Sclera & Iris: matching left eye gaze!
    set_p(31, 22, 'e2')
    set_p(32, 22, 'e1')
    set_p(34, 22, 'e1')
    set_p(35, 23, 's2')

    set_p(32, 23, 'e0') # Shine
    set_p(33, 22, 'K')  # Pupil
    set_p(33, 23, 'e4')
    set_p(32, 24, 'e3') # Glowing cyan
    set_p(33, 24, 'e3')

    # Lower lid
    set_p(33, 25, 's3')
    set_p(34, 24, 'K')

    # ==========================================
    # 5. RED SCARF (Wrapped snug under chin + Dynamic fluttering tails)
    # ==========================================
    # Wrap directly under chin/jaw (y=36..43):
    # Top roll:
    fill_poly([(22, 36), (28, 35), (35, 36), (35, 40), (28, 40), (22, 38)], 'r2')
    fill_poly([(23, 36), (28, 35), (34, 36), (33, 39), (28, 39), (23, 37)], 'r1')
    fill_poly([(24, 36), (28, 36), (32, 37)], 'r0') # highlight fold

    # Bottom roll & knot:
    fill_poly([(21, 39), (35, 39), (36, 44), (22, 44)], 'r3')
    fill_poly([(23, 40), (34, 40), (34, 43), (24, 43)], 'r2')
    fill_poly([(25, 40), (32, 40), (31, 42), (26, 42)], 'r1')
    fill_poly([(27, 41), (30, 41)], 'r0')

    # Folds & creases
    set_p(22, 39, 'r4')
    set_p(27, 40, 'r4')
    set_p(33, 41, 'r4')
    set_p(35, 43, 'r4')

    # Flowing scarf tails (Fluttering heroically in the wind to the right into the sky!):
    # Upper tail:
    t1_pts = [
        (34, 40), (40, 38), (47, 37), (54, 39), (60, 41), (63, 43),
        (61, 46), (55, 45), (48, 43), (41, 43), (34, 43)
    ]
    fill_poly(t1_pts, 'r2')
    fill_poly([(35, 40), (41, 39), (48, 38), (54, 40), (60, 42), (55, 43), (48, 41), (41, 41), (35, 42)], 'r1')
    fill_poly([(42, 39), (48, 39), (53, 41)], 'r0')
    # Tail 1 shadows:
    for x in range(35, 42): set_p(x, 43, 'r3')
    for x in range(42, 49): set_p(x, 43, 'r3')
    for x in range(49, 56): set_p(x, 45, 'r3')
    for x in range(56, 62): set_p(x, 46, 'r3')
    set_p(63, 43, 'r4')
    set_p(62, 45, 'r4')

    # Lower tail:
    t2_pts = [
        (35, 43), (42, 45), (50, 47), (57, 49), (61, 52),
        (56, 54), (48, 51), (41, 49), (35, 46)
    ]
    fill_poly(t2_pts, 'r3')
    fill_poly([(36, 44), (42, 46), (50, 48), (56, 50), (52, 51), (44, 49), (37, 46)], 'r2')
    fill_poly([(43, 47), (49, 49), (46, 50)], 'r1')
    set_p(61, 52, 'r4')
    set_p(60, 53, 'r4')

    # ==========================================
    # 6. FRONT HAIR & BANGS (Full, gorgeous anime styling!)
    # ==========================================
    # Hair Crown behind goggles (Solid golden blonde hair):
    fill_poly([(22, 6), (32, 4), (40, 5), (41, 12), (32, 12), (22, 12)], 'h2')
    fill_poly([(24, 6), (32, 5), (39, 6), (38, 9), (31, 8), (24, 8)], 'h1')
    fill_poly([(27, 5), (33, 5), (36, 6)], 'h0')

    # Left side hair lock (cascading beside face and tapering smoothly):
    fill_poly([(17, 16), (22, 15), (22, 24), (19, 30), (17, 33), (16, 30), (16, 23)], 'h3')
    fill_poly([(18, 17), (21, 16), (21, 23), (19, 29), (17, 24)], 'h2')
    fill_poly([(18, 19), (20, 22)], 'h1')
    set_p(17, 33, 'h4')
    set_p(16, 34, 'h5')

    # Forehead bangs (Solid hair layers, no weird gaps):
    # Left bang:
    fill_poly([(21, 14), (24, 14), (23, 20), (20, 19)], 'h1')
    set_p(23, 20, 'h2')
    set_p(20, 19, 'h3')

    # Center-left swooping bang:
    fill_poly([(24, 13), (28, 13), (27, 20), (25, 20)], 'h2')
    fill_poly([(25, 14), (27, 14), (26, 19)], 'h1')
    fill_poly([(26, 15), (27, 16)], 'h0')
    set_p(27, 20, 'h3')
    set_p(26, 20, 'h4')

    # Center bang (Solid hair connecting right under goggle bridge):
    fill_poly([(28, 12), (33, 12), (32, 19), (29, 19)], 'h2')
    fill_poly([(29, 13), (32, 13), (31, 18), (30, 18)], 'h1')
    fill_poly([(29, 14), (31, 14), (30, 16)], 'h0')
    set_p(30, 19, 'h3')
    set_p(31, 19, 'h3')

    # Right side bang:
    fill_poly([(33, 13), (37, 13), (37, 22), (35, 26), (34, 23), (34, 16)], 'h2')
    fill_poly([(34, 14), (36, 14), (36, 21), (35, 22)], 'h1')
    set_p(35, 26, 'h3')
    set_p(34, 25, 'h4')

    # Dynamically swept wisp across forehead:
    fill_poly([(27, 15), (32, 16), (36, 17), (32, 17)], 'h0')

    # ==========================================
    # 7. GOGGLES (Distinct Oval Brass Rims, Cyan Glass, Leather Strap!)
    # ==========================================
    # Leather strap:
    fill_poly([(16, 14), (22, 12), (22, 14), (16, 16)], 'l1')
    set_p(17, 14, 'l0')
    fill_poly([(41, 10), (48, 11), (48, 13), (41, 12)], 'l1')
    set_p(43, 11, 'g1') # brass adjustment buckle
    set_p(43, 12, 'g0')

    # --- LEFT GOGGLE (Round brass aviator goggle) ---
    # Center around (26, 11), radius 4
    g1_outer = [
        (24, 7), (25, 7), (26, 7), (27, 7), (28, 7),
        (23, 8), (29, 8),
        (22, 9), (30, 9),
        (21, 10), (31, 10),
        (21, 11), (31, 11),
        (21, 12), (31, 12),
        (22, 13), (30, 13),
        (23, 14), (29, 14),
        (24, 15), (25, 15), (26, 15), (27, 15), (28, 15)
    ]
    for x, y in g1_outer:
        set_p(x, y, 'g2')
    # Highlights top-left
    for x, y in [(24, 7), (25, 7), (26, 7), (23, 8), (22, 9), (21, 10), (21, 11)]:
        set_p(x, y, 'g0')
    for x, y in [(27, 7), (28, 7), (29, 8), (30, 9), (22, 10), (22, 11)]:
        set_p(x, y, 'g1')
    # Shadows bottom-right
    for x, y in [(31, 11), (31, 12), (30, 13), (29, 14), (28, 15), (27, 15), (26, 15)]:
        set_p(x, y, 'g3')
    set_p(31, 12, 'g4')
    set_p(30, 13, 'g4')

    # Left Lens (Teal glass with diagonal highlight):
    fill_poly([(24, 9), (28, 9), (29, 11), (29, 12), (28, 14), (24, 14), (23, 12), (23, 11)], 'e5')
    fill_poly([(24, 10), (27, 10), (28, 11), (28, 13), (25, 13), (24, 12)], 'e4')
    fill_poly([(25, 10), (27, 10), (27, 12), (25, 12)], 'e3')
    # Diagonal reflection gleam!
    set_p(25, 10, 'e0')
    set_p(26, 11, 'e0')
    set_p(27, 12, 'e0')
    set_p(28, 13, 'e1')

    # Center Bridge connecting goggles:
    fill_poly([(30, 10), (33, 9), (33, 12), (30, 12)], 'g3')
    fill_poly([(30, 10), (33, 9), (33, 11), (30, 11)], 'g1')
    set_p(31, 9, 'g0')
    set_p(32, 9, 'g0')
    set_p(31, 11, 'g4')

    # --- RIGHT GOGGLE (In 3/4 perspective) ---
    # Center (37, 10)
    g2_outer = [
        (35, 6), (36, 6), (37, 6), (38, 6), (39, 6),
        (34, 7), (40, 7),
        (33, 8), (41, 8),
        (32, 9), (42, 9),
        (32, 10), (42, 10),
        (32, 11), (42, 11),
        (33, 12), (41, 12),
        (34, 13), (40, 13),
        (35, 14), (36, 14), (37, 14), (38, 14), (39, 14)
    ]
    for x, y in g2_outer:
        set_p(x, y, 'g2')
    # Highlights
    for x, y in [(35, 6), (36, 6), (37, 6), (34, 7), (33, 8), (32, 9), (32, 10)]:
        set_p(x, y, 'g0')
    for x, y in [(38, 6), (39, 6), (40, 7), (33, 9), (33, 10)]:
        set_p(x, y, 'g1')
    # Shadows
    for x, y in [(42, 10), (42, 11), (41, 12), (40, 13), (39, 14), (38, 14), (37, 14)]:
        set_p(x, y, 'g3')
    set_p(42, 11, 'g4')
    set_p(41, 12, 'g4')

    # Right Lens:
    fill_poly([(35, 8), (39, 8), (40, 10), (40, 11), (39, 13), (35, 13), (34, 11), (34, 10)], 'e5')
    fill_poly([(35, 9), (38, 9), (39, 10), (39, 12), (36, 12), (35, 11)], 'e4')
    fill_poly([(36, 9), (38, 9), (38, 11), (36, 11)], 'e3')
    # Gleam:
    set_p(36, 9, 'e0')
    set_p(37, 10, 'e0')
    set_p(38, 11, 'e0')
    set_p(39, 12, 'e1')

    # ==========================================
    # 8. FINISHING FLYAWAYS & CLEANUP
    # ==========================================
    # Extra cute wind-blown strands atop head
    set_p(29, 4, 'h1')
    set_p(30, 3, 'h0')
    set_p(31, 3, 'h1')
    set_p(43, 2, 'h0')
    set_p(44, 1, 'h1')

    # Convert grid to canvas
    for y in range(64):
        for x in range(64):
            key = grid[y][x]
            if key != '.' and key in P:
                c.set(x, y, P[key])

    print("Stats:", c.stats_text())
    return c

c = create_sky_pirate()
view(c)
finish(c)
