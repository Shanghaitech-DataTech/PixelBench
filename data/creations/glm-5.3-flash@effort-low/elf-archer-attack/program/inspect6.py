c = canvas(-1)
targets = {c.color(spec) for spec in ('#8a5a2b','#5e3a17','#121311','#c5956a','#7b4231')}
print(targets)
for y in range(15, 36):
    row = ''.join('#' if c.get(x,y) in targets else '.' for x in range(0,35))
    print(f"{y:2d} {row}")
