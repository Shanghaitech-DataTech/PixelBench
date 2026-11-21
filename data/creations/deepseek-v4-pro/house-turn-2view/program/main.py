import numpy as np

# Palette indices (from the input image's shared palette)
BROWN_D = 1
BROWN = 2
TAN = 3
DARK = 4
RED = 5
GOLD = 6
YELLOW = 7
DOOR = 8
WALL_GRAY = 9
WALL_TAN = 10
SHADOW = 11

W_IN, H_IN = 112, 157
W_OUT, H_OUT = 176, 157


def hscale(src, dst_w, name=None):
    """Horizontal nearest-neighbour scale of a canvas (keeps height)."""
    W, H, inds, pal = src.to_indexed(scale=1)
    inds = np.frombuffer(inds, dtype=np.uint8).reshape((H, W))
    out = new_canvas(dst_w, H, name=name)
    for y in range(H):
        for x in range(dst_w):
            sx = x * W // dst_w
            if sx >= W:
                sx = W - 1
            idx = int(inds[y, sx])
            if idx != 0:
                out.set(x, y, idx)
    return out


def build_right_face():
    """Side wall (with a window) plus the sloped side roof, seen from 90 deg."""
    rf = new_canvas(W_IN, H_IN, name='right_face')

    # Sloped side roof plane (y 0..114)
    rf.rect(0, 0, 112, 115, TAN, fill=True)
    for y in range(0, 115, 7):
        rf.rect(0, y, 112, 3, BROWN, fill=True)
        rf.rect(0, y + 3, 112, 2, GOLD, fill=True)
    rf.rect(0, 0, 112, 1, YELLOW, fill=True)   # ridge highlight
    rf.rect(0, 114, 112, 1, DARK, fill=True)   # eave line

    # Side wall (y 115..156)
    rf.rect(0, 115, 112, 42, WALL_GRAY, fill=True)
    rf.rect(0, 115, 112, 2, WALL_TAN, fill=True)

    # Window on the right-hand wall
    wx, wy, ww, wh = 36, 124, 40, 26
    rf.rect(wx, wy, ww, wh, DARK, fill=True)
    rf.rect(wx + 2, wy + 2, ww - 4, wh - 4, GOLD, fill=True)
    rf.rect(wx + ww // 2 - 1, wy + 2, 2, wh - 4, DARK, fill=True)
    rf.rect(wx + 2, wy + wh // 2 - 1, ww - 4, 2, DARK, fill=True)

    # Soft ground shadow at the base
    rf.rect(8, 150, 96, 7, SHADOW, fill=True)
    return rf


src = input_canvas
right_face = build_right_face()

# Frame 1: 45 degree yaw -> front face (door/front wall) + right face (window wall)
front45 = hscale(src, 79, name='front45')
right45 = hscale(right_face, 79, name='right45')

f1 = new_canvas(W_OUT, H_OUT, name='f1_45deg')
ox = (W_OUT - 158) // 2
f1.blit(front45, ox, 0)
f1.blit(right45, ox + 79, 0)

# Frame 2: 90 degree yaw -> only the right-hand wall and its window
f2 = new_canvas(W_OUT, H_OUT, name='f2_90deg')
f2.blit(right_face, (W_OUT - W_IN) // 2, 0)

print('f1', f1.stats_text())
print('f2', f2.stats_text())

finish([f1, f2])
