from pixelbench_api import new_canvas, finish

# Create 128x128 canvas for cyberpunk alley
c = new_canvas(128, 128, name="cyberpunk_alley")

# Define color palette
# Background and atmosphere
c.color("#0a0a14", "night_sky")      # Dark night sky
c.color("#12121f", "dark_wall")       # Building walls
c.color("#1a1a2e", "wall_mid")        # Mid-tone walls
c.color("#0d1b2a", "wet_ground")      # Wet ground base

# Neon colors - bright and saturated
c.color("#ff006e", "neon_pink")       # Hot pink neon
c.color("#00f5d4", "neon_cyan")       # Bright cyan
c.color("#ffe600", "neon_yellow")     # Yellow neon
c.color("#9d4edd", "neon_purple")     # Purple neon
c.color("#ff6b35", "neon_orange")     # Orange neon
c.color("#00b4d8", "neon_blue")       # Blue neon

# Building details
c.color("#2d2d44", "brick_dark")      # Dark bricks
c.color("#3d3d5c", "brick_mid")       # Mid bricks
c.color("#1f1f33", "shadow")          # Deep shadows
c.color("#4a4a6a", "highlight")       # Wall highlights

# Ground and reflections
c.color("#16213e", "puddle_dark")     # Puddle base
c.color("#1e3a5f", "puddle_mid")      # Puddle reflection base
c.color("#0f3460", "reflection")      # Light reflection in water

# Person silhouette
c.color("#050508", "person_silhouette")  # Person figure
c.color("#1a1a25", "umbrella_edge")   # Umbrella rim

# Vending machine
c.color("#2a2a40", "vending_body")    # Vending machine body
c.color("#00ff88", "vending_light")   # Vending glow
c.color("#ff3366", "vending_red")     # Vending red elements

# Power cables
c.color("#3a3a50", "cable")           # Cable color
c.color("#5a5a7a", "cable_highlight") # Cable highlight

# Windows
c.color("#1a3a5c", "window_dark")     # Dark window
c.color("#2a5a8c", "window_lit")      # Lit window
c.color("#4a8acc", "window_bright")   # Bright window

# Rain
c.color("#6a8acc", "rain")            # Rain streaks

# === DRAWING THE SCENE ===

# 1. Background - night sky and ground
c.rect(0, 0, 128, 50, "night_sky")      # Sky area
c.rect(0, 80, 128, 48, "wet_ground")    # Ground area

# 2. Left building facade (perspective - wider at bottom)
# Main wall
for y in range(10, 90):
    x_offset = (y - 10) // 4
    c.rect(x_offset, y, 35 - x_offset//2, 1, "dark_wall")

# Brick pattern on left wall
for y in range(15, 85, 4):
    x_offset = (y - 10) // 4
    for x in range(x_offset, 35 - x_offset//2, 6):
        c.rect(x, y, 4, 2, "brick_mid")

# Right building facade
for y in range(10, 90):
    x_start = 95 + (y - 10) // 4
    c.rect(x_start, y, 33 - (y-10)//4, 1, "dark_wall")

# Brick pattern on right wall
for y in range(15, 85, 4):
    x_start = 95 + (y - 10) // 4
    for x in range(x_start, 128 - (y-10)//4, 6):
        c.rect(x, y, 4, 2, "brick_mid")

# 3. Neon signs - left side
# Pink neon sign (vertical)
c.rect(8, 20, 18, 4, "neon_pink")
c.rect(10, 24, 14, 12, "neon_pink", fill=False)
c.rect(11, 25, 12, 10, "night_sky")  # Inner cut
# Glow effect
c.rect(7, 19, 20, 6, "neon_pink")
c.set(6, 20, "neon_pink")
c.set(27, 20, "neon_pink")

# Cyan neon sign
c.rect(5, 45, 22, 3, "neon_cyan")
c.rect(6, 48, 20, 8, "neon_cyan", fill=False)

# Yellow neon (horizontal)
c.rect(10, 60, 15, 3, "neon_yellow")

# 4. Neon signs - right side
# Purple neon
c.rect(105, 25, 16, 4, "neon_purple")
c.rect(107, 29, 12, 10, "neon_purple", fill=False)

# Orange neon
c.rect(100, 50, 20, 3, "neon_orange")
c.rect(102, 53, 16, 6, "neon_orange", fill=False)

# Blue neon (small)
c.rect(110, 65, 12, 3, "neon_blue")

# 5. Windows with lights
# Left building windows
c.rect(12, 35, 8, 10, "window_dark")
c.rect(13, 36, 6, 8, "window_lit")
c.rect(12, 55, 8, 10, "window_dark")
c.rect(14, 56, 5, 8, "window_bright")

c.rect(25, 40, 7, 9, "window_dark")
c.rect(26, 41, 5, 7, "window_lit")

# Right building windows
c.rect(108, 38, 7, 9, "window_dark")
c.rect(109, 39, 5, 7, "window_bright")
c.rect(108, 58, 7, 9, "window_dark")
c.rect(109, 59, 5, 7, "window_lit")

# 6. Vending machine (left side, ground level)
c.rect(5, 65, 14, 20, "vending_body")
c.rect(6, 66, 12, 12, "vending_light")  # Glowing display
c.rect(7, 67, 10, 10, "night_sky")  # Inner
# Products in vending machine
c.set(8, 68, "neon_pink")
c.set(10, 68, "neon_cyan")
c.set(12, 68, "neon_yellow")
c.set(8, 72, "neon_orange")
c.set(10, 72, "neon_purple")
c.set(12, 72, "neon_blue")
# Vending machine glow on ground
c.rect(4, 85, 16, 3, "vending_light")

# 7. Puddles on ground with reflections
# Large puddle center-left
c.ellipse(35, 95, 20, 6, "puddle_dark", fill=True)
c.ellipse(35, 94, 18, 5, "puddle_mid", fill=True)
# Neon reflections in puddle
c.rect(28, 92, 4, 3, "neon_pink")
c.rect(35, 91, 3, 4, "neon_cyan")
c.rect(42, 93, 3, 2, "neon_yellow")

# Puddle center-right
c.ellipse(85, 100, 18, 5, "puddle_dark", fill=True)
c.ellipse(85, 99, 16, 4, "puddle_mid", fill=True)
c.rect(78, 97, 4, 3, "neon_purple")
c.rect(85, 96, 3, 4, "neon_orange")
c.rect(92, 98, 3, 2, "neon_blue")

# Small puddle near person
c.ellipse(60, 105, 12, 4, "puddle_dark", fill=True)
c.ellipse(60, 104, 10, 3, "puddle_mid", fill=True)

# 8. Power cables overhead
# Main cable line
c.line(0, 15, 127, 18, "cable")
# Drooping effect
for x in range(20, 110, 5):
    sag = abs(x - 64) // 10
    c.set(x, 16 + sag//2, "cable_highlight")

# Secondary cables
c.line(10, 12, 60, 25, "cable")
c.line(70, 22, 118, 14, "cable")

# Cable connection points
c.rect(2, 14, 4, 5, "brick_dark")
c.rect(122, 14, 4, 5, "brick_dark")

# 9. Person with umbrella (center, walking away)
# Person silhouette
c.rect(60, 60, 8, 25, "person_silhouette")  # Body
c.rect(58, 62, 12, 8, "person_silhouette")  # Shoulders/head area
c.rect(61, 60, 6, 5, "person_silhouette")   # Head

# Legs
c.rect(59, 85, 3, 12, "person_silhouette")  # Left leg
c.rect(66, 85, 3, 12, "person_silhouette")  # Right leg

# Umbrella (transparent - just outline and rim)
# Umbrella dome
c.ellipse(64, 52, 14, 8, "umbrella_edge", fill=False)
# Umbrella handle
c.line(64, 58, 64, 62, "umbrella_edge")
# Umbrella spokes (faint)
c.line(64, 52, 52, 56, "umbrella_edge")
c.line(64, 52, 76, 56, "umbrella_edge")
c.line(64, 52, 64, 44, "umbrella_edge")

# Umbrella transparency - can see neon through it
c.set(60, 50, "neon_pink")
c.set(64, 48, "neon_cyan")
c.set(68, 50, "neon_purple")

# Person's reflection in puddle below
c.rect(60, 108, 8, 10, "person_silhouette")
c.set(60, 108, "umbrella_edge")
c.set(67, 108, "umbrella_edge")

# 10. Rain streaks (subtle diagonal lines)
for i in range(0, 128, 8):
    c.line(i, 0, i+3, 15, "rain")
    c.line(i+4, 30, i+7, 45, "rain")
    c.line(i+2, 60, i+5, 75, "rain")
    c.line(i+6, 90, i+9, 105, "rain")

# 11. Additional atmosphere
# Steam/fog near ground (lighter pixels)
for x in range(10, 120, 12):
    c.set(x, 82, "highlight")
    c.set(x+2, 83, "highlight")
    c.set(x+4, 82, "highlight")

# Street light glow (top center, casting light down)
c.ellipse(64, 5, 8, 6, "neon_yellow", fill=True)
c.ellipse(64, 8, 12, 8, "neon_yellow")

# Light rays from street lamp
for i in range(-3, 4):
    c.line(64+i*2, 10, 64+i*4, 40, "neon_yellow")

# Ground highlights from street light
c.rect(55, 80, 18, 5, "highlight")

# 12. Final details
# Trash/debris on ground
c.set(20, 88, "brick_dark")
c.set(21, 89, "brick_dark")
c.set(95, 92, "brick_dark")
c.set(96, 91, "brick_dark")

# Doorway on left (dark entrance)
c.rect(15, 70, 10, 18, "shadow")
c.rect(16, 71, 8, 16, "night_sky")

# Doorway on right
c.rect(103, 72, 9, 16, "shadow")
c.rect(104, 73, 7, 14, "night_sky")

# Sign poles
c.rect(25, 30, 2, 35, "cable")
c.rect(100, 32, 2, 33, "cable")

# Additional neon text hints (abstract Japanese-style characters)
# Left sign - stylized characters
c.set(11, 21, "neon_pink")
c.set(13, 21, "neon_pink")
c.set(15, 21, "neon_pink")
c.set(17, 21, "neon_pink")
c.set(12, 23, "neon_pink")
c.set(16, 23, "neon_pink")
c.set(14, 25, "neon_pink")

# Right sign - more characters
c.set(107, 26, "neon_purple")
c.set(109, 26, "neon_purple")
c.set(111, 26, "neon_purple")
c.set(113, 26, "neon_purple")
c.set(115, 26, "neon_purple")
c.set(108, 28, "neon_purple")
c.set(112, 28, "neon_purple")
c.set(110, 30, "neon_purple")

# Wet ground sheen - more reflections
for y in range(82, 128, 3):
    for x in range(0, 128, 20):
        c.set(x + (y % 10), y, "reflection")

# More ground reflections from neon signs
c.rect(15, 90, 8, 2, "neon_pink")
c.rect(100, 95, 8, 2, "neon_purple")
c.rect(50, 100, 6, 2, "neon_cyan")

# Add fire escape / metal stairs on left building
for i in range(4):
    y_pos = 45 + i * 12
    c.rect(3, y_pos, 8, 2, "cable")  # Platform
    c.line(5, y_pos, 5, y_pos + 12, "cable")  # Ladder

# Fire escape on right
for i in range(3):
    y_pos = 50 + i * 12
    c.rect(117, y_pos, 8, 2, "cable")
    c.line(123, y_pos, 123, y_pos + 12, "cable")

# Air conditioning units on walls
c.rect(30, 50, 6, 5, "brick_dark")
c.rect(31, 51, 4, 3, "shadow")
c.rect(92, 55, 6, 5, "brick_dark")
c.rect(93, 56, 4, 3, "shadow")

# Pipes running down walls
c.line(35, 40, 35, 80, "cable")
c.line(90, 45, 90, 80, "cable")

# Add more rain for atmosphere
for i in range(5, 128, 6):
    c.line(i, 5, i+2, 20, "rain")
    c.line(i+3, 35, i+5, 50, "rain")
    c.line(i+1, 65, i+3, 80, "rain")
    c.line(i+4, 95, i+6, 110, "rain")

# Distant lights at end of alley (vanishing point)
c.set(62, 45, "neon_yellow")
c.set(64, 45, "neon_orange")
c.set(66, 45, "neon_yellow")
c.set(63, 47, "neon_orange")
c.set(65, 47, "neon_yellow")

# Graffiti on walls (abstract shapes)
c.set(32, 60, "neon_cyan")
c.set(33, 61, "neon_cyan")
c.set(34, 60, "neon_cyan")
c.set(33, 62, "neon_cyan")
c.set(95, 65, "neon_pink")
c.set(96, 66, "neon_pink")
c.set(97, 65, "neon_pink")

# Pigeon/bird silhouette flying
c.set(45, 12, "person_silhouette")
c.set(46, 11, "person_silhouette")
c.set(47, 12, "person_silhouette")

# Second person in distance (smaller silhouette)
c.rect(70, 68, 4, 12, "person_silhouette")
c.set(71, 66, "umbrella_edge")
c.set(72, 66, "umbrella_edge")

# Shop entrance glow (left)
c.rect(14, 88, 12, 2, "neon_yellow")

# Shop entrance glow (right)
c.rect(102, 88, 10, 2, "neon_orange")

print(c.stats_text())
print(c.matrix_text(region=(50, 40, 78, 110)))

finish(c)
