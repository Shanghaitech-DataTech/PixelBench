from pixelbench_api import *

W, H = 48, 38
OX, OY = 4, 3
LEAN = 3


def paste_sheared(src, dst, ox, oy, lean=0):
    """Stamp src into dst with a horizontal shear: top rows shift right by
    `lean` px, bottom rows stay put. Transparent pixels are skipped."""
    sw, sh = src.stats()["size"]
    dw, dh = dst.stats()["size"]
    for y in range(sh):
        shift = round(lean * (1.0 - y / max(1, sh - 1))) if lean else 0
        for x in range(sw):
            idx = src.get(x, y)
            if idx != 0:
                dx = ox + x + shift
                dy = oy + y
                if 0 <= dx < dw and 0 <= dy < dh:
                    dst.set(dx, dy, idx)
    return dst


def build_frame2_src():
    s = input_canvas.copy(name="frame2_src")

    # Eye rolls upward: erase the old pupil and draw a new one higher.
    s.rect(17, 16, 3, 3, "c5", fill=True)   # old pupil -> eye white
    s.rect(17, 15, 3, 3, "c0", fill=True)   # new pupil at top of the eye

    # Mouth opens: dark interior below the existing upper lip, with pale teeth.
    s.rect(13, 20, 11, 3, "c0", fill=True)
    s.rect(14, 20, 9, 1, "c5", fill=True)

    # The image-left foot (the monster's right foot) lifts off the ground.
    foot = s.select(5, 29, 8, 4)
    foot.move_to(5, 26, s, mode="over")

    return s


# Frame 1: the original picture, placed on the shared output canvas.
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas.copy(name="src0"), OX, OY)

# Frame 2: recoil pose (foot up, body leaning back, eye rolled up, mouth open).
f2src = build_frame2_src()
f2 = new_canvas(W, H, name="f2")
paste_sheared(f2src, f2, OX, OY, LEAN)

# Frame 3: the blow landing - same recoil pose under a red impact filter.
ov = new_canvas(W, H, name="red_overlay")
red = (255, 0, 0, 120)
for y in range(H):
    for x in range(W):
        if f2.get(x, y) != 0:
            ov.set(x, y, red)
f3 = flatten([f2, ov], name="f3")

print("f1", f1.stats_text())
print("f2", f2.stats_text())
print("f3", f3.stats_text())

finish([f1, f2, f3])
