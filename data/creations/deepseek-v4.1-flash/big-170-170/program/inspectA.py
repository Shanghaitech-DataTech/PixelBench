c = input_canvas
pal = {p['index']: p['rgba'] for p in c.palette()}
W, H = 170, 170
def cls(x, y):
    r, g, b, a = pal[c.get(x, y)]
    mx = max(r, g, b); mn = min(r, g, b)
    if mn > 190 and mx > 220: return 'W'
    if r > 95 and r > g+38 and r > b+30: return '#'
    if r > 60 and r > g+18 and r > b+14: return 'r'
    if g > 90 and g > r+14 and g > b+8: return 'G'
    if b > 110 and b > r+30 and g > 80: return 'C'
    if b > 100 and r > 80 and b > g+18: return 'P'
    if mx < 55: return '.'
    if mx < 75: return ':'
    if mx < 95: return '-'
    return '+'
x0, x1 = 0, 85
print("    " + "".join(str((x//10)%10) for x in range(x0, x1)))
print("    " + "".join(str(x%10) for x in range(x0, x1)))
for y in range(H):
    print("%3d " % y + "".join(cls(x, y) for x in range(x0, x1)))
