from pixelbench_api import *

# Frame 1: Original image on 44x44 canvas
f1 = new_canvas(44, 44)
f1.blit(input_canvas, 0, 0)

# Frame 2: Edited image on 44x44 canvas
f2 = new_canvas(44, 44)
f2.blit(input_canvas, 0, 0)

# Clear the original left arm (which was folded up)
f2.clear(x=12, y=7, w=15, h=11)

# Re-draw the right side of the torso (which is the character's front/chest)
# y=7
f2.set(12, 7, 'c2')
f2.set(13, 7, 'c0')
# y=8
f2.set(12, 8, 'c2')
f2.set(13, 8, 'c0')
# y=9
f2.set(12, 9, 'c2')
f2.set(13, 9, 'c0')
# y=10
f2.set(12, 10, 'c2')
# y=11
f2.set(12, 11, 'c2')
# y=12
f2.set(12, 12, 'c2')
f2.set(13, 12, 'c4')
# y=13
f2.set(12, 13, 'c2')
f2.set(13, 13, 'c2')
# y=14
f2.set(12, 14, 'c2')
f2.set(13, 14, 'c2')
f2.set(14, 14, 'c2')
f2.set(15, 14, 'c5')
f2.set(16, 14, 'c0')
# y=15
f2.set(12, 15, 'c4')
f2.set(13, 15, 'c4')
f2.set(14, 15, 'c4')
f2.set(15, 15, 'c4')
f2.set(16, 15, 'c5')
f2.set(17, 15, 'c0')
# y=16
f2.set(12, 16, 'c4')
f2.set(13, 16, 'c2')
f2.set(14, 16, 'c2')
f2.set(15, 16, 'c4')
f2.set(16, 16, 'c0')
# y=17
f2.set(12, 17, 'c2')
f2.set(13, 17, 'c2')
f2.set(14, 17, 'c2')
f2.set(15, 17, 'c4')
f2.set(16, 17, 'c0')

# Now draw the extended arm
# Top outline
f2.line(13, 9, 26, 9, 'c0')
# Bottom outline
f2.line(14, 13, 26, 13, 'c0')

# Arm fill
f2.rect(13, 10, 14, 3, 'c2') # main skin tone
f2.line(13, 12, 26, 12, 'c4') # shadow on bottom of arm

# Fist
f2.rect(27, 9, 5, 5, 'c0') # outline
f2.rect(28, 10, 3, 3, 'c2') # fist fill
f2.set(28, 12, 'c4')
f2.set(29, 12, 'c4')
f2.set(30, 12, 'c4')
f2.set(30, 11, 'c0') # finger separation

# Shoulder joint area
f2.set(13, 10, 'c2')
f2.set(13, 11, 'c2')
f2.set(13, 12, 'c4')

finish([f1, f2])
