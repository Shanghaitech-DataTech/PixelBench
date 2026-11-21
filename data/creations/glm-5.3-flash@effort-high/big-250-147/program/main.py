# Task: convert the sunset city scene to noon on a clear day.
# The input has a pink/magenta sunset sky with a low sun disc + halo around
# (124, 36) above a dark city skyline. At noon the sun is overhead (not in
# frame), so we repaint the whole sky region (everything above the per-column
# skyline of dark building pixels) with a clear blue gradient, which removes
# the sun disc and its glow. Buildings below the skyline are left untouched.

out = input_canvas.copy(name='output')
W, H = 250, 147

# 1) find skyline: first dark (building) pixel per column
first_dark = [H] * W
Wd, Hd, data = input_canvas.to_rgba()
for x in range(W):
    for y in range(Hd):
        i = (y * Wd + x) * 4
        r, g, b, a = data[i:i + 4]
        if a and max(r, g, b) < 120:
            first_dark[x] = y
            break

# 2) repaint sky with a clear-day blue gradient (lighter toward the horizon)
TOP = (106, 156, 224)   # deeper blue high up
BOT = (156, 202, 240)   # paler blue near the horizon

for x in range(W):
    ylimit = first_dark[x]
    for y in range(ylimit):
        t = min(1.0, y / 64.0)
        r = TOP[0] + (BOT[0] - TOP[0]) * t
        g = TOP[1] + (BOT[1] - TOP[1]) * t
        b = TOP[2] + (BOT[2] - TOP[2]) * t
        # keep a hint of the original dithered texture
        n = ((x * 13 + y * 7) % 7) - 3
        out.set(x, y, (int(r) + n, int(g) + n, int(b) + n))

print(out.stats_text())
finish(out)
