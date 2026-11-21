c = input_canvas.copy(name="output")

f2 = input_canvas.copy(name="frame2")
# clear wing regions (left x0..9, right x17..26)
f2.rect(0, 0, 10, 22, None)
f2.rect(17, 0, 10, 22, None)

d = "#432f53"
h = "#5c436f"
a = "#1d181e"
e = "#5f5f7b"

# left raised wing: tip up-left, membrane to shoulder
f2.poly([(1, 1), (9, 8), (8, 12), (6, 10), (5, 13), (3, 11), (1, 1)], d)
f2.poly([(1, 1), (9, 8), (8, 12), (6, 10), (5, 13), (3, 11)], a, fill=False)
# right wing mirrored
f2.poly([(25, 1), (17, 8), (18, 12), (20, 10), (21, 13), (23, 11), (25, 1)], d)
f2.poly([(25, 1), (17, 8), (18, 12), (20, 10), (21, 13), (23, 11)], a, fill=False)
# keep lower wing edges near body
f2.line(1, 1, 5, 13, a)
f2.line(25, 1, 21, 13, a)

print(f2.stats_text())
print(f2.matrix_text())

finish([c, f2])
