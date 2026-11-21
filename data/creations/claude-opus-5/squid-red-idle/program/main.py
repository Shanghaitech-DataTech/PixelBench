W, H = 58, 59
SRC_Y = 1          # original image placed one row down, so the body can rise
S = 49             # first "planted" row in frame coords (= original row 48, the legs)

# Frame 1: original picture content, unchanged, on the taller canvas
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, 0, SRC_Y)


def bob(name, dy):
    """Legs stay planted; the blob (rows 0..S-1) shifts by dy and the seam row is
    duplicated (dy<0, stretch) or absorbed (dy>0, squash)."""
    c = new_canvas(W, H, name=name)
    f1.select(0, S, W, H - S).copy_to(0, S, c)              # planted legs
    f1.select(0, 0, W, S).copy_to(0, dy, c, mode="over")    # bobbing blob
    if dy < 0:
        seam = f1.select(0, S - 1, W, 1)
        for k in range(-dy):
            seam.copy_to(0, S - 1 - k, c, mode="over")
    return c


f2 = bob("f2", -1)   # inhale: blob lifts
f3 = bob("f3", 1)    # exhale: blob settles

view(f1)
view(f2)
view(f3)

finish([f1, f2, f3])
