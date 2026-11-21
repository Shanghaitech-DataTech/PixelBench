from pixelbench_api import *

DARK = '#3a3737'
LIGHT = '#b7b3b2'
MID = '#827c7c'
PALE = '#efe9e7'
TAN = '#d6b39d'
BROWN = '#bc8b6d'
GOLD = '#cdae67'

W, H = 40, 30

def hlimb(c, x0, y0, x1, y1, color, hw=1):
    for oy in range(-hw-1, hw+2):
        c.line(x0, y0+oy, x1, y1+oy, DARK)
    for oy in range(-hw, hw+1):
        c.line(x0, y0+oy, x1, y1+oy, color)

# ---------- frame 1: original rabbit, kept unchanged ----------
f1 = new_canvas(W, H, background=None, name='frame1')
f1.blit(input_canvas, 7, 1)

# ---------- frame 2: mid-leap rabbit (shifted up + forward-left) ----------
f2 = new_canvas(W, H, background=None, name='frame2')

# far limbs (behind the body)
hlimb(f2, 17, 16, 10, 18, LIGHT)    # far front leg
hlimb(f2, 33, 16, 37, 17, LIGHT)    # far hind leg

# far feet
f2.ellipse(9, 17, 2, 1, LIGHT)
f2.ellipse(9, 17, 2, 1, DARK, fill=False)
f2.ellipse(36, 16, 2, 1, LIGHT)
f2.ellipse(36, 16, 2, 1, DARK, fill=False)

# body (clean oval with a soft underside shade)
f2.ellipse(25, 13, 9, 4, PALE)
f2.ellipse(25, 15, 7, 2, LIGHT)
f2.ellipse(25, 13, 9, 4, DARK, fill=False)

# near limbs (in front of the body)
hlimb(f2, 20, 15, 5, 19, PALE)      # near front leg
hlimb(f2, 31, 14, 37, 17, PALE)     # near hind leg

# near paws/feet and tail
f2.ellipse(5, 19, 2, 1, PALE)
f2.ellipse(5, 19, 2, 1, DARK, fill=False)
f2.ellipse(36, 17, 3, 2, PALE)
f2.ellipse(36, 17, 3, 2, DARK, fill=False)

f2.ellipse(32, 5, 2, 2, GOLD)
f2.ellipse(32, 5, 2, 2, DARK, fill=False)

# head + ears pasted over everything in front
sel = input_canvas.select(6, 0, 19, 13)
sel.copy_to(2, 2, f2, mode="over")

print("=== frame1 ===")
print(f1.stats_text())
print("=== frame2 ===")
print(f2.stats_text())
print(f2.matrix_text())

finish([f1, f2])
