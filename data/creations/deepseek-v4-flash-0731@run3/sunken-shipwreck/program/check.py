from pixelbench_api import load

c = load('exports/c2.pixelart.json', add=False)
pal = c.palette()
def col(x, y):
    return pal[c.get(x, y)]['rgba']

print("left edge rows 28-50, cols 0-11:")
for y in range(28, 51):
    print(y, [col(x, y) for x in range(0, 12)])
print("mast area cols 18-30 rows 2-30:")
for y in range(2, 31):
    print(y, [col(x, y) for x in range(18, 31)])
