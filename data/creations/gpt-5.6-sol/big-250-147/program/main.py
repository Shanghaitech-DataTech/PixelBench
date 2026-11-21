# Convert the supplied dusk landscape into a clear, sunless noon scene.
output = input_canvas.copy(name="output")
pal = input_canvas.palette()

sky = [
    (48, 145, 211), (56, 153, 217), (65, 162, 222),
    (77, 173, 226), (91, 185, 229), (109, 196, 232),
    (130, 207, 235),
]
mountain = [
    (32, 62, 70), (42, 76, 82), (53, 91, 96),
    (68, 108, 111), (87, 126, 128), (109, 145, 146),
    (137, 165, 164),
]
forest = [
    (12, 35, 27), (17, 48, 34), (23, 61, 40),
    (31, 76, 46), (43, 91, 51), (59, 107, 58),
]

for y in range(147):
    for x in range(250):
        idx = input_canvas.get(x, y)
        r, g, b, a = pal[idx]["rgba"]
        lum = (3*r + 5*g + 2*b) // 10
        if idx <= 71:
            # The original sky, clouds, and sun become one uninterrupted blue sky.
            band = min(6, max(0, (y + 3) // 14))
            col = sky[band]
            # Restrained ordered texture keeps the original pixel-art character.
            if (x + 2*y) % 11 == 0 and band < 6:
                col = sky[band + 1]
        elif idx <= 170:
            # Cooler, brighter atmospheric perspective for the mountain layers.
            level = min(6, max(0, (lum - 42) // 18))
            col = mountain[level]
            if r > b + 22 and level < 6:
                col = mountain[level + 1]
        else:
            # Sunlit evergreen forest, still dark enough to retain its silhouettes.
            level = min(5, max(0, (lum - 18) // 14))
            col = forest[level]
        output.set(x, y, col)

# Clean the sky to the actual ridgeline; dusk haze used some terrain palette entries.
ridge = [(0, 99), (18, 89), (36, 84), (55, 76), (70, 80), (88, 94),
         (101, 99), (111, 84), (120, 71), (128, 76), (139, 78), (151, 81),
         (165, 72), (174, 63), (184, 58), (193, 64), (204, 73), (214, 78),
         (221, 69), (230, 76), (240, 89), (249, 97)]
for i in range(len(ridge) - 1):
    x0, y0 = ridge[i]
    x1, y1 = ridge[i + 1]
    for x in range(x0, x1 + 1):
        top = round(y0 + (y1 - y0) * (x - x0) / (x1 - x0))
        for y in range(top):
            band = min(6, max(0, (y + 3) // 14))
            col = sky[min(6, band + 1)] if (x + 2*y) % 11 == 0 else sky[band]
            output.set(x, y, col)

# A few small, high-altitude fair-weather streaks: no solar disc or glow.
cloud_hi = (205, 232, 240)
cloud_lo = (173, 217, 235)
output.rect(28, 29, 18, 2, cloud_lo)
output.rect(34, 27, 14, 2, cloud_hi)
output.rect(39, 26, 8, 1, cloud_hi)
output.rect(188, 20, 22, 2, cloud_lo)
output.rect(194, 18, 13, 2, cloud_hi)
output.rect(199, 17, 7, 1, cloud_hi)

view(output, scale=3, margin=0)
finish(output)
