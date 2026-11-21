from pixelbench_api import *

src = input_canvas
W, H = 62, 61
OX, OY = 2, 2
ANCHOR_Y = 40


def copy_pixel(dst, x, y, dx=0, dy=0):
    dst.set(OX + x + dx, OY + y + dy, src.get(x, y))


def make_frame(name, upper_shift):
    frame = new_canvas(W, H, background=None, name=name)

    # Plant the lower tentacles first. The mantle and upper arms then bob
    # around this anchor, preserving the character's stance.
    for y in range(ANCHOR_Y, 57):
        for x in range(58):
            copy_pixel(frame, x, y)

    for y in range(ANCHOR_Y):
        for x in range(58):
            copy_pixel(frame, x, y, dy=upper_shift)

    # On the raised pose, bridge the single-pixel transition at the waist.
    if upper_shift < 0:
        y = ANCHOR_Y
        for x in range(58):
            copy_pixel(frame, x, y, dy=-1)

    return frame


# Frame 1 keeps every original pixel unchanged, merely adding shared padding.
f1 = new_canvas(W, H, background=None, name="squid-red-idle-1")
f1.blit(src, OX, OY)
f2 = make_frame("squid-red-idle-2", -1)
f3 = make_frame("squid-red-idle-3", 1)

print(f1.stats_text())
print(f2.stats_text())
print(f3.stats_text())
view(f1, scale=8, margin=1, edges="all")
view(f2, scale=8, margin=1, edges="all")
view(f3, scale=8, margin=1, edges="all")
finish([f1, f2, f3])
