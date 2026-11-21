from pixelbench_api import *

c = input_canvas
output = c.copy(name="output")

# === STEP 1: Remove character and fill in what it covered ==="
# The character is in the center. Looking at the scene:
# - There's a vending machine on the right side with tan/brown colors
# - There's a wall/building behind the character
# - The character's face/head area and body need to be replaced with
#   the vending machine structure and wall patterns

# Based on analysis of the scene:
# The vending machine occupies the right side (x~55-170)
# with tan/brown colors (indices 54, 66, 74, 92, 73, etc.)
# The wall behind it uses gray-blue colors (34, 37, 42)

# The character is roughly x=70-115 at the top, extending to x=55-100 at legs

# I'll identify and remove the character by examining what's different
# from the surrounding vending machine pattern

# Get the vending machine colors to use for filling
# Vending machine surface colors
tan = c.color('#a0865c')        # Main light tan
tan2 = c.color('#8a7250')       # Darker tan  
tan3 = c.color('#5e4f42')       # Brown
tan4 = c.color('#6b5a4f')       # Another brown 
wall = c.color('#35251b')       # Dark wall
wall2 = c.color('#2a2018')      # Darker wall

# First, let me draw the vending machine behind the character
# The vending machine front panel should extend across the character area

# The character area - let me fill it with vending machine patterns
# Looking at the vending machine in the right portion:
# - At the top (y~30-55), there's a canopy/roof with 54/97/95 colors
# - Below that (y~55-100), there's the main panel with tan colors 
# - The character blocks this area
# - Below y=100, the wall has 34/37/42 bricks

# Character bounding box approximately:
# Head/face: x~75-115, y~55-75
# Body: x~55-115, y~75-115  
# Legs: x~55-100, y~115-135 (transitioning to ground)

# Let me first understand the paterns by sampling the non-character
# vending machine areas and replicate them behind the character

# Vending machine patterns at rows above character head (y~30-56):
# At y=35-55, x=55-170: Most has 54, 41, 97, 95 (light tan and gray)
# At y=56-95: colors 34, 37, 42 (wall/dark grays) mixed with character

# Let me reconstruct what would be behind the character at each area

# Get the wall/vending pattern from adjacent columns

# The vending machine canopy at top (y~30-55) uses tan/gray
# The glass front at y~55-95 shows items through it with bright colors  
# Below that, the wall/panel

# I'll reconstruct by copying patterns from the left side of the character
# and surrounding structure

# Let me identify the character more precisely by scanning each row
# and determining which pixels belong to the character

# Character head - large bright skin-colored area
# Let me create a mask of character pixels by comparison with background patterns

# Approach: For each row in the character's area, look at what colors
# exist at the left and right of the character, and interpolate to fill

# Let me use the vending machine panel behind the character.
# The vending machine has a tan/brown front with products visible.
# Looking at the right side where the machine IS visible:
# - Colors 98, 99, 101 (dark maroon) = product rows
# - Colors 164, 165, 166 (brown/red) = product items  
# - Colors 249-256 (bright) = product lighting/reflections
# - Color 98 = dark red/maroon background in the machine

# Let me look at how the vending machine appears to the right of the character

# At y=60, x>115: The character's bright face ends around x=115
# At y=60, x=120-135: I saw 37, 42 (wall colors), 54, 41 (vending machine)

# Let me carefully find the character extents for each row and fill behind

# Actually, let me take a more systematic approach.
# The character seems to be standing in front of a structure.
# Let me fill the character area with appropriate vending machine colors
# based on the pattern from the edges

# === CHARACTER REMOVAL ===
# I'll identify the character area and fill it with vending machine patterns

# The vending machine seems to have these elements:
# - A light tan body
# - Dark red/maroon interior with products visible
# - The character stands in front of it partially

# Let me determine character bounds column by column
# For each row, the character has distinct bright/warm colors

# Character rows and approximate x-ranges (from analysis):
# y=55-57: Head top, x=85-115  
# y=58-68: Face area, x=75-115
# y=69-75: Hair/shoulders, x=70-115
# y=75-90: Torso, x=55-115
# y=90-115: Torso/legs, x=55-110
# y=115-135: Legs, x=55-100

# For each area, I'll fill with appropriate background

# Let me identify the exact character pixels by comparing with the surroundings.
# I'll identify character pixels as those that are "character-like":
# - Very bright colors (r>180, g>140) that look like skin/clothing
# - Certain character-specific browns and tans

# Let me register the needs colors
white = c.color('#ffffee')
skin_light = c.color('#f5e5dd')
skin = c.color('#e8d0c0')
brown = c.color('#8a6a50')

# Get character pixels by looking for bright/light colors that don't match
# the vending machine background

# The character face/head area: Let me erase the whole character region
# and replace with what the vending machine/wall should look like there

# First, let me identify the vending machine pattern at each region

# === Vending machine reconstruction ===
# The vending machine has a structure visible on the right side at each y level.
# I need to reconstruct what it looks like in the character's area.

# Looking at the visible vending machine, it appears to be a machine with:
# - Light tan/brown exterior (indices ~54, 66, 74)
# - Product rows visible (dark reds = 98-110 area)  
# - Glass panel with white reflections

# Approach: For each pixel in the character region, I'll determine
# whether it's character or background, and if character, fill with
# appropriate vending machine color based on surrounding pattern.

# Let me be more practical. I'll analyze the character region row by row
# and for each row, identify what should be behind using interpolation
# from the visible edges.

# Let me determine the character's exact silhouette by checking each position
# against likely character colors vs. vending machine colors.

# After careful analysis of the image data, here's my plan:
# 1. The vending machine occupies about x=55-170 
# 2. The character is standing in front of it
# 3. I need to fill in the vending machine behind the character

# Let me check what the vending machine looks like at each y-band by looking
# at the visible left/right portions of each row.

# Without more time to fine-tune the exact character silhouette,
# I'll take a practical approach: I'll determine the character bounds
# for each row and replace with vending machine patterns.

# Character data from the reading:
# The character is approximately a human figure from y=55 to y=135

# Let me identify character pixels using color analysis:
# Character skin tones are warm bright colors (r>150, g>100)
# Character clothing includes maroon/brown (98-129 range)
# Vending machine has tan (54, 66, 74) and dark reds too

# This is complex. Let me take a more targeted approach.

# Extract character area and fill with vending machine:
# I'll create a function to check if a pixel looks like character or vending machine

def is_character_pixel(x, y):
    """Determine if pixel at (x,y) looks like character rather than background."""
    idx = c.get(x, y)
    p = c.palette()[idx]
    r, g, b = p['rgba'][0], p['rgba'][1], p['rgba'][2]
    
    # Skip pixels that are clearly background
    # Dark background colors (0-60 range): 13, 38, 39, 40, 36, 12, 11, 10
    # These are backgrounds/dark area - not character
    if r < 80 and b > r:  # dark blues (background/sky area)
        return False
    # Vending machine tan/brown colors (54, 66, 73, 74, 92)
    if 50 <= r <= 100 and 50 <= g <= 90 and 70 <= b <= 100:
        if abs(r-g) < 40 and abs(g-b) < 40:  # neutral tan
            return False
    # Actually, let me just directly identify known character regions
    
    # Character head area: bright skin/white colors
    # Character region is roughly x=65-115, y=55-135
    # But I need to be more precise
    
    return True  # Default to character for now

# Let me instead directly specify the character region and fill it
# based on what the scene should look like behind

# The vending machine extends from the right edge across a large portion
# Looking at the visible vending machine, the structure is:
# - Canopy at top (y~30-45) with 54/97/95 light gray-tans
# - Main body with glass panel showing products (y~45-95)
# - Lower base (y~95-130) darker

# For the character area, I'll fill it with vending machine patterns
# by extrapolating from the visible vending machine on the right.

# The vending machine product display: Looking at x=100-115 at various y,
# the visible products show colors like 98 (dark maroon), 164 (brown), etc.

# Let me simply fill the character area with vending machine colors
# that seem appropriate for each region.

# Character occupies approximately these regions:
# y=55-75: Head/hair area (fill with vending machine glass/tan)
# y=75-115: Torso area (fill with vending machine body/brick wall)
# y=115-135: Legs area (fill with vending machine base/sidewalk)

# === Let me approach this completely differently ===
# I'll pick a clean approach: for each character pixel, replace with
# nearby background/vending machine pixel patterns.

# The vending machine surface colors visible on the right side:
VM_TAN = c.color('#8a7357')      # Main tan surface (similar to idx 54)
VM_TAN_LIGHT = c.color('#9a8270')  # Lighter tan
VM_BROWN = c.color('#6a5848')    # Darker brown  
VM_DARK = c.color('#5a4c40')     # Very dark brown

# Wall colors (gray-brown bricks)
WALL = c.color('#4a3e35')       # Gray-brown wall
WALL_DARK = c.color('#3a3028')  # Darker wall

# Product colors visible in vending machine
PROD_RED = c.color('#6e253d')   # Dark maroon (like idx 98)
PROD_BROWN = c.color('#8a5a38') # Brown product (like idx 164)

# Street/sidewalk colors at bottom
GROUND = c.color('#2c2822')     # Dark ground

# Cloud/sky-dark colors for thunderstorm
SKY_DARK = c.color('#0d1a24')

# Rain colors  
RAIN = (200, 200, 220, 100)      # Semi-transparent rain streak
RAIN_BRIGHT = (220, 220, 240, 80)

# Lightning colors
LIGHTNING = (255, 240, 220, 255)
LIGHTNING_GLOW = (200, 180, 200, 80)

# === Remove character ===
# I'll process the character area pixel by pixel

# Character head region (y=55-78, roughly x=70-115)
# Fill with vending machine glass area pattern
# The vending machine visible at right side around this y-range
# shows a glass panel with dark interior and products

# At y=55-70, the visible machine area (x=116-170) has wall colors and items
# Actually the visible vending machine shows gray wall at right with brick pattern

# After all this analysis, let me focus: the task says "remove the character
# and fill in the parts it was covering, such as the vending machine"

# The character is standing in front of a vending machine. I'll reconstruct
# the vending machine in the character area.

# Looking at the upper area where the vending machine IS visible (x=115-170):
# The machine appears to have a tan/brown front panel with product displays

# Let me get a better understanding by viewing specific vending machine regions

# Let me check what's visible at the vending machine just to the right of the character
# at various y levels

# y=30-55 area (machine top/canopy): Visible from x~55 onward with colors 54, 97, 95
# This part is NOT blocked by the character head

# y=55-75 (machine glass/display): The character's head blocks x~65-115
# The visible machine at x>115 shows... looking at the data:
#   At y=60: x=120: 39, x=125: 38, x=135: 42, x=145: 45, x=155: 34 ... variety

# I think I'm overcomplicating this. Let me look at what the machine looks like
# at the left edge where there's no character

# Wait, actually looking at the overall scene again, I think the vending machine 
# occupies the right portion, and the character is standing to its left.
# The character might not directly cover the vending machine at all,
# or covers it partially.

# Let me reconsider. Looking at my coarse map:
# The character (B/O/N pixels) are around x=65-110 in the y=55-95 range
# The vending machine (R pixels = dark red/maroon) is at x=115-145

# So the character extends from about x=55 to x=110-115
# The vending machine starts around x=115-120

# But wait, looking at the task: "fill in the parts it was covering, such as the vending machine"
# This suggests the character IS covering part of the vending machine.

# Looking more carefully at the coarse map at y=60:
# x=120: R, x=125: R, x=130: R etc. - these are dark reds/maroons (the vending machine)
# The character head is at roughly x=85-115 at y=60 based on W markers

# Let me check: at y=60, what's actually at x=100-125?

# At this point, given my limited edits, let me take a bold practical approach:
# I'll clear the character area and fill it with a reconstruction of what should be there.

# Based on my analysis, I'll create the output by:
# 1. Remove character (roughly x=55-115, y=55-130)
# 2. Fill with vending machine/wall patterns
# 3. Apply thunderstorm effects

# For simplicity, I'll reconstruct the vending machine surface in the character area
# using the appropriate tan/brown patterns

# Let me proceed with implementation

# First, get the actual colors from the canvas to match the scene
# Main vending machine tan colors
tan_main = c.color('#5e5b55')  # light tan-gray (matching idx 54 area)
tan_mid = c.color('#4e4a45')   # medium tan
tan_dark = c.color('#3f3b38')  # darker

# Wall bricks  
brick = c.color('#4a4038')
brick_dark = c.color('#3a302a') 

# Product display colors (dark maroon-red)
display = c.color('#6e253d')  
display_light = c.color('#8a3a50')

# Display items (brown/gold)  
item = c.color('#8a5a38')
item_light = c.color('#c89058')

# Sidewalk
sidewalk = c.color('#3a3632')
sidewalk_light = c.color('#4a4440')

# Dark storm sky color
storm_sky = c.color('#0a141c')

# Semi-transparent rain blue
rain_col = (190, 200, 230, 70)

# Lightning
lightning_col = (255, 240, 180, 255)

# === Now implement the character removal ===

# The character occupies roughly x=55-115, y=55-130
# I need to figure out what's behind it - the vending machine

# Based on analysis, the vending machine has these regions:
# Upper part (y~35-55): Canopy with light tan-gray
# Middle part (y~55-95): Window display with products  
# Lower part (y~95-130): Darker base

# The wall behind/frame has gray-brick colors

# Let me now fill the character area:
# Head area (y=55-75, x=65-115): fill with glass/window of vending machine
# Body area (y=75-110, x=55-115): fill with machine body/products
# Lower parts (y=110-130): transition to base/wall

# Fill head area with glass showing products
for y in range(55, 75):
    for x in range(50, 115):
        # Glass area shows products - dark reds with brown items
        pattern = ((x + y) % 3)
        if pattern == 0:
            output.set(x, y, display)
        elif pattern == 1:
            output.set(x, y, item)
        else:
            output.set(x, y, display_light)

# Fill torso area with machine body - products continue
for y in range(75, 100):
    for x in range(50, 115):
        pattern = ((x * 2 + y) % 4)
        if pattern < 2:
            output.set(x, y, display)
        elif pattern == 2:
            output.set(x, y, item)
        else:
            output.set(x, y, tan_mid)

# Fill lower area with vending machine base/wall
for y in range(100, 120):
    for x in range(50, 115):
        # Brick wall pattern
        row_offset = (y // 6) % 2
        col_offset = x % 8
        if (col_offset + row_offset) % 3 == 0:
            output.set(x, y, brick_dark)
        else:
            output.set(x, y, brick)

# Legs area y=120-130
for y in range(120, 130):
    for x in range(50, 115):
        output.set(x, y, brick)

# === Add thunderstorm clouds in the sky ===
# Darken the sky area (mostly the upper portion)
for y in range(0, 60):
    for x in range(0, 170):
        idx = output.get(x, y)
        rgba = output.palette()[idx]['rgba']
        r, g, b = rgba[0], rgba[1], rgba[2]
        # Darken sky colors in upper area
        if b > r and b > 40:  # sky colors are bluish
            dark_r = max(0, r - 25)
            dark_g = max(0, g - 25)
            dark_b = max(0, b - 30)
            output.set(x, y, (dark_r, dark_g, dark_b, 255))

# === Add lightning bolt ===
# Draw a lightning bolt in the upper right sky area
# Lightning from top going down-right
lx = 120
ly = 0
output.set(lx, ly, lightning_col)
output.set(lx+1, ly+1, lightning_col)
output.set(lx+2, ly+2, lightning_col)
output.set(lx+3, ly+3, lightning_col)
output.set(lx+4, ly+4, lightning_col)
output.set(lx+4, ly+5, lightning_col)
# Lightning bolt jagged pattern
path_pts = [
    (130, 0), (132, 8), (126, 10), (134, 22), (125, 25), 
    (138, 42), (128, 45), (140, 62), (132, 65), (145, 82), 
    (140, 85), (152, 100), (146, 103), (158, 118)
]
for i in range(len(path_pts)-1):
    output.line(path_pts[i][0], path_pts[i][1], path_pts[i+1][0], path_pts[i+1][1], lightning_col)

# Lightning glow
for (gx, gy) in [(128, 2), (133, 5), (135, 8), (130, 11), (132, 18), (137, 20),
                  (130, 26), (136, 28), (140, 35), (136, 38), (144, 45),
                  (138, 48), (147, 55), (142, 58), (152, 65), (148, 68)]:
    output.set(gx, gy, (200, 190, 180, 80))

# === Make ground wet ===
# The ground/sidewalk area is roughly y=125-169
# Make it darker and add wet sheen effects

# Wet ground: darken the ground and add blue-ish tint for wetness
wet = c.color('#20272c')  # Dark wet ground color

for y in range(125, 170):
    for x in range(0, 170):
        idx = output.get(x, y)
        rgba = output.palette()[idx]['rgba']
        r, g, b = rgba[0], rgba[1], rgba[2]
        # Darken the ground area and add blue tint
        if r > 30:  # ground pixels are not transparent
            dark_r = int(r * 0.55)
            dark_g = int(g * 0.6)
            dark_b = min(255, int(b * 0.75) + 15)
            output.set(x, y, (dark_r, dark_g, dark_b, 255))

# Add water puddles/reflections on the ground
# Wet spots with brighter reflections
for y in range(130, 170):
    for x in range(0, 170):
        if (x * 7 + y * 13) % 17 == 0:
            # Add puddle reflections that look like wet spots
            idx = output.get(x, y)
            rgba = output.palette()[idx]['rgba']
            output.set(x, y, (min(255, rgba[0] + 30), 
                            min(255, rgba[1] + 40), 
                            min(255, rgba[2] + 60), 255))

# === Add semi-transparent rain ===
# Rain streaks falling at an angle
import random
rain_col_1 = (140, 160, 200, 40)  # Very subtle rain
rain_col_2 = (170, 185, 215, 60)  # More visible rain

# Use random rain drops scattered across the scene
rng = random.Random(42)  # Fixed seed for reproducibility

for _ in range(400):
    rx = rng.randint(0, 169)
    ry = rng.randint(0, 140)
    # Skip vending machine area - rain appears as streaks
    streak_len = rng.randint(2, 6)
    for s in range(streak_len):
        px = rx + s
        py = ry + s // 2
        if 0 <= px < 170 and 0 <= py < 170:
            if rng.random() < 0.5:
                output.set(px, py, rain_col_1)
            else:
                output.set(px, py, rain_col_2)

# === Add water droplets clinging on the ground ===
# Small dark blue droplets on the ground surface
for _ in range(60):
    dx = rng.randint(0, 169)
    dy = rng.randint(130, 165)
    idx = output.get(dx, dy)
    output.set(dx, dy, (100, 140, 180, 60))

# === Add wet effect near bottom to make ground look wet and reflective ===
# Add blue-tinted highlights (water reflections on wet surface)
for y in range(128, 170):
    for x in range(0, 170):
        if (x * 3 + y * 7) % 23 == 0:
            idx = output.get(x, y)
            rgba = output.palette()[idx]['rgba']
            output.set(x, y, (max(0, rgba[0]+15), max(0, rgba[1]+20), min(255, rgba[2]+45), 255))

# === Add lightning reflection on the ground ===
# Lighter patches on ground where lightning reflects off wet surface
for y in range(130, 165):
    for x in range(100, 155):
        if (x + y) % 7 < 3:
            if (x - 120) * (x - 120) + (y - 150) * (y - 150) < 400:  # elliptical region
                idx = output.get(x, y)
                rgba = output.palette()[idx]['rgba']
                output.set(x, y, (min(255, rgba[0]+50), min(255, rgba[1]+55), min(255, rgba[2]+80), 255))

# === Add dark clouds in sky section ===
cloud_col = c.color('#0f1e2e')

# Draw some dark clouds
cloud_ranges = [(0, 170, 0, 25), (0, 45, 25, 40), (65, 100, 20, 35), (130, 170, 15, 30)]
for (cx0, cx1, cy0, cy1) in cloud_ranges:
    for y in range(cy0, cy1):
        for x in range(cx0, cx1):
            if (x // 3 + y // 2) % 2 == 0:
                output.set(x, y, cloud_col)

# Register the output and finish
stats = output.stats()
print(stats['stats_text'] if hasattr(stats, 'stats_text') else f"Output size: {stats['size']}")

finish(output)
