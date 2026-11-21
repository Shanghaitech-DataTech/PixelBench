from pixelbench_api import load
c = load("exports/standoff.pixelart.json", add=False)
print("== KNIGHT (8,52)-(48,114) ==")
print(c.matrix_text(region=(8, 52, 48, 114)))
print("== ROGUE (82,65)-(118,114) ==")
print(c.matrix_text(region=(82, 65, 118, 114)))
