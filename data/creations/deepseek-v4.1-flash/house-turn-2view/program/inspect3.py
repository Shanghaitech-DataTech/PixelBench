c = input_canvas
W, H = 112, 157
same = 0
diff = 0
for y in range(H):
    for x in range(W):
        a = c.get(x, y)
        b = c.get(W - 1 - x, y)
        if a == b:
            same += 1
        else:
            diff += 1
print('mirror symmetry same/diff', same, diff)

# also check half-turn symmetry about y center
same = diff = 0
for y in range(H):
    for x in range(W):
        if c.get(x, y) == c.get(W - 1 - x, H - 1 - y):
            same += 1
        else:
            diff += 1
print('180 symmetry', same, diff)

# find bbox per row of visible pixels
for y in range(0, H, 3):
    xs = [x for x in range(W) if c.get(x, y) != 0]
    if xs:
        print(y, min(xs), max(xs), len(xs))
