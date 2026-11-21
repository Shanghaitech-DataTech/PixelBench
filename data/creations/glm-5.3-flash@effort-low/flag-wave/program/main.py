# Flag-wave: 3 frames. Frame 1 = original. Frames 2 and 3 continue the
# looping wave, with the fly end (right edge of the flag) swinging from its
# highest point to its lowest point.
c = input_canvas
W, H = 48, 56
DARK = c.color('#141b1b')

# --- extract flag (red/orange cloth) and pole (dark vertical) pixels ---
flag = new_canvas(W, H, name='flag')      # red/orange cloth only
pole = new_canvas(W, H, name='pole')      # dark pole only
for y in range(H):
    for x in range(W):
        p = c.get(x, y)
        if p == 0:
            continue
        if p in (1, 2):   # c1 red, c2 orange = cloth
            flag.set(x, y, p)
        else:             # dark outline / pole colour
            pole.set(x, y, p)

# Pole occupies x 0..19; flag cloth starts at x=20 (hoist) and flies to x=43.
HOIST = 20
FLY = 43


def wave_frame(offset):
    """offset: vertical shift of the fly end (positive = down)."""
    f = new_canvas(W, H, name='frame')
    f.blit(pole, 0, 0)
    for x in range(HOIST, FLY + 1):
        t = (x - HOIST) / (FLY - HOIST)          # 0 at hoist, 1 at fly end
        dy = round(offset * t * t)               # swing grows toward fly end
        # copy the cloth column, shifted by dy
        for y in range(H):
            p = flag.get(x, y)
            if p != 0:
                ny = y + dy
                if 0 <= ny < H:
                    f.set(x, ny, p)
    return f


f1 = input_canvas.copy(name='output')            # frame 1: original
f2 = wave_frame(-6)                              # fly end highest
f3 = wave_frame(6)                               # fly end lowest

print(f1.stats_text())
print(f2.stats_text())
print(f3.stats_text())
finish([f1, f2, f3])
