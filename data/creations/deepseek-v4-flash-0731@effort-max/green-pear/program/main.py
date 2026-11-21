from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

OUT = "#1b5e20"    # dark green outline
MAIN = "#4caf50"   # main green
LIGHT = "#a5d6a7"  # light green
SPEC = "#c8e6c9"   # pale highlight
SHADE = "#2e7d32"  # shade green
STEM = "#6d4c41"   # brown stem
STEMD = "#3e2723"  # dark brown stem outline


def in_pear(x, y):
    u = ((x - 16) / 4.3) ** 2 + ((y - 9.5) / 5.0) ** 2 <= 1.0   # upper neck bulb
    l = ((x - 16) / 8.9) ** 2 + ((y - 18.5) / 9.6) ** 2 <= 1.0  # big lower bulb
    return u or l


inside = [[in_pear(x, y) for x in range(32)] for y in range(32)]

for y in range(32):
    for x in range(32):
        if inside[y][x]:
            c.set(x, y, MAIN)


def is_out(x, y):
    if not inside[y][x]:
        return True
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if not (0 <= nx < 32 and 0 <= ny < 32) or not inside[ny][nx]:
            return True
    return False


# body outline
for y in range(32):
    for x in range(32):
        if inside[y][x] and is_out(x, y):
            c.set(x, y, OUT)

# shading + highlights
for y in range(32):
    for x in range(32):
        if not inside[y][x] or is_out(x, y):
            continue
        if x >= 15.5 and ((x - 17.8) / 5.5) ** 2 + ((y - 21.0) / 7.2) ** 2 <= 1.0:
            c.set(x, y, SHADE)
            continue
        if ((x - 12.3) / 4.0) ** 2 + ((y - 14.0) / 4.3) ** 2 <= 1.0:
            c.set(x, y, LIGHT)
        if ((x - 12.6) / 1.4) ** 2 + ((y - 13.3) / 1.4) ** 2 <= 1.0:
            c.set(x, y, SPEC)

# stem (rows 1-4, 3 wide)
stem = set((x, y) for y in range(1, 5) for x in range(15, 18))

def stem_out(x, y):
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if (x + dx, y + dy) not in stem:
            return True
    return False

for x, y in stem:
    c.set(x, y, STEMD if stem_out(x, y) else STEM)

print(c.stats_text())
print(c.matrix_text())

finish(c)
