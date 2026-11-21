from pixelbench_api import *

c = new_canvas(64, 64, background=None, name="subway")

# Palette
ceiling = (130, 135, 145)
wall = (185, 190, 200)
floor_top = (125, 128, 135)
floor_dark = (105, 108, 115)
floor_line = (235, 210, 60)
track_dark = (60, 62, 70)
track = (78, 81, 88)
train_dark = (40, 42, 50)
train_mid = (80, 86, 98)
train_light = (115, 122, 136)
train_window = (150, 188, 210)
train_win_d = (110, 140, 163)
head_light = (255, 240, 180)
door_frame = (125, 130, 140)
glass_panel = (175, 200, 218)
glass_shade = (140, 165, 185)
bench = (95, 75, 55)
bench_lit = (120, 95, 70)
bench_metal = (115, 120, 130)
sign_board = (22, 26, 40)
sign_white = (240, 240, 240)
line_red = (185, 40, 55)
skin = (222, 182, 150)
hair = (25, 25, 32)
jacket_blue = (48, 90, 152)
jacket_red = (158, 55, 60)
jacket_green = (58, 115, 85)
pants = (48, 48, 60)
shoes = (72, 72, 82)
body_dark = (38, 38, 46)
sweat = (96, 96, 110)
phone = (140, 150, 170)

# ============ CEILING ============
c.rect(0, 0, 64, 5, ceiling)

# ============ TRACK (right) ============
c.rect(37, 5, 27, 59, track_dark)

# ============ PLATFORM WALL (left) ============
c.rect(0, 5, 33, 44, wall)

# ============ TRAIN ARRIVING ============
# Train body, slight ramp into the arcade from the right
c.rect(44, 12, 20, 40, train_mid)
# roof stripe (sloped up going back = depth)
c.rect(44, 12, 20, 3, train_dark)
# nose (front face on left edge)
c.rect(44, 15, 3, 37, train_light)
# windshield / cab window near front
c.rect(44, 20, 3, 8, train_window)
# windows shrinking toward back-right (depth)
c.rect(49, 20, 6, 12, train_window)
c.rect(56, 21, 4, 11, train_window)
c.rect(61, 22, 3, 10, train_window)
# window frame over rail
c.rect(44, 19, 17, 1, train_light)
c.rect(44, 31, 18, 1, train_light)
# window divider tint lines
c.rect(55, 20, 1, 12, train_win_d)
c.rect(60, 21, 1, 11, train_win_d)
# headlight beams at nose (motion + arrival)
c.rect(44, 16, 2, 2, head_light)
for bx in range(3):
    c.rect(40+bx, 16+bx, 2, 2, head_light)
# lower body strip
c.rect(44, 34, 20, 2, train_light)
# door on train lower
c.rect(49, 36, 6, 16, train_dark)
# door window
c.rect(50, 37, 4, 6, train_window)
# wheels/bogies at track level
c.rect(46, 50, 6, 3, train_dark)
c.rect(54, 50, 6, 3, train_dark)
# speed/motion streaks on track (forward of train)
for i in range(5):
    c.rect(38, 44+i, 14-i, 1, track)
    # thin streak highlights
    c.rect(40, 45+i, 4, 1, track_dark)

# ============ PLATFORM FLOOR ============
c.rect(0, 51, 38, 8, floor_top)
c.rect(0, 59, 38, 5, floor_dark)
# warning line along platform edge
c.rect(0, 49, 39, 2, floor_line)

# ============ STATION SIGNS (hang from ceiling, top area) ============
# Main sign
c.rect(10, 7, 22, 5, sign_board)      # board at rows 7-11
c.rect(13, 5, 2, 2, bench_metal)       # chain
c.rect(16, 5, 2, 2, bench_metal)
c.rect(19, 5, 2, 2, bench_metal)
c.rect(22, 5, 2, 2, bench_metal)
c.text(11, 8, "EXIT", sign_white, spacing=0)   # short label fits
c.rect(10, 12, 22, 1, line_red)

# ============ PLATFORM SCREEN DOORS (below signs) ============
# Top rail of doors at rows 14-15
c.rect(0, 14, 34, 2, door_frame)
# Door panels: alternating glass and frame
for seg in range(4):
    gx = 2 + seg*8
    # glass segment
    c.rect(gx, 16, 5, 31, glass_panel)
    c.rect(gx, 16, 5, 3, glass_shade)
    # vertical frame border on right of glass
    c.rect(gx+5, 14, 1, 33, door_frame)
# bottom rail
c.rect(0, 47, 34, 2, door_frame)

# ============ BENCH on platform ============
# legs
c.rect(3, 48, 2, 3, bench_metal)
c.rect(13, 48, 2, 3, bench_metal)
c.rect(23, 48, 2, 3, bench_metal)
# seat
c.rect(2, 44, 25, 4, bench)
c.rect(2, 44, 25, 1, bench_lit)
# backrest
c.rect(2, 38, 2, 6, bench)
c.rect(24, 38, 2, 6, bench)
c.rect(2, 38, 25, 1, bench_lit)

# ============ PASSENGERS ============

# Passenger 1: SITTING on bench, reading phone
# torso
c.rect(5, 36, 6, 8, jacket_red)
# shoulders
c.rect(5, 35, 6, 2, jacket_red)
# head bowed toward phone
c.rect(6, 32, 5, 4, skin)
c.rect(6, 31, 5, 1, hair)
c.rect(7, 35, 4, 1, skin)
# phone in hands (bright)
c.rect(8, 38, 3, 2, phone)
# legs over bench edge
c.rect(6, 44, 2, 2, pants)
c.rect(8, 44, 2, 2, pants)
c.rect(6, 46, 3, 1, shoes)
c.rect(8, 46, 3, 1, shoes)

# Passenger 2: STANDING, walking left (stride), mid
# body leaning forward (dark silhouette)
c.rect(17, 28, 6, 9, body_dark)
# head
c.rect(17, 24, 5, 4, skin)
c.rect(17, 23, 5, 1, hair)
# arm swinging back
c.rect(16, 29, 1, 6, body_dark)
# front leg (extended left, stride)
c.rect(18, 37, 3, 8, pants)
c.rect(17, 45, 4, 1, shoes)
# back leg (behind, shorter)
c.rect(21, 37, 2, 6, pants)
c.rect(22, 43, 3, 1, shoes)
# small bag held in back arm
c.rect(15, 35, 2, 3, pants)

# Passenger 3: STANDING near platform edge, watching train, one hand raised
# body upright (dark silhouette for contrast)
c.rect(30, 26, 6, 10, jacket_green)
# head turned toward train (right)
c.rect(30, 21, 6, 5, skin)
c.rect(30, 20, 6, 1, hair)
# legs
c.rect(31, 36, 2, 9, pants)
c.rect(34, 36, 2, 9, pants)
c.rect(31, 45, 3, 1, shoes)
c.rect(34, 45, 3, 1, shoes)
# raised arm (pointing right toward train)
c.rect(29, 27, 1, 8, jacket_green)

print(c.stats_text())
finish(c)
