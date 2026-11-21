from pixelbench_api import new_canvas, finish

W = H = 32
c = new_canvas(W, H)

dark = c.color('#143b10')   # outline dark green
shadow = c.color('#2f6b1f')# shadow green
mid = c.color('#5aa73b')   # main green
light = c.color('#93d05e') # light green
hl = c.color('#cceba5')   # highlight
brown = c.color('#7a4a21')# stem

# pear silhouette: y -> (left, right) inclusive
edges = {
    4: (14, 17), 5: (13, 18), 6: (12, 19), 7: (11, 20), 8: (10, 21),
    9: (9, 22), 10: (9, 22), 11: (8, 23), 12: (7, 24), 13: (6, 25),
    14: (6, 25), 15: (5, 26), 16: (5, 26), 17: (5, 26), 18: (5, 26),
    19: (4, 27), 20: (4, 27), 21: (4, 27), 22: (5, 26), 23: (5, 26),
    24: (6, 25), 25: (7, 24), 26: (8, 23), 27: (10, 21), 28: (12, 19),
    29: (14, 17), 30: (15, 16),
}

for y, (L, R) in edges.items():
    for x in range(L, R + 1):
        c.set(x, y, mid)
    # light band on the left (upper) side
    if y <= 16 and R - L >= 5:
        for x in range(L + 1, L + 3):
            c.set(x, y, light)
    # shadow just inside the right edge
    if R - L >= 3:
        c.set(R - 1, y, shadow)
    # dark outline
    c.set(L, y, dark)
    c.set(R, y, dark)

# highlight spot upper-left
for (hx, hy) in [(12, 7), (13, 7), (12, 8), (13, 8), (11, 9), (12, 9), (12, 10)]:
    c.set(hx, hy, hl)

# dimple where the stem meets the body
c.set(14, 5, shadow)
c.set(17, 5, shadow)

# stem
for sy in range(0, 4):
    c.set(15, sy, brown)
    c.set(16, sy, brown)
c.set(15, 4, brown)
c.set(16, 4, brown)

print(c.stats_text())
print(c.matrix_text(region=(4, 0, 27, 30)))
finish(c)
