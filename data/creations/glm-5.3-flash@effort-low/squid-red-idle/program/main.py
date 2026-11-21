inp = input_canvas.copy(name="orig")
W, H = 58, 59

f1 = new_canvas(W, H, name="frame1")
f1.blit(inp, 0, 1)

f2 = f1.copy(name="frame2")
f2.shift(0, -1)

f3 = f1.copy(name="frame3")
f3.shift(0, 1)

print(f1.stats_text(), f2.stats_text(), f3.stats_text())
finish([f1, f2, f3])
