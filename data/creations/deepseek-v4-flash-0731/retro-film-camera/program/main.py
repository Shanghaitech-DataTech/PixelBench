import random
from pixelbench_api import new_canvas, finish

def main():
    CX, CY = 15, 17
    OUT      = "#161210"
    METAL_D  = "#6a6e74"
    METAL    = "#9aa0a6"
    METAL_L  = "#ccd2d8"
    LEATHER   = "#54402a"
    LEATHER_D = "#3e2e1d"
    LEATHER_L = "#705840"
    BARREL   = "#1d1d22"
    GLASS   = "#1b2d49"
    GLASS_D = "#0f1c31"
    GLASS_L = "#4d75ac"
    CATCH   = "#eef6ff"
    RED     = "#c4452e"

    c = new_canvas(32, 32)

    # ---- silhouette ----
    c.rect(5, 8, 22, 19, LEATHER)     # body leather  x5..26 y8..26
    c.rect(5, 8, 22, 3, METAL)        # top plate     y8..10
    c.rect(5, 25, 22, 2, METAL_D)     # base plate    y25..26
    c.rect(11, 5, 10, 4, METAL)       # viewfinder hump  x11..20 y5..8
    c.rect(23, 4, 3, 1, METAL_L)      # shutter button top
    c.rect(23, 5, 3, 2, METAL)        # shutter button
    c.rect(6, 4, 3, 1, METAL)         # accessory shoe
    c.rect(6, 5, 3, 3, METAL_D)
    # rounded corners
    for x, y in [(5, 8), (26, 8), (5, 26), (26, 26), (11, 5), (20, 5)]:
        c.set(x, y, None)
    c.outline(OUT)

    # ---- body shading ----
    c.rect(6, 12, 2, 12, LEATHER_L)   # left light band  x6..7 y12..23
    c.rect(25, 12, 1, 12, LEATHER_D)  # right shade     x25  y12..23

    # ---- leather speckle ----
    rng = random.Random(42)
    for _ in range(64):
        x = rng.randint(7, 24)
        y = rng.randint(11, 24)
        if c.get(x, y) == LEATHER:
            c.set(x, y, LEATHER_D if rng.random() < 0.55 else LEATHER_L)

    # ---- small front details ----
    c.rect(15, 6, 2, 2, GLASS_D)      # viewfinder window
    c.rect(6, 10, 2, 1, RED)          # indicator light

    # ---- lens ----
    c.circle(CX, CY, 7, BARREL)
    c.circle(CX, CY, 6, METAL)
    c.circle(CX, CY, 5, METAL_D)
    c.circle(CX, CY, 4, GLASS)
    c.circle(CX, CY, 3, GLASS_D)
    c.set(CX, CY - 6, METAL_L)
    c.set(CX + 1, CY - 6, METAL_L)
    c.set(CX - 6, CY, METAL_L)
    c.set(CX - 4, CY - 2, GLASS_L)
    c.set(CX - 3, CY - 3, GLASS_L)
    c.set(CX - 2, CY - 4, GLASS_L)
    c.set(CX - 3, CY - 2, GLASS_L)
    c.set(CX - 2, CY - 3, CATCH)
    c.set(CX + 3, CY + 3, GLASS_L)

    c.outline(OUT)

    # ---- post-outline highlights (stay bright) ----
    c.rect(21, 4, 2, 1, METAL)       # wind lever
    c.rect(23, 4, 3, 1, METAL_L)     # shutter button top
    c.set(7, 4, METAL_L)              # shoe gleam
    # lens rim gleam arc
    for x in (13, 14, 15, 16, 17):
        c.set(x, 11, METAL_L)
    c.set(12, 12, METAL_L)
    c.set(13, 12, METAL_L)
    c.set(16, 12, METAL_L)
    c.set(17, 12, METAL_L)

    print(c.stats_text())
    print(c.matrix_text())
    finish(c)

main()
