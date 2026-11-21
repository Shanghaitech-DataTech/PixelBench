from pixelbench_api import *

c = new_canvas(32, 32, name="usb")

# ---- palette ----
outline = c.color('#1a1a1e', name='outline')
metal = c.color('#c9cfd8', name='metal')
metal_hi = c.color('#e9edf3', name='metal_hi')
metal_sh = c.color('#8d95a1', name='metal_sh')
connector = c.color('#d3d9e2', name='connector')
connector_sh = c.color('#9aa2ae', name='connector_sh')
tongue = c.color('#e0ddd2', name='tongue')
hole = c.color('#14161a', name='hole')
gold = c.color('#d4a83c', name='gold')
strap = c.color('#4a8ec9', name='strap')
led = c.color('#5fd98a', name='led')

# ---- keychain strap loop (oval fabric loop) ----
c.ellipse(16, 5, 4, 3, outline, fill=True)
c.ellipse(16, 5, 3, 2, strap, fill=True)
c.ellipse(16, 5, 2, 1, None, fill=True)

# ---- body: dark outline with rounded corners ----
c.rect(5, 8, 22, 14, outline)
for x, y in [(5, 8), (6, 8), (5, 9),
             (26, 8), (25, 8), (26, 9),
             (5, 21), (6, 21), (5, 20),
             (26, 21), (25, 21), (26, 20)]:
    c.set(x, y, None)

# ---- body: metal fill ----
c.rect(6, 9, 20, 12, metal)
for x, y in [(6, 9), (25, 9), (6, 20), (25, 20)]:
    c.set(x, y, None)

# ---- body: metallic shading ----
c.line(7, 9, 24, 9, metal_hi)     # top edge
c.line(7, 20, 24, 20, metal_sh)   # bottom edge
c.line(6, 10, 6, 19, metal_hi)    # left edge
c.line(7, 10, 7, 19, metal_hi)    # left bevel
c.line(24, 10, 24, 19, metal_sh)  # right bevel
c.line(25, 10, 25, 19, metal_sh)  # right edge

# ---- body: activity LED ----
c.rect(20, 11, 2, 2, led)

# ---- connector: dark outline (square top, rounded tip) ----
c.rect(10, 21, 12, 9, outline)
for x, y in [(10, 29), (11, 29), (10, 28),
             (21, 29), (20, 29), (21, 28)]:
    c.set(x, y, None)

# ---- connector: metal fill ----
c.rect(11, 22, 10, 7, connector)
c.set(11, 28, None)
c.set(20, 28, None)

# ---- connector: shading ----
c.line(11, 22, 20, 22, metal_hi)       # top edge
c.line(11, 23, 11, 27, metal_hi)       # left edge
c.line(20, 23, 20, 27, connector_sh)   # right edge
c.line(12, 28, 19, 28, connector_sh)   # bottom rim

# ---- connector: USB plug details (latch holes + tongue + contacts) ----
c.rect(12, 25, 2, 3, hole)   # left latch hole
c.rect(18, 25, 2, 3, hole)   # right latch hole
c.rect(14, 25, 4, 3, tongue) # plastic tongue
c.rect(14, 26, 4, 1, gold)   # gold contact band

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))
finish(c)
