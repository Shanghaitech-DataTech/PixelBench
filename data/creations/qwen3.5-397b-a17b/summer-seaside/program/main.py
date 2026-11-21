import math
from pixelbench_api import new_canvas, finish

# Create 128x128 canvas
c = new_canvas(128, 128, name="summer_seaside")

# Define colors
sky_light = c.color("#87CEEB", "sky_light")      # Light sky blue
sky_medium = c.color("#4A90C8", "sky_medium")    # Medium sky blue
sky_dark = c.color("#2E5C8A", "sky_dark")        # Darker sky blue
sun_yellow = c.color("#FFD700", "sun_yellow")    # Bright sun yellow
sun_orange = c.color("#FFA500", "sun_orange")    # Sun outer glow
cloud_white = c.color("#FFFFFF", "cloud_white")  # Pure white clouds
cloud_shadow = c.color("#E8E8E8", "cloud_shadow")# Cloud shadow

# Sea colors - teal near shore to deep blue at horizon
sea_deep = c.color("#003366", "sea_deep")        # Deep blue at horizon
sea_mid = c.color("#006699", "sea_mid")          # Mid sea blue
sea_light = c.color("#0099CC", "sea_light")      # Lighter sea
sea_teal = c.color("#20B2AA", "sea_teal")        # Teal near shore
sea_shore = c.color("#40C4C0", "sea_shore")      # Very light teal at shore

# Wave foam
foam_white = c.color("#F0F0F0", "foam_white")    # Wave foam
foam_shadow = c.color("#D0D0D0", "foam_shadow")  # Foam shadow

# Sand colors
sand_dark = c.color("#D2B48C", "sand_dark")      # Darker sand
sand_medium = c.color("#E6C89C", "sand_medium")  # Medium sand
sand_light = c.color("#F4D8A8", "sand_light")    # Light sand highlights

# Umbrella colors
umbrella_red = c.color("#DC143C", "umbrella_red")     # Crimson red
umbrella_white = c.color("#FFFAFA", "umbrella_white") # Off-white

# Towel colors
towel_blue = c.color("#4169E1", "towel_blue")    # Royal blue
towel_white = c.color("#FFFFFF", "towel_white2") # White stripes

# Flip-flop colors
flip_flop = c.color("#8B4513", "flip_flop")      # Brown

# Sailboat colors
sail_white = c.color("#FFFFFF", "sail_white")    # White sail
hull_brown = c.color("#8B7355", "hull_brown")    # Brown hull
mast_brown = c.color("#654321", "mast_brown")    # Dark brown mast

# Gull colors
gull_white = c.color("#FFFFFF", "gull_white")    # Gull white
gull_gray = c.color("#A9A9A9", "gull_gray")      # Gull gray wing tips

# ============ SKY GRADIENT ============
# Top to horizon gradient
for y in range(0, 50):
    # Gradient from light blue at top to medium blue at horizon
    if y < 15:
        sky_color = sky_light
    elif y < 30:
        sky_color = sky_medium
    else:
        sky_color = sky_dark
    c.rect(0, y, 128, 1, sky_color)

# ============ SUN ============
# Sun position: upper right area
sun_cx, sun_cy = 95, 18
sun_r = 10

# Sun glow (outer ring)
c.circle(sun_cx, sun_cy, sun_r + 3, sun_orange)
# Sun body
c.circle(sun_cx, sun_cy, sun_r, sun_yellow)
# Sun center highlight
c.circle(sun_cx, sun_cy, sun_r - 3, "#FFFF80")

# ============ CLOUDS ============
# Cloud 1 - fluffy cloud top left
def draw_cloud(cx, cy, size):
    # Main cloud body
    c.circle(cx, cy, size, cloud_white)
    c.circle(cx - size//2, cy + size//3, size//2, cloud_white)
    c.circle(cx + size//2, cy + size//3, size//2, cloud_white)
    c.circle(cx - size//3, cy - size//3, size//2, cloud_white)
    c.circle(cx + size//3, cy - size//3, size//2, cloud_white)
    # Shadow underneath
    c.circle(cx, cy + size//2, size//2, cloud_shadow)

draw_cloud(25, 20, 8)
draw_cloud(55, 15, 6)
draw_cloud(105, 28, 7)

# ============ SEA ============
# Sea from horizon (y=50) to shore (y=95)
# Layered colors from deep blue at horizon to teal at shore

# Deep blue at horizon (y=50 to y=60)
c.rect(0, 50, 128, 10, sea_deep)
# Mid blue (y=60 to y=72)
c.rect(0, 60, 128, 12, sea_mid)
# Lighter blue (y=72 to y=82)
c.rect(0, 72, 128, 10, sea_light)
# Teal near shore (y=82 to y=90)
c.rect(0, 82, 128, 8, sea_teal)
# Light teal at shore (y=90 to y=95)
c.rect(0, 90, 128, 5, sea_shore)

# ============ SAILBOAT ============
# Small sailboat far out on horizon
boat_x, boat_y = 35, 52
# Hull
c.rect(boat_x - 4, boat_y, 8, 3, hull_brown)
# Mast
c.line(boat_x, boat_y, boat_x, boat_y - 12, mast_brown)
# Sail (triangle)
c.poly([(boat_x + 1, boat_y - 11), (boat_x + 1, boat_y - 2), (boat_x + 8, boat_y - 2)], sail_white, fill=True)

# ============ WAVES ============
# White foam waves rolling onto shore
# Wave 1
wave_y = 92
for x in range(0, 128, 8):
    offset = (x // 16) % 2 * 2
    c.line(x, wave_y + offset, x + 6, wave_y + 2 + offset, foam_white)
    c.line(x + 2, wave_y + offset - 1, x + 8, wave_y + 1 + offset, foam_shadow)

# Wave 2 (further out)
wave_y2 = 85
for x in range(4, 128, 10):
    c.line(x, wave_y2, x + 5, wave_y2 + 1, foam_white)

# ============ SAND/BEACH ============
# Beach from y=95 to bottom
c.rect(0, 95, 128, 33, sand_medium)
# Add some texture/variations
for y in range(97, 128, 3):
    for x in range(0, 128, 5):
        if (x + y) % 7 == 0:
            c.set(x, y, sand_light)
        elif (x + y) % 11 == 0:
            c.set(x, y, sand_dark)

# Wet sand at water line (darker)
c.rect(0, 93, 128, 4, sand_dark)

# ============ BEACH UMBRELLA ============
# Umbrella position: left side of beach
umb_x, umb_y = 30, 105

# Umbrella pole
c.rect(umb_x - 1, umb_y, 2, 20, "#654321")

# Umbrella canopy (semi-circle with stripes)
umb_r = 12
# Draw striped canopy using filled circles for stripes
# Draw alternating red and white wedge-like sections
for i in range(9):  # 9 sections for 180 degrees
    angle_start = i * 20
    angle_mid = angle_start + 10
    rad = math.radians(angle_mid)
    # Position for this stripe section
    stripe_x = int(umb_x + umb_r * 0.7 * math.cos(rad))
    stripe_y = int(umb_y - umb_r * 0.7 * math.sin(rad))
    stripe_color = umbrella_red if i % 2 == 0 else umbrella_white
    c.circle(stripe_x, stripe_y, umb_r // 2 + 2, stripe_color)

# Top cap of umbrella
c.circle(umb_x, umb_y - umb_r + 2, 3, "#654321")

# ============ BEACH TOWEL ============
# Striped towel on sand
towel_x, towel_y = 60, 110
towel_w, towel_h = 20, 12

# Towel base
c.rect(towel_x, towel_y, towel_w, towel_h, towel_blue)
# White stripes
for stripe_x in range(towel_x + 2, towel_x + towel_w, 4):
    c.rect(stripe_x, towel_y, 2, towel_h, towel_white)

# ============ FLIP-FLOPS ============
# Two flip-flops near towel
# Left flip-flop
ff1_x, ff1_y = 85, 112
c.ellipse(ff1_x, ff1_y + 4, 5, 3, flip_flop, fill=True)
c.line(ff1_x - 2, ff1_y, ff1_x + 2, ff1_y + 3, flip_flop)

# Right flip-flop
ff2_x, ff2_y = 95, 115
c.ellipse(ff2_x, ff2_y + 4, 5, 3, flip_flop, fill=True)
c.line(ff2_x - 2, ff2_y, ff2_x + 2, ff2_y + 3, flip_flop)

# ============ GULLS ============
# Two gulls flying in the sky
def draw_gull(gx, gy, size):
    # Left wing
    c.line(gx - size, gy, gx, gy + size//2, gull_white)
    c.line(gx - size + 1, gy - 1, gx, gy + size//2 - 1, gull_gray)
    # Right wing
    c.line(gx, gy + size//2, gx + size, gy, gull_white)
    c.line(gx, gy + size//2 - 1, gx + size - 1, gy - 1, gull_gray)
    # Body
    c.set(gx, gy + size//2, gull_white)

draw_gull(45, 35, 6)
draw_gull(75, 30, 5)

# Check stats
print(c.stats_text())

# Submit the canvas
finish(c)
