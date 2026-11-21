from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

OUT = c.color((18, 14, 12), name="outline")
LEATHER = c.color((76, 54, 38), name="leather")
LEATHER_DK = c.color((62, 44, 30), name="leather_dk")
LEATHER_LT = c.color((100, 74, 52), name="leather_lt")
METAL_DK = c.color((90, 92, 96), name="metal_dk")
METAL = c.color((172, 174, 180), name="metal")
METAL_LT = c.color((226, 228, 234), name="metal_lt")
LENS_BL = c.color((8, 8, 10), name="lens_black")
LENS_DG = c.color((44, 46, 56), name="lens_dkgray")
GLASS = c.color((58, 78, 120), name="glass")
GLASS_LT = c.color((110, 136, 186), name="glass_lt")
GLASS_HI = c.color((190, 214, 248), name="glass_hi")
RED = c.color((188, 48, 40), name="red")

# ---- body silhouette with dark outline ----
c.rect(4, 8, 24, 22, OUT)          # x4..27, y8..29
c.rect(5, 9, 22, 1, METAL)         # metal top plate edge
c.rect(5, 10, 22, 1, METAL_DK)
c.rect(5, 11, 22, 17, LEATHER)     # leather body x5..26, y11..27
c.rect(5, 28, 22, 1, METAL_DK)     # bottom trim

# rounded corners
for x, y in ((4, 8), (27, 8), (4, 29), (27, 29)):
    c.set(x, y, None)

# leather grain
for y in range(11, 28, 2):
    for x in range(5, 27, 2):
        m = (x + y) % 4
        if m == 0:
            c.set(x, y, LEATHER_DK)
        elif m == 2:
            c.set(x, y, LEATHER_LT)

# ---- viewfinder hump ----
c.rect(11, 5, 10, 5, OUT)          # hump silhouette x11..20, y5..9
c.rect(12, 6, 8, 3, METAL_DK)      # hump face
c.rect(13, 7, 5, 2, OUT)           # window frame
c.rect(14, 7, 3, 2, LENS_DG)        # window glass
c.set(14, 7, GLASS)

# ---- lug top-left ----
c.rect(5, 6, 3, 3, OUT)
c.rect(6, 7, 1, 1, LENS_DG)

# ---- shutter button ----
c.circle(23, 6, 2, OUT)            # x21..25, y4..8
c.circle(23, 6, 1, METAL)
c.set(23, 5, METAL_LT)

# ---- small front viewfinder window ----
c.rect(7, 12, 3, 3, OUT)
c.rect(8, 13, 1, 1, LENS_DG)

# ---- lens stack (concentric) ----
c.circle(16, 20, 8, OUT)           # outer dark outline ring
c.circle(16, 20, 7, METAL)         # silver rim
c.circle(16, 20, 6, METAL_DK)      # rim step
c.circle(16, 20, 5, LENS_BL)        # black ring
c.circle(16, 20, 4, LENS_DG)        # dark inner ring
c.circle(16, 20, 3, GLASS)         # glass
# glass reflections
c.set(16, 17, GLASS_LT)
c.set(15, 18, GLASS_LT)
c.set(16, 18, GLASS_LT)
c.set(17, 18, GLASS_LT)
c.set(19, 19, GLASS_LT)
c.set(14, 19, GLASS_LT)
c.set(15, 19, GLASS_HI)
c.set(16, 19, GLASS_HI)
c.set(19, 21, GLASS_LT)
c.set(18, 22, GLASS_LT)
# metal rim highlights
c.set(16, 13, METAL_LT)
c.set(14, 14, METAL_LT)
c.set(21, 17, METAL_LT)
c.set(16, 26, METAL_DK)

# small red accent dot on leather
c.set(23, 25, RED)

# lens inner depth shading
c.set(16, 20, LENS_BL)  # keep center dark base under glass (glass covers it)
c.set(13, 21, LENS_DG)

print(c.stats_text())
finish(c)
