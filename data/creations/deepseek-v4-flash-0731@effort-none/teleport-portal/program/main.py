import math
from pixelbench_api import new_canvas, finish

W = 48
H = 48
CX = 24
CY = 24

c = new_canvas(W, H, background=(0,0,0,0), name="teleport_portal")

# ==================== COLORS ====================
BLACK    = (5, 2, 10, 255)
DARK_P   = (25, 10, 48, 255)
DEEP_P   = (50, 20, 88, 255)
MID_P    = (78, 35, 122, 255)
PURPLE   = (108, 50, 156, 255)
LGT_P    = (140, 68, 190, 255)
PINK_P   = (175, 92, 220, 255)
MAGENTA  = (210, 125, 245, 255)
WHT_PNK  = (242, 168, 255, 255)
PURE_W   = (255, 220, 255, 255)

G_DIM    = (36, 16, 68, 255)
G_SOFT   = (58, 28, 96, 255)
G_MED    = (85, 40, 130, 255)
G_BRIGHT = (112, 55, 164, 255)

# ==================== HELPER: point_in_circle ====================
def dist_from_center(x, y):
    return math.sqrt((x-CX)**2 + (y-CY)**2)

# ==================== 1. OUTER GLOW ====================
# Soft aura extending from vortex edge
for y in range(H):
    for x in range(W):
        d = dist_from_center(x, y)
        if d > 20.5:
            if d <= 23.5:
                c.set(x, y, G_DIM)
        elif d > 19.8:
            c.set(x, y, G_SOFT)
        elif d > 18.8:
            c.set(x, y, G_MED)

# ==================== 2. HALO RING ====================
# Luminous ring framing the vortex at radius ~18-19
for y in range(H):
    for x in range(W):
        d = dist_from_center(x, y)
        if d >= 18.0 and d <= 18.6:
            c.set(x, y, WHT_PNK)
        elif d > 18.6 and d < 19.2:
            c.set(x, y, MAGENTA)
        elif d > 17.4 and d < 18.0:
            c.set(x, y, G_BRIGHT)

# Pulse points on the halo - small bright sparks
for a in range(10):
    ang = a * math.pi / 5.0
    for rr in [18.2, 18.6, 19.0]:
        px = int(CX + rr * math.cos(ang))
        py = int(CY + rr * math.sin(ang))
        c.set(px, py, PURE_W)

# ==================== 3. VORTEX: spiral energy ====================
# Core disc with swirling arms - makes the "vortex" look
R_MAX = 17.8

for y in range(H):
    for x in range(W):
        dx = x - CX
        dy = y - CY
        d2 = dx*dx + dy*dy
        if d2 >= R_MAX*R_MAX:
            continue
        if d2 <= 3.5*3.5:
            continue  # skip center, drawn later
        
        d = math.sqrt(d2)
        ang = math.atan2(dy, dx)
        
        # The vortex pattern:
        # Multiple spiral arms sweeping inward - creates a rich swirling texture
        swirl = ang + d * 0.30
        
        # Combined spiral pattern for visual richness
        # Use multiple overlapping waves for complexity
        tri = abs((swirl * 1.5 / math.pi) % 2 - 1) * 2 - 1
        wave2 = math.sin(3.0 * ang - d * 0.2)
        
        # The radial gradient goes DARK → LIGHT from center to edge
        t = d / R_MAX
        
        if tri > 0.55:
            # Bright arm core
            if t < 0.25:
                c.set(x, y, PURPLE)
            elif t < 0.45:
                c.set(x, y, LGT_P)
            elif t < 0.65:
                c.set(x, y, PINK_P)
            elif t < 0.85:
                c.set(x, y, MAGENTA)
            else:
                c.set(x, y, WHT_PNK)
        elif tri > 0.2:
            # Medium band
            if t < 0.25:
                c.set(x, y, MID_P)
            elif t < 0.6:
                c.set(x, y, PURPLE)
            else:
                c.set(x, y, MAGENTA)
        elif tri > -0.1:
            # Boundary layer
            if t < 0.3:
                c.set(x, y, MID_P)
            else:
                c.set(x, y, LGT_P)
        elif wave2 > 0.6:
            # Secondary wave detail
            if t < 0.4:
                c.set(x, y, MID_P)
            else:
                c.set(x, y, PURPLE)
        else:
            # Dark zones between arms
            if t < 0.3:
                c.set(x, y, DEEP_P)
            elif t < 0.7:
                c.set(x, y, MID_P)
            else:
                c.set(x, y, PINK_P)

# ==================== 4. CENTER VOID ====================
# The dark portal opening
for y in range(H):
    for x in range(W):
        d = dist_from_center(x, y)
        if d <= 4.0:
            c.set(x, y, BLACK)
        elif d <= 5.0:
            c.set(x, y, DARK_P)

# Bright edge glow at inner opening
for a in range(24):
    ang = a * 2*math.pi / 24.0
    px = int(CX + 5.5 * math.cos(ang))
    py = int(CY + 5.5 * math.sin(ang))
    c.set(px, py, MAGENTA)

# ==================== 5. BRIGHT ENERGY FILAMENTS ====================
# Clearly visible curved streaks spiraling through the vortex
# These give the distinct "swirling energy" look

# Primary bright filaments - long sweeping arcs
for arm in range(3):
    # Each arm starts at a different angle
    base = arm * 2*math.pi/3
    # Sweep the arm through the vortex
    segments = []
    for r in range(4, 18):
        rf = float(r)
        # Arm curves as radius increases
        ang = base + rf * 0.45  # clockwise swirl
        segments.append((CX + rf*math.cos(ang), CY + rf*math.sin(ang)))
    # Draw each segment
    for px, py in segments:
        x0, y0 = int(px), int(py)
        dd = dist_from_center(x0, y0)
        if dd > 4.5 and dd < 17.5:
            c.set(x0, y0, WHT_PNK)

# Bright at arm centers
for arm in range(3):
    base = arm * 2*math.pi/3 + 0.15
    for r in range(5, 18):
        rf = float(r)
        ang = base + rf * 0.40
        px = int(CX + rf*math.cos(ang))
        py = int(CY + rf*math.sin(ang))
        dd = dist_from_center(px, py)
        if dd > 5 and dd < 17.5:
            c.set(px, py, PURE_W)

# ==================== 6. SPARKS & PARTICLES ====================
# Scattered energy particles around the vortex
particles = [
    # Vortex interior sparks
    (32, 19, PURE_W), (17, 31, WHT_PNK), (30, 30, PURE_W), (20, 16, MAGENTA),
    (34, 24, PURE_W), (15, 20, WHT_PNK), (28, 33, PURE_W), (14, 26, LGT_P),
    (36, 21, MAGENTA), (13, 25, PURE_W), (25, 14, WHT_PNK), (19, 34, MAGENTA),
    (33, 28, WHT_PNK), (27, 34, PURE_W), (14, 33, MAGENTA),
    
    # Halo ring sparks 
    (36, 13, MAGENTA), (42, 24, PURE_W), (25, 41, G_BRIGHT), (11, 35, MAGENTA),
    (38, 30, WHT_PNK), (8, 28, G_BRIGHT), (30, 38, PURE_W), (35, 9, WHT_PNK),
    (40, 27, MAGENTA), (19, 40, G_MED), (28, 8, MAGENTA), (7, 23, G_BRIGHT),
    (39, 18, WHT_PNK), (20, 7, MAGENTA),
    
    # Floating debris sparks
    (38, 38, G_BRIGHT), (10, 10, G_SOFT), (40, 16, MAGENTA), (33, 39, G_BRIGHT),
    (22, 43, G_SOFT), (42, 33, MAGENTA), (36, 41, G_MED), (12, 39, MAGENTA),
]
for px, py, color in particles:
    if 0 <= px < W and 0 <= py < H:
        c.set(px, py, color)

# ==================== 7. ENSURE DARK CENTER ====================
# Guarantee dark center
for y in range(H):
    for x in range(W):
        d = dist_from_center(x, y)
        if d <= 3.5:
            c.set(x, y, BLACK)

print(c.stats_text())

seen = set()
for y in range(H):
    for x in range(W):
        idx = c.get(x, y)
        if idx is not None and idx is not False:
            seen.add(idx)
print(f"Unique visible colors: {len(seen)}")

finish(c)
