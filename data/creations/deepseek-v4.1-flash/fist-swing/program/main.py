from pixelbench_api import *

src = input_canvas

W, H = 42, 46
OX, OY = 5, 1

SKIN = '#eec39a'
BROWN = '#8f563b'
DARK = '#222034'

f1 = new_canvas(W, H, name="f1")
f1.blit(src, OX, OY)

f2 = new_canvas(W, H, name="f2")
f2.blit(src, OX, OY)

skin = f2.color(SKIN)
brown = f2.color(BROWN)
dark = f2.color(DARK)
LEG = {'S': skin, 'B': brown, 'D': dark}


def stamp(canvas, ox, oy, rows, legend):
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            if ch == '.':
                continue
            canvas.set(ox + i, oy + j, legend[ch])


# ---- FRAME 2: left arm (image right) thrown out in a light straight punch ----

# 1. remove the protruding folded-arm pixels of the original pose
f2.clear(22, 10, 5, 2)
f2.set(21, 10, dark)
f2.set(21, 11, dark)

# 2. new extended arm + fist, stamped from x=19, y=10
ARM = [
    "............DDDDD.",   # y=10  top of fist
    "...........DSSSSSD",   # y=11  fist, rounded corners
    "DDDDDDDDDDDDSSSSSD",   # y=12  arm top outline + fist
    "DSSSSSSSSSSDSSSBSD",   # y=13  forearm; wrist crease; knuckle
    "DSSSSSSSSSSDSSSSSD",   # y=14
    "DSSSSSSSSSSDBBSSSD",   # y=15  thumb shadow inside fist
    "DDDDDDDDDDDDBBBBBD",   # y=16  arm underside + fingers underside
    "............DDDDD.",   # y=17  bottom of fist
]
stamp(f2, 19, 10, ARM, LEG)

print(f1.stats_text())
print(f2.stats_text())
print(f2.matrix_text(region=(17, 8, 38, 19), indices=True))
save("f1", f1)
save("f2", f2)
view(f1)
view(f2)
finish([f1, f2])
