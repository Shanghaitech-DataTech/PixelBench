from pixelbench_api import *

# Create 64x64 canvas for laboratory workbench
c = new_canvas(64, 64, background=None)

# Define color palette
# Workbench colors
wood_dark = c.color((62, 39, 25), "wood_dark")
wood_mid = c.color((94, 61, 40), "wood_mid")
wood_light = c.color((128, 84, 55), "wood_light")

# Microscope colors
micro_black = c.color((28, 28, 30), "micro_black")
micro_gray_dark = c.color((70, 70, 75), "micro_gray_dark")
micro_gray_mid = c.color((120, 120, 125), "micro_gray_mid")
micro_gray_light = c.color((180, 180, 185), "micro_gray_light")
micro_silver = c.color((200, 200, 210), "micro_silver")
micro_knob = c.color((45, 45, 50), "micro_knob")

# Test tube colors
tube_glass = c.color((220, 235, 245, 180), "tube_glass")
tube_glass_dark = c.color((180, 200, 220, 150), "tube_glass_dark")
tube_liquid = c.color((100, 180, 220), "tube_liquid")
rack_metal = c.color((140, 140, 150), "rack_metal")
rack_shadow = c.color((100, 100, 110), "rack_shadow")

# Dropper colors
dropper_bulb = c.color((200, 220, 230, 200), "dropper_bulb")
dropper_glass = c.color((180, 200, 210), "dropper_glass")
dropper_tip = c.color((130, 130, 140), "dropper_tip")

# Bottle colors
bottle_amber = c.color((180, 140, 80, 180), "bottle_amber")
bottle_clear = c.color((200, 220, 230, 170), "bottle_clear")
cap_red = c.color((180, 60, 60), "cap_red")
cap_blue = c.color((60, 100, 180), "cap_blue")
cap_green = c.color((80, 140, 80), "cap_green")
bottle_label = c.color((240, 240, 230), "bottle_label")

# Notebook colors
note_paper = c.color((245, 240, 220), "note_paper")
note_lines = c.color((180, 180, 200), "note_lines")
note_binding = c.color((60, 80, 120), "note_binding")
note_shadow = c.color((200, 195, 175), "note_shadow")

# Background wall
wall_color = c.color((220, 225, 230), "wall_color")

# Draw background wall (top portion)
c.rect(0, 0, 64, 28, wall_color)

# Draw workbench surface (bottom portion)
c.rect(0, 28, 64, 36, wood_dark)
c.rect(0, 30, 64, 4, wood_mid)
c.rect(0, 34, 64, 2, wood_light)

# ============ MICROSCOPE (left side) ============
# Base
c.rect(8, 35, 22, 6, micro_black)
c.rect(10, 33, 18, 2, micro_gray_dark)

# Arm and stage
c.rect(16, 20, 4, 13, micro_gray_mid)
c.rect(12, 30, 16, 3, micro_gray_dark)  # stage

# Body tube
c.rect(15, 8, 6, 12, micro_gray_light)
c.rect(16, 6, 4, 4, micro_silver)  # eyepiece top

# Objective lenses
c.rect(15, 28, 2, 4, micro_silver)
c.rect(17, 28, 2, 4, micro_silver)
c.rect(19, 28, 2, 4, micro_silver)

# Focus knobs
c.circle(26, 22, 3, micro_knob)
c.circle(26, 27, 2, micro_knob)

# ============ TEST TUBE RACK (center-left) ============
# Rack base
c.rect(34, 38, 16, 4, rack_metal)
c.rect(34, 36, 16, 2, rack_shadow)

# Rack top
c.rect(34, 32, 16, 3, rack_metal)

# Test tubes (3 tubes)
# Tube 1
c.rect(36, 22, 4, 12, tube_glass)
c.rect(37, 24, 2, 8, tube_liquid)
c.rect(36, 22, 4, 2, tube_glass_dark)  # rim

# Tube 2
c.rect(42, 20, 4, 14, tube_glass)
c.rect(43, 26, 2, 6, tube_liquid)
c.rect(42, 20, 4, 2, tube_glass_dark)

# Tube 3
c.rect(48, 23, 4, 11, tube_glass)
c.rect(49, 25, 2, 7, tube_glass_dark)  # empty tube
c.rect(48, 23, 4, 2, tube_glass_dark)

# ============ DROPPER (center-right, lying down) ============
c.rect(52, 42, 10, 3, dropper_glass)  # glass tube
c.circle(51, 43, 2, dropper_bulb)  # bulb
c.rect(60, 43, 2, 1, dropper_tip)  # metal tip

# ============ BOTTLES (right side) ============
# Bottle 1 (amber with red cap)
c.rect(38, 44, 8, 10, bottle_amber)
c.rect(39, 44, 6, 6, bottle_label)
c.rect(39, 42, 6, 3, cap_red)

# Bottle 2 (clear with blue cap)
c.rect(48, 46, 7, 8, bottle_clear)
c.rect(49, 47, 5, 5, bottle_label)
c.rect(49, 44, 5, 3, cap_blue)

# Bottle 3 (amber with green cap)
c.rect(56, 44, 7, 9, bottle_amber)
c.rect(57, 45, 5, 5, bottle_label)
c.rect(57, 42, 5, 3, cap_green)

# ============ OPEN NOTEBOOK (front center) ============
# Left page
c.poly([(18, 52), (30, 50), (30, 62), (18, 64)], note_paper)
c.poly([(18, 52), (30, 50), (30, 52), (18, 54)], note_shadow)

# Right page
c.poly([(30, 50), (44, 52), (44, 64), (30, 62)], note_paper)
c.poly([(30, 50), (44, 52), (44, 54), (30, 52)], note_shadow)

# Binding
c.rect(29, 50, 2, 14, note_binding)

# Lines on pages (suggesting writing/diagrams)
c.line(20, 55, 28, 55, note_lines)
c.line(20, 58, 28, 58, note_lines)
c.line(20, 61, 26, 61, note_lines)

c.line(32, 55, 42, 55, note_lines)
c.line(32, 58, 42, 58, note_lines)
c.line(32, 61, 40, 61, note_lines)

# Small diagram circle on notebook
c.circle(36, 57, 2, note_lines, fill=False)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 64, 64), indices=False))

finish(c)
