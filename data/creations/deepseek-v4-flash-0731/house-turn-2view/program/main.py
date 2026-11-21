from pixelbench_api import *

DARK   = (22, 28, 46, 255)      # c3 outline navy
ROOF_B = (151, 118, 61, 255)    # c1 roof brown
ROOF_T = (189, 167, 89, 255)    # c2 roof tan
WALL_F = (220, 170, 70, 255)    # c5 front wall (orange)
WALL_R = (152, 105, 78, 255)    # c4 right wall (brick)
GLASS  = (187, 174, 147, 255)   # c8 glass
CHIM   = (108, 81, 58, 255)     # c0 chimney
SHAD   = (22, 28, 46, 69)       # c10 shadow

W, H = 120, 150

# ---------------- FRAME 1 : 45 deg view (front wall + door, right wall + window) ----
f1 = new_canvas(W, H, name="f1")

# ground shadow
f1.color(SHAD)
f1.poly([(22, 118), (96, 118), (112, 129), (60, 131), (22, 122)], SHAD)
f1.poly([(22, 118), (96, 118), (112, 129), (60, 131), (22, 122)], SHAD)

# right wall (perspective side), brick tone
f1.color(WALL_R)
f1.poly([(92, 60), (112, 66), (112, 124), (92, 118)], WALL_R)
f1.poly([(92, 60), (112, 66), (112, 124), (92, 118)], DARK)

# front wall (facing viewer), warm tone
f1.color(WALL_F)
f1.rect(28, 60, 64, 58, WALL_F, fill=True)
f1.rect(28, 60, 64, 58, DARK, fill=False)

# roof gable, elevated view
f1.color(DARK)
f1.poly([(20, 58), (60, 18), (100, 58)], DARK)
f1.poly([(26, 56), (60, 20), (96, 56)], ROOF_B)
f1.line(60, 20, 96, 56, ROOF_T)

# chimney
f1.rect(38, 24, 10, 16, CHIM, fill=True)
f1.rect(38, 24, 10, 16, DARK, fill=False)
f1.line(37, 23, 49, 23, ROOF_T)

# door on front wall
f1.rect(48, 88, 24, 30, DARK, fill=False)          # frame
f1.rect(50, 90, 20, 26, ROOF_B, fill=True)          # door leaf
f1.line(50, 98, 70, 98, DARK)
f1.line(50, 106, 70, 106, DARK)
f1.set(65, 104, DARK)                                 # knob

# window on right wall (skewed by the side face)
f1.poly([(97, 62), (108, 67), (108, 82), (97, 77)], DARK, fill=False)
f1.poly([(99, 64), (106, 68), (106, 78), (99, 74)], GLASS)
f1.line(102, 66, 102, 76, DARK)

# ---------------- FRAME 2 : 90 deg view (only right wall + window) ---------------
f2 = new_canvas(W, H, name="f2")

# ground shadow
f2.color(SHAD)
f2.poly([(22, 120), (96, 120), (96, 132), (60, 134), (22, 128)], SHAD)

# right wall now faces the viewer
f2.color(WALL_R)
f2.rect(28, 60, 64, 60, WALL_R, fill=True)
f2.rect(28, 60, 64, 60, DARK, fill=False)

# window
f2.rect(42, 76, 36, 30, DARK, fill=False)
f2.rect(44, 78, 32, 26, GLASS, fill=True)
f2.line(60, 78, 60, 104, DARK)
f2.line(44, 91, 76, 91, DARK)

# roof gable above the wall, same elevated camera
f2.poly([(20, 58), (60, 18), (100, 58)], DARK)
f2.poly([(26, 56), (60, 20), (96, 56)], ROOF_B)
f2.line(60, 20, 96, 56, ROOF_T)

# chimney
f2.rect(38, 24, 10, 16, CHIM, fill=True)
f2.rect(38, 24, 10, 16, DARK, fill=False)
f2.line(37, 23, 49, 23, ROOF_T)

print(f1.stats_text())
print(f2.stats_text())
print("sizes equal:", f1.stats()['size'], f2.stats()['size'])

finish([f1, f2])
