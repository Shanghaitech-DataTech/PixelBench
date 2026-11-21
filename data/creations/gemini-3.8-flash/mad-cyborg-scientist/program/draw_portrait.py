import numpy as np
from pixelbench_api import *

def build_portrait():
    c = new_canvas(64, 64, name="mad_scientist")
    
    pal = {
        # Background
        "bg_void": "#06080d",
        "bg_dark": "#0c1018",
        "bg_slate": "#141a27",
        "bg_pipe": "#181f2b",
        "bg_pipe_hi": "#2d3a4e",
        "bg_wire": "#090b10",
        "bg_gauge_rim": "#384457",
        "bg_gauge_face": "#0f1520",
        
        # Skin tones (Mad human scientist)
        "skin_void": "#241117",
        "skin_deep": "#4a252a",
        "skin_shadow": "#6e3f3b",
        "skin_crease": "#542b2d",
        "skin_mid": "#9c6356",
        "skin_light": "#c48877",
        "skin_pale": "#dfab9a",
        "skin_hi": "#f5cbbe",
        "eyebag": "#462834",
        "eyebag_dark": "#301923",
        "lip_dark": "#4f1e27",
        "lip": "#78303b",
        "lip_hi": "#a64956",
        "mouth_void": "#140608",
        "teeth_dark": "#696357",
        "teeth_mid": "#9e9381",
        "teeth_light": "#ded6c3",
        "human_iris": "#361b10",
        "human_pupil": "#0a0302",
        "sclera": "#e3decb",
        "sclera_red": "#b85c5c",
        "scar_seam": "#380f14",
        "staple": "#c4d5e8",
        
        # Metal / Cyborg (High contrast chrome & steel)
        "metal_black": "#0a0d12",
        "metal_dark": "#1a202b",
        "metal_shadow": "#293242",
        "metal_mid": "#415066",
        "metal_light": "#657896",
        "metal_bright": "#93aac7",
        "metal_gleam": "#cbe0f5",
        "metal_white": "#ffffff",
        
        # Brass / Bronze
        "brass_dark": "#341e08",
        "brass_mid": "#754512",
        "brass_light": "#ba761f",
        "brass_hi": "#f7bc3e",
        
        # Glowing cybernetic (Cyan / Neon Electric Blue)
        "glow_deep": "#002f3d",
        "glow_mid": "#006d8a",
        "glow_bright": "#00b5db",
        "glow_neon": "#3de6ff",
        "glow_white": "#eefeff",
        
        # Hair (MESSY WHITE HAIR: Bright, brilliant, electric white!)
        "hair_back": "#1a1d26",
        "hair_shadow": "#3a3f52",
        "hair_mid": "#6a7287",
        "hair_light": "#9ea7bd",
        "hair_bright": "#d4d9e6",
        "hair_white": "#ffffff",
        
        # Lab Coat
        "coat_black": "#11131b",
        "coat_shadow": "#252a38",
        "coat_mid": "#4d5469",
        "coat_light": "#7f889e",
        "coat_bright": "#b8c0d1",
        "coat_white": "#ebedf5",
        
        # Stains
        "stain_acid_dark": "#3a470c",
        "stain_acid": "#637a12",
        "stain_acid_hi": "#9ec418",
        "stain_rust": "#521e12",
        "stain_oil": "#1f1b16",
        
        # Leather Apron & Belts
        "leather_black": "#140a06",
        "leather_dark": "#26130a",
        "leather_mid": "#4a2614",
        "leather_light": "#734023",
        "leather_hi": "#9c5d35",
        "leather_stitch": "#b59c77",
        
        # Hazard stripes & cables
        "hazard_yel": "#e6a817",
        "hazard_blk": "#121317",
        "wire_red": "#a61922",
        "wire_red_hi": "#f52f3c",
        "wire_yellow": "#b87c0b",
        "wire_yellow_hi": "#ffc526",
        "wire_blue": "#144ea1",
        "wire_blue_hi": "#2e7eff",
        
        # Toxic Syringe & Glass
        "toxic_dark": "#0a4015",
        "toxic_mid": "#16b83c",
        "toxic_hi": "#5eff7e",
        "toxic_bubble": "#d4ffdc",
        "glass_body": "#628296",
        "glass_hi": "#d8f4fc",
    }

    # ====================================================
    # 1. BACKGROUND
    # ====================================================
    c.rect(0, 0, 64, 64, pal["bg_void"])
    for y in range(64):
        c.set(0, y, pal["bg_slate"])
        c.set(63, y, pal["bg_slate"])
        c.line(1, y, 62, y, pal["bg_dark"] if y < 45 else pal["bg_void"])
        c.set(2, y, pal["bg_pipe"])
        c.set(3, y, pal["bg_pipe_hi"])
        c.set(4, y, pal["bg_pipe"])
        c.set(59, y, pal["bg_pipe"])
        c.set(60, y, pal["bg_pipe_hi"])
        c.set(61, y, pal["bg_pipe"])

    c.rect(1, 21, 5, 3, pal["bg_gauge_rim"])
    c.set(3, 22, pal["brass_mid"])
    
    # Oscilloscope monitor on upper left
    c.rect(7, 4, 10, 9, pal["bg_slate"])
    c.rect(8, 5, 8, 7, pal["bg_gauge_face"])
    for gy in [6, 8, 10]:
        c.line(8, gy, 15, gy, pal["bg_dark"])
    c.set(9, 9, pal["toxic_mid"])
    c.set(10, 8, pal["toxic_hi"])
    c.set(11, 7, pal["toxic_hi"])
    c.set(12, 10, pal["toxic_mid"])
    c.set(13, 8, pal["toxic_hi"])
    c.set(14, 9, pal["toxic_mid"])
    c.set(15, 5, pal["wire_red_hi"])
    
    # Pressure gauge on right
    c.circle(58, 9, 3, pal["bg_gauge_rim"])
    c.circle(58, 9, 2, pal["bg_gauge_face"])
    c.set(58, 9, pal["brass_hi"])
    c.set(59, 8, pal["wire_red_hi"])
    
    c.path("M 16 0 Q 20 6 25 3 Q 28 1 30 0", pal["bg_wire"], fill=False)
    c.path("M 48 0 Q 52 8 57 5", pal["bg_wire"], fill=False)

    # ====================================================
    # 2. BACK HAIR (Deep layer)
    # ====================================================
    # Left back hair mass
    c.poly([(20, 16), (14, 12), (10, 16), (8, 22), (11, 30), (16, 32), (21, 28)], pal["hair_shadow"])
    # Right back hair mass
    c.poly([(42, 15), (48, 12), (53, 16), (54, 24), (49, 31), (43, 29)], pal["hair_shadow"])

    # ====================================================
    # 3. TORSO & DIRTY LAB COAT
    # ====================================================
    c.poly([(14, 42), (24, 38), (32, 40), (28, 63), (5, 63), (5, 53), (9, 45)], pal["coat_black"])
    c.poly([(15, 43), (24, 39), (30, 41), (27, 63), (7, 63), (7, 54), (11, 46)], pal["coat_shadow"])
    c.poly([(16, 44), (24, 40), (27, 43), (25, 63), (10, 63), (9, 55), (13, 48)], pal["coat_mid"])
    c.poly([(18, 45), (24, 41), (25, 44), (23, 63), (13, 63), (12, 56), (15, 50)], pal["coat_light"])
    c.poly([(20, 46), (23, 43), (24, 46), (22, 63), (16, 63), (15, 58), (17, 52)], pal["coat_bright"])

    # Popped collar
    c.poly([(19, 36), (25, 33), (27, 39), (22, 41)], pal["coat_bright"])
    c.poly([(20, 37), (24, 34), (26, 39)], pal["coat_white"])
    c.line(26, 34, 27, 39, pal["coat_mid"])
    
    # Torn right collar
    c.poly([(37, 34), (43, 37), (40, 42), (36, 40)], pal["coat_shadow"])
    c.poly([(38, 35), (42, 38), (39, 41)], pal["coat_mid"])
    c.set(43, 37, pal["coat_bright"])

    # Chemical stains
    c.set(16, 48, pal["stain_acid_dark"])
    c.set(17, 49, pal["stain_acid"])
    c.set(17, 50, pal["stain_acid_hi"])
    c.set(18, 51, pal["stain_acid"])
    c.set(18, 52, pal["stain_acid_hi"])
    c.set(18, 53, pal["stain_acid"])
    c.set(19, 54, pal["stain_acid_dark"])
    c.set(12, 57, pal["stain_acid"])
    c.set(12, 58, pal["stain_acid_hi"])
    c.set(13, 59, pal["stain_acid"])
    c.set(22, 53, pal["stain_oil"])
    c.set(23, 54, pal["stain_oil"])
    c.set(14, 52, pal["stain_rust"])
    c.set(15, 53, pal["stain_rust"])

    # ====================================================
    # 4. LEATHER APRON
    # ====================================================
    c.poly([(24, 42), (38, 42), (40, 56), (22, 56)], pal["leather_black"])
    c.poly([(25, 43), (37, 43), (39, 55), (23, 55)], pal["leather_dark"])
    c.poly([(26, 44), (36, 44), (37, 54), (24, 54)], pal["leather_mid"])
    c.poly([(27, 45), (34, 45), (35, 53), (25, 53)], pal["leather_light"])
    c.poly([(28, 46), (32, 46), (32, 51), (26, 51)], pal["leather_hi"])
    
    c.line(25, 43, 37, 43, pal["leather_stitch"])
    c.line(23, 55, 39, 55, pal["leather_dark"])
    
    # Apron straps with brass buckles
    c.line(22, 38, 25, 43, pal["leather_dark"])
    c.line(23, 38, 26, 43, pal["leather_light"])
    c.rect(24, 40, 2, 2, pal["brass_hi"])
    c.set(24, 41, pal["brass_dark"])
    
    c.line(39, 38, 36, 43, pal["leather_dark"])
    c.line(38, 38, 35, 43, pal["leather_light"])
    c.rect(36, 40, 2, 2, pal["brass_hi"])
    c.set(37, 41, pal["brass_dark"])
    
    # Apron front pocket with probe
    c.rect(26, 47, 7, 5, pal["leather_black"])
    c.rect(27, 48, 5, 4, pal["leather_dark"])
    c.line(27, 47, 31, 47, pal["leather_stitch"])
    c.line(28, 44, 28, 48, pal["metal_bright"])
    c.set(28, 43, pal["wire_red_hi"])
    c.set(28, 42, pal["wire_red"])

    # ====================================================
    # 5. TOOL BELT
    # ====================================================
    c.rect(13, 55, 35, 4, pal["leather_black"])
    c.rect(14, 56, 33, 2, pal["leather_dark"])
    c.line(14, 56, 46, 56, pal["leather_light"])
    c.line(14, 57, 46, 57, pal["leather_mid"])
    
    # Central brass buckle
    c.rect(28, 54, 7, 5, pal["brass_dark"])
    c.rect(29, 55, 5, 3, pal["brass_light"])
    c.set(30, 56, pal["brass_hi"])
    c.set(31, 56, pal["brass_dark"])
    c.set(32, 56, pal["brass_hi"])
    
    # Tool 1: Leather pouch
    c.rect(13, 56, 5, 7, pal["leather_black"])
    c.rect(14, 57, 3, 5, pal["leather_dark"])
    c.set(15, 59, pal["brass_hi"])
    
    # Tool 2: Glowing toxic syringe
    c.line(20, 53, 22, 53, pal["metal_bright"])
    c.set(21, 54, pal["metal_mid"])
    c.rect(20, 55, 3, 7, pal["glass_body"])
    c.rect(20, 56, 3, 5, pal["toxic_dark"])
    c.rect(21, 56, 2, 5, pal["toxic_mid"])
    c.set(21, 57, pal["toxic_hi"])
    c.set(21, 58, pal["toxic_bubble"])
    c.set(20, 59, pal["toxic_hi"])
    c.line(20, 55, 20, 61, pal["glass_hi"])
    c.line(21, 62, 21, 63, pal["metal_gleam"])
    c.set(21, 63, pal["toxic_hi"])
    
    # Tool 3: Steel wrench
    c.line(38, 55, 38, 62, pal["metal_shadow"])
    c.line(39, 55, 39, 62, pal["metal_mid"])
    c.line(39, 56, 39, 61, pal["metal_light"])
    c.rect(37, 61, 4, 3, pal["metal_dark"])
    c.set(37, 62, pal["metal_bright"])
    c.set(40, 62, pal["metal_bright"])
    c.set(38, 62, pal["metal_black"])
    c.set(39, 62, pal["metal_black"])
    c.set(38, 63, pal["metal_mid"])
    c.set(39, 63, pal["metal_mid"])

    # ====================================================
    # 6. NECK & THROAT
    # ====================================================
    c.poly([(25, 34), (31, 34), (31, 41), (24, 41)], pal["skin_deep"])
    c.poly([(26, 35), (31, 35), (31, 40), (25, 40)], pal["skin_shadow"])
    c.poly([(27, 36), (30, 36), (30, 39), (26, 39)], pal["skin_mid"])
    c.line(28, 35, 27, 40, pal["skin_light"])
    c.set(28, 37, pal["skin_pale"])
    
    # Right neck (Cyborg piston & spine)
    c.rect(31, 34, 8, 8, pal["metal_black"])
    for sy in [34, 36, 38, 40]:
        c.rect(32, sy, 3, 2, pal["metal_shadow"])
        c.set(33, sy, pal["metal_mid"])
    c.line(36, 34, 37, 41, pal["metal_light"])
    c.line(37, 34, 38, 41, pal["metal_mid"])
    c.set(36, 34, pal["brass_hi"])
    c.set(37, 41, pal["brass_hi"])
    c.line(39, 36, 39, 41, pal["glow_bright"])
    c.set(39, 38, pal["glow_neon"])

    # ====================================================
    # 7. EXPOSED METAL ROBOTIC ARM & PROSTHETIC HAND
    # ====================================================
    # Torn sleeve edge at shoulder
    c.path("M 41 38 L 45 42 L 43 45 L 47 44 L 46 48", pal["coat_bright"], fill=False)
    c.set(43, 41, pal["coat_shadow"])
    c.set(44, 43, pal["coat_black"])
    
    # Heavy shoulder ball joint
    c.circle(49, 42, 4, pal["metal_black"])
    c.circle(49, 42, 3, pal["metal_dark"])
    c.circle(49, 42, 2, pal["metal_mid"])
    c.set(49, 42, pal["brass_hi"])
    
    # Upper arm casing with hazard stripes
    c.rect(48, 44, 7, 6, pal["metal_shadow"])
    c.rect(49, 45, 5, 5, pal["metal_mid"])
    c.set(50, 45, pal["hazard_yel"])
    c.set(52, 45, pal["hazard_yel"])
    c.set(49, 46, pal["hazard_yel"])
    c.set(51, 46, pal["hazard_yel"])
    c.set(53, 46, pal["hazard_yel"])
    c.set(50, 47, pal["hazard_yel"])
    c.set(52, 47, pal["hazard_yel"])
    c.set(49, 48, pal["hazard_yel"])
    c.set(51, 48, pal["hazard_yel"])
    c.set(53, 48, pal["hazard_yel"])
    c.set(50, 46, pal["hazard_blk"])
    c.set(51, 47, pal["hazard_blk"])
    c.set(52, 48, pal["hazard_blk"])
    c.line(47, 45, 47, 49, pal["metal_bright"])
    c.set(47, 46, pal["metal_white"])
    
    # Elbow joint
    c.rect(49, 49, 6, 3, pal["metal_black"])
    c.rect(50, 50, 4, 2, pal["brass_mid"])
    c.set(51, 50, pal["brass_hi"])
    
    # Forearm chassis
    c.poly([(49, 51), (55, 50), (56, 55), (50, 55)], pal["metal_black"])
    c.poly([(50, 52), (54, 51), (55, 54), (51, 54)], pal["metal_shadow"])
    c.line(51, 52, 54, 53, pal["metal_light"])
    c.line(52, 52, 55, 52, pal["metal_bright"])
    
    # Forearm cables
    c.line(49, 52, 54, 52, pal["wire_red_hi"])
    c.set(49, 52, pal["wire_red"])
    c.line(50, 53, 55, 53, pal["wire_yellow_hi"])
    c.line(50, 54, 55, 54, pal["glow_neon"])
    
    # PROSTHETIC HAND WITH CABLES
    # Wrist servo collar
    c.rect(49, 54, 6, 2, pal["metal_black"])
    c.set(51, 54, pal["glow_white"])
    c.set(52, 54, pal["glow_bright"])
    
    # Hand plate
    c.rect(48, 55, 7, 3, pal["metal_mid"])
    c.line(49, 55, 54, 55, pal["metal_bright"])
    c.line(50, 56, 53, 56, pal["metal_light"])
    
    # Segmented claw digits
    # Thumb
    c.line(48, 55, 45, 54, pal["metal_light"])
    c.set(45, 54, pal["brass_hi"])
    c.line(45, 54, 43, 55, pal["metal_gleam"])
    c.set(43, 55, pal["metal_white"])
    
    # Index finger
    c.line(49, 57, 47, 59, pal["metal_light"])
    c.set(47, 59, pal["brass_mid"])
    c.line(47, 60, 46, 62, pal["metal_bright"])
    c.set(46, 62, pal["metal_white"])
    
    # Middle finger
    c.line(51, 57, 50, 60, pal["metal_light"])
    c.set(50, 60, pal["brass_hi"])
    c.line(50, 61, 49, 63, pal["metal_gleam"])
    c.set(49, 63, pal["metal_white"])
    
    # Ring finger
    c.line(53, 57, 53, 59, pal["metal_mid"])
    c.set(53, 59, pal["brass_mid"])
    c.line(53, 60, 52, 62, pal["metal_bright"])
    c.set(52, 62, pal["metal_white"])
    
    # Pinky finger
    c.line(55, 56, 56, 58, pal["metal_shadow"])
    c.line(56, 58, 55, 61, pal["metal_light"])
    c.set(55, 61, pal["metal_gleam"])
    
    # Trailing cables dangling from prosthetic hand
    c.path("M 51 56 Q 48 59 46 63", pal["wire_red_hi"], fill=False)
    c.set(46, 63, pal["brass_hi"])
    c.path("M 53 57 Q 52 61 50 63", pal["wire_blue_hi"], fill=False)
    
    # Crackling energy spark
    c.set(45, 56, pal["glow_neon"])
    c.set(46, 57, pal["glow_white"])
    c.set(47, 56, pal["glow_bright"])
    c.set(44, 57, pal["glow_deep"])

    # ====================================================
    # 8. HEAD & CRANIUM STRUCTURE
    # ====================================================
    # Human Left Side (x: 21..31, y: 13..36)
    c.poly([(23, 14), (31, 13), (31, 36), (28, 36), (23, 33), (20, 27), (21, 19)], pal["skin_deep"])
    c.poly([(24, 15), (31, 14), (31, 35), (28, 35), (24, 32), (21, 26), (22, 20)], pal["skin_shadow"])
    c.poly([(25, 15), (31, 15), (31, 34), (29, 34), (25, 30), (22, 25), (23, 21)], pal["skin_mid"])
    c.poly([(26, 16), (31, 16), (31, 30), (29, 29), (25, 27), (23, 23)], pal["skin_light"])
    
    # Forehead
    c.rect(25, 15, 6, 4, pal["skin_light"])
    c.rect(26, 16, 5, 3, pal["skin_pale"])
    c.line(27, 16, 30, 16, pal["skin_hi"])
    c.line(25, 15, 30, 15, pal["skin_crease"])
    c.line(26, 17, 31, 17, pal["skin_crease"])
    c.line(27, 19, 31, 19, pal["skin_crease"])
    
    # Human ear
    c.poly([(18, 24), (21, 22), (21, 29), (19, 29)], pal["skin_deep"])
    c.poly([(19, 24), (21, 23), (21, 28), (20, 28)], pal["skin_shadow"])
    c.set(20, 25, pal["skin_mid"])
    c.set(20, 26, pal["skin_light"])
    
    # Robotic Right Side (x: 31..44, y: 11..36)
    c.poly([(31, 11), (40, 11), (43, 16), (44, 25), (41, 33), (36, 36), (31, 36)], pal["metal_black"])
    c.poly([(31, 12), (39, 12), (42, 17), (43, 25), (40, 32), (35, 35), (31, 35)], pal["metal_dark"])
    c.poly([(32, 13), (38, 13), (41, 18), (41, 24), (38, 31), (34, 34), (32, 34)], pal["metal_shadow"])
    c.poly([(32, 14), (37, 14), (40, 19), (39, 24), (36, 30), (33, 31), (32, 31)], pal["metal_mid"])
    
    # Metal skull plating highlights & seams
    c.line(33, 13, 37, 13, pal["metal_light"])
    c.line(34, 14, 38, 14, pal["metal_bright"])
    c.line(38, 15, 40, 18, pal["metal_gleam"])
    c.set(37, 13, pal["metal_white"])
    c.set(39, 16, pal["metal_white"])
    
    # Seams & rivets
    c.line(34, 17, 41, 17, pal["metal_black"])
    c.line(37, 12, 37, 17, pal["metal_black"])
    c.set(35, 16, pal["brass_hi"])
    c.set(39, 16, pal["brass_hi"])
    
    # Central cybernetic seam with surgical staples
    c.line(31, 12, 31, 36, pal["scar_seam"])
    c.line(32, 12, 32, 36, pal["metal_bright"])
    for seam_y in [14, 18, 24, 28, 33]:
        c.set(30, seam_y, pal["staple"])
        c.set(31, seam_y, pal["metal_white"])
        c.set(30, seam_y + 1, pal["skin_deep"])
        
    # Audio sensor / antenna
    c.rect(43, 22, 3, 6, pal["metal_dark"])
    c.rect(44, 23, 2, 4, pal["metal_light"])
    c.set(44, 24, pal["brass_hi"])
    c.set(44, 25, pal["glow_bright"])
    c.line(45, 17, 45, 22, pal["metal_bright"])
    c.set(45, 16, pal["glow_neon"])
    
    # Cooling vent slots on cheek
    for vy in range(25, 29):
        c.set(40, vy, pal["metal_black"])
        c.set(41, vy, pal["metal_mid"])
        c.set(42, vy, pal["metal_light"])

    # ====================================================
    # 9. BRAIN ELECTRODE PLUGS
    # ====================================================
    c.rect(35, 9, 4, 3, pal["metal_black"])
    c.rect(36, 9, 2, 2, pal["metal_light"])
    c.set(36, 8, pal["brass_hi"])
    c.set(37, 7, pal["metal_gleam"])
    
    c.rect(40, 11, 3, 3, pal["metal_black"])
    c.rect(41, 11, 2, 2, pal["brass_mid"])
    c.set(42, 10, pal["brass_hi"])
    
    # Cables arching from electrodes over cranium
    c.path("M 36 8 Q 34 4 40 3 Q 45 3 48 8 Q 50 14 52 20", pal["wire_red_hi"], fill=False)
    c.path("M 37 8 Q 35 5 40 4 Q 44 4 47 9", pal["wire_red"], fill=False)
    c.path("M 42 10 Q 46 7 50 11 Q 53 17 54 26", pal["wire_yellow_hi"], fill=False)
    c.path("M 38 9 Q 42 8 46 12 Q 48 18 49 24", pal["glow_bright"], fill=False)

    # ====================================================
    # 10. EYES (Human Crazed & Glowing Cybernetic)
    # ====================================================
    # Human Eye (Unhinged psychotic stare)
    c.rect(23, 20, 7, 6, pal["eyebag_dark"])
    c.line(22, 26, 29, 26, pal["eyebag"])
    c.line(23, 27, 28, 27, pal["skin_shadow"])
    
    c.rect(24, 21, 5, 4, pal["sclera"])
    c.set(24, 21, pal["sclera_red"])
    c.set(24, 24, pal["sclera_red"])
    c.set(28, 21, pal["sclera_red"])
    c.set(28, 24, pal["sclera_red"])
    
    c.rect(25, 22, 3, 2, pal["human_iris"])
    c.set(26, 22, pal["human_pupil"])
    c.set(26, 23, pal["human_pupil"])
    c.set(25, 22, pal["metal_white"])
    
    # Arched wild eyebrow
    c.line(22, 19, 24, 18, pal["hair_shadow"])
    c.line(24, 18, 29, 16, pal["hair_light"])
    c.line(25, 17, 30, 15, pal["hair_bright"])
    c.set(27, 15, pal["hair_white"])
    c.set(29, 14, pal["hair_white"])
    c.set(31, 15, pal["hair_white"])
    
    # Glowing Cybernetic Eye
    c.rect(34, 19, 7, 7, pal["metal_black"])
    c.circle(37, 22, 3, pal["metal_dark"])
    c.circle(37, 22, 2, pal["metal_shadow"])
    
    # Glowing halo
    c.circle(37, 22, 4, pal["glow_deep"], fill=False)
    c.set(37, 17, pal["glow_deep"])
    c.set(37, 27, pal["glow_deep"])
    c.set(32, 22, pal["glow_deep"])
    c.set(42, 22, pal["glow_deep"])
    
    # Neon core
    c.circle(37, 22, 2, pal["glow_bright"])
    c.circle(37, 22, 1, pal["glow_neon"])
    c.set(37, 22, pal["glow_white"])
    
    # Reticle marks
    c.set(34, 22, pal["glow_bright"])
    c.set(35, 22, pal["glow_neon"])
    c.set(39, 22, pal["glow_neon"])
    c.set(40, 22, pal["glow_bright"])
    c.set(37, 19, pal["glow_bright"])
    c.set(37, 20, pal["glow_neon"])
    c.set(37, 24, pal["glow_neon"])
    c.set(37, 25, pal["glow_bright"])
    
    c.line(33, 19, 41, 19, pal["metal_light"])
    c.line(34, 18, 40, 18, pal["metal_bright"])
    c.set(38, 18, pal["metal_gleam"])

    # ====================================================
    # 11. NOSE
    # ====================================================
    c.line(30, 23, 29, 27, pal["skin_mid"])
    c.line(30, 24, 30, 27, pal["skin_pale"])
    c.set(30, 26, pal["skin_hi"])
    c.set(28, 27, pal["skin_shadow"])
    c.set(29, 28, pal["skin_deep"])
    
    c.line(31, 23, 31, 29, pal["scar_seam"])
    c.line(32, 23, 32, 29, pal["metal_bright"])
    c.set(33, 27, pal["metal_mid"])
    c.set(33, 28, pal["metal_dark"])

    # ====================================================
    # 12. MANIACAL GRIN
    # ====================================================
    c.line(23, 26, 25, 28, pal["skin_crease"])
    c.line(24, 25, 26, 27, pal["skin_shadow"])
    c.set(25, 26, pal["skin_pale"])
    
    # Open mouth void
    c.poly([(24, 29), (31, 30), (40, 28), (39, 34), (31, 35), (25, 34)], pal["mouth_void"])
    
    # Human lips & teeth
    c.line(25, 28, 31, 29, pal["lip_dark"])
    c.line(26, 28, 30, 29, pal["lip"])
    c.line(26, 35, 31, 35, pal["lip_dark"])
    c.set(28, 35, pal["lip_hi"])
    
    c.rect(26, 29, 5, 2, pal["teeth_mid"])
    c.set(26, 29, pal["teeth_light"])
    c.set(27, 30, pal["teeth_dark"])
    c.set(28, 29, pal["teeth_light"])
    c.set(29, 29, pal["teeth_light"])
    c.set(30, 30, pal["teeth_dark"])
    c.set(27, 34, pal["teeth_light"])
    c.set(29, 34, pal["teeth_light"])
    c.set(30, 34, pal["teeth_mid"])
    
    # Cyborg jaw
    c.poly([(31, 29), (40, 27), (41, 34), (38, 36), (31, 36)], pal["metal_dark"])
    c.line(32, 35, 37, 35, pal["metal_shadow"])
    c.line(39, 26, 39, 33, pal["metal_bright"])
    c.line(40, 26, 40, 33, pal["metal_mid"])
    c.set(39, 26, pal["brass_hi"])
    c.set(39, 33, pal["brass_hi"])
    
    # Chrome servo teeth
    c.rect(32, 29, 7, 4, pal["metal_shadow"])
    for tx in [32, 34, 36, 38]:
        c.line(tx, 29, tx, 32, pal["metal_gleam"])
        c.set(tx, 29, pal["metal_white"])
        c.set(tx+1, 30, pal["metal_black"])
        c.set(tx+1, 31, pal["metal_black"])
    
    # Chin
    c.poly([(27, 35), (31, 35), (31, 37), (28, 37)], pal["skin_mid"])
    c.set(29, 36, pal["skin_pale"])
    c.set(30, 36, pal["skin_hi"])
    c.poly([(31, 35), (36, 35), (35, 37), (31, 37)], pal["metal_mid"])
    c.line(32, 36, 34, 36, pal["metal_bright"])
    c.set(33, 36, pal["metal_gleam"])

    # ====================================================
    # 13. MESSY WILD WHITE HAIR (Bright, Brilliant, Spiky!)
    # ====================================================
    # Left hair clusters: drawn with bright white and light silver!
    left_hair_data = [
        # Upper tuft
        [(21, 16), (16, 12), (12, 10), (14, 15), (18, 17)],
        [(19, 14), (15, 11), (13, 11), (15, 14)],
        # Mid tufts
        [(19, 18), (14, 15), (9, 14), (12, 19), (16, 21)],
        [(17, 18), (13, 16), (10, 15), (13, 19)],
        # Lower tufts
        [(18, 22), (12, 20), (7, 21), (10, 25), (15, 25)],
        [(16, 22), (11, 21), (8, 22), (11, 24)],
        [(17, 26), (11, 26), (7, 28), (11, 31), (15, 30)],
        [(15, 27), (10, 28), (8, 29), (11, 30)],
        # Bottom sideburn tufts
        [(16, 30), (12, 32), (9, 35), (13, 35), (16, 33)],
    ]
    for poly in left_hair_data:
        c.poly(poly, pal["hair_bright"])
    
    # Internal soft shading inside left hair
    c.line(16, 13, 17, 16, pal["hair_light"])
    c.line(14, 17, 15, 20, pal["hair_light"])
    c.line(13, 22, 14, 24, pal["hair_light"])
    c.line(12, 27, 13, 30, pal["hair_light"])
    c.line(13, 32, 14, 34, pal["hair_light"])
    
    # White core highlights and spiky edges on left hair
    c.line(12, 10, 15, 12, pal["hair_white"])
    c.line(14, 12, 19, 15, pal["hair_white"])
    c.set(11, 10, pal["hair_white"])
    c.set(10, 11, pal["hair_white"])
    
    c.line(9, 14, 13, 16, pal["hair_white"])
    c.line(13, 16, 17, 18, pal["hair_white"])
    c.set(8, 14, pal["hair_white"])
    c.set(7, 15, pal["hair_white"])
    
    c.line(7, 21, 11, 22, pal["hair_white"])
    c.line(11, 22, 16, 22, pal["hair_white"])
    c.set(6, 21, pal["hair_white"])
    c.set(5, 22, pal["hair_white"])
    
    c.line(7, 28, 11, 28, pal["hair_white"])
    c.line(11, 28, 15, 27, pal["hair_white"])
    c.set(6, 28, pal["hair_white"])
    c.set(5, 29, pal["hair_white"])
    
    c.line(9, 35, 12, 33, pal["hair_white"])
    c.set(8, 36, pal["hair_white"])
    
    # Right wild hair clusters (behind robotic skull & temple)
    right_hair_data = [
        # Upper right tuft
        [(42, 13), (47, 9), (51, 6), (48, 12), (44, 15)],
        [(44, 12), (48, 8), (50, 7), (47, 11)],
        # Mid right tuft
        [(43, 17), (50, 14), (55, 12), (52, 18), (46, 20)],
        [(46, 17), (51, 14), (54, 13), (50, 17)],
        # Lower right tuft
        [(44, 21), (51, 20), (56, 19), (52, 24), (46, 25)],
        [(46, 22), (52, 21), (55, 20), (51, 23)],
        # Bottom tuft
        [(44, 26), (50, 27), (54, 29), (49, 32), (45, 30)],
    ]
    for poly in right_hair_data:
        c.poly(poly, pal["hair_bright"])
        
    # Internal shading inside right hair
    c.line(45, 12, 47, 14, pal["hair_light"])
    c.line(47, 17, 50, 19, pal["hair_light"])
    c.line(48, 22, 51, 24, pal["hair_light"])
    c.line(47, 28, 49, 31, pal["hair_light"])
    
    # White core highlights on right hair
    c.line(47, 8, 51, 6, pal["hair_white"])
    c.set(52, 6, pal["hair_white"])
    c.set(53, 5, pal["hair_white"])
    
    c.line(50, 13, 55, 12, pal["hair_white"])
    c.set(56, 12, pal["hair_white"])
    c.set(57, 11, pal["hair_white"])
    
    c.line(51, 19, 56, 19, pal["hair_white"])
    c.set(57, 19, pal["hair_white"])
    c.set(58, 18, pal["hair_white"])
    
    c.line(50, 28, 54, 29, pal["hair_white"])
    c.set(55, 30, pal["hair_white"])
    c.set(56, 31, pal["hair_white"])
    
    # Stray wild frizz hairs floating in the air
    stray_hairs = [
        (13, 8), (17, 7), (20, 5), (25, 4), (32, 2), (38, 3), (45, 3), (51, 5), (56, 10),
        (7, 18), (5, 24), (6, 30), (10, 36)
    ]
    for sx, sy in stray_hairs:
        c.set(sx, sy, pal["hair_white"])

    # ====================================================
    # 14. DRAMATIC LIGHTING & SPECULAR POLISH
    # ====================================================
    # Cyan glow reflections on cheek & jaw
    c.set(38, 25, pal["glow_deep"])
    c.set(39, 26, pal["glow_mid"])
    c.set(36, 26, pal["glow_deep"])
    c.set(37, 27, pal["glow_mid"])
    c.set(38, 28, pal["glow_deep"])
    c.set(41, 41, pal["glow_deep"])
    c.set(45, 41, pal["glow_mid"])
    c.set(47, 42, pal["glow_bright"])
    c.set(48, 23, pal["glow_mid"])
    
    # Chrome gleams
    c.set(34, 14, pal["metal_white"])
    c.set(37, 12, pal["metal_white"])
    c.set(43, 22, pal["metal_gleam"])
    c.set(45, 23, pal["metal_white"])
    c.set(39, 34, pal["metal_white"])

    return c, pal

if __name__ == "__main__":
    c, pal = build_portrait()
    view(c)
