# Empirical test: how does this engine rasterise circles?
c = new_canvas(64, 26, background=None, name="circletest")

NAVY = "#22303F"
WHITE = "#FFFFFF"

# r4 variants, centres at y=6
c.circle(6, 6, 4, NAVY, fill=False)            # A outline
c.circle(20, 6, 4, NAVY, fill=True)            # B filled
c.circle(34, 6, 4, NAVY, fill=True); c.circle(34, 6, 3, WHITE, fill=True)   # C ring thin
c.circle(48, 6, 4, NAVY, fill=True); c.circle(48, 6, 2, WHITE, fill=True)   # D ring thick

# r2 variants, centres at y=19
c.circle(6, 19, 2, NAVY, fill=False)
c.circle(20, 19, 2, NAVY, fill=True)
c.circle(34, 19, 2, NAVY, fill=True); c.circle(34, 19, 1, WHITE, fill=True)

print(c.matrix_text(region=(0, 0, 63, 25)))
