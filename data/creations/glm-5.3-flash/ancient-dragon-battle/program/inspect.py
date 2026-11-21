ns = {}
exec(open('main.py').read(), ns)
result = ns['result']

w, h, idx, pal = result.to_indexed()

RAMP = " .:-=+*#%@"
print("LUMINANCE MAP (each char = 4x4 px block, dark -> bright):")
for by in range(0, h, 4):
    row = []
    for bx in range(0, w, 4):
        rs = gs = bs = n = 0
        for y in range(by, by + 4):
            for x in range(bx, bx + 4):
                r, g, b, a = pal[idx[y * w + x]]
                rs += r; gs += g; bs += b; n += 1
        lum = (0.3 * rs + 0.55 * gs + 0.15 * bs) / n / 255.0
        row.append(RAMP[min(9, int(lum * 10))])
    print("".join(row))

CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&*+-/<>?@^~"


def dump(name, x0, y0, x1, y1):
    print("=" * 20, name, (x0, y0, x1, y1))
    seen = {}
    for y in range(y0, y1 + 1):
        line = []
        for x in range(x0, x1 + 1):
            i = idx[y * w + x]
            if i not in seen:
                seen[i] = CHARS[len(seen) % len(CHARS)]
            line.append(seen[i])
        print("".join(line))
    print("legend:")
    for i, ch in sorted(seen.items(), key=lambda kv: kv[1]):
        r, g, b, a = pal[i]
        print(f"  {ch} = #{r:02x}{g:02x}{b:02x}")


dump("LEFT TOWER + KNIGHTS", 50, 40, 100, 105)
dump("SIEGE TOWER LEFT", 0, 130, 70, 200)
