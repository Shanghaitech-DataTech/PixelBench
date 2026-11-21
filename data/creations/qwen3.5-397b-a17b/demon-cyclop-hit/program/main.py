# Demon cyclops hit animation - 3 frames - debug view

W, H = 50, 45

c0 = input_canvas.color('#141b1b')
c1 = input_canvas.color('#ffe18d')
c2 = input_canvas.color('#adbc3a')
c3 = input_canvas.color('#74a334')
c4 = input_canvas.color('#c8966b')
c5 = input_canvas.color('#fce2cf')

f1 = new_canvas(W, H, name="frame1_original")
f1.blit(input_canvas, 6, 6)

f2 = new_canvas(W, H, name="frame2_recoil")
f2.blit(input_canvas, 6, 6)

# Clear original foot area
f2.clear(x=10, y=32, w=12, h=10)

# Draw lifted foot
f2.set(14, 32, c0)
f2.set(15, 32, c1)
f2.set(16, 32, c3)
f2.set(17, 32, c1)
f2.set(18, 32, c0)
f2.set(15, 31, c1)
f2.set(16, 31, c1)
f2.set(17, 31, c1)
f2.set(16, 30, c1)
f2.set(14, 31, c3)
f2.set(18, 31, c3)
f2.set(13, 30, c3)
f2.set(19, 30, c3)

# Clear eye and redraw with highlight at top
f2.clear(x=18, y=20, w=14, h=10)
for x in range(20, 29):
    f2.set(x, 21, c5)
f2.set(19, 22, c4)
f2.set(20, 22, c5)
f2.set(21, 22, c5)
for x in range(22, 28):
    f2.set(x, 22, c0)
f2.set(28, 22, c5)
f2.set(29, 22, c4)
f2.set(18, 23, c4)
f2.set(19, 23, c4)
f2.set(20, 23, c5)
for x in range(21, 29):
    f2.set(x, 23, c0)
f2.set(29, 23, c5)
f2.set(30, 23, c4)
f2.set(31, 23, c4)
f2.set(18, 24, c4)
f2.set(19, 24, c4)
for x in range(20, 30):
    f2.set(x, 24, c0)
f2.set(30, 24, c4)
f2.set(31, 24, c4)
f2.set(18, 25, c4)
for x in range(19, 30):
    f2.set(x, 25, c5)
f2.set(30, 25, c4)

# Open mouth
f2.clear(x=19, y=26, w=13, h=6)
for x in range(20, 31):
    f2.set(x, 27, c0)
    f2.set(x, 28, c0)
    f2.set(x, 29, c0)
for x in range(20, 31, 2):
    f2.set(x, 26, c1)

f3 = new_canvas(W, H, name="frame3_impact")
f3.blit(input_canvas, 6, 6)
for y in range(33):
    for x in range(37):
        idx = input_canvas.get(x, y)
        if idx is not None:
            pal = input_canvas.palette()
            orig_rgba = pal[idx]['rgba']
            r = min(255, orig_rgba[0] + 100)
            g = max(0, orig_rgba[1] - 30)
            b = max(0, orig_rgba[2] - 30)
            a = orig_rgba[3]
            tinted = input_canvas.color((r, g, b, a))
            f3.set(x + 6, y + 6, tinted)

# Show full frame 2
print("=== FRAME 2 FULL ===")
print(f2.matrix_text())

finish([f1, f2, f3])
