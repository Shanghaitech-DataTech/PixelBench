import math
import numpy as np

# ------------------------------------------------------------------ 1. re-pose the knife
# original: tip up-left, cutting edge (bright band) on the lower-left side.
work = input_canvas.copy(name="work")
work.mirror(axis="h")                                    # tip now points up-right
rot = work.select(0, 0, 93, 128).rotate(53, algorithm="rotsprite").preview()
bx0, by0, bx1, by1 = rot.stats()["bbox"]
sprite = rot.select(bx0, by0, bx1 - bx0 + 1, by1 - by0 + 1).preview()
SW, SH = sprite.stats()["size"]

sarr = np.frombuffer(sprite.to_rgba()[2], dtype=np.uint8).reshape(SH, SW, 4)
svis = sarr[:, :, 3] > 0
TIPX = int(np.nonzero(svis.any(axis=0))[0].max())
TIPY = int(round(np.nonzero(svis[:, TIPX])[0].mean()))
print("knife sprite %dx%d, tip at local (%d,%d)" % (SW, SH, TIPX, TIPY))

# ------------------------------------------------------------------ 2. output canvas
W, H = 256, 128
DX, DY = 48, 50                       # main knife paste position (tip -> (201,61))
result = new_canvas(W, H, name="output")

# ------------------------------------------------------------------ 3. helpers
def stamp(dst, src, dx, dy, alpha):
    """Draw src onto dst at (dx,dy), replacing every pixel's alpha (ghost copy)."""
    w2, h2, idx, _p = src.to_indexed()
    if isinstance(idx, (bytes, bytearray, memoryview)):
        idx = np.frombuffer(bytes(idx), dtype=np.uint8)
    else:
        idx = np.asarray(idx).astype(np.uint8).ravel()
    idx = idx.reshape(h2, w2)
    rgba = {p["index"]: tuple(p["rgba"]) for p in src.palette()}
    for y in range(h2):
        row = idx[y]
        x = 0
        while x < w2:
            ci = int(row[x])
            if ci == 0:
                x += 1
                continue
            x0 = x
            while x < w2 and int(row[x]) == ci:
                x += 1
            r, g, b, _a = rgba[ci]
            dst.line(dx + x0, dy + y, dx + x - 1, dy + y, (r, g, b, alpha))

def draw_streak(c, pts, hmax, colour, power=0.62, step=0.4):
    """Tapered streak along a polyline centreline; thickness hmax*sin(pi*u)**power."""
    segs, L = [], 0.0
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        d = math.hypot(x1 - x0, y1 - y0)
        segs.append((x0, y0, x1, y1, d))
        L += d
    s = 0.0
    while s <= L + 1e-9:
        rem = min(s, L)
        cx = cy = None
        for (x0, y0, x1, y1, d) in segs:
            if rem <= d + 1e-9:
                t = rem / d if d > 0 else 0.0
                cx, cy = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
                break
            rem -= d
        half = hmax * (math.sin(math.pi * s / L) ** power)
        px = int(round(cx))
        lo = int(math.floor(cy - half - 0.4))
        hi = int(math.ceil(cy + half + 0.4))
        for yy in range(lo, hi + 1):
            if abs(yy - cy) <= half + 0.4:
                c.set(px, yy, colour)
        s += step

# ------------------------------------------------------------------ 4. afterimages
stamp(result, sprite, DX - 36, DY, 58)      # oldest, faintest, furthest behind
stamp(result, sprite, DX - 18, DY, 112)

# ------------------------------------------------------------------ 5. white slash effect
tx, ty = DX + TIPX, DY + TIPY
# centreline: starts on the edge bevel (hidden by the blade), blooms past the tip
rel = [(-26, 11.0), (-13, 4.6), (0, 0.0), (15, -3.6), (30, -5.9), (44, -7.2)]
pts = [(tx + a, ty + b) for a, b in rel]
draw_streak(result, pts, 3.8, (204, 211, 248, 64))     # soft halo
draw_streak(result, pts, 2.5, (222, 232, 255, 136))    # mid glow
draw_streak(result, pts, 1.45, (255, 255, 255, 238), power=0.45)   # white core
# two fading streaks continuing past the slash tip
result.line(248, 53, 252, 53, (255, 255, 255, 118))
result.line(249, 57, 252, 57, (255, 255, 255, 76))

# ------------------------------------------------------------------ 6. the knife itself
result.blit(sprite, DX, DY)

# ------------------------------------------------------------------ 7. inspect
def coarse(c, x0, x1, y0, y1, sx=3, sy=2):
    for y in range(y0, y1, sy):
        row = ""
        for x in range(x0, x1, sx):
            row += "." if c.get(x, y) == 0 else "#"
        print("y=%3d %s" % (y, row))

print(result.stats_text())
print("--- silhouette (1 char = 3x2 px) ---")
coarse(result, 0, 256, 40, 88)
print("--- slash region ---")
print(result.matrix_text(region=(190, 44, 255, 74)))

finish(result)
