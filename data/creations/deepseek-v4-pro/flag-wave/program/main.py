from pixelbench_api import *

src = input_canvas
W, H = src.stats()['size']

# Frame 1: keep the original picture content unchanged.
f1 = src.copy(name="frame1")

def cloth_top(x):
    """Topmost visible cloth pixel (y <= 35) in a column."""
    for y in range(0, 36):
        if src.get(x, y) != 0:
            return y
    return None

def make_frame(Yf, name):
    """
    Build a waving frame. The flag's hoist/sleeve (x < 20) stays fixed,
    while the waving cloth (x >= 20) is shifted downward column by column
    so that its top edge runs from y=12 at x=20 to y=Yf at the fly end.
    """
    out = src.copy(name=name)

    # Erase only the part of the cloth that will be redrawn.
    out.clear(x=20, y=0, w=W - 20, h=36)

    for x in range(20, W):
        top0 = cloth_top(x)
        if top0 is None:
            continue

        if x < 36:
            t = (x - 20) / 16.0
            target_top = 12 + (Yf - 12) * t
            shift = int(round(target_top)) - top0
        else:
            # The fly end moves as a rigid vertical band.
            shift = Yf - top0

        for y in range(0, 36):
            col = src.get(x, y)
            if col != 0:
                ny = y + shift
                if 0 <= ny < H:
                    out.set(x, ny, col)

    return out

# Frame 2: fly end at the middle of its swing (level with the hoist).
f2 = make_frame(12, "frame2")

# Frame 3: fly end at the lowest point of the swing.
f3 = make_frame(24, "frame3")

print(f1.stats_text())
print(f2.stats_text())
print(f3.stats_text())

finish([f1, f2, f3])
