src = open('main.py').read()
src = src.replace("save('magic-forest-cottage', c)", "pass").replace("finish(c)", "pass")
ns = {}
exec(compile(src, 'main.py', 'exec'), ns)
c = ns['c']

w, h, raw = c.to_rgba()

def lum(px):
    return 0.299 * px[0] + 0.587 * px[1] + 0.114 * px[2]

def hue_char(px):
    r, g, b, a = px[0], px[1], px[2], px[3]
    if a == 0:
        return '.'
    L = lum(px) / 255.0
    warm = r - b
    green = g - max(r, b) * 0.55
    if L > 0.80:
        return '@'
    if L > 0.55:
        return 'O' if warm > 30 else '+'
    if L > 0.35:
        if green > 12:
            return 'm'
        return 'o' if warm > 20 else '='
    if L > 0.18:
        if green > 10:
            return ','
        return '-' if warm > 10 else ':'
    return ' '

print('Coarse 64x64 (each cell = 2x2 px, brightest of block)')
for by in range(0, 128, 2):
    row = []
    for bx in range(0, 128, 2):
        best = None
        for dy in (0, 1):
            for dx in (0, 1):
                i = ((by + dy) * w + (bx + dx)) * 4
                px = raw[i:i + 4]
                if best is None or lum(px) > lum(best):
                    best = px
        row.append(hue_char(best))
    print(''.join(row))
