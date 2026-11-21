from main import c

for y in range(0, 6):
    print(y, [c.get(x, y) for x in range(10, 23)])
print("spots:")
for x, y in [(29, 4), (2, 4), (13, 3), (18, 3), (29, 8), (27, 12), (25, 16), (24, 27)]:
    print((x, y), c.color_name(c.get(x, y)))
