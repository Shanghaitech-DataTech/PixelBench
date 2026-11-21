c = canvas(-1)
# check bow/string pixels
for y in range(15, 36):
    row = ''.join('#' if c.get(x,y) not in (0, None) and c.color_name(c.get(x,y)) in ('#8a5a2b','#5e3a17','#121311','#c5956a','#7b4231') else '.' for x in range(0,35))
    print(f"{y:2d} {row}")
