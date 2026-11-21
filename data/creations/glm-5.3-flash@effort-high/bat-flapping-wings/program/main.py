W, H = 27, 22

# ---- Frame 1: exact copy of the input (bat with drooping wings) ----
f1 = input_canvas.copy(name='frame1')

# ---- Frame 2: same bat, wings flapped up into a raised, spread position ----
f2 = input_canvas.copy(name='frame2')

# erase the drooping wings (keep the inner junction column x9 / x17)
f2.rect(0, 6, 9, 16, None)    # x0..8, y6..21
f2.rect(18, 6, 9, 16, None)   # x18..26, y6..21

A  = input_canvas.color('#1d181e')   # dark outline
D  = input_canvas.color('#432f53')   # wing membrane
Hc = input_canvas.color('#5c436f')   # wing shading
C  = input_canvas.color('#b572b1')   # highlight

# ---- left raised wing: tip up-left, broad membrane down to the body ----
pts = [(2, 1), (7, 5), (8, 7), (8, 12), (6, 11), (4, 11), (2, 9), (0, 7), (0, 4)]
f2.poly(pts, D)
f2.poly(pts, A, fill=False)          # closed outline
# leading-edge highlight along the raised arm
f2.set(2, 2, C); f2.set(3, 3, C); f2.set(4, 4, C); f2.set(5, 5, C)
# membrane shading near the body
f2.set(7, 9, Hc); f2.set(7, 10, Hc); f2.set(6, 9, Hc); f2.set(7, 8, Hc)

# ---- right wing = mirror of the left ----
for y in range(H):
    for x in range(0, 10):
        idx = f2.get(x, y)
        if idx:
            f2.set(26 - x, y, idx)

print("FRAME1:", f1.stats_text())
print("FRAME2:", f2.stats_text())
print(f2.matrix_text())

finish([f1, f2])
