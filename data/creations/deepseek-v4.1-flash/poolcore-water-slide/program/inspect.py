from pixelbench_api import *

c = load('exports/result.pixelart.json', add=False)

# coarse map: 2x2 downsample -> 64x64
pal = c.palette()
idx2ch = {}
chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*+-=~?/\\|<>"
n = 0
for p in pal:
    idx2ch[p['index']] = chars[n % len(chars)]
    n += 1

print("coarse 2x2 (col=2px,row=2px)")
hdr = '    ' + ''.join(str((x // 2) % 10) for x in range(0, 128, 2))
print(hdr)
for y in range(0, 128, 2):
    row = []
    for x in range(0, 128, 2):
        i = c.get(x, y)
        ch = idx2ch.get(i, '?')
        if c.get(x, y) == 0 and pal[0]['rgba'][3] == 0:
            ch = '.'
        row.append(ch)
    print(f'{y:3d} ' + ''.join(row))

print()
print("legend:")
for p in pal:
    r, g, b, a = p['rgba']
    print(f"  {idx2ch[p['index']]} {p['index']:3d} {p['name']:<10} #{r:02x}{g:02x}{b:02x} a={a}")
