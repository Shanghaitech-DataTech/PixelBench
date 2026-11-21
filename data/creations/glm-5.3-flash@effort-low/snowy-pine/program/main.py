out = input_canvas.copy(name='output')
W, H = 82, 135
SNOW = out.color('#eef4f8', name='snow')
SHADE = out.color('#b9cbdb', name='snow_shade')

foliage = {out.color('#317266'), out.color('#3d997a'), out.color('#213138'), out.color('#2d5656')}

def idx(x, y):
    return out.get(x, y)

def is_fol(x, y):
    if 0 <= x < W and 0 <= y < H:
        return idx(x, y) in foliage
    return False

def is_open(x, y):
    if 0 <= x < W and 0 <= y < H:
        p = idx(x, y)
        return p is None or p == 0
    return True

# pass 1: exposed tops -> snow
tops = []
for y in range(H):
    for x in range(W):
        if is_fol(x, y) and is_open(x, y - 1):
            tops.append((x, y))
for x, y in tops:
    out.set(x, y, SNOW)
    if is_fol(x, y + 1):
        out.set(x, y + 1, SNOW)

# pass 2: thicken — snow pixel with foliage left/right/up spreads sideways
changed = True
while changed:
    changed = False
    for y in range(H):
        for x in range(W):
            if idx(x, y) in foliage:
                nb = 0
                for dx, dy in ((-1, 0), (1, 0), (0, -1)):
                    if 0 <= x + dx < W and 0 <= y + dy < H and idx(x + dx, y + dy) == SNOW:
                        nb += 1
                if nb >= 2 and (is_open(x, y - 1) or is_open(x - 1, y) or is_open(x + 1, y)):
                    out.set(x, y, SNOW)
                    changed = True

# shade: bottom edge of snow patches that sits on foliage
for y in range(H - 1, -1, -1):
    for x in range(W):
        if idx(x, y) == SNOW and is_fol(x, y + 1) and is_open(x, y - 1):
            out.set(x, y + 1, SHADE)

print(out.stats_text())
print(out.matrix_text(region=(30, 0, 82, 30)))
save('snowy-pine', out)
finish(out)