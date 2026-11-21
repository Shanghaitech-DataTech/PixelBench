from pixelbench_api import *

# Create 128x128 canvas with transparent background
c = new_canvas(128, 128, background=None, name="motorcycle")

# Define colors
black = c.color("#1a1a1a", "black")           # Main body, tires
dark_gray = c.color("#3a3a3a", "dark_gray")   # Fairing, body panels
medium_gray = c.color("#5a5a5a", "medium_gray")  # Shading
silver = c.color("#c0c0c0", "silver")         # Metal parts, frame, fork
light_silver = c.color("#d8d8d8", "light_silver")  # Highlights
red = c.color("#cc0000", "red")               # Accents, tail light
bright_red = c.color("#ff3333", "bright_red") # Tail light highlight
white = c.color("#ffffff", "white")           # Spokes
dark_red = c.color("#880000", "dark_red")     # Shadow on red parts
charcoal = c.color("#2a2a2a", "charcoal")     # Tire detail
gray_hub = c.color("#808080", "gray_hub")     # Wheel hub

# Position constants
wheel_y = 88
wheel_radius = 18
front_wheel_x = 32
rear_wheel_x = 96

# ============ REAR WHEEL (left side of image) ============
# Tire - thick black circle
c.circle(rear_wheel_x, wheel_y, wheel_radius, black, fill=True)
# Inner tire detail
c.circle(rear_wheel_x, wheel_y, wheel_radius - 3, charcoal, fill=True)
# Hub - gray center
c.circle(rear_wheel_x, wheel_y, 6, gray_hub, fill=True)
c.circle(rear_wheel_x, wheel_y, 3, silver, fill=True)
# White spokes - 8 spokes
for angle in range(0, 360, 45):
    import math
    rad = math.radians(angle)
    x1 = int(rear_wheel_x + 8 * math.cos(rad))
    y1 = int(wheel_y + 8 * math.sin(rad))
    x2 = int(rear_wheel_x + (wheel_radius - 4) * math.cos(rad))
    y2 = int(wheel_y + (wheel_radius - 4) * math.sin(rad))
    c.line(x1, y1, x2, y2, white)

# ============ FRONT WHEEL (right side of image) ============
c.circle(front_wheel_x, wheel_y, wheel_radius, black, fill=True)
c.circle(front_wheel_x, wheel_y, wheel_radius - 3, charcoal, fill=True)
c.circle(front_wheel_x, wheel_y, 6, gray_hub, fill=True)
c.circle(front_wheel_x, wheel_y, 3, silver, fill=True)
# White spokes
for angle in range(0, 360, 45):
    import math
    rad = math.radians(angle)
    x1 = int(front_wheel_x + 8 * math.cos(rad))
    y1 = int(wheel_y + 8 * math.sin(rad))
    x2 = int(front_wheel_x + (wheel_radius - 4) * math.cos(rad))
    y2 = int(wheel_y + (wheel_radius - 4) * math.sin(rad))
    c.line(x1, y1, x2, y2, white)

# ============ FRONT FORK (silver) ============
# Fork tubes going down to front wheel
c.line(front_wheel_x - 3, wheel_y - wheel_radius + 2, front_wheel_x - 3, wheel_y - 45, silver)
c.line(front_wheel_x + 3, wheel_y - wheel_radius + 2, front_wheel_x + 3, wheel_y - 45, silver)
# Fork crown
c.rect(front_wheel_x - 5, wheel_y - 48, 10, 6, silver, fill=True)

# ============ MAIN FRAME (silver tubular) ============
# Frame backbone from steering head to tail
c.line(front_wheel_x, wheel_y - 48, 65, wheel_y - 38, silver)  # Top tube
c.line(65, wheel_y - 38, 85, wheel_y - 35, silver)  # Seat area support
c.line(85, wheel_y - 35, 100, wheel_y - 28, silver)  # Tail rise

# Down tube
c.line(front_wheel_x + 2, wheel_y - 45, 55, wheel_y - 15, silver)
# Bottom frame rail
c.line(55, wheel_y - 15, 88, wheel_y - 18, silver)

# ============ ENGINE (round silver cover) ============
# Main engine body
c.circle(60, wheel_y - 5, 14, silver, fill=True)
c.circle(60, wheel_y - 5, 10, light_silver, fill=True)
# Engine detail
c.circle(60, wheel_y - 5, 5, medium_gray, fill=True)

# ============ FAIRING (wide dark gray) ============
# Front fairing covering engine area
c.poly([
    (front_wheel_x + 8, wheel_y - 40),
    (front_wheel_x + 20, wheel_y - 35),
    (50, wheel_y - 30),
    (55, wheel_y - 15),
    (55, wheel_y + 5),
    (45, wheel_y + 5),
    (40, wheel_y - 10),
    (30, wheel_y - 25),
    (front_wheel_x + 5, wheel_y - 35),
], dark_gray, fill=True)

# Fairing highlight
c.poly([
    (front_wheel_x + 12, wheel_y - 38),
    (front_wheel_x + 18, wheel_y - 34),
    (45, wheel_y - 28),
    (48, wheel_y - 20),
    (42, wheel_y - 20),
    (35, wheel_y - 30),
], medium_gray, fill=True)

# ============ BODY / TANK (black and dark gray) ============
# Fuel tank area
c.poly([
    (55, wheel_y - 38),
    (70, wheel_y - 42),
    (80, wheel_y - 40),
    (82, wheel_y - 35),
    (75, wheel_y - 32),
    (60, wheel_y - 35),
], black, fill=True)

# Tank highlight
c.poly([
    (60, wheel_y - 40),
    (72, wheel_y - 41),
    (78, wheel_y - 39),
    (75, wheel_y - 36),
    (65, wheel_y - 37),
], dark_gray, fill=True)

# Side panel under tank
c.poly([
    (55, wheel_y - 35),
    (75, wheel_y - 32),
    (78, wheel_y - 25),
    (75, wheel_y - 20),
    (58, wheel_y - 22),
    (55, wheel_y - 28),
], dark_gray, fill=True)

# ============ WINDSCREEN (tilted small black) ============
c.poly([
    (front_wheel_x + 5, wheel_y - 45),
    (front_wheel_x + 12, wheel_y - 52),
    (front_wheel_x + 18, wheel_y - 52),
    (front_wheel_x + 15, wheel_y - 42),
    (front_wheel_x + 8, wheel_y - 40),
], black, fill=True)
# Windscreen highlight
c.line(front_wheel_x + 10, wheel_y - 50, front_wheel_x + 14, wheel_y - 50, medium_gray)

# ============ SEAT (black) ============
c.poly([
    (75, wheel_y - 35),
    (90, wheel_y - 35),
    (95, wheel_y - 32),
    (98, wheel_y - 28),
    (95, wheel_y - 28),
    (80, wheel_y - 30),
    (75, wheel_y - 32),
], black, fill=True)

# ============ UPSWEPT TAIL ============
c.poly([
    (90, wheel_y - 32),
    (100, wheel_y - 30),
    (108, wheel_y - 25),
    (112, wheel_y - 22),
    (110, wheel_y - 18),
    (102, wheel_y - 22),
    (95, wheel_y - 26),
], dark_gray, fill=True)

# Tail accent
c.poly([
    (105, wheel_y - 24),
    (110, wheel_y - 22),
    (110, wheel_y - 20),
    (105, wheel_y - 22),
], black, fill=True)

# ============ RED TAIL LIGHT ============
c.circle(112, wheel_y - 20, 4, red, fill=True)
c.circle(112, wheel_y - 21, 2, bright_red, fill=True)

# ============ RED ACCENTS ============
# Accent stripe on fairing
c.line(front_wheel_x + 15, wheel_y - 30, 45, wheel_y - 25, red)
c.line(front_wheel_x + 15, wheel_y - 28, 45, wheel_y - 23, dark_red)

# Accent on tank
c.poly([
    (62, wheel_y - 39),
    (75, wheel_y - 40),
    (75, wheel_y - 38),
    (62, wheel_y - 37),
], red, fill=True)

# ============ EXHAUST (silver) ============
c.line(65, wheel_y - 8, 85, wheel_y - 5, silver)
c.line(85, wheel_y - 5, 92, wheel_y - 8, silver)
c.circle(93, wheel_y - 8, 4, dark_gray, fill=True)
c.circle(93, wheel_y - 8, 2, black, fill=True)

# ============ BRAKE DISC (front) ============
c.circle(front_wheel_x, wheel_y, 10, silver, fill=False)
c.circle(front_wheel_x, wheel_y, 8, light_silver, fill=False)

# ============ BRAKE DISC (rear) ============
c.circle(rear_wheel_x, wheel_y, 10, silver, fill=False)
c.circle(rear_wheel_x, wheel_y, 8, light_silver, fill=False)

# ============ HANDLEBARS ============
c.line(front_wheel_x - 2, wheel_y - 50, front_wheel_x + 8, wheel_y - 48, silver)
c.circle(front_wheel_x + 8, wheel_y - 48, 3, black, fill=True)

# ============ FOOT PEG ============
c.rect(70, wheel_y - 10, 6, 4, silver, fill=True)
c.rect(70, wheel_y - 10, 6, 2, black, fill=True)

# ============ ADDITIONAL DETAILS ============
# Air intake on fairing
c.ellipse(35, wheel_y - 20, 4, 3, charcoal, fill=True)

# Frame detail near engine
c.line(58, wheel_y - 18, 62, wheel_y - 12, silver)

print(c.stats_text())

# Submit the result
finish(c)
