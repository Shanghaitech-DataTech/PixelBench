lc = load("exports/seaside.pixelart.json", add=False)
crop = new_canvas(56, 32, name="crop")
crop.blit(lc, -56, -100)
view(crop, scale=8, margin=0)
