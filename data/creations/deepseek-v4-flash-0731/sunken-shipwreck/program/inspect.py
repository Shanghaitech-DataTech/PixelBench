from pixelbench_api import load, canvas
c = load("exports/shipwreck.png", add=False)
# print several regions
print(c.matrix_text(region=(0,0,31,31), indices=False))
