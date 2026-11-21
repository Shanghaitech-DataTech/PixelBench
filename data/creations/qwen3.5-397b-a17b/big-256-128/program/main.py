from pixelbench_api import *

# Create output canvas
output = input_canvas.copy(name='output')

# Define the demon castle color palette
COLORS = {
    'bg_dark': output.color('#0a0510'),
    'bg_mid': output.color('#1a0a15'),
    'castle_dark': output.color('#150810'),
    'castle_mid': output.color('#2a1018'),
    'castle_light': output.color('#3d1820'),
    'blood_moon_core': output.color('#8b0000'),
    'blood_moon_mid': output.color('#b22222'),
    'blood_moon_edge': output.color('#cd5c5c'),
    'blood_moon_glow': output.color('#ff4444'),
    'accent_purple': output.color('#4a1a4a'),
    'accent_crimson': output.color('#660000'),
    'window_glow': output.color('#ff6600'),
    'spire_dark': output.color('#0d0308'),
    'mist': output.color('#2a1520'),
}

# Fill background with dark sky
output.rect(0, 0, 256, 128, COLORS['bg_dark'])

# Create gradient sky - blood red at top, dark at bottom
for y in range(0, 60):
    intensity = y / 60.0
    r = int(26 + (139 - 26) * intensity)
    g = int(10 + (0 - 10) * intensity)
    b = int(21 + (0 - 21) * intensity)
    color = output.color((r, g, b))
    output.rect(0, y, 256, 1, color)

for y in range(60, 128):
    intensity = (y - 60) / 68.0
    r = int(26 + (10 - 26) * intensity)
    g = int(10 + (5 - 10) * intensity)
    b = int(21 + (16 - 21) * intensity)
    color = output.color((r, g, b))
    output.rect(0, y, 256, 1, color)

# Draw blood moon
moon_cx, moon_cy = 180, 35
moon_r = 28

for r in range(moon_r, -1, -1):
    if r > moon_r * 0.7:
        color = COLORS['blood_moon_edge']
    elif r > moon_r * 0.4:
        color = COLORS['blood_moon_mid']
    else:
        color = COLORS['blood_moon_core']
    output.circle(moon_cx, moon_cy, r, color, fill=True)

# Moon glow
for r in range(moon_r + 2, moon_r + 8):
    alpha = int(80 * (1 - (r - moon_r) / 8))
    if alpha > 0:
        glow_color = output.color((255, 68, 68, alpha))
        output.circle(moon_cx, moon_cy, r, glow_color, fill=True)

# Castle - main structures
castle_base_y = 85

# Left tower
output.rect(20, 60, 35, 68, COLORS['castle_dark'])
output.rect(25, 50, 25, 15, COLORS['castle_mid'])
for i in range(12):
    width = max(1, 8 - i)
    output.rect(30 - width//2, 50 - i, width, 1, COLORS['spire_dark'])

# Center main keep
output.rect(80, 70, 70, 58, COLORS['castle_mid'])
output.rect(90, 55, 50, 20, COLORS['castle_dark'])
output.rect(95, 40, 40, 20, COLORS['castle_mid'])
for i in range(18):
    width = max(1, 12 - i)
    output.rect(115 - width//2, 40 - i, width, 1, COLORS['spire_dark'])

# Flag on main spire
output.rect(125, 28, 12, 1, COLORS['accent_crimson'])
output.rect(125, 29, 10, 1, COLORS['accent_crimson'])
output.rect(125, 30, 8, 1, COLORS['accent_crimson'])

# Right tower
output.rect(180, 65, 35, 63, COLORS['castle_dark'])
output.rect(185, 52, 25, 18, COLORS['castle_mid'])
for i in range(14):
    width = max(1, 9 - i)
    output.rect(197 - width//2, 52 - i, width, 1, COLORS['spire_dark'])

# Small towers
output.rect(55, 80, 20, 48, COLORS['castle_dark'])
for i in range(8):
    width = max(1, 6 - i)
    output.rect(65 - width//2, 80 - i, width, 1, COLORS['spire_dark'])

output.rect(220, 75, 25, 53, COLORS['castle_dark'])
for i in range(10):
    width = max(1, 7 - i)
    output.rect(232 - width//2, 75 - i, width, 1, COLORS['spire_dark'])

# Battlements
for bx in range(85, 145, 8):
    output.rect(bx, 68, 5, 6, COLORS['castle_dark'])

# Windows
window_positions = [
    (35, 75), (45, 75), (35, 95), (45, 95),
    (100, 85), (120, 85), (140, 85),
    (100, 105), (120, 105), (140, 105),
    (195, 80), (205, 80), (195, 100),
    (60, 95), (227, 95),
]

for wx, wy in window_positions:
    output.rect(wx, wy, 4, 6, COLORS['window_glow'])
    output.set(wx, wy, COLORS['castle_dark'])
    output.set(wx+3, wy, COLORS['castle_dark'])
    output.set(wx, wy+5, COLORS['castle_dark'])
    output.set(wx+3, wy+5, COLORS['castle_dark'])

# Mist at base
for y in range(115, 128):
    for x in range(0, 256, 4):
        if (x + y) % 7 < 4:
            alpha = 60 - (y - 115) * 5
            if alpha > 0:
                mist_color = output.color((42, 21, 32, alpha))
                output.rect(x, y, 4, 1, mist_color)

# Banners
for i in range(20):
    output.rect(15, 55 + i, 2, 1, COLORS['accent_crimson'])
output.rect(15, 75, 8, 1, COLORS['accent_crimson'])
output.rect(15, 76, 6, 1, COLORS['accent_crimson'])

for i in range(15):
    output.rect(245, 60 + i, 2, 1, COLORS['accent_purple'])
output.rect(245, 75, 7, 1, COLORS['accent_purple'])

# Floating particles
import random
random.seed(42)
for _ in range(30):
    px = moon_cx + random.randint(-50, 50)
    py = moon_cy + random.randint(-40, 40)
    if 0 <= px < 256 and 0 <= py < 128:
        output.set(px, py, COLORS['blood_moon_glow'])

# Ground
output.rect(0, 120, 256, 8, COLORS['castle_dark'])
output.rect(0, 125, 256, 3, COLORS['bg_dark'])

print("Demon King's Castle transformation complete!")
print(output.stats_text())

finish(output)
