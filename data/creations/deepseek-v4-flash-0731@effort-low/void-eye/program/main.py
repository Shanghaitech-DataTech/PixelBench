from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, name="void-eye")

# ---- palette ----
OUT  = c.color("#0b0320", "outline")       # near-black, readable silhouette
BODY = c.color("#331458", "body")          # deep dark purple body
BODY_D = c.color("#1c0b36", "body_dark")   # lower shading
BODY_L = c.color("#55257e", "body_light")  # top highlight
BODY_H = c.color("#7a3da6", "body_hi")     # bright specular
SLC   = c.color("#efe6a8", "sclera")       # pale yellow sclera
SLC_S = c.color("#a8905a", "sclera_shade") # sclera inner shading
IRIS  = c.color("#7119b0", "iris")         # deep purple iris
IRIS_D= c.color("#3d0f66", "iris_dark")
IRIS_R= c.color("#9a4fe0", "iris_ring")
PUP   = c.color("#ffe27a", "pupil")        # faintly glowing pupil
HALO  = c.color((255, 226, 150, 110), "halo")
HALO2 = c.color((255, 226, 150, 60), "halo2")
SHAD  = c.color((18, 5, 36, 85), "shadow")
SHAD2 = c.color((12, 3, 26, 50), "shadow2")

# ---- soft shadow on the ground (hovering) ----
c.ellipse(32, 59, 21, 3, SHAD2)
c.ellipse(32, 58, 16, 2, SHAD)

# ---- horns (top spikes, boss silhouette) ----
for (hx, htip, base) in ((19, 12, 17), (45, 12, 47)):
    # outline triangles
    c.poly([(hx-2, base), (htip-1, 10), (hx+2, base)], OUT)
    c.poly([(hx-1, base-1), (htip, 11), (hx+2, base-1)], BODY)

# left horn fill
c.poly([(18, 17), (18, 12), (14, 17)], BODY)
c.poly([(46, 17), (46, 12), (50, 17)], BODY)

# ---- body (bulbous floating mass) ----
c.ellipse(32, 28, 19, 15, OUT)          # outline ring
c.ellipse(32, 28, 18, 14, BODY)         # main body

# bottom shading for volume
c.ellipse(32, 34, 15, 6, BODY_D)
# top-left highlight
c.ellipse(25, 20, 7, 4, BODY_L)
c.ellipse(24, 19, 4, 2, BODY_H)

# ---- giant single eye ----
c.ellipse(32, 29, 12, 10, OUT)          # eye outline
c.ellipse(32, 29, 11, 9, SLC)           # sclera
# sclera shading bottom
c.ellipse(32, 33, 9, 4, SLC_S)

# angry brow creases above the eye
c.line(18, 20, 25, 16, OUT)
c.line(25, 16, 32, 20, OUT)
c.line(32, 19, 38, 15, OUT)
c.line(38, 15, 47, 19, OUT)

# deep purple iris
c.circle(32, 30, 8, IRIS_D)             # outer dark ring
c.circle(32, 30, 7, IRIS)
c.circle(32, 30, 5, IRIS_D)
c.circle(32, 29, 4, IRIS_R)             # light ring top
c.circle(32, 30, 3, IRIS_D)

# faintly glowing pupil
c.circle(32, 31, 4, HALO)               # soft glow
c.circle(32, 31, 3, HALO2)
c.circle(32, 31, 2, PUP)
# bright core of the glow
c.set(32, 30, PUP)
c.set(32, 32, PUP)

# ---- short tentacles hanging below ----
tents = [(20, 39, 46, -1), (26, 40, 50, 1), (33, 41, 52, 0), (40, 40, 50, -1), (46, 39, 46, 1)]
for (tx, t0, t1, curl) in tents:
    # outline silhouette (tapering)
    c.poly([(tx-3, t0-2), (tx+3, t0-2), (tx+curl, t1)], OUT)
    c.poly([(tx-2, t0-2), (tx+2, t0-2), (tx+curl, t1-1)], BODY)
    c.poly([(tx-2, t0-3), (tx-1, (t0+t1)//2), (tx+curl, t1-1)], BODY_D)

print(c.matrix_text(region=(8, 4, 56, 50)))
# ---- floating glowing motes (ominous atmosphere) ----
for (mx, my) in ((15, 12), (51, 14), (10, 30), (53, 33), (22, 50), (42, 49)):
    c.set(mx, my, HALO)

# ---- finish ----
print(c.stats_text())
finish(c)
