from pixelbench_api import load

c = load("/workspace/exports/public-transport-icons.pixelart.json", add=False)
for i, (x0, y0) in enumerate([(1, 1), (33, 1), (1, 33), (33, 33)]):
    print("=== tile", i, "at", x0, y0, "===")
    print(c.matrix_text(region=(x0, y0, x0 + 29, y0 + 29)))
