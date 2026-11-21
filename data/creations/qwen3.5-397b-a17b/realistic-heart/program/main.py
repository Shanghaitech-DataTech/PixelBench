from pixelbench_api import *

# Create a 64x64 canvas
c = new_canvas(64, 64, name="heart")

# Define a realistic heart color palette
# Base reds, shadows, highlights, and subtle variations
colors = {
    'shadow_dark': c.color('#4a0a0a'),      # deepest shadow
    'shadow': c.color('#6b1212'),           # dark shadow
    'shadow_mid': c.color('#8b1a1a'),       # medium shadow
    'base_dark': c.color('#a32020'),        # dark base red
    'base': c.color('#c42b2b'),             # main red
    'base_light': c.color('#d93838'),       # lighter red
    'highlight': c.color('#e85252'),        # highlight
    'highlight_light': c.color('#f06868'),  # lighter highlight
    'specular': c.color('#ffb3b3'),         # specular highlight
    'rim_light': c.color('#ff8080'),        # rim light
    'inner_shadow': c.color('#5c0f0f'),     # inner depth shadow
    'vein': c.color('#8b1515'),             # subtle vein color
    'warm_shadow': c.color('#7a1818'),      # warm shadow tone
}

# Draw the heart shape using path for smooth curves
# Heart is centered, roughly 48x48 pixels with some margin
heart_path = """
M 32 52
C 10 35, 2 22, 2 12
C 2 4, 8 -2, 16 -2
C 24 -2, 28 6, 32 12
C 36 6, 40 -2, 48 -2
C 56 -2, 62 4, 62 12
C 62 22, 54 35, 32 52
Z
"""

# Fill the heart with base color
c.path(heart_path, colors['base'], fill=True)

# Add depth shading - darker on bottom and edges
# Bottom shadow gradient
for y in range(40, 53):
    shade_intensity = (y - 40) / 13
    if shade_intensity < 0.3:
        shade = colors['shadow_mid']
    elif shade_intensity < 0.6:
        shade = colors['shadow']
    else:
        shade = colors['shadow_dark']
    
    # Calculate width at this y level for the heart shape
    # Heart gets narrower toward bottom
    width_factor = (52 - y) / 12
    half_width = int(20 * width_factor)
    if half_width < 2:
        half_width = 2
    
    for x in range(32 - half_width, 32 + half_width + 1):
        if 0 <= x < 64:
            existing = c.get(x, y)
            if existing == colors['base'] or existing == colors['base_dark']:
                c.set(x, y, shade)

# Left lobe shadow (darker on outer edge)
for angle in range(180, 270, 5):
    import math
    rad = math.radians(angle)
    for r in range(15, 22):
        x = int(16 + r * math.cos(rad))
        y = int(8 + r * math.sin(rad) * 0.8)
        if 0 <= x < 64 and 0 <= y < 64:
            c.set(x, y, colors['shadow_mid'])

# Right lobe shadow
for angle in range(270, 360, 5):
    import math
    rad = math.radians(angle)
    for r in range(15, 22):
        x = int(48 + r * math.cos(rad))
        y = int(8 + r * math.sin(rad) * 0.8)
        if 0 <= x < 64 and 0 <= y < 64:
            c.set(x, y, colors['shadow_mid'])

# Add highlights on upper lobes (light source from top-left)
# Left lobe highlight
for y in range(2, 14):
    for x in range(8, 24):
        # Check if we're on the upper-left curve
        dist_from_center = math.sqrt((x - 16)**2 + (y - 8)**2)
        if 10 < dist_from_center < 16:
            existing = c.get(x, y)
            if existing == colors['base']:
                if dist_from_center < 12:
                    c.set(x, y, colors['highlight'])
                elif dist_from_center < 14:
                    c.set(x, y, colors['highlight_light'])

# Right lobe highlight (slightly less intense)
for y in range(2, 14):
    for x in range(40, 56):
        dist_from_center = math.sqrt((x - 48)**2 + (y - 8)**2)
        if 10 < dist_from_center < 16:
            existing = c.get(x, y)
            if existing == colors['base']:
                if dist_from_center < 13:
                    c.set(x, y, colors['highlight_light'])

# Specular highlight near center-top (the "shine")
c.circle(30, 14, 3, colors['specular'], fill=True)
c.circle(32, 12, 2, colors['specular'], fill=True)

# Add subtle gradient from top to bottom
for y in range(10, 45):
    gradient_factor = (y - 10) / 35
    for x in range(10, 54):
        existing = c.get(x, y)
        if existing == colors['base']:
            if gradient_factor < 0.4:
                c.set(x, y, colors['base_light'])
            elif gradient_factor > 0.7:
                c.set(x, y, colors['base_dark'])

# Add inner shadow/depth in the center cleft
for y in range(12, 25):
    for x in range(28, 36):
        dist_from_cleft = abs(x - 32)
        if dist_from_cleft < 3 and y > 15:
            c.set(x, y, colors['inner_shadow'])

# Add rim light on bottom right edge
for y in range(45, 53):
    for x in range(35, 45):
        dist = math.sqrt((x - 40)**2 + (y - 50)**2)
        if 3 < dist < 6:
            existing = c.get(x, y)
            if existing in [colors['shadow'], colors['shadow_mid']]:
                c.set(x, y, colors['rim_light'])

# Add subtle veins/texture (very faint)
import random
random.seed(42)
for _ in range(30):
    vx = random.randint(18, 46)
    vy = random.randint(20, 45)
    existing = c.get(vx, vy)
    if existing in [colors['base'], colors['base_dark']]:
        c.set(vx, vy, colors['vein'])

# Outline the heart subtly with darker edge
c.outline(colors['shadow'])

print(c.stats_text())
print(c.matrix_text(region=(10, 0, 54, 54)))

finish(c)
