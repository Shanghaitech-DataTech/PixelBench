import math
from pixelbench_api import new_canvas, view, finish

c = new_canvas(48, 48)

PALETTE = {
    # Core & brilliant light
    "white": "#ffffff",
    "core_hot": "#fff5fe",
    "spark_cyan_bright": "#e0f2fe",
    "spark_cyan": "#7dd3fc",
    "lavender_white": "#f5e8ff",
    "lavender_pale": "#e9d5ff",
    "lavender_bright": "#d8b4fe",
    
    # Electric / magical energy highlights
    "filament_light": "#fae8ff",
    "magenta_electric": "#f0abfc",
    "magenta_vivid": "#e879f9",
    "electric_violet": "#c084fc",
    "neon_purple": "#a855f7",
    "vivid_purple": "#9333ea",
    
    # Mid and deep cosmic shades
    "royal_purple": "#7e22ce",
    "deep_purple": "#6b21a8",
    "dark_violet": "#581c87",
    "shadow_deep": "#3b0764",
    "space_void": "#240046",
    
    # Halo glow
    "halo_aura": "#c084fc",
    "halo_soft": "#9333ea",
}

for name, hex_val in PALETTE.items():
    c.color(hex_val, name=name)

def get_vortex_pixel(dx, dy, rot_deg):
    dist = math.hypot(dx, dy)
    if dist > 8.8:
        return None
        
    ang = math.atan2(dy, dx) - math.radians(rot_deg)
    
    # 3-arm spiral: phase in [0, 1)
    k = 0.82
    phase = ((ang - k * dist) % (2 * math.pi / 3)) / (2 * math.pi / 3)

    # Core singularity & rotating inner filaments
    if dist <= 0.8:
        return "white"
    elif dist <= 1.8:
        if phase < 0.40:
            return "white"
        elif phase < 0.70:
            return "core_hot"
        else:
            return "lavender_white"
    elif dist <= 2.8:
        if phase < 0.30:
            return "white"
        elif phase < 0.60:
            return "lavender_white"
        else:
            return "lavender_pale"
        
    # Main swirling vortex arms
    if dist <= 5.2:
        if phase < 0.20:
            return "filament_light"
        elif phase < 0.45:
            return "magenta_electric"
        elif phase < 0.72:
            return "electric_violet"
        elif phase < 0.88:
            return "neon_purple"
        else:
            return "dark_violet"
    elif dist <= 7.4:
        if phase < 0.15:
            return "magenta_electric"
        elif phase < 0.35:
            return "electric_violet"
        elif phase < 0.60:
            return "vivid_purple"
        elif phase < 0.80:
            return "royal_purple"
        elif phase < 0.92:
            return "shadow_deep"
        else:
            return "space_void"
    else: # 7.4 < dist <= 8.8 (outer tips of arms)
        if phase < 0.16:
            return "lavender_bright"
        elif phase < 0.35:
            return "neon_purple"
        elif phase < 0.55:
            return "deep_purple"
        elif phase < 0.72:
            return "shadow_deep"
        else:
            return None

def draw_clean_halo(cx, cy):
    # A crisp, perfectly circular glowing halo at radius ~10.4
    halo_points = set()
    for dy in range(-12, 13):
        for dx in range(-12, 13):
            dist = math.hypot(dx, dy)
            if 9.8 <= dist <= 10.8:
                halo_points.add((dx, dy))

    # Draw the halo ring: brilliant white & cyan-lavender
    for dx, dy in halo_points:
        x = cx + dx
        y = cy + dy
        if 0 <= x < 48 and 0 <= y < 48:
            if abs(dx) <= 1 or abs(dy) <= 1 or abs(dx) == abs(dy):
                c.set(x, y, "white")
            else:
                c.set(x, y, "spark_cyan_bright")

    # Add soft glowing aura pixels outside the ring
    for dx, dy in halo_points:
        nx = int(round(dx * 1.12))
        ny = int(round(dy * 1.12))
        gx = cx + nx
        gy = cy + ny
        if 0 <= gx < 48 and 0 <= gy < 48:
            if c.get(gx, gy) == 0 and (gx + gy) % 2 == 0:
                c.set(gx, gy, "halo_aura")

    # Cardinal star flares radiating from the halo
    # Top flare
    c.set(cx, cy - 11, "white")
    c.set(cx, cy - 12, "spark_cyan_bright")
    c.set(cx, cy - 13, "spark_cyan")
    
    # Bottom flare
    c.set(cx, cy + 11, "white")
    c.set(cx, cy + 12, "spark_cyan_bright")
    c.set(cx, cy + 13, "spark_cyan")
    
    # Left flare (cx=36: 36-11=25, 36-12=24)
    c.set(cx - 11, cy, "white")
    c.set(cx - 12, cy, "spark_cyan_bright")
    
    # Right flare (cx=36: 36+11=47)
    c.set(cx + 11, cy, "white")
    
    # Diagonal subtle glints
    for ddx, ddy in [(-8, -8), (8, -8), (-8, 8), (8, 8)]:
        gx, gy = cx + ddx, cy + ddy
        if 0 <= gx < 48 and 0 <= gy < 48:
            c.set(gx, gy, "white")
        sx, sy = cx + int(round(ddx * 1.18)), cy + int(round(ddy * 1.18))
        if 0 <= sx < 48 and 0 <= sy < 48 and c.get(sx, sy) == 0:
            c.set(sx, sy, "spark_cyan")

def add_floating_particles(cx, cy, rot_deg=0, is_frame2=False):
    rad = math.radians(rot_deg)
    cos_r = math.cos(rad)
    sin_r = math.sin(rad)
    
    # Swirling orbital motes (rotate with the vortex)
    orbital = [
        (-6, -6, "spark_cyan"),
        (6, -5, "lavender_white"),
        (-7, 4, "spark_cyan_bright"),
        (5, 6, "magenta_electric"),
        (-8, -1, "lavender_bright"),
        (7, 2, "electric_violet"),
        (-2, -7, "spark_cyan"),
        (2, 7, "magenta_vivid"),
    ]
    for px, py, col in orbital:
        rx = int(round(px * cos_r - py * sin_r))
        ry = int(round(px * sin_r + py * cos_r))
        x = cx + rx
        y = cy + ry
        if 0 <= x < 48 and 0 <= y < 48:
            if c.get(x, y) == 0:
                c.set(x, y, col)
                
    # Rising magical energy stream
    rising_sparks = [
        (-2, -14, "spark_cyan_bright"),
        (1, -16, "spark_cyan"),
        (3, -13, "lavender_bright"),
        (-1, -18, "spark_cyan"),
        (0, -20, "spark_cyan_bright"),
        (2, -21, "spark_cyan"),
        
        # Lower energy anchor
        (-2, 14, "royal_purple"),
        (1, 15, "neon_purple"),
        (-1, 17, "deep_purple"),
        (0, 19, "shadow_deep"),
    ]
    
    shift_y = -1 if is_frame2 else 0
    for px, py, col in rising_sparks:
        x = cx + px
        y = cy + py + shift_y
        if 0 <= x < 48 and 0 <= y < 48:
            if c.get(x, y) == 0:
                c.set(x, y, col)
                
    if is_frame2:
        extra_sparks = [
            (-9, -13, "spark_cyan"),
            (9, -13, "spark_cyan"),
            (-10, 12, "lavender_bright"),
            (10, 12, "spark_cyan"),
        ]
        for px, py, col in extra_sparks:
            x = cx + px
            y = cy + py
            if 0 <= x < 48 and 0 <= y < 48:
                if c.get(x, y) == 0:
                    c.set(x, y, col)

# Render Frame 1
cx1, cy1 = 11, 23
for dy in range(-10, 11):
    for dx in range(-10, 11):
        col = get_vortex_pixel(dx, dy, rot_deg=0)
        if col:
            c.set(cx1 + dx, cy1 + dy, col)
add_floating_particles(cx1, cy1, rot_deg=0, is_frame2=False)

# Render Frame 2 (rotated by 60 deg + glowing halo)
cx2, cy2 = 36, 23
for dy in range(-10, 11):
    for dx in range(-10, 11):
        col = get_vortex_pixel(dx, dy, rot_deg=60)
        if col:
            c.set(cx2 + dx, cy2 + dy, col)
draw_clean_halo(cx2, cy2)
add_floating_particles(cx2, cy2, rot_deg=60, is_frame2=True)

print("Canvas stats:", c.stats())
finish(c)
view(c)
