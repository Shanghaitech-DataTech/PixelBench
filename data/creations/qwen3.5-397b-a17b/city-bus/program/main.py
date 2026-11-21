from pixelbench_api import new_canvas, finish

# Create a 64x32 canvas with transparent background
c = new_canvas(64, 32, background=None, name="city_bus")

# Define color palette - keeping under 86 colors
body_main = c.color("#4A8BC7", "body_main")        # Modern blue body
body_dark = c.color("#2E5A7A", "body_dark")        # Darker blue for details
body_light = c.color("#6BA3D7", "body_light")      # Lighter blue for highlights
window_tint = c.color("#1A3A52", "window_tint")    # Dark tinted windows
window_frame = c.color("#2E5A7A", "window_frame")  # Window frames
wheel_tire = c.color("#1a1a1a", "wheel_tire")      # Black tires
wheel_rim = c.color("#999999", "wheel_rim")        # Silver rims
headlight = c.color("#FFFFAA", "headlight")        # Yellow headlights
door_frame = c.color("#1a1a1a", "door_frame")      # Door outlines
route_bg = c.color("#000000", "route_bg")          # Route display background
route_text = c.color("#00FF66", "route_text")      # LED green text
undercarriage = c.color("#222222", "undercarriage") # Dark undercarriage
bumper = c.color("#1a1a1a", "bumper")              # Black bumpers
mirror = c.color("#2E5A7A", "mirror")              # Side mirror
taillight = c.color("#FF4444", "taillight")        # Red taillights
glass_reflect = c.color("#5A9FC7", "glass_reflect") # Window reflection highlight

# Bus body - main shape (side view, streamlined modern design)
# Main body: from x=4 to x=60, y=8 to y=24 (16px tall body)
c.rect(4, 8, 56, 16, body_main, fill=True)

# Rounded front (left side)
c.set(3, 10, body_main)
c.set(3, 11, body_main)
c.set(3, 12, body_main)
c.set(3, 13, body_main)
c.set(3, 14, body_main)
c.set(3, 15, body_main)
c.set(3, 16, body_main)
c.set(3, 17, body_main)
c.set(2, 12, body_main)
c.set(2, 13, body_main)
c.set(2, 14, body_main)
c.set(2, 15, body_main)
c.set(2, 16, body_main)

# Rounded rear (right side)
c.set(60, 10, body_main)
c.set(60, 11, body_main)
c.set(60, 12, body_main)
c.set(60, 13, body_main)
c.set(60, 14, body_main)
c.set(60, 15, body_main)
c.set(60, 16, body_main)
c.set(60, 17, body_main)
c.set(61, 12, body_main)
c.set(61, 13, body_main)
c.set(61, 14, body_main)
c.set(61, 15, body_main)
c.set(61, 16, body_main)

# Roof highlight line
c.line(5, 8, 59, 8, body_light)

# Bottom trim line
c.line(5, 23, 59, 23, body_dark)

# Windows - row of 8 passenger windows
# Starting after front door area
window_y = 10
window_h = 6
window_positions = [10, 17, 24, 31, 38, 45, 52, 56]

for wx in window_positions:
    # Window tinted glass
    c.rect(wx, window_y, 5, window_h, window_tint, fill=True)
    # Small reflection highlight on each window
    c.set(wx+1, window_y+1, glass_reflect)

# Front door (near front, x=14-19)
door1_x = 14
door1_w = 5
door1_y = 9
door1_h = 14
c.rect(door1_x, door1_y, door1_w, door1_h, body_dark, fill=True)
# Door windows (2 small panes)
c.rect(door1_x+1, door1_y+2, 3, 4, window_tint, fill=True)
c.rect(door1_x+1, door1_y+8, 3, 4, window_tint, fill=True)

# Rear door (near back, x=40-45)
door2_x = 40
door2_w = 5
door2_y = 9
door2_h = 14
c.rect(door2_x, door2_y, door2_w, door2_h, body_dark, fill=True)
# Door windows
c.rect(door2_x+1, door2_y+2, 3, 4, window_tint, fill=True)
c.rect(door2_x+1, door2_y+8, 3, 4, window_tint, fill=True)

# Wheels - two wheels
# Front wheel
wheel1_x = 16
wheel1_y = 24
wheel_r = 4
c.circle(wheel1_x, wheel1_y, wheel_r, wheel_tire, fill=True)
c.circle(wheel1_x, wheel1_y, wheel_r-1, wheel_rim, fill=True)
c.circle(wheel1_x, wheel1_y, wheel_r-2, wheel_tire, fill=True)

# Rear wheel
wheel2_x = 48
wheel2_y = 24
wheel_r = 4
c.circle(wheel2_x, wheel2_y, wheel_r, wheel_tire, fill=True)
c.circle(wheel2_x, wheel2_y, wheel_r-1, wheel_rim, fill=True)
c.circle(wheel2_x, wheel2_y, wheel_r-2, wheel_tire, fill=True)

# Headlights - front of bus
c.set(2, 19, headlight)
c.set(3, 19, headlight)
c.set(2, 20, headlight)
c.set(3, 20, headlight)

# Front bumper
c.rect(2, 21, 3, 2, bumper, fill=True)

# Rear taillights
c.set(61, 19, taillight)
c.set(61, 20, taillight)
c.set(62, 19, taillight)
c.set(62, 20, taillight)

# Electronic route display - at top front area
route_x = 6
route_y = 5
route_w = 12
route_h = 3
c.rect(route_x, route_y, route_w, route_h, route_bg, fill=True)
# Route number "42" in LED pixel style
# "4" pattern (3 wide x 3 tall area starting at route_x+1)
c.set(route_x+1, route_y+0, route_text)
c.set(route_x+3, route_y+0, route_text)
c.set(route_x+1, route_y+1, route_text)
c.set(route_x+2, route_y+1, route_text)
c.set(route_x+3, route_y+1, route_text)
c.set(route_x+3, route_y+2, route_text)
# "2" pattern (3 wide x 3 tall area starting at route_x+5)
c.set(route_x+5, route_y+0, route_text)
c.set(route_x+6, route_y+0, route_text)
c.set(route_x+7, route_y+0, route_text)
c.set(route_x+7, route_y+1, route_text)
c.set(route_x+5, route_y+1, route_text)
c.set(route_x+6, route_y+1, route_text)
c.set(route_x+5, route_y+2, route_text)
c.set(route_x+6, route_y+2, route_text)
c.set(route_x+7, route_y+2, route_text)

# Side mirror
c.rect(4, 8, 2, 3, mirror, fill=True)

# Undercarriage detail panels
c.rect(10, 24, 8, 2, undercarriage, fill=True)
c.rect(42, 24, 10, 2, undercarriage, fill=True)

# Body panel seam lines
c.line(20, 8, 20, 23, body_dark)
c.line(35, 8, 35, 23, body_dark)

# Wheel arches (darker curve above wheels)
# Front wheel arch
c.set(14, 23, body_dark)
c.set(15, 23, body_dark)
c.set(16, 23, body_dark)
c.set(17, 23, body_dark)
c.set(18, 23, body_dark)
# Rear wheel arch
c.set(46, 23, body_dark)
c.set(47, 23, body_dark)
c.set(48, 23, body_dark)
c.set(49, 23, body_dark)
c.set(50, 23, body_dark)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 31)))

finish(c)
