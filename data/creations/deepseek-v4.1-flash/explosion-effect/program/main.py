import math

# ---------------------------------------------------------------- palette
WHITE  = "#FFFFFF"
CREAM  = "#FFF8CC"
YELLOW = "#FFE94A"
GOLD   = "#FFC417"
ORANGE = "#FF9500"
DEEP   = "#FF6B00"
REDOR  = "#FF3B00"
RED    = "#DE1000"
DARKRED= "#9B0A00"
EMBER  = "#5C0500"

c = new_canvas(64, 64, background=None, name="result")

# ---------------------------------------------------------------- helper
def rnd(x, y, s):
    h = (x * 374761393 + y * 668265263 + s * 1442695041) & 0xFFFFFFFF
    h = ((h ^ (h >> 13)) * 1274126177) & 0xFFFFFFFF
    h = (h ^ (h >> 16)) & 0xFFFFFFFF
    return h / 0xFFFFFFFF

def put(x, y, col, x0, x1, y0, y1):
    if x0 <= x <= x1 and y0 <= y <= y1:
        c.set(x, y, col)


# ================================================================ FRAME 1
# compact, bright yellow fireball
def fireball(cx, cy, R=11.0, seed=11, x0=0, x1=31, y0=16, y1=47):
    for y in range(cy - 16, cy + 17):
        for x in range(cx - 16, cx + 17):
            dx, dy = x - cx, y - cy
            d = math.hypot(dx, dy)
            if d > R + 2.4:
                continue
            amp = 0.30 + 0.60 * (d / R)
            dd = d + (rnd(x, y, seed) * 2 - 1) * amp
            if dd <= R:
                if dd < 2.1:
                    col = WHITE
                elif dd < 3.4:
                    col = CREAM
                elif dd < 7.3:
                    col = YELLOW
                elif dd < 8.8:
                    col = GOLD
                elif dd < 9.9:
                    col = ORANGE
                elif dd < 10.6:
                    col = DEEP
                else:
                    col = REDOR
                put(x, y, col, x0, x1, y0, y1)
            else:
                # a few flickering flame licks just outside the rim
                if rnd(x, y, seed + 77) > 0.80 and d < R + 1.9:
                    put(x, y, DEEP if rnd(x, y, seed + 5) > 0.30 else ORANGE,
                        x0, x1, y0, y1)
    # hot highlight flecks inside the core so the yellow reads as fire
    for i in range(10):
        a = rnd(i, 3, seed + 21) * math.tau
        rr = 6.5 + rnd(i, 9, seed + 41) * 3.2
        px = int(round(cx + math.cos(a) * rr))
        py = int(round(cy + math.sin(a) * rr * 0.95))
        put(px, py, ORANGE if rnd(px, py, seed + 61) > 0.5 else GOLD, x0, x1, y0, y1)


# ================================================================ FRAME 2
# expanding orange-red blast with sparks
def blast(cx, cy, R=14.0, seed=27, x0=32, x1=63, y0=16, y1=47):
    for y in range(cy - 17, cy + 18):
        for x in range(cx - 17, cx + 18):
            dx, dy = x - cx, y - cy
            d = math.hypot(dx, dy)
            if d > R + 1.0:
                continue
            amp = 0.28 + 0.62 * (d / R)
            dd = d + (rnd(x, y, seed) * 2 - 1) * amp
            if dd > R:
                continue
            # dissipating ragged outer fringe
            if dd > 12.2:
                p = 1.0 - (dd - 12.2) / (R - 12.2 + 0.001)
                if rnd(x, y, seed + 13) > p * 0.90 + 0.10:
                    continue
            # lacy holes so the shell reads as gas, not a solid disc
            if dd > 7.4 and rnd(x, y, seed + 31) < 0.05 + 0.09 * (dd / R):
                continue
            # the old core is blown open: only hot debris in the middle
            if dd < 3.2 and rnd(x, y, seed + 53) < 0.55:
                continue
            if dd < 3.0:
                col = DEEP if rnd(x, y, seed + 57) > 0.45 else ORANGE
            elif dd < 4.8:
                col = GOLD
            elif dd < 8.0:
                col = DEEP
            elif dd < 10.5:
                col = REDOR
            elif dd < 12.2:
                col = RED
            else:
                col = DARKRED
            put(x, y, col, x0, x1, y0, y1)

    # ---- sparks flying out of the blast
    spark_cols = [YELLOW, GOLD, ORANGE, ORANGE, DEEP, DEEP, REDOR, RED]
    for i in range(34):
        a = rnd(i, 101, seed + 7) * math.tau
        rr = 12.0 + rnd(i, 202, seed + 9) * 3.0
        px = int(round(cx + math.cos(a) * rr))
        py = int(round(cy + math.sin(a) * rr))
        col = spark_cols[int(rnd(i, 303, seed + 17) * len(spark_cols)) % len(spark_cols)]
        put(px, py, col, x0, x1, y0, y1)
        # little tail towards the centre so streaks read as motion
        if rnd(i, 404, seed + 23) > 0.35:
            tx = int(round(cx + math.cos(a) * (rr - 1.1)))
            ty = int(round(cy + math.sin(a) * (rr - 1.1)))
            tail = {YELLOW: CREAM, GOLD: YELLOW, ORANGE: GOLD,
                    DEEP: ORANGE, REDOR: DEEP, RED: REDOR}.get(col, DEEP)
            put(tx, ty, tail, x0, x1, y0, y1)

    # ---- embers scattered beyond the shock front
    for i in range(14):
        a = rnd(i, 505, seed + 29) * math.tau
        rr = 13.0 + rnd(i, 606, seed + 37) * 2.0
        px = int(round(cx + math.cos(a) * rr))
        py = int(round(cy + math.sin(a) * rr))
        put(px, py, RED if rnd(i, 707, seed + 43) > 0.4 else DARKRED,
            x0, x1, y0, y1)


fireball(16, 32)
blast(48, 32)

print(c.stats_text())
print("--- FRAME 1 (x0-31, y16-47) ---")
print(c.matrix_text(region=(0, 16, 31, 47)))
print("--- FRAME 2 (x32-63, y16-47) ---")
print(c.matrix_text(region=(32, 16, 63, 47)))

save("explosion", c)
finish(c)
