import math
import numpy as np
from pixelbench_api import new_canvas, view, finish

c = new_canvas(64, 64)

# =============================================================================
# REFINED REALISTIC PALETTE (48 colors)
# =============================================================================
P = {
    # Outlines & deepest crevices
    "void":       "#0a0205",
    "crease":     "#180307",
    "out_myo":    "#24050c",
    "out_vein":   "#0a0f1d",
    "out_ao":     "#2c070a",

    # Myocardium (Deep rich crimson / mahogany / fleshy tones)
    "m1": "#2c060e", # deepest shadow
    "m2": "#440b17",
    "m3": "#601121",
    "m4": "#7f172c",
    "m5": "#9f1f38", # base mid red
    "m6": "#bf2944",
    "m7": "#db3853",
    "m8": "#ee4d68",
    "m9": "#f76981",
    "m_hl": "#fba0b0",
    "m_spec": "#fde0e6",
    "white": "#ffffff",

    # Aorta (Arterial muscular trunk - warm terracotta / crimson ramp)
    "ao1": "#38090d",
    "ao2": "#571116",
    "ao3": "#7b1a20",
    "ao4": "#a1272b",
    "ao5": "#c53835",
    "ao6": "#e34f43",
    "ao7": "#f56a5b",
    "ao_hl": "#fa998a",
    "ao_spec": "#fcd0c6",

    # Vena Cava & Systemic Veins (Venous slate blue)
    "v1": "#0b1120",
    "v2": "#162138",
    "v3": "#243252",
    "v4": "#364972",
    "v5": "#4d6596",
    "v6": "#6a86bf",
    "v_hl": "#96b2e5",
    "v_spec": "#d6e4fc",

    # Pulmonary Trunk & Arteries (Indigo/slate-blue hue)
    "p1": "#121329",
    "p2": "#1e203e",
    "p3": "#2d3057",
    "p4": "#404576",
    "p5": "#59609c",
    "p6": "#7880bf",
    "p_hl": "#9ea6df",
    "p_spec": "#d6dbfa",

    # Adipose Tissue (Warm natural peach/cream fat)
    "f1": "#4a2419",
    "f2": "#6e3a24",
    "f3": "#995533",
    "f4": "#c27447",
    "f5": "#dd9461",
    "f6": "#f0b37f",
    "f_hl": "#fcd5a9",
    "f_spec": "#fff0d6",

    # Coronary Arteries (Vivid scarlet blood vessels)
    "art_dark": "#5a0710",
    "art_mid":  "#aa131e",
    "art_bright":"#f02431",
    "art_light": "#ff525d",
    "art_hl":   "#ffa3a9",

    # Coronary Veins (Rich cobalt/sapphire vessels)
    "vn_dark":  "#0f1e3d",
    "vn_mid":   "#1e3e7a",
    "vn_bright":"#3865b8",
    "vn_hl":    "#7ca6fa",

    # Vessel Lumen interiors
    "lum_dark":     "#120306",
    "lum_rim":      "#d6786e",
    "lum_blue_dark":"#060815",
    "lum_blue_rim": "#6184b8",
}

grid = {}

def set_px(x, y, col):
    if 0 <= x < 64 and 0 <= y < 64:
        grid[(x, y)] = P[col]

def get_px(x, y):
    return grid.get((x, y), None)

# =============================================================================
# 1. SUPERIOR VENA CAVA (SVC) - Left Upper (x: 18..25, y: 7..24)
# =============================================================================
for y in range(8, 25):
    t = (y - 8) / 16.0
    x0 = int(round(18.5 - 1.5 * t))
    x1 = int(round(24.0 + 1.0 * t))
    for x in range(x0, x1 + 1):
        rel = (x - x0) / max(1, x1 - x0)
        if rel < 0.15:
            col = "v2"
        elif rel < 0.35:
            col = "v4"
        elif rel < 0.65:
            col = "v5"
        elif rel < 0.85:
            col = "v3"
        else:
            col = "v2"
        set_px(x, y, col)

# SVC Highlights & Specular
for y in range(10, 18):
    set_px(20, y, "v_hl")
set_px(20, 13, "v_spec")
set_px(20, 14, "v_spec")

# SVC Lumen cut at top (y=7..8):
for x, y, col in [
    (18, 8, "v3"), (19, 7, "lum_blue_rim"), (20, 7, "lum_blue_rim"), (21, 7, "lum_blue_rim"),
    (22, 7, "lum_blue_rim"), (23, 7, "v3"), (24, 8, "v2"),
    (19, 8, "lum_blue_dark"), (20, 8, "lum_blue_dark"), (21, 8, "lum_blue_dark"),
    (22, 8, "lum_blue_dark"), (23, 8, "lum_blue_rim")
]:
    set_px(x, y, col)


# =============================================================================
# 2. AORTIC ARCH - Majestic curved tubular arch
# Spans x: 26..45, y: 7..25
# =============================================================================
# Centerline of the arch tube:
# Curves from ascending aorta (29, 24) -> (30, 15) -> (33, 10) -> (38, 9) -> (42, 13) -> (44, 24)
# Outer radius ~4.8, inner radius ~0.0 (tube thickness ~4.8)
# Under the arch (between the legs) is the aortopulmonary recess / shadow (x: 34..39, y: 14..18)

arch_path = [
    (29.0, 24.0), (29.5, 18.0), (31.0, 13.0), (34.0, 9.5),
    (38.0, 9.0), (41.5, 11.5), (43.5, 16.0), (44.5, 24.0)
]

for y in range(7, 26):
    for x in range(26, 46):
        # find distance to arch centerline
        min_d = 999.0
        closest_t = 0.0
        for i in range(len(arch_path) - 1):
            p1 = arch_path[i]
            p2 = arch_path[i+1]
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            L2 = dx*dx + dy*dy
            u = max(0.0, min(1.0, ((x - p1[0])*dx + (y - p1[1])*dy) / L2))
            px = p1[0] + u * dx
            py = p1[1] + u * dy
            d = math.hypot(x - px, y - py)
            if d < min_d:
                min_d = d
                closest_t = i + u

        r_tube = 4.8
        if min_d <= r_tube:
            # Inside the aorta tube!
            # Lighting from top-left:
            # We compute normal vector from centerline
            p_idx = min(len(arch_path)-1, int(round(closest_t)))
            pc = arch_path[p_idx]
            vx = (x - pc[0]) / r_tube
            vy = (y - pc[1]) / r_tube
            dot = -vx * 0.55 - vy * 0.70
            
            # Position along arch
            t_norm = closest_t / (len(arch_path) - 1)
            
            # Shading:
            shade = 0.50 + 0.40 * dot
            if t_norm > 0.65: # descending aorta in shadow
                shade -= 0.15
            elif t_norm < 0.25 and y > 18: # ascending aorta lower
                shade -= 0.05

            if shade > 0.82:
                col = "ao6"
            elif shade > 0.64:
                col = "ao5"
            elif shade > 0.45:
                col = "ao4"
            elif shade > 0.26:
                col = "ao3"
            elif shade > 0.10:
                col = "ao2"
            else:
                col = "ao1"
            set_px(x, y, col)
        elif x >= 33 and x <= 40 and y >= 13 and y <= 20:
            # Inside the aortopulmonary window (dark recess behind pulmonary trunk)
            set_px(x, y, "p1")

# Aorta smooth crest highlight along upper curve
for x, y, col in [
    (31, 9, "ao6"), (32, 8, "ao6"), (33, 8, "ao_hl"), (34, 7, "ao_hl"),
    (35, 7, "ao_spec"), (36, 7, "white"), (37, 7, "ao_spec"), (38, 8, "ao_hl"),
    (39, 8, "ao6"), (40, 9, "ao5"), (41, 11, "ao4"), (42, 13, "ao3")
]:
    set_px(x, y, col)

# 3 Aortic Branches (short, angled with arch curve):
# Branch 1: Brachiocephalic (x=29..32, y=3..8)
for y in range(4, 9):
    dx_val = (8 - y) * 0.25
    x0 = int(round(29 - dx_val))
    x1 = int(round(32 - dx_val))
    for x in range(x0, x1 + 1):
        col = "ao4" if x == x0 else ("ao5" if x < x1 else "ao3")
        set_px(x, y, col)
set_px(28, 4, "ao4")
set_px(29, 3, "lum_rim")
set_px(30, 3, "lum_rim")
set_px(31, 3, "ao3")
set_px(29, 4, "lum_dark")
set_px(30, 4, "lum_dark")

# Branch 2: Left Carotid (x=34..36, y=2..7)
for y in range(3, 8):
    for x in range(34, 37):
        col = "ao5" if x == 35 else "ao4"
        set_px(x, y, col)
set_px(34, 3, "lum_rim")
set_px(35, 2, "lum_rim")
set_px(36, 3, "ao3")
set_px(35, 3, "lum_dark")

# Branch 3: Left Subclavian (x=38..41, y=3..8)
for y in range(4, 9):
    dx_val = (8 - y) * 0.3
    x0 = int(round(38 + dx_val))
    x1 = int(round(40 + dx_val))
    for x in range(x0, x1 + 1):
        col = "ao4" if x == x0 else ("ao5" if x < x1 else "ao3")
        set_px(x, y, col)
set_px(38, 4, "ao4")
set_px(39, 3, "lum_rim")
set_px(40, 3, "lum_rim")
set_px(39, 4, "lum_dark")
set_px(40, 4, "ao3")


# =============================================================================
# 3. PULMONARY TRUNK & ARTERY (Arches cleanly across in front of aorta)
# Spans y: 16..26, x: 28..51
# =============================================================================
for y in range(16, 27):
    t = (26 - y) / 10.0
    x_c = 32.0 + 9.5 * t
    r = 4.4 - 0.4 * t
    x0 = int(round(x_c - r))
    x1 = int(round(x_c + r))
    for x in range(x0, x1 + 1):
        rel = (x - x0) / max(1, x1 - x0)
        if rel < 0.15:
            col = "p2"
        elif rel < 0.35:
            col = "p4"
        elif rel < 0.65:
            col = "p5"
        elif rel < 0.85:
            col = "p3"
        else:
            col = "p2"
        set_px(x, y, col)

# Left PA branch extension (x: 44..51, y: 16..20)
for y in range(16, 20):
    for x in range(44, 51):
        col = "p4" if y == 17 else ("p5" if y == 16 else "p3")
        if x >= 49: col = "p3"
        set_px(x, y, col)

# LPA cut lumen at (50..51, 17..18)
set_px(50, 16, "lum_blue_rim")
set_px(51, 17, "lum_blue_rim")
set_px(51, 18, "p2")
set_px(50, 19, "p2")
set_px(50, 17, "lum_blue_dark")
set_px(50, 18, "lum_blue_dark")

# Specular gloss on pulmonary trunk
for x, y, col in [
    (34, 21, "p_hl"), (35, 20, "p_hl"), (36, 19, "p_spec"), (37, 19, "white"),
    (38, 18, "p_spec"), (39, 18, "p_hl")
]:
    set_px(x, y, col)


# =============================================================================
# 4. RIGHT ATRIUM & AURICLE (Viewer's left: x=14..25, y=19..33)
# =============================================================================
for y in range(19, 34):
    for x in range(14, 26):
        dx = (x - 19) / 5.2
        dy = (y - 26) / 6.5
        if dx*dx + dy*dy <= 1.0:
            fold = math.sin(y * 1.3 - x * 0.9)
            light = 0.55 - 0.3 * dx - 0.2 * dy + 0.15 * fold
            if light > 0.75:
                col = "m6"
            elif light > 0.55:
                col = "m5"
            elif light > 0.35:
                col = "m4"
            elif light > 0.15:
                col = "m3"
            else:
                col = "m2"
            set_px(x, y, col)

set_px(16, 24, "m7")
set_px(16, 25, "m_hl")
set_px(17, 24, "m7")
set_px(15, 27, "m6")
set_px(16, 28, "m7")


# =============================================================================
# 5. LEFT ATRIUM & AURICLE (Viewer's right: x=45..52, y=22..32)
# =============================================================================
for y in range(22, 32):
    for x in range(45, 52):
        dx = (x - 47) / 4.0
        dy = (y - 27) / 4.5
        if dx*dx + dy*dy <= 1.0:
            col = "m3" if x < 48 else ("m2" if x < 50 else "m1")
            set_px(x, y, col)

# Left Pulmonary Veins:
for x in range(49, 52):
    set_px(x, 26, "v4")
    set_px(x, 27, "v3")
set_px(52, 26, "lum_blue_dark")
set_px(52, 27, "lum_blue_rim")

for x in range(49, 52):
    set_px(x, 30, "v4")
    set_px(x, 31, "v3")
set_px(52, 30, "lum_blue_dark")
set_px(52, 31, "lum_blue_rim")


# =============================================================================
# 6. VENTRICLES - ORGANIC CONVEX CURVES (NO FLAT TABLETOP!)
# Spans y=23..59, rising up naturally to meet pulmonary trunk & atria!
# =============================================================================
ventricle_rows = {}
for y in range(23, 60):
    t = (y - 23) / 36.0
    
    # Left flank: broad, rounded curve
    if t < 0.40:
        u = t / 0.40
        x_left = 18.0 - 4.5 * math.sin(u * math.pi * 0.5)
    else:
        u = (t - 0.40) / 0.60
        x_left = 13.5 + 21.0 * (u ** 1.30)
        
    # Right flank: muscular wall of LV
    if t < 0.35:
        u = t / 0.35
        x_right = 44.0 + 6.5 * math.sin(u * math.pi * 0.5)
    else:
        u = (t - 0.35) / 0.65
        x_right = 50.5 - 13.5 * (u ** 1.15)
        
    # Apex blunt rounding at (36, 58)
    if y >= 57:
        x_left = max(x_left, 31.0 + (y - 57) * 2.0)
        x_right = min(x_right, 40.0 - (y - 57) * 1.5)
        
    # Natural base curvature at y=23..25:
    # Under the atria, the ventricle base recedes upward organically
    if y == 23:
        x_left = max(x_left, 24.0)
        x_right = min(x_right, 38.0)
    elif y == 24:
        x_left = max(x_left, 20.0)
        x_right = min(x_right, 42.0)
        
    ventricle_rows[y] = (int(round(x_left)), int(round(x_right)))

# Render Myocardial Muscle
for y in range(23, 60):
    x_l, x_r = ventricle_rows[y]
    t_y = (y - 23) / 36.0
    
    # Diagonal sulcus groove
    sulcus_x = 27.5 + 10.0 * (t_y ** 1.05)
    
    for x in range(x_l, x_r + 1):
        # Don't overwrite pulmonary trunk or great vessels
        cur = get_px(x, y)
        if cur is not None and y < 27 and (cur in [P["p2"], P["p3"], P["p4"], P["p5"], P["p_hl"], P["p_spec"], P["white"]]):
            continue
            
        if x < sulcus_x:
            # RIGHT VENTRICLE (viewer's left)
            width_rv = max(1.0, sulcus_x - x_l)
            rel_rv = (x - x_l) / width_rv
            dome = math.sin(rel_rv * math.pi)
            
            # Key light from top-left
            light = 0.42 + 0.34 * (1.0 - t_y * 0.5) + 0.40 * dome
            fiber = 0.05 * math.sin(x * 1.5 + y * 1.2)
            light += fiber
            
            dist_s = abs(x - sulcus_x)
            if dist_s < 2.0:
                light -= 0.10 * (2.0 - dist_s)
                
            if light < 0.42:
                col = "m3"
            elif light < 0.56:
                col = "m4"
            elif light < 0.72:
                col = "m5"
            elif light < 0.88:
                col = "m6"
            elif light < 1.05:
                col = "m7"
            else:
                col = "m8"
                
            if rel_rv < 0.08:
                col = "m3"
                
        else:
            # LEFT VENTRICLE (viewer's right)
            width_lv = max(1.0, x_r - sulcus_x)
            rel_lv = (x - sulcus_x) / width_lv
            dome = math.sin(rel_lv * math.pi)
            
            light = 0.50 + 0.30 * (1.0 - rel_lv * 0.95) - 0.22 * t_y + 0.30 * dome
            fiber = 0.05 * math.sin(x * 1.1 - y * 1.4)
            light += fiber
            
            dist_s = abs(x - sulcus_x)
            if dist_s < 2.0:
                light -= 0.10 * (2.0 - dist_s)
                
            if rel_lv > 0.88:
                col = "m1" if rel_lv > 0.94 else "m2"
            elif light < 0.45:
                col = "m3"
            elif light < 0.60:
                col = "m4"
            elif light < 0.75:
                col = "m5"
            elif light < 0.90:
                col = "m6"
            else:
                col = "m7"
                
            if rel_lv > 0.90 and 34 <= y <= 47:
                col = "m3"
                
        set_px(x, y, col)

# Specular wet sheen on RV anterior bulge (x: 20..26, y: 32..37)
for x, y, col in [
    (21, 34, "m_spec"), (22, 33, "m_spec"), (23, 33, "white"), (24, 33, "white"),
    (21, 35, "m_hl"),   (22, 34, "white"),  (23, 34, "white"), (24, 34, "white"),
    (22, 35, "m_spec"), (23, 35, "m_hl"),   (24, 35, "m7"),    (25, 34, "m_spec"),
    (20, 35, "m7"),     (21, 36, "m7"),     (22, 36, "m7"),
]:
    set_px(x, y, col)

# Specular wet sheen on LV upper flank (x: 39..43, y: 31..34)
for x, y, col in [
    (39, 32, "m7"), (40, 31, "m_hl"), (41, 31, "m_spec"), (42, 32, "m7"),
    (39, 33, "m6"), (40, 32, "m_spec"), (41, 32, "m_hl"), (42, 33, "m6"),
]:
    set_px(x, y, col)


# =============================================================================
# 7. NATURAL CARDIAC FAT PADS
# =============================================================================
# Origin cushion under pulmonary trunk:
for x, y, col in [
    (27, 26, "f4"), (28, 26, "f5"), (29, 26, "f_hl"), (30, 26, "f5"),
    (27, 27, "f3"), (28, 27, "f5"), (29, 27, "f_hl"), (30, 27, "f4"),
    (28, 28, "f4"), (29, 28, "f5"), (30, 28, "f3"),
    (29, 29, "f3"), (30, 29, "f4"), (31, 29, "f3"),
    (30, 32, "f4"), (31, 32, "f5"), (31, 33, "f4"),
    (32, 36, "f3"), (32, 37, "f4"),
]:
    set_px(x, y, col)

# AV Groove Fat cushions at heart base:
for x, y, col in [
    (18, 26, "f2"), (19, 26, "f3"), (20, 26, "f4"), (21, 26, "f5"), (22, 26, "f_hl"),
    (23, 26, "f4"), (24, 26, "f3"),
    (19, 27, "f3"), (20, 27, "f4"), (21, 27, "f5"), (22, 27, "f4"), (23, 27, "f3"),
]:
    set_px(x, y, col)

for x, y, col in [
    (43, 27, "f3"), (44, 27, "f4"), (45, 27, "f5"), (46, 28, "f4"), (47, 28, "f3"),
    (44, 28, "f3"), (45, 28, "f4"), (46, 29, "f3")
]:
    set_px(x, y, col)

# Delicate wet glints on fat:
set_px(22, 26, "f_spec")
set_px(29, 27, "f_spec")
set_px(31, 32, "f_spec")


# =============================================================================
# 8. CORONARY BLOOD VESSELS (Exquisite, delicate 1-px scarlet & cobalt branching)
# =============================================================================
# Left Anterior Descending (LAD) Artery:
lad_points = [
    (28, 26), (28, 27), (29, 28), (29, 29), (30, 30),
    (30, 31), (30, 32), (31, 33), (31, 34), (31, 35),
    (32, 36), (32, 37), (32, 38), (33, 39), (33, 40),
    (33, 41), (34, 42), (34, 43), (34, 44), (35, 45),
    (35, 46), (35, 47), (36, 48), (36, 49), (36, 50),
    (37, 51), (37, 52), (37, 53), (37, 54), (38, 55),
    (38, 56), (38, 57)
]
for i, (x, y) in enumerate(lad_points):
    set_px(x, y, "art_bright")
    if i % 4 == 0:
        set_px(x, y, "art_hl")
    elif i % 4 == 2:
        set_px(x, y, "art_light")

# Diagonal Arterial Branches across Left Ventricle:
# Branch 1 (Upper LV):
for x, y, col in [
    (31, 34, "art_bright"), (32, 34, "art_light"), (33, 35, "art_hl"),
    (35, 35, "art_bright"), (36, 36, "art_light"), (38, 36, "art_mid"),
    (39, 37, "art_mid"), (41, 37, "art_dark"), (43, 38, "art_dark")
]:
    set_px(x, y, col)

# Branch 2 (Mid LV):
for x, y, col in [
    (34, 43, "art_bright"), (35, 43, "art_light"), (36, 44, "art_hl"),
    (38, 45, "art_bright"), (40, 46, "art_mid"), (42, 47, "art_dark")
]:
    set_px(x, y, col)

# Branch 3 (Lower LV):
for x, y, col in [
    (36, 49, "art_bright"), (37, 50, "art_light"), (39, 51, "art_mid"), (41, 52, "art_dark")
]:
    set_px(x, y, col)

# Great Cardiac Vein:
vein_points = [
    (27, 26), (27, 27), (27, 28), (28, 29), (28, 31),
    (28, 33), (29, 35), (29, 37), (30, 39)
]
for i, (x, y) in enumerate(vein_points):
    set_px(x, y, "vn_mid")
    if i % 3 == 0:
        set_px(x, y, "vn_bright")
    elif i % 3 == 1:
        set_px(x, y, "vn_hl")

# Venous tributary branching across Right Ventricle:
for x, y, col in [
    (27, 32, "vn_bright"), (26, 33, "vn_bright"), (25, 35, "vn_hl"),
    (24, 36, "vn_mid"), (23, 38, "vn_mid"), (22, 39, "vn_dark")
]:
    set_px(x, y, col)

# Right Coronary Artery (marginal branch across RV):
for x, y, col in [
    (24, 29, "art_mid"), (23, 31, "art_bright"), (22, 33, "art_hl"),
    (21, 35, "art_light"), (20, 37, "art_mid"), (19, 40, "art_dark"), (18, 42, "art_dark")
]:
    set_px(x, y, col)


# =============================================================================
# 9. SELECTIVE COLOR-KEYED OUTLINES
# =============================================================================
occupied = set(grid.keys())
border_pixels = set()
for (x, y) in occupied:
    is_border = False
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (x + dx, y + dy) not in occupied:
            is_border = True
            break
    if is_border:
        border_pixels.add((x, y))

for (bx, by) in border_pixels:
    current_col = grid[(bx, by)]
    if current_col in [P["white"], P["ao_spec"], P["m_spec"], P["v_spec"], P["p_spec"]]:
        continue
        
    if bx < 25 and by < 20: # SVC left
        set_px(bx, by, "out_vein")
    elif by < 10 and 30 <= bx <= 42: # Aorta crest
        pass # keep bright
    elif bx > 46: # Right flank
        set_px(bx, by, "out_myo")
    elif by > 55: # Apex bottom
        set_px(bx, by, "out_myo")
    elif bx < 17: # Left flank
        set_px(bx, by, "out_myo")

# Apply all pixels to canvas
for (x, y), hex_col in grid.items():
    c.set(x, y, hex_col)

unique_colors = set(grid.values())
print(f"Total unique visible colors used: {len(unique_colors)}")

view(c)
finish(c)
