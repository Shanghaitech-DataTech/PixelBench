import math

# ---------------------------------------------------------------- canvas setup
W, H = 88, 96          # both frames share these dimensions
OX, OY = 10, 18        # where the original 62x72 picture is placed
BLACK = '#000000'


def crescent(cv, A, B, sag, tmax, peak=0.5, power=1.25, N=600):
    """Solid, tapered black crescent from A to B, bulging to the upper-left.

    The band is centred on a quadratic Bezier between the two tips; its
    thickness peaks at `peak` and tapers to nothing at both ends, so the
    trail reads as a swing that starts thin, swells and whips out again.
    """
    ax, ay = A
    bx, by = B
    dx, dy = bx - ax, by - ay
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    if nx > 0:                      # force the bulge toward the upper left
        nx, ny = -nx, -ny
    mx, my = (ax + bx) / 2.0, (ay + by) / 2.0
    cx = 2 * (mx + nx * sag) - mx
    cy = 2 * (my + ny * sag) - my

    samples = []
    for i in range(N + 1):
        t = i / N
        q = 1 - t
        px = q * q * ax + 2 * q * t * cx + t * t * bx
        py = q * q * ay + 2 * q * t * cy + t * t * by
        u = t / peak if t <= peak else (1 - t) / (1 - peak)
        th = tmax * (math.sin(math.pi * 0.5 * u)) ** power
        samples.append((px, py, th * 0.5))

    col = cv.color(BLACK)
    x0 = max(0, int(min(p[0] for p in samples)) - 2)
    x1 = min(W - 1, int(max(p[0] for p in samples)) + 2)
    y0 = max(0, int(min(p[1] for p in samples)) - 2)
    y1 = min(H - 1, int(max(p[1] for p in samples)) + 2)
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            px, py = x + 0.5, y + 0.5
            for (sx, sy, h) in samples:
                ddx = px - sx
                ddy = py - sy
                if ddx * ddx + ddy * ddy <= (h + 0.35) ** 2:
                    cv.set(x, y, col)
                    break


# ---------------------------------------------------------------- frame 1
f1 = new_canvas(W, H, name='f1')
f1.blit(input_canvas, OX, OY)

# ---------------------------------------------------------------- frame 2
f2 = new_canvas(W, H, name='f2')
# left-handed slash: sweeps from the lower left up to the upper right
crescent(f2, (2, 92), (84, 8), 24, 9.5)
crescent(f2, (2, 92), (84, 8), 33, 2.2, peak=0.5, power=1.0)
# the character is stamped on top, so every original pixel is preserved
f2.blit(input_canvas, OX, OY)

# ---------------------------------------------------------------- checks
bad = 0
for y in range(72):
    for x in range(62):
        if input_canvas.get(x, y) != f1.get(x + OX, y + OY):
            bad += 1
print('f1 mismatch vs input:', bad)

bad = 0
for y in range(H):
    for x in range(W):
        if f1.get(x, y) != 0 and f2.get(x, y) != f1.get(x, y):
            bad += 1
print('f2 overwrote character pixels:', bad)
print('f1 outside character:', f1.stats()['visible_pixels'], 'f2 total visible:', f2.stats()['visible_pixels'])
print('trail pixels:', f2.stats()['visible_pixels'] - f1.stats()['visible_pixels'])

print(save('slash_f1', f1))
print(save('slash_f2', f2))
finish([f1, f2])
