from pixelbench_api import new_canvas, finish

# Create 48x48 canvas with transparent background
c = new_canvas(48, 48, background=None, name="magic_staff")

# Define colors - staying well within 86 color limit
# Wood tones (5 colors)
dark_wood = c.color('#4A2810')
mid_wood = c.color('#7A4A25')
light_wood = c.color('#A67C52')
highlight_wood = c.color('#C9A87C')
pale_wood = c.color('#E8D5B7')

# Purple magic colors (6 colors)
deep_purple = c.color('#2E003E')
magic_purple = c.color('#5C007A')
bright_purple = c.color('#8B00B8')
vivid_purple = c.color('#A642D0')
light_purple = c.color('#C47AE0')
pale_purple = c.color('#E0B0F0')
glow_white = c.color('#FFFFFF')

# Draw staff - curved wooden pole from bottom-left to upper-center
staff_path = [
    (22, 44), (21, 42), (20, 40), (19, 38), (18, 36),
    (18, 34), (19, 32), (20, 30), (21, 28), (22, 26),
    (23, 24), (24, 22), (25, 20), (26, 18), (27, 16),
    (27, 14), (27, 12)
]

# Draw staff body with wood grain
for idx, (sx, sy) in enumerate(staff_path):
    # Staff width varies - thicker at bottom
    width = 5 if idx < 6 else (4 if idx < 12 else 3)
    half_w = width // 2
    
    for ox in range(-half_w, half_w + 1):
        px = sx + ox
        if 0 <= px < 48 and 0 <= sy < 48:
            # Wood grain with variation
            grain = (idx + ox) % 3
            if grain == 0:
                c.set(px, sy, mid_wood)
            elif grain == 1:
                c.set(px, sy, light_wood)
            else:
                c.set(px, sy, dark_wood)
    
    # Highlight along right edge
    if sx + half_w + 1 < 48:
        c.set(sx + half_w + 1, sy, highlight_wood if idx % 2 == 0 else pale_wood)

# Add wood rings/texture details
ring_positions = [(21, 40), (20, 34), (22, 28), (25, 20), (27, 14)]
for rx, ry in ring_positions:
    c.set(rx, ry, dark_wood)
    if rx - 1 >= 0:
        c.set(rx - 1, ry, mid_wood)

# Crescent head - elegant curved horns
# Left horn
left_horn_outline = [
    (23, 10), (21, 8), (19, 6), (17, 5), (15, 4), (13, 4),
    (12, 5), (11, 7), (11, 9), (11, 11), (12, 13), (14, 14),
    (16, 15), (18, 15), (20, 14), (22, 12)
]

# Right horn
right_horn_outline = [
    (31, 10), (33, 8), (35, 6), (37, 5), (39, 4), (41, 4),
    (42, 5), (43, 7), (43, 9), (43, 11), (42, 13), (40, 14),
    (38, 15), (36, 15), (34, 14), (32, 12)
]

# Draw left horn outline
for px, py in left_horn_outline:
    if 0 <= px < 48 and 0 <= py < 48:
        c.set(px, py, magic_purple)

# Fill left horn with gradient
for py in range(4, 15):
    for px in range(11, 23):
        dist = ((px - 17) ** 2 + (py - 9) ** 2) ** 0.5
        if dist < 6:
            if dist < 1.5:
                c.set(px, py, glow_white)
            elif dist < 2.5:
                c.set(px, py, light_purple)
            elif dist < 3.5:
                c.set(px, py, vivid_purple)
            elif dist < 4.5:
                c.set(px, py, bright_purple)
            elif dist < 5.5:
                c.set(px, py, magic_purple)
            else:
                c.set(px, py, deep_purple)

# Draw right horn outline
for px, py in right_horn_outline:
    if 0 <= px < 48 and 0 <= py < 48:
        c.set(px, py, magic_purple)

# Fill right horn with gradient
for py in range(4, 15):
    for px in range(31, 44):
        dist = ((px - 37) ** 2 + (py - 9) ** 2) ** 0.5
        if dist < 6:
            if dist < 1.5:
                c.set(px, py, glow_white)
            elif dist < 2.5:
                c.set(px, py, light_purple)
            elif dist < 3.5:
                c.set(px, py, vivid_purple)
            elif dist < 4.5:
                c.set(px, py, bright_purple)
            elif dist < 5.5:
                c.set(px, py, magic_purple)
            else:
                c.set(px, py, deep_purple)

# Central ornate gem at the apex
gem_x, gem_y = 27, 9
c.circle(gem_x, gem_y, 3, vivid_purple, fill=True)
c.set(gem_x, gem_y, glow_white)
c.set(gem_x - 1, gem_y, light_purple)
c.set(gem_x, gem_y - 1, light_purple)
c.set(gem_x + 1, gem_y, light_purple)
c.set(gem_x, gem_y + 1, light_purple)

# Gem setting/connector to staff
for i in range(3):
    c.set(gem_x, gem_y + 3 + i, magic_purple)
    if i < 2:
        c.set(gem_x - 1, gem_y + 3 + i, deep_purple)
        c.set(gem_x + 1, gem_y + 3 + i, deep_purple)

# Magic particle effects - swirling energy around staff head
particles = [
    # Left side swirl
    (6, 6), (4, 9), (5, 12), (7, 15), (9, 17), (11, 19),
    # Right side swirl
    (48, 6), (50, 9), (49, 12), (47, 15), (45, 17), (43, 19),
    # Top arc
    (14, 2), (18, 1), (22, 0), (27, 0), (32, 0), (36, 1), (40, 2),
    # Inner sparkles near horns
    (12, 5), (42, 5), (15, 7), (39, 7),
    # Rising particles from gem
    (25, 5), (29, 5), (27, 3), (24, 4), (30, 4)
]

for px, py in particles:
    if 0 <= px < 48 and 0 <= py < 48:
        c.set(px, py, pale_purple)

# Tiny sparkle dots
sparkles = [
    (8, 5), (10, 10), (46, 5), (44, 10),
    (13, 3), (41, 3), (18, 5), (36, 5),
    (11, 14), (43, 14), (23, 6), (31, 6),
    (20, 8), (34, 8), (16, 11), (38, 11)
]
for px, py in sparkles:
    if 0 <= px < 48 and 0 <= py < 48:
        c.set(px, py, light_purple)

# Magic trail wisps - ethereal lines
wisps = [
    (7, 4), (6, 7), (7, 10), (9, 13), (12, 16),
    (47, 4), (48, 7), (47, 10), (45, 13), (42, 16),
    (16, 2), (20, 1), (34, 1), (38, 2)
]
for px, py in wisps:
    if 0 <= px < 48 and 0 <= py < 48:
        c.set(px, py, pale_purple)

# Additional magic glow dots around the whole head area
glow_dots = [
    (10, 8), (44, 8), (14, 12), (40, 12),
    (19, 4), (35, 4), (22, 7), (32, 7)
]
for px, py in glow_dots:
    if 0 <= px < 48 and 0 <= py < 48:
        c.set(px, py, pale_purple)

print(c.stats_text())
print(c.matrix_text(region=(4, 0, 48, 47)))

finish(c)
