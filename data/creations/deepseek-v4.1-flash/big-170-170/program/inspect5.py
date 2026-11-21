c = input_canvas
pal = {p['index']: p['rgba'] for p in c.palette()}
W, H = 170, 170
def cat(x, y):
    r, g, b, a = pal[c.get(x, y)]
    mn = min(r, g, b); mx = max(r, g, b)
    if mn > 185: return 'W'
    if r > 200 and 120 < g < 205 and 70 < b < 185: return 'S'
    if mx > 140 and r > 130 and r > g*1.5 and r > b*1.5: return 'R'
    if mx > 120 and g > 95 and g > r*1.25 and g > b*1.15: return 'G'
    if mx > 150 and b > 110 and r > 95 and b > g*1.15: return 'P'
    if mx > 130 and b > 110 and g > 95 and b > r*1.3: return 'C'
    if mx > 150 and b > 150 and r < 100: return 'B'
    return '.'
# 2x2 blocks
out = []
for by in range(0, H, 2):
    row = ""
    for bx in range(0, W, 2):
        cs = [cat(bx+dx, by+dy) for dx in (0, 1) for dy in (0, 1)]
        nz = [x for x in cs if x not in '.B']
        row += (nz[0] if nz else ('.' if all(x == '.' for x in cs) else 'B'))
    out.append(row)
print("    " + "".join(str((i//10)%10) if i % 10 == 0 else ' ' for i in range(85)))
print("    " + "".join(str(i%10) for i in range(85)))
for i, r in enumerate(out):
    print("%3d " % (i*2) + r)
