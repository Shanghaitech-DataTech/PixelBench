import numpy as np

# Create an editable copy of input_canvas
output = input_canvas.copy(name='output')
stats = output.stats()
w, h = stats['size']

palette = input_canvas.palette()
pal_dict = {p['index']: p['rgba'] for p in palette}

orig_rgba = np.zeros((h, w, 4), dtype=np.uint8)
for y in range(h):
    for x in range(w):
        orig_rgba[y, x] = pal_dict[input_canvas.get(x, y)]

# 1. Determine the mountain skyline for each column x
skyline_y = np.zeros(w, dtype=int)
for x in range(w):
    found = False
    for y in range(45, h):
        r, g, b, _ = orig_rgba[y, x]
        # Dark mountain ridges have b >= 48 and r < 105 and g < 65
        # Pink mountain peak has y >= 65 and r > 180 and g < 135 and b >= 48
        if b >= 48:
            if (r < 105 and g < 65) or (y >= 65 and r > 180 and g < 135):
                skyline_y[x] = y
                found = True
                break
    if not found:
        skyline_y[x] = 80

# Smooth out any 1-pixel noise in skyline if any
for x in range(1, w - 1):
    if abs(skyline_y[x] - skyline_y[x-1]) > 5 and abs(skyline_y[x] - skyline_y[x+1]) > 5:
        skyline_y[x] = (skyline_y[x-1] + skyline_y[x+1]) // 2

# 2. Define clear day noon sky colors (zenith blue to horizon pale blue)
sky_palette = [
    np.array([46, 102, 180]),   # Tone 0: Deep zenith blue
    np.array([56, 118, 196]),   # Tone 1
    np.array([70, 134, 210]),   # Tone 2
    np.array([86, 152, 224]),   # Tone 3
    np.array([106, 170, 236]),  # Tone 4
    np.array([128, 186, 244]),  # Tone 5
    np.array([152, 202, 250]),  # Tone 6
    np.array([176, 216, 254]),  # Tone 7: Pale horizon sky
]

max_sky_y = 100.0

# 3. Mountain color mapping dictionary for exact dusk colors
mountain_color_map = {
    # Pink lit slope -> sunlit midday mountain peak
    (212, 122, 132): (214, 228, 246),
    (204, 118, 132): (196, 214, 236),
    (188, 114, 132): (178, 198, 224),
    (180, 114, 140): (170, 192, 220),
    (172, 110, 140): (162, 184, 214),

    # Distant mountain shadow slopes
    (84, 46, 68): (112, 134, 162),
    (76, 46, 68): (100, 122, 150),
    (68, 42, 68): (88, 110, 138),

    # Closer mountain ridges and highlights
    (84, 46, 76): (88, 112, 140),
    (76, 46, 76): (76, 98, 124),
    (76, 42, 68): (72, 94, 120),

    # Closer mountain shadow slopes
    (52, 34, 60): (54, 72, 94),
    (52, 30, 52): (48, 64, 84),
    (44, 34, 60): (44, 60, 80),
    (44, 30, 52): (38, 52, 70),
    (44, 34, 52): (40, 54, 72),
    (52, 34, 52): (50, 66, 86),
}

# 4. Process each pixel and set output canvas
for y in range(h):
    for x in range(w):
        r, g, b, a = orig_rgba[y, x]

        # Is this pixel in the sky?
        if y < skyline_y[x]:
            # Sky gradient
            pos = (y / max_sky_y) * (len(sky_palette) - 1)
            pos = max(0.0, min(float(len(sky_palette) - 1), pos))
            idx = int(pos)
            frac = pos - idx
            if idx >= len(sky_palette) - 1:
                color = sky_palette[-1]
            else:
                # 2-pixel checkerboard dithering between gradient bands
                if frac > 0.5:
                    color = sky_palette[idx + 1] if ((x + y) % 2 == 0 or frac > 0.8) else sky_palette[idx]
                else:
                    color = sky_palette[idx + 1] if ((x + y) % 2 == 0 and frac > 0.2) else sky_palette[idx]

            output.set(x, y, (int(color[0]), int(color[1]), int(color[2]), 255))

        else:
            # Below skyline: Mountains or Trees
            if b >= 48:
                # Mountain region
                key = (int(r), int(g), int(b))
                if key in mountain_color_map:
                    mc = mountain_color_map[key]
                else:
                    # General mountain mapping: cool daylight slate blue
                    if r > 160 and g > 100:
                        # Sunlit rock/snow
                        lum = (r + g + b) / 3.0
                        mc = (int(lum * 0.95), int(lum * 1.02), int(min(255, lum * 1.12)))
                    else:
                        # Shadow mountain slope
                        lum = 0.299 * r + 0.587 * g + 0.114 * b
                        mc = (int(lum * 0.8 + 10), int(lum * 1.1 + 22), int(lum * 1.4 + 32))

                output.set(x, y, (int(mc[0]), int(mc[1]), int(mc[2]), 255))

            else:
                # Forest / Trees region (b < 48)
                if r <= 32:
                    # Deep evergreen pine shadow
                    tc = (14 + int(r * 0.2), 26 + int(r * 0.3), 18 + int(b * 0.3))
                else:
                    # Pine foliage illuminated by midday noon sun
                    # r ranges from ~35 to ~120
                    t = max(0.0, min(1.0, (r - 35) / 85.0))
                    # Midday sunlit pine green
                    tc = (
                        int(22 + t * 68),
                        int(42 + t * 108),
                        int(24 + t * 56)
                    )

                output.set(x, y, (int(tc[0]), int(tc[1]), int(tc[2]), 255))

view(output)
finish(output)
