from pixelbench_api import new_canvas, finish

c = new_canvas(16, 16)

# Magnifying glass icon for detective game
# Colors
RING = c.color('#1a2332', name='ring')
LENS = c.color('#8fc7e8', name='lens')
LENS_HI = c.color('#d5eefa', name='lens_hi')
HANDLE = c.color('#8b5e34', name='handle')
HANDLE_DK = c.color('#5c3c22', name='handle_dk')
GOLD = c.color('#d4a636', name='gold')
GOLD_LT = c.color('#e8c34c', name='gold_lt')

# === Lens ===
# Outer frame ring
c.circle(6, 5, 5, RING, fill=False)
# Lens glass
c.circle(6, 5, 4, LENS, fill=True)
# Glass reflections (upper-left highlights)
c.set(4, 3, LENS_HI)
c.set(5, 3, LENS_HI)
c.set(4, 4, LENS_HI)
# Clue / evidence dots inside the lens
c.set(6, 5, RING)
c.set(5, 6, RING)

# === Handle ===
# Thick diagonal handle with shading

# Handle main body
handle_pixels = [
    (10, 8), (11, 8),
    (10, 9), (11, 9),
    (11, 10), (12, 10), (13, 10),
    (12, 11), (13, 11), (14, 11),
    (13, 12), (14, 12), (15, 12),
]
for x, y in handle_pixels:
    c.set(x, y, HANDLE)

# Handle shadow on bottom edge
c.set(13, 10, HANDLE_DK)
c.set(14, 11, HANDLE_DK)
c.set(15, 12, HANDLE_DK)

# Gold metal cap at the handle tip
c.set(13, 13, GOLD)
c.set(14, 13, GOLD)
c.set(14, 14, GOLD)
c.set(15, 13, GOLD)
c.set(14, 15, GOLD)
c.set(15, 14, GOLD)
c.set(15, 15, GOLD_LT)

finish(c)
