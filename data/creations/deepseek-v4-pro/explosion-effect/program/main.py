import math

W, H = 64, 64
c = new_canvas(W, H, background=None, name="explosion")

# Register a small, coherent palette (well under the 86-colour limit).
white      = c.color((255, 255, 255), "white")
pale_y     = c.color((255, 255, 180), "pale_yellow")
bright_y   = c.color((255, 255,   0), "bright_yellow")
golden     = c.color((255, 200,   0), "golden")
orange     = c.color((255, 140,   0), "orange")
orange_red = c.color((255,  60,   0), "orange_red")
red        = c.color((215,  30,   0), "red")
dark_red   = c.color((140,  15,   0), "dark_red")
spark_y    = c.color((255, 235, 110), "spark_yellow")


def star_points(cx, cy, r_out, r_in, n=12):
    """A simple, non-self-crossing burst polygon (gear/flower shape)."""
    pts = []
    for i in range(2 * n):
        ang = math.pi * i / n
        r = r_out if i % 2 == 0 else r_in
        pts.append((round(cx + r * math.cos(ang)), round(cy + r * math.sin(ang))))
    return pts


def draw_fireball(canvas, cx, cy):
    """Frame 1: bright yellow fireball."""
    canvas.circle(cx, cy, 10, golden)
    canvas.circle(cx, cy, 8, bright_y)
    canvas.circle(cx, cy, 5, pale_y)
    canvas.circle(cx, cy, 2, white)
    # Short flame licks around the rim.
    for ang_deg in range(0, 360, 30):
        ang = math.radians(ang_deg)
        for r, col in ((11, golden), (12, bright_y)):
            x = round(cx + r * math.cos(ang))
            y = round(cy + r * math.sin(ang))
            canvas.set(x, y, col)


def draw_blast(canvas, cx, cy):
    """Frame 2: expanding orange-red blast with sparks."""
    # Layered jagged burst: dark red tips -> red -> orange-red -> orange -> core.
    canvas.poly(star_points(cx, cy, 15, 11), dark_red, fill=True)
    canvas.poly(star_points(cx, cy, 13, 9), red, fill=True)
    canvas.circle(cx, cy, 10, orange_red)
    canvas.circle(cx, cy, 8, orange)
    canvas.circle(cx, cy, 5, golden)
    canvas.circle(cx, cy, 3, pale_y)
    canvas.circle(cx, cy, 1, white)

    # Sparks flying outward (angle deg, radius, colour).
    sparks = [
        (10, 14, white), (25, 16, spark_y), (45, 18, white),
        (65, 19, orange), (85, 18, spark_y), (105, 17, white),
        (125, 16, orange), (145, 15, spark_y), (165, 15, white),
        (185, 16, orange), (205, 17, spark_y), (225, 18, white),
        (245, 19, orange), (265, 18, spark_y), (285, 17, white),
        (305, 16, orange), (325, 15, spark_y), (345, 14, white),
    ]
    for ang_deg, r, col in sparks:
        ang = math.radians(ang_deg)
        # Two-pixel streak: base then tip.
        for rr in (r - 1, r):
            x = round(cx + rr * math.cos(ang))
            y = round(cy + rr * math.sin(ang))
            canvas.set(x, y, col)


# Two-frame animation strip on one 64x64 canvas:
# frame 1 in the left half, frame 2 in the right half.
draw_fireball(c, 16, 32)
draw_blast(c, 48, 32)

print(c.stats_text())
print("--- frame 1 ---")
print(c.matrix_text(region=(2, 18, 30, 46)))
print("--- frame 2 ---")
print(c.matrix_text(region=(32, 8, 63, 56)))

finish(c)
