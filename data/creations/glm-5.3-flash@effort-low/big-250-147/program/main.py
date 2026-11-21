import numpy as np

c = input_canvas.copy(name='output')
w, h = 250, 147

# --- Recolour the sky region (top ~62 rows) from pink sunset to clear noon blue,
#     which also erases the low sun disc.
W, H, rgba = c.to_rgba()
a = np.frombuffer(rgba, dtype=np.uint8).reshape(H, W, 4).copy()

SKY_TOP = np.array([86, 146, 232], dtype=float)   # deep clear blue
SKY_LOW = np.array([168, 208, 245], dtype=float)  # paler near horizon
SUN_LIT = np.array([205, 228, 250], dtype=float)  # bright haze where the sun was

for y in range(62):
    t = y / 61.0
    base = SKY_TOP * (1 - t) + SKY_LOW * t
    row = a[y, :, :3].astype(float)
    lum = 0.3 * row[:, 0] + 0.6 * row[:, 1] + 0.1 * row[:, 2]
    # how "sunlit" a pixel was (bright pink/white glow) -> soft bright haze
    glow = np.clip((lum - 120) / 90.0, 0, 1) ** 1.5
    col = base[None, :] * (1 - glow[:, None]) + SUN_LIT[None, :] * glow[:, None]
    a[y, :, :3] = np.clip(col, 0, 255).astype(np.uint8)

# write recoloured sky back through the palette-free rgba path
c2 = c.copy(name='tmp')
from pixelbench_api import new_canvas
out = new_canvas(w, h, name='output')
out2 = out  # placeholder
# Rebuild: easier to set pixels directly on the copy via numpy-backed canvas
# Use the canvas API: clear top region then stamp recoloured pixels
for y in range(62):
    for x in range(w):
        r, g, b = a[y, x, :3]
        c.set(x, y, '#%02x%02x%02x' % (r, g, b))

# --- A few crisp white cumulus clouds for a clear midday sky
cloud = new_canvas(60, 18, name='cloud')
cloud.ellipse(14, 12, 13, 6, '#ffffff')
cloud.ellipse(30, 9, 12, 7, '#ffffff')
cloud.ellipse(46, 12, 12, 5, '#ffffff')
cloud.ellipse(22, 7, 8, 5, '#ffffff')

c.blit(cloud, 20, 12)
c.blit(cloud, 150, 26)
c.blit(cloud, 88, 8)

result = c
print(result.stats_text())
finish(result)
