W, H = 27, 31
DY = 9  # original art sits low, leaving headroom for raised wings

# Frame 1: original content, taller canvas
f1 = new_canvas(W, H, name="frame1")
f1.blit(input_canvas, 0, DY)

# Frame 2: wings flipped upward into a raised spread, body/head unchanged
f2 = f1.copy(name="frame2")
f2.clear(0, DY + 6, 9, 16)
f2.clear(18, DY + 6, 9, 16)

f1.select(0, DY + 6, 9, 16).flip("v").copy_to(0, DY - 9, f2, mode="over")
f1.select(18, DY + 6, 9, 16).flip("v").copy_to(18, DY - 9, f2, mode="over")

view(f1)
view(f2)
finish([f1, f2])
