# test rasterization rules
t = new_canvas(20, 12, background=None, name="t")
t.ellipse(10, 6, 6, 2, "#ff0000")
w, h, rgba = t.to_rgba()
for y in range(h):
    print("".join("." if rgba[(y * w + x) * 4 + 3] == 0 else "X" for x in range(w)))
print("---circle r=3---")
t2 = new_canvas(12, 12, background=None, name="t2")
t2.circle(6, 6, 3, "#ff0000")
w, h, rgba = t2.to_rgba()
for y in range(h):
    print("".join("." if rgba[(y * w + x) * 4 + 3] == 0 else "X" for x in range(w)))
print("---poly diamond---")
t3 = new_canvas(12, 12, background=None, name="t3")
t3.poly([(6, 2), (10, 6), (6, 10), (2, 6)], "#ff0000")
w, h, rgba = t3.to_rgba()
for y in range(h):
    print("".join("." if rgba[(y * w + x) * 4 + 3] == 0 else "X" for x in range(w)))
