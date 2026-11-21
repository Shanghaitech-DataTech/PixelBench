from pixelbench_api import new_canvas, finish

W = H = 16
c = new_canvas(W, H)

# Deterministic hash so the texture is computed per-pixel from (x, y) ->
# identical at the seam, hence perfectly seamless when tiled.
def hsh(x, y, s):
    h = (x * 374761393 + y * 668265263 + s * 0x9E3779B9) & 0xFFFFFFFF
    h = ((h ^ (h >> 13)) * 1274126177) & 0xFFFFFFFF
    h ^= h >> 16
    return (h & 0xFFFFFFFF) / 0xFFFFFFFF

# Minecraft-style dirt palette (7 colours, well under the 10 limit).
darkest  = (66, 41, 21)
darker   = (86, 54, 30)
dark     = (104, 68, 38)
base     = (125, 85, 48)
light    = (139, 98, 59)
lighter  = (154, 114, 72)
highlight= (169, 128, 83)

def tval(x, y):
    # fine granular noise + two coarse cluster scales
    f = hsh(x, y, 1)
    m = hsh(x // 2, y // 2, 2)
    g = hsh(x // 4, y // 4, 3)
    t = 0.50 + 0.34 * (f - 0.5) + 0.16 * (m - 0.5) + 0.08 * (g - 0.5)
    if t < 0.30: return darkest
    if t < 0.41: return darker
    if t < 0.52: return dark
    if t < 0.62: return base
    if t < 0.74: return light
    if t < 0.86: return lighter
    return highlight

for y in range(H):
    for x in range(W):
        c.set(x, y, tval(x, y))

print(c.stats_text())
print(c.matrix_text())

finish(c)
