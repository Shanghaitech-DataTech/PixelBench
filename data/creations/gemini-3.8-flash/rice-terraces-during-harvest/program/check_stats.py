from main import build_scene

c = build_scene()
stats = c.stats()
print("Stats:", stats["size"], "Colors used:", stats["colors_used"])
