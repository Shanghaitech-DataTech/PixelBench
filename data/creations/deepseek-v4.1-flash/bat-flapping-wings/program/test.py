src = input_canvas.copy(name="src")
big = new_canvas(48, 40, name="test")
big.blit(src, 6, 12)
for ang in (90, 100, 110):
    s = big.select(6, 18, 9, 16)   # left drooping wing patch
    r = s.rotate(ang)
    p = r.preview()
    print("=== angle", ang, "patch size", r.size)
    print(p.matrix_text())
    print(p.stats_text())
