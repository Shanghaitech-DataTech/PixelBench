from pixelbench_api import new_canvas, finish

# Create 64x64 canvas for convenience store on rainy night
c = new_canvas(64, 64, background=None)

# Define color palette
# Night sky colors
sky_dark = c.color("#0a0f1f", "sky_dark")
sky_mid = c.color("#1a2540", "sky_mid")
sky_light = c.color("#2a3550", "sky_light")

# Store building colors
store_wall = c.color("#3d4a5c", "store_wall")
store_dark = c.color("#2a3545", "store_dark")
store_trim = c.color("#5a6a7a", "store_trim")

# Interior light (bright warm)
interior_bright = c.color("#fff5d0", "interior_bright")
interior_warm = c.color("#ffd9a0", "interior_warm")
interior_mid = c.color("#ffcc80", "interior_mid")

# Window glass
window_glass = c.color("#8ab4d8", "window_glass")
window_reflect = c.color("#a8c8e8", "window_reflect")

# Ground and puddles
ground_dark = c.color("#1a1a25", "ground_dark")
ground_mid = c.color("#252535", "ground_mid")
puddle_dark = c.color("#2a3040", "puddle_dark")
puddle_reflect = c.color("#5a7090", "puddle_reflect")
puddle_bright = c.color("#8ab0d0", "puddle_bright")

# Rain
rain_light = c.color("#aaccff", "rain_light")
rain_mid = c.color("#7799cc", "rain_mid")

# Umbrella rack
rack_metal = c.color("#6a7a8a", "rack_metal")
rack_dark = c.color("#4a5a6a", "rack_dark")

# Umbrellas
umbrella_red = c.color("#cc3344", "umbrella_red")
umbrella_blue = c.color("#4466aa", "umbrella_blue")
umbrella_yellow = c.color("#ddaa33", "umbrella_yellow")

# Bicycle
bike_frame = c.color("#cc4455", "bike_frame")
bike_dark = c.color("#883344", "bike_dark")
bike_wheel = c.color("#3a3a4a", "bike_wheel")
bike_seat = c.color("#2a2a3a", "bike_seat")

# Person in raincoat
raincoat = c.color("#ffdd44", "raincoat")
raincoat_dark = c.color("#ccaa33", "raincoat_dark")
person_pants = c.color("#3a4a5a", "person_pants")
person_skin = c.color("#d4a88a", "person_skin")
person_hair = c.color("#2a2a3a", "person_hair")

# Store sign
sign_bg = c.color("#ff6644", "sign_bg")
sign_text = c.color("#ffffff", "sign_text")
sign_glow = c.color("#ffaa88", "sign_glow")

# Door
door_frame = c.color("#4a5a6a", "door_frame")
door_glass = c.color("#6a8ab0", "door_glass")

# Draw sky (top portion)
c.rect(0, 0, 64, 28, sky_dark, fill=True)

# Add some sky variation
for y in range(0, 28, 4):
    c.rect(0, y, 64, 2, sky_mid, fill=True)
for y in range(2, 28, 6):
    c.rect(10, y, 20, 1, sky_light, fill=True)
    c.rect(40, y, 15, 1, sky_light, fill=True)

# Draw store building (main structure)
c.rect(8, 18, 48, 30, store_wall, fill=True)
c.rect(6, 18, 2, 30, store_dark, fill=True)  # Left edge shadow
c.rect(56, 18, 2, 30, store_dark, fill=True)  # Right edge shadow

# Store roof/awning
c.rect(4, 16, 56, 4, store_dark, fill=True)
c.rect(2, 14, 60, 2, store_wall, fill=True)

# Store sign above entrance
c.rect(24, 10, 16, 4, sign_bg, fill=True)
c.rect(24, 10, 16, 1, sign_glow, fill=True)  # Top glow
# Simple text representation (no brand names)
c.set(26, 11, sign_text)
c.set(27, 11, sign_text)
c.set(29, 11, sign_text)
c.set(30, 11, sign_text)
c.set(32, 11, sign_text)
c.set(33, 11, sign_text)
c.set(26, 12, sign_text)
c.set(33, 12, sign_text)

# Windows with interior light
# Left window
c.rect(10, 22, 14, 12, interior_bright, fill=True)
c.rect(10, 22, 14, 1, interior_warm, fill=True)  # Top highlight
# Window frame
c.rect(9, 21, 1, 14, store_trim, fill=True)
c.rect(24, 21, 1, 14, store_trim, fill=True)
c.rect(9, 21, 16, 1, store_trim, fill=True)
c.rect(9, 35, 16, 1, store_trim, fill=True)
# Window crossbar
c.rect(9, 28, 16, 1, store_trim, fill=True)
c.rect(16, 21, 1, 14, store_trim, fill=True)
# Glass reflection
c.set(11, 23, window_reflect)
c.set(12, 23, window_reflect)
c.set(11, 24, window_glass)
c.set(12, 24, window_glass)

# Right window
c.rect(40, 22, 14, 12, interior_bright, fill=True)
c.rect(40, 22, 14, 1, interior_warm, fill=True)
# Window frame
c.rect(39, 21, 1, 14, store_trim, fill=True)
c.rect(54, 21, 1, 14, store_trim, fill=True)
c.rect(39, 21, 16, 1, store_trim, fill=True)
c.rect(39, 35, 16, 1, store_trim, fill=True)
# Window crossbar
c.rect(39, 28, 16, 1, store_trim, fill=True)
c.rect(46, 21, 1, 14, store_trim, fill=True)
# Glass reflection
c.set(41, 23, window_reflect)
c.set(42, 23, window_reflect)
c.set(41, 24, window_glass)
c.set(42, 24, window_glass)

# Interior details (shelves visible through windows)
# Left window shelves
c.set(13, 26, store_dark)
c.set(14, 26, store_dark)
c.set(13, 29, store_dark)
c.set(14, 29, store_dark)
c.set(13, 32, store_dark)
c.set(14, 32, store_dark)
# Right window shelves
c.set(43, 26, store_dark)
c.set(44, 26, store_dark)
c.set(43, 29, store_dark)
c.set(44, 29, store_dark)
c.set(43, 32, store_dark)
c.set(44, 32, store_dark)

# Door in center
c.rect(28, 28, 8, 20, door_glass, fill=True)
c.rect(27, 27, 1, 22, door_frame, fill=True)  # Left frame
c.rect(36, 27, 1, 22, door_frame, fill=True)  # Right frame
c.rect(27, 27, 10, 1, door_frame, fill=True)  # Top frame
# Door handle
c.set(34, 35, rack_metal)
c.set(34, 36, rack_metal)

# Ground
c.rect(0, 48, 64, 16, ground_dark, fill=True)

# Wet ground texture
for x in range(0, 63, 3):
    c.set(x, 49, ground_mid)
    if x+1 < 64:
        c.set(x+1, 51, ground_mid)
for x in range(2, 62, 4):
    c.set(x, 53, ground_mid)
    if x+2 < 64:
        c.set(x+2, 55, ground_mid)

# Puddles with reflections
# Large puddle left
c.rect(5, 52, 18, 6, puddle_dark, fill=True)
c.rect(6, 53, 16, 4, puddle_reflect, fill=True)
# Interior light reflection in puddle
c.set(8, 54, interior_warm)
c.set(9, 54, interior_warm)
c.set(10, 54, interior_mid)
c.set(8, 55, interior_warm)
c.set(9, 55, interior_warm)
# Sky reflection
c.set(12, 53, sky_light)
c.set(13, 53, sky_light)

# Large puddle right
c.rect(42, 54, 16, 5, puddle_dark, fill=True)
c.rect(43, 55, 14, 3, puddle_reflect, fill=True)
# Sign reflection
c.set(45, 56, sign_bg)
c.set(46, 56, sign_bg)
c.set(47, 56, sign_glow)

# Small puddle center
c.rect(26, 56, 10, 4, puddle_dark, fill=True)
c.rect(27, 57, 8, 2, puddle_bright, fill=True)
# Person reflection hint
c.set(29, 57, raincoat)
c.set(30, 57, raincoat)

# Umbrella rack (left side near door)
c.rect(20, 40, 6, 2, rack_dark, fill=True)  # Base
c.set(21, 38, rack_metal)
c.set(22, 38, rack_metal)
c.set(23, 38, rack_metal)
c.set(24, 38, rack_metal)
c.set(21, 36, rack_metal)
c.set(22, 36, rack_metal)
c.set(23, 36, rack_metal)
c.set(24, 36, rack_metal)
# Umbrellas in rack
c.set(21, 35, umbrella_red)
c.set(22, 35, umbrella_blue)
c.set(23, 35, umbrella_yellow)
c.set(21, 34, umbrella_red)
c.set(22, 34, umbrella_blue)
c.set(23, 34, umbrella_yellow)

# Bicycle (right side)
# Wheels
c.circle(52, 46, 4, bike_wheel, fill=False)
c.circle(52, 46, 1, rack_metal, fill=True)  # Hub
c.circle(58, 46, 4, bike_wheel, fill=False)
c.circle(58, 46, 1, rack_metal, fill=True)  # Hub
# Frame
c.line(52, 46, 55, 42, bike_frame)
c.line(55, 42, 58, 46, bike_frame)
c.line(55, 42, 55, 38, bike_frame)
c.line(55, 38, 53, 36, bike_frame)
# Seat
c.rect(53, 35, 4, 2, bike_seat, fill=True)
# Handlebars
c.set(55, 36, rack_metal)
c.set(55, 35, rack_dark)

# Person in raincoat entering (center, near door)
# Body
c.rect(30, 36, 4, 8, raincoat, fill=True)
c.set(30, 36, raincoat_dark)  # Shadow side
c.set(30, 37, raincoat_dark)
c.set(30, 38, raincoat_dark)
# Hood/head
c.rect(30, 33, 4, 4, raincoat, fill=True)
c.set(31, 33, raincoat_dark)
c.set(32, 33, raincoat_dark)
# Legs
c.set(31, 44, person_pants)
c.set(32, 44, person_pants)
c.set(31, 45, person_pants)
c.set(32, 45, person_pants)
c.set(31, 46, person_pants)
c.set(32, 46, person_pants)
# Feet
c.set(31, 47, store_dark)
c.set(32, 47, store_dark)
# Arm reaching for door
c.set(33, 38, raincoat)
c.set(34, 38, raincoat)
c.set(35, 38, person_skin)  # Hand

# Rain streaks (diagonal lines)
for i in range(30):
    x = 2 + (i * 7) % 60
    y = (i * 5) % 48
    if 0 <= x < 64 and 0 <= y < 64:
        c.set(x, y, rain_light)
    if 0 <= x-1 < 64 and 0 <= y+1 < 64:
        c.set(x-1, y+1, rain_mid)
    if 0 <= x-2 < 64 and 0 <= y+2 < 64:
        c.set(x-2, y+2, rain_mid)

# More rain in foreground
for i in range(20):
    x = 2 + (i * 11) % 60
    y = 10 + (i * 8) % 40
    if 0 <= x < 64 and 0 <= y < 64:
        c.set(x, y, rain_light)
    if 0 <= x-1 < 64 and 0 <= y+1 < 64:
        c.set(x-1, y+1, rain_light)

# Add some rain near person
for i in range(10):
    x = 25 + (i * 3) % 15
    y = 20 + i * 4
    if 0 <= x < 64 and 0 <= y < 48:
        c.set(x, y, rain_light)
    if 0 <= x-1 < 64 and 0 <= y+1 < 48:
        c.set(x-1, y+1, rain_mid)

# Light glow around windows (exterior)
for y in range(21, 36):
    c.set(8, y, sign_glow)
    c.set(25, y, sign_glow)
    c.set(38, y, sign_glow)
    c.set(55, y, sign_glow)

# Ground wetness highlights near building
for x in range(8, 55):
    if x % 4 == 0:
        c.set(x, 48, ground_mid)
        c.set(x+1, 48, sign_glow)

# Check stats
print(c.stats_text())

# Submit the canvas
finish(c)
