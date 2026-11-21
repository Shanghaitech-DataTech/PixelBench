from pixelbench_api import *
import numpy as np

src = input_canvas
W, H, raw = src.to_rgba(1)
A = np.frombuffer(raw, dtype=np.uint8).reshape(H, W, 4)

def perspective_3q(arr, turn):
    """Inverse-mapped asymmetric horizontal foreshortening (pivot at canvas center).
    turn 'L': character turns to ITS left -> its left side (image-right half) is near.
    turn 'R': character turns to ITS right -> its right side (image-left half) is near.
    """
    cx = W / 2.0
    s_far = 0.52
    s_near = 0.97
    if turn == 'L':
        sL, sR = s_far, s_near
    else:
        sL, sR = s_near, s_far
    out = np.zeros((H, W, 4), dtype=np.uint8)
    for y in range(H):
        row = arr[y]
        for xo in range(W):
            if xo < cx:
                xi = int(round(cx + (xo - cx) / sL))
            else:
                xi = int(round(cx + (xo - cx) / sR))
            if 0 <= xi < W:
                col = row[xi]
                if col[3]:
                    out[y, xo] = col
    return out

def center_crop(arr):
    xs = np.where(arr[:, :, 3] > 0)[1]
    if len(xs) == 0:
        return arr
    x0, x1 = xs.min(), xs.max()
    w = x1 - x0 + 1
    off = (W - w) // 2
    out = np.zeros((H, W, 4), dtype=np.uint8)
    out[:, off:off + w] = arr[:, x0:x1 + 1]
    return out

def to_canvas(arr, name):
    ch, cw = arr.shape[:2]
    c = new_canvas(cw, ch, name=name)
    for y in range(ch):
        row = arr[y]
        for x in range(cw):
            r, g, b, a = row[x]
            if a:
                c.set(x, y, (int(r), int(g), int(b), int(a)))
    return c

def rear_view(arr):
    B = arr[:, ::-1, :].copy()  # mirror horizontally
    face_cols = {
        (0xfd, 0xd5, 0xb7, 0xff),  # g skin
        (0xea, 0xa3, 0x77, 0xff),  # h skin shadow
        (0x9e, 0x3e, 0x37, 0xff),  # j red
        (0x50, 0xd4, 0xec, 0xff),  # k cyan
        (0xf2, 0xf8, 0xf9, 0xff),  # l white
        (0x51, 0x87, 0xb3, 0xff),  # m blue
        (0x29, 0x3d, 0x4b, 0xff),  # n navy
        (0xd2, 0x85, 0x60, 0xff),  # o cheek shadow
    }
    a_col = np.array([0x05, 0x01, 0x00, 0xff], np.uint8)
    b_col = np.array([0x16, 0x07, 0x01, 0xff], np.uint8)
    c_col = np.array([0x29, 0x0e, 0x02, 0xff], np.uint8)
    h_col = np.array([0xea, 0xa3, 0x77, 0xff], np.uint8)

    def strand(x, y):
        if x in (25, 26, 37, 38):
            return b_col
        if x in (31,) and y % 2 == 0:
            return c_col
        if x in (34,) and y % 2 == 1:
            return c_col
        if x in (28, 35) and y < 37:
            return h_col
        if x in (24, 39) and y > 40:
            return c_col
        return a_col

    # rows 24-30: forehead skin -> hair
    for y in range(24, 31):
        for x in range(B.shape[1]):
            if tuple(B[y, x]) in face_cols:
                B[y, x] = strand(x, y) if y > 26 else a_col
    # rows 31-48: face + jaw -> back-of-head hair
    for y in range(31, 49):
        for x in range(B.shape[1]):
            if tuple(B[y, x]) in face_cols:
                B[y, x] = strand(x, y)
    return B

# ----- Frame 1: three-quarter view, character turned 45 degrees to ITS LEFT -----
f1a = center_crop(perspective_3q(A, 'L'))
# ----- Frame 2: three-quarter view, character turned 45 degrees to ITS RIGHT -----
f2a = center_crop(perspective_3q(A, 'R'))
# ----- Frame 3: rear view (seen from directly behind) -----
f3a = rear_view(A)

f1 = to_canvas(f1a, "frame1_3q_left")
f2 = to_canvas(f2a, "frame2_3q_right")
f3 = to_canvas(f3a, "frame3_rear")

for f in (f1, f2, f3):
    print(f.name, f.stats_text())

finish([f1, f2, f3])
