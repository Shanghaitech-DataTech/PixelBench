output = input_canvas.copy(name="output")
w, h, raw = input_canvas.to_rgba()

sky = ["#62b9df", "#69bee2", "#71c3e4", "#7ac8e6"]
mountain = ["#263f52", "#315369", "#3e667a", "#527f8d", "#719aa0", "#94b5b2"]
forest = ["#0d1b16", "#14271d", "#1b3525", "#274a31", "#386442"]
bark = ["#34271f", "#4b3829", "#654b33", "#80613e"]

ridge_points = [
    (0, 95), (18, 87), (55, 75), (69, 78), (82, 88), (101, 94),
    (118, 85), (126, 75), (145, 81), (161, 69), (173, 62), (190, 72),
    (203, 79), (213, 69), (222, 73), (249, 96),
]

def ridge_y(x):
    for (x0, y0), (x1, y1) in zip(ridge_points, ridge_points[1:]):
        if x <= x1:
            t = (x - x0) / (x1 - x0)
            return round(y0 + (y1 - y0) * t)
    return ridge_points[-1][1]

def rgb_at(x, y):
    i = (y * w + x) * 4
    return raw[i], raw[i + 1], raw[i + 2]

for y in range(h):
    for x in range(w):
        r, g, b = rgb_at(x, y)
        lum = (3 * r + 4 * g + b) // 8

        # A clean blue vault replaces the sunset clouds and the low sun.
        if y < ridge_y(x):
            # Noon sky is lighter toward the horizon, with only sparse,
            # low-contrast pixels to preserve the source's texture.
            band = min(3, y // 24)
            colour = sky[band]
            if ((x * 7 + y * 11) % 97 == 0) and 16 < y < 88:
                colour = sky[min(3, band + 1)]
        elif y < 108:
            # Daylit atmospheric perspective across the mountain layers.
            level = max(0, min(5, (lum - 30) // 24))
            colour = mountain[level]
            if (x + 2 * y) % 17 == 0 and level < 5:
                colour = mountain[level + 1]
        else:
            # Retain the original forest detail while translating its sunset
            # purples and reds into shaded foliage and sunlit bark.
            is_bark = r > b * 1.45 and r > g * 1.18 and lum > 40
            if is_bark:
                level = max(0, min(3, (lum - 34) // 20))
                colour = bark[level]
            else:
                level = max(0, min(4, (lum - 10) // 18))
                colour = forest[level]
                if y < 132 and (x + y) % 23 == 0 and level < 4:
                    colour = forest[level + 1]
        output.set(x, y, colour)

view(output, size=(750, 441), margin=0)
finish(output)
