from pixelbench_api import *

c = input_canvas

f1 = c.copy(name="f1")

# Frame 2: the 90-degree view - only the right-hand wall (with its window)
# faces the camera, from the same elevated fixed camera. The right-hand wall
# slice of the 45-degree view (columns 74..94) is re-faced at its frontal
# width so the wall spans the frame frontally, and the door-side clutter is
# excluded so only the right wall with its window remains.
sel = f1.select(70, 0, 25, 157)
rs = sel.resize(34, 157)
pv = rs.preview()
f2 = new_canvas(112, 157, name="f2")
f2.blit(pv, 39, 0)

print("f2:", f2.stats())
chars = {0:'.', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'s', 11:'g'}
ruler = ""
for i in range(112):
    if i % 4 == 0:
        ruler += str((i//4)%10)
    else:
        ruler += ' '
print("   " + ruler)
for y in range(0, 157, 4):
    row = ''.join(chars.get(f2.get(x, y), '?') for x in range(112))
    print(f"{y:3d} {row}")

finish([f1, f2])
