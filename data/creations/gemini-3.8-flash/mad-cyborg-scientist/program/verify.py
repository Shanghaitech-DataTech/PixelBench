import main

c, pal = main.draw_portrait.build_portrait()
stats = c.stats()
print("Colors used:", stats["colors_used"])
print("Visible pixels:", stats["visible_pixels"])
print("Size:", stats["size"])
assert stats["colors_used"] <= 86, f"Too many colors: {stats['colors_used']}"
assert stats["size"] == [64, 64], f"Wrong size: {stats['size']}"
print("All assertions passed!")
