from pixelbench_api import *

W, H = 96, 96
OX, OY = 0, 24

# Frame 1: original picture content kept (on a larger working canvas).
f1 = new_canvas(W, H, background=None, name='f1')
f1.blit(input_canvas, OX, OY)

# Frame 2: completed drawn-sword slash.
f2 = f1.copy(name='f2')

# Register the colours needed (palette is shared across canvases).
black  = f2.color('#000000', name='black')
silver = f2.color('#b2aeb1', name='silver')   # bright blade
dark   = f2.color('#231c2c', name='dark')     # blade edge
torso  = f2.color('#454463', name='torso')    # repair colour behind old blade

# Remove the old blade (it pointed up-left from the grip) and repair the torso.
f2.clear(44, 57, 10, 4)          # x44-53, y57-60 in the enlarged canvas
f2.rect(44, 57, 10, 4, torso, fill=True)

# Black slash trail: a tapering crescent sweeping lower-left -> upper-right.
f2.path("M 6 92 C 22 62, 58 26, 88 8 L 76 20 C 50 36, 28 68, 16 86 Z",
        black, fill=True)

# Completed slash: the blade now extends from the left-hand grip up to the
# upper right, ending on the slash.
f2.poly([(85, 12), (83, 10), (49, 57), (55, 61)], silver, fill=True)
f2.line(55, 61, 85, 12, dark)
f2.line(49, 57, 83, 10, dark)

print("F1:", f1.stats_text())
print("F2:", f2.stats_text())
print(f2.matrix_text(region=(0, 0, 95, 95)))

finish([f1, f2])
