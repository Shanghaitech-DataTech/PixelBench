src = open('main.py').read().split("print(f1.stats_text())")[0]
exec(src)

KNOWN = {
 (0,0,0,0):'  ',
}
pal = input_canvas.palette()
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for p in pal:
    KNOWN[tuple(p['rgba'])] = letters[p['index'] % 52]
# my drawn colours get fixed letters
for k, v in {'@':(0,0,0,0),'#':OU,'W':WOOD,'w':WOODL,'h':WOODH,'k':WOODD,'S':SKIN,'s':SKINL,'g':SAGE,'G':SAGEL,'I':STRW,'c':CREAM}.items():
    KNOWN[v] = k

def dump(c, x0, y0, x1, y1):
    print("     " + "".join(str(x % 10) for x in range(x0, x1 + 1)))
    print("     " + "".join(str((x // 10) % 10) for x in range(x0, x1 + 1)))
    rp = {p['index']: tuple(p['rgba']) for p in c.palette()}
    for y in range(y0, y1 + 1):
        row = ''
        for x in range(x0, x1 + 1):
            v = c.get(x, y)
            col = rp[v]
            row += KNOWN.get(col, '?') if v else '..'
        print("%3d  %s" % (y, row))

dump(f2, 10, 12, 50, 36)
print()
print("legend:", {v: k for k, v in KNOWN.items() if v.strip()})
