from pixelbench_api import load, canvas

c = load("exports/battle.pixelart.json", add=False)
print("=== DRAGON HEAD REGION (98..178, 28..74) ===")
print(c.matrix_text(region=(98, 28, 178, 74)))
