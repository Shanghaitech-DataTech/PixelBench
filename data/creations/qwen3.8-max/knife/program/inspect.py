c = input_canvas
print(c.stats_text())
print(c.size if hasattr(c, "size") else "")
print(c.matrix_text())
