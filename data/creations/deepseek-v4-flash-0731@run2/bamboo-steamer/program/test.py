from pixelbench_api import *

t = new_canvas(32, 24, name="test")
r = t.color("#FF0000", "red")
g = t.color("#00FF00", "green")
b = t.color("#0000FF", "blue")

t.ellipse(10, 12, 6, 3, r)
t.ellipse(10, 12, 6, 3, g, fill=False)
t.ellipse(16, 12, 3, 6, b)

print(t.matrix_text())
print(t.stats_text())
print("DONE")
