from pixelbench_api import *

# Create a 64x64 canvas with transparent background
c = new_canvas(64, 64, background=None)

# Define a consistent palette (max 86 visible colors)
# Using a simple, cohesive color scheme
bg = c.color((235, 240, 245), "background")      # light blue-gray background
outline = c.color((45, 50, 60), "outline")       # dark blue-gray for outlines
primary = c.color((60, 100, 140), "primary")     # medium blue for fills
accent = c.color((200, 120, 60), "accent")       # orange accent
highlight = c.color((180, 200, 220), "highlight") # light highlight
wheel_color = c.color((70, 70, 80), "wheel")     # dark gray for wheels
ped_color = c.color((90, 130, 170), "pedestrian") # pedestrian fill

# Fill background
c.rect(0, 0, 64, 64, bg, fill=True)

# Each icon cell: 32x32 with 2px padding between cells
# Grid layout:
# [0,0] Bus       [32,0] Subway
# [0,32] Bicycle  [32,32] Pedestrian

# ========== TOP-LEFT: BUS (cell: 2,2 to 30,30) ==========
# Bus body - rounded rectangle shape
bus_x, bus_y = 4, 6
bus_w, bus_h = 24, 18

# Main bus body
c.rect(bus_x, bus_y, bus_w, bus_h, primary, fill=True)
c.rect(bus_x, bus_y, bus_w, bus_h, outline, fill=False)

# Windows (3 windows)
win_y = bus_y + 3
for i in range(3):
    wx = bus_x + 3 + i * 7
    c.rect(wx, win_y, 5, 5, highlight, fill=True)

# Wheels (2 wheels)
wheel_y = bus_y + bus_h - 3
c.circle(bus_x + 5, wheel_y, 3, wheel_color, fill=True)
c.circle(bus_x + bus_w - 5, wheel_y, 3, wheel_color, fill=True)

# Headlight
c.set(bus_x + bus_w - 2, bus_y + bus_h - 5, accent)

# ========== TOP-RIGHT: SUBWAY (cell: 34,2 to 62,30) ==========
sub_x, sub_y = 36, 6
sub_w, sub_h = 24, 18

# Subway car body (more rectangular, longer look)
c.rect(sub_x, sub_y, sub_w, sub_h, primary, fill=True)
c.rect(sub_x, sub_y, sub_w, sub_h, outline, fill=False)

# Windows (4 windows for subway)
sub_win_y = sub_y + 4
for i in range(4):
    swx = sub_x + 2 + i * 5
    c.rect(swx, sub_win_y, 4, 5, highlight, fill=True)

# Wheels (2 wheels, partially visible)
sub_wheel_y = sub_y + sub_h - 2
c.circle(sub_x + 5, sub_wheel_y, 3, wheel_color, fill=True)
c.circle(sub_x + sub_w - 5, sub_wheel_y, 3, wheel_color, fill=True)

# Door indication
c.line(sub_x + sub_w // 2, sub_y + 6, sub_x + sub_w // 2, sub_y + sub_h - 4, outline)

# ========== BOTTOM-LEFT: BICYCLE (cell: 2,34 to 30,62) ==========
bike_x, bike_y = 4, 38
bike_w, bike_h = 24, 20

# Wheels
wheel_r = 7
left_wheel_cx = bike_x + 6
right_wheel_cx = bike_x + bike_w - 6
wheel_cy = bike_y + bike_h - wheel_r - 1

# Draw wheel outlines and spokes
c.circle(left_wheel_cx, wheel_cy, wheel_r, wheel_color, fill=False)
c.circle(left_wheel_cx, wheel_cy, 2, wheel_color, fill=True)
c.circle(right_wheel_cx, wheel_cy, wheel_r, wheel_color, fill=False)
c.circle(right_wheel_cx, wheel_cy, 2, wheel_color, fill=True)

# Frame (diamond shape)
seat_x = left_wheel_cx + 3
seat_y = wheel_cy - 9
pedal_x = bike_x + bike_w // 2
pedal_y = wheel_cy - 2
handle_x = right_wheel_cx - 2
handle_y = wheel_cy - 8

# Main frame lines
c.line(left_wheel_cx, wheel_cy - 4, pedal_x, pedal_y, outline)  # seat tube
c.line(pedal_x, pedal_y, right_wheel_cx, wheel_cy - 4, outline)  # down tube
c.line(left_wheel_cx, wheel_cy - 4, right_wheel_cx, wheel_cy - 4, outline)  # chain stay
c.line(seat_x, seat_y, pedal_x, pedal_y, outline)  # top tube
c.line(seat_x, seat_y, left_wheel_cx, wheel_cy - 4, outline)  # seat stay

# Handlebars
c.line(handle_x, handle_y, handle_x + 2, wheel_cy - 4, outline)
c.line(handle_x - 2, handle_y, handle_x + 2, handle_y, outline)

# Seat
c.rect(seat_x - 2, seat_y - 2, 6, 3, primary, fill=True)

# Pedal crank
c.circle(pedal_x, pedal_y, 2, accent, fill=True)

# ========== BOTTOM-RIGHT: PEDESTRIAN (cell: 34,34 to 62,62) ==========
ped_x, ped_y = 36, 36

# Head
head_cx = ped_x + 12
head_cy = ped_y + 4
head_r = 5
c.circle(head_cx, head_cy, head_r, ped_color, fill=True)
c.circle(head_cx, head_cy, head_r, outline, fill=False)

# Body (torso)
body_top = ped_y + 10
body_bottom = ped_y + 20
c.rect(head_cx - 4, body_top, 8, 10, ped_color, fill=True)
c.rect(head_cx - 4, body_top, 8, 10, outline, fill=False)

# Arms (simple lines)
arm_y = body_top + 3
c.line(head_cx - 4, arm_y, head_cx - 8, arm_y + 4, outline)  # left arm
c.line(head_cx + 4, arm_y, head_cx + 8, arm_y + 4, outline)  # right arm

# Legs (walking pose)
leg_top = body_bottom
left_foot_x = head_cx - 3
right_foot_x = head_cx + 5
foot_y = ped_y + 25

c.line(head_cx - 2, leg_top, left_foot_x, foot_y, outline)  # left leg
c.line(head_cx + 2, leg_top, right_foot_x, foot_y - 2, outline)  # right leg

# Feet
c.rect(left_foot_x - 2, foot_y, 4, 2, outline, fill=True)
c.rect(right_foot_x - 2, foot_y - 1, 4, 2, outline, fill=True)

# Check stats
print(c.stats_text())
print(c.matrix_text())

# Submit the canvas
finish(c)
