from pixelbench_api import new_canvas, finish

# Create 64x64 canvas
c = new_canvas(64, 64, name="subway_platform")

# Color palette - keeping under 86 colors
# Background/tunnel
bg_dark = c.color("#1a1a2e", "bg_dark")
bg_medium = c.color("#2d2d44", "bg_medium")
bg_light = c.color("#3d3d5c", "bg_light")

# Platform
plat_dark = c.color("#4a4a4a", "plat_dark")
plat_medium = c.color("#6b6b6b", "plat_medium")
plat_light = c.color("#8a8a8a", "plat_light")
plat_edge = c.color("#ffff00", "plat_edge")  # Yellow safety line

# Screen doors - glass and frame
door_frame = c.color("#5a5a6e", "door_frame")
door_glass = c.color("#6b7a8f", "door_glass")
door_glass_light = c.color("#8a9fb5", "door_glass_light")
door_handle = c.color("#c0c0c0", "door_handle")

# Train
train_body = c.color("#e63946", "train_body")
train_stripe = c.color("#ffffff", "train_stripe")
train_window = c.color("#1a1a2e", "train_window")
train_window_light = c.color("#4a5a7a", "train_window_light")
train_light = c.color("#ffdd00", "train_light")

# Bench
bench_leg = c.color("#3a3a3a", "bench_leg")
bench_seat = c.color("#8b4513", "bench_seat")
bench_back = c.color("#a0522d", "bench_back")

# Passengers - varied colors
# Passenger 1 (standing, looking at phone)
p1_skin = c.color("#d4a574", "p1_skin")
p1_shirt = c.color("#4a90d9", "p1_shirt")
p1_pants = c.color("#2d2d2d", "p1_pants")
p1_hair = c.color("#1a1a1a", "p1_hair")

# Passenger 2 (sitting on bench)
p2_skin = c.color("#f5d0a9", "p2_skin")
p2_shirt = c.color("#6b8e23", "p2_shirt")
p2_pants = c.color("#4a4a6a", "p2_pants")
p2_hair = c.color("#8b4513", "p2_hair")

# Passenger 3 (walking with bag)
p3_skin = c.color("#c68642", "p3_skin")
p3_shirt = c.color("#e85d75", "p3_shirt")
p3_pants = c.color("#3d3d5c", "p3_pants")
p3_hair = c.color("#0a0a0a", "p3_hair")
p3_bag = c.color("#654321", "p3_bag")

# Station sign
sign_bg = c.color("#2d4a6e", "sign_bg")
sign_text = c.color("#ffffff", "sign_text")
sign_pole = c.color("#4a4a4a", "sign_pole")

# Speed lines for motion effect
speed_line = c.color("#ffffff40", "speed_line")

# === DRAWING ===

# Background - tunnel ceiling and walls (top portion)
c.rect(0, 0, 64, 20, bg_dark, fill=True)
c.rect(0, 20, 64, 8, bg_medium, fill=True)

# Tunnel back wall with perspective lines
for y in range(28, 40):
    shade = int(28 + (y - 28) * 3)
    c.rect(0, y, 64, 1, f"#{shade:02x}{shade:02x}{shade+20:02x}", fill=True)

# Platform floor (bottom portion) - perspective gradient
for y in range(40, 64):
    shade = 70 + (y - 40) * 2
    c.rect(0, y, 64, 1, f"#{shade:02x}{shade:02x}{shade:02x}", fill=True)

# Platform edge line (yellow safety strip)
c.rect(0, 39, 64, 2, plat_edge, fill=True)

# === Platform Screen Doors (middle ground) ===
# Door frames - vertical pillars
for x in [8, 20, 32, 44, 56]:
    c.rect(x, 18, 4, 22, door_frame, fill=True)

# Glass panels between frames
for x in [12, 24, 36, 48]:
    c.rect(x, 18, 8, 22, door_glass, fill=True)
    # Glass reflection highlights
    c.rect(x+1, 19, 2, 8, door_glass_light, fill=True)
    c.rect(x+5, 25, 2, 6, door_glass_light, fill=True)

# Door handles
for x in [10, 22, 34, 46, 58]:
    c.set(x+2, 30, door_handle)
    c.set(x+2, 31, door_handle)

# === Train (background, partially visible through doors) ===
# Train body - receding into distance on the right
c.rect(0, 22, 55, 14, train_body, fill=True)

# White stripe along train
c.rect(0, 26, 55, 3, train_stripe, fill=True)

# Train windows (showing through screen doors)
for i, x in enumerate([2, 14, 26, 38, 50]):
    if x < 52:
        c.rect(x, 23, 8, 6, train_window, fill=True)
        # Window interior light
        c.rect(x+1, 24, 6, 4, train_window_light, fill=True)

# Train headlight (bright, on the left - train arriving from left)
c.rect(1, 30, 4, 4, train_light, fill=True)
c.set(2, 31, "#ffffff")

# === Speed lines (conveying motion) ===
for i in range(5):
    y = 25 + i * 3
    length = 15 - i * 2
    c.rect(5, y, length, 1, speed_line, fill=True)

# === Station Sign (hanging from ceiling) ===
# Sign pole
c.rect(10, 8, 2, 10, sign_pole, fill=True)

# Sign background
c.rect(6, 4, 20, 8, sign_bg, fill=True)

# Station name text (generic - no brand)
# "STATION" in simple block letters
c.text(8, 6, "STATION", sign_text, font="5x7")

# === Bench (on platform) ===
# Bench legs
c.rect(46, 35, 2, 8, bench_leg, fill=True)
c.rect(56, 35, 2, 8, bench_leg, fill=True)

# Bench seat
c.rect(44, 34, 16, 3, bench_seat, fill=True)

# Bench back
c.rect(44, 30, 16, 4, bench_back, fill=True)

# === Passenger 1: Standing, looking at phone (left side) ===
# Position: x=15-20, y=32-40
# Legs
c.rect(16, 36, 2, 6, p1_pants, fill=True)
c.rect(19, 36, 2, 6, p1_pants, fill=True)
# Body/shirt
c.rect(15, 28, 7, 9, p1_shirt, fill=True)
# Head
c.rect(16, 24, 5, 5, p1_skin, fill=True)
c.rect(16, 23, 5, 2, p1_hair, fill=True)
# Arms (one holding phone)
c.rect(14, 29, 2, 5, p1_shirt, fill=True)
c.rect(20, 30, 3, 2, p1_skin, fill=True)  # hand
c.set(21, 30, "#333333")  # phone

# === Passenger 2: Sitting on bench (right side) ===
# Position: x=48-54, y=28-36
# Legs (sitting)
c.rect(48, 34, 2, 5, p2_pants, fill=True)
c.rect(51, 34, 2, 5, p2_pants, fill=True)
# Body
c.rect(47, 28, 7, 7, p2_shirt, fill=True)
# Head
c.rect(48, 24, 5, 5, p2_skin, fill=True)
c.rect(48, 23, 5, 2, p2_hair, fill=True)
# Arms
c.rect(46, 29, 2, 4, p2_shirt, fill=True)
c.rect(53, 29, 2, 4, p2_shirt, fill=True)

# === Passenger 3: Walking with bag (center-left) ===
# Position: x=28-34, y=32-42, mid-stride
# Legs (walking pose - one forward)
c.rect(29, 37, 2, 5, p3_pants, fill=True)
c.rect(32, 36, 2, 6, p3_pants, fill=True)
# Body
c.rect(28, 29, 7, 9, p3_shirt, fill=True)
# Head
c.rect(29, 25, 5, 5, p3_skin, fill=True)
c.rect(29, 24, 5, 2, p3_hair, fill=True)
# Arms
c.rect(27, 30, 2, 5, p3_shirt, fill=True)
c.rect(34, 30, 2, 5, p3_shirt, fill=True)
# Bag
c.rect(35, 33, 3, 5, p3_bag, fill=True)
c.rect(35, 31, 2, 3, p3_bag, fill=True)  # strap

# Add subtle floor shadows under passengers
c.rect(15, 41, 7, 1, "#00000040", fill=True)
c.rect(46, 41, 8, 1, "#00000040", fill=True)
c.rect(27, 42, 10, 1, "#00000040", fill=True)

# Check color count and stats
print(c.stats_text())

# Submit the canvas
finish(c)
