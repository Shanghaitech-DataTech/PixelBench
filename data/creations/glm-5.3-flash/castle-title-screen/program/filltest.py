import pixelbench_api as api

# Test A: bottom vertex at y=10 on a 12-high canvas
t = api.new_canvas(12, 12, None, "tA")
t.poly([(2, 10), (9, 4), (9, 10)], "#ff0000")
print("A: poly bottom edge y=10 ->")
print(t.matrix_text(region=(0, 0, 11, 11)))

# Test B: bottom vertex at y=12 (out of bounds by 1)
t2 = api.new_canvas(12, 12, None, "tB")
t2.poly([(2, 12), (9, 4), (9, 12)], "#ff0000")
print("B: poly bottom edge y=12 (OOB) ->")
print(t2.matrix_text(region=(0, 0, 11, 11)))
