c = input_canvas
groups = {
 'outline(1)':[1],
 'skin(24,28)':[24,28],
 'white(18,30)':[18,30],
 'silver(2,5,6,15,16)':[2,5,6,15,16],
 'gold(20,25,32,36,10)':[20,25,32,36,10],
 'pink(8,11,12,13,9)':[8,11,12,13,9],
 'skin2(34,35)':[34,35],
}
for name, idxs in groups.items():
    pts = [(x,y) for y in range(61) for x in range(43) if c.get(x,y) in idxs]
    print(name, len(pts))
    rows = {}
    for x,y in pts: rows.setdefault(y, []).append(x)
    for y in sorted(rows):
        print('  y%2d: %s' % (y, ','.join(str(v) for v in sorted(rows[y]))))
