from pixelbench_api import new_canvas, finish, view, save

c = new_canvas(64, 64, background=None, name="void-eye")

# ---- palette ----
FLESH_D = c.color("#1c0b31", "flesh_dark")
FLESH_M = c.color("#3a1660", "flesh_mid")
FLESH_L = c.color("#5c2a8f", "flesh_light")
LID_SH  = c.color("#2a1447", "lid_shadow")
SCLERA  = c.color("#efe6f2", "sclera")
SCL_SH  = c.color("#c3b2cc", "sclera_shade")
SCL_DK  = c.color("#8f7a9c", "sclera_dark")
VEIN    = c.color("#a34a6b", "vein")
IRIS_L  = c.color("#6f3bb0", "iris_light")
IRIS_M  = c.color("#4b1f86", "iris_mid")
IRIS_D  = c.color("#2a0f52", "iris_dark")
GLOW_D  = c.color("#8a3fc4", "glow_dim")
GLOW    = c.color("#c94dff", "pupil_glow")
CORE    = c.color("#ff9df5", "pupil_core")
HILITE  = c.color("#ffffff", "highlight")
SHADOW  = c.color((16, 5, 26, 100), "shadow")
SHADOW2 = c.color((16, 5, 26, 60), "shadow_soft")

# ---- soft hovering shadow ----
c.ellipse(32, 59, 17, 3, SHADOW2)
c.ellipse(32, 59, 12, 2, SHADOW)

# ---- short tentacles: circles stepped along the spine so they stay connected ----
def tentacle(pts, r0, r1, col):
    segs = []
    total = 0.0
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        d = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        segs.append((x0, y0, x1, y1, d))
        total += d
    walked = 0.0
    for x0, y0, x1, y1, d in segs:
        steps = max(1, int(round(d)))
        for i in range(steps):
            t = i / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            r = r0 + (r1 - r0) * walked / total
            c.circle(int(round(x)), int(round(y)), max(1, int(round(r))), col)
        walked += d
    x, y = pts[-1]
    c.circle(int(round(x)), int(round(y)), max(1, int(round(r1))), col)

tentacle([(16, 38), (13, 43), (11, 48), (10, 52)], 3, 2, FLESH_D)
tentacle([(24, 42), (22, 47), (21, 52)], 3, 2, FLESH_D)
tentacle([(32, 44), (31, 49), (30, 54)], 3, 2, FLESH_D)
tentacle([(40, 42), (42, 47), (43, 52)], 3, 2, FLESH_D)
tentacle([(48, 38), (51, 43), (53, 48), (54, 52)], 3, 2, FLESH_D)
# faint mid-tone core on the two outer tentacles for form
tentacle([(15, 39), (13, 44), (11, 49)], 1, 1, FLESH_M)
tentacle([(49, 39), (51, 44), (53, 49)], 1, 1, FLESH_M)

# ---- body ----
c.circle(32, 26, 19, FLESH_D)
c.circle(32, 25, 18, FLESH_M)
c.circle(30, 23, 17, FLESH_L)
c.circle(32, 26, 16, FLESH_M)

# ---- body spikes (ominous silhouette) ----
c.poly([(14, 18), (9, 8), (19, 13)], FLESH_D)
c.poly([(24, 9), (27, 1), (31, 8)], FLESH_D)
c.poly([(36, 8), (40, 2), (43, 10)], FLESH_D)
c.poly([(47, 14), (53, 7), (52, 18)], FLESH_D)
# small side nubs
c.poly([(13, 27), (8, 30), (13, 33)], FLESH_D)
c.poly([(51, 27), (56, 30), (51, 33)], FLESH_D)

# ---- eyeball ----
c.circle(33, 27, 13, SCL_DK)
c.circle(31, 25, 13, SCL_SH)
c.circle(30, 24, 13, SCLERA)

# veins
c.line(19, 23, 24, 26, VEIN)
c.line(42, 32, 38, 30, VEIN)
c.line(23, 36, 26, 33, VEIN)
c.line(40, 19, 37, 22, VEIN)

# ---- deep purple iris ----
c.circle(32, 26, 7, IRIS_L)
c.circle(32, 26, 6, IRIS_M)
c.circle(32, 26, 4, IRIS_D)

# ---- faintly glowing pupil ----
c.circle(32, 26, 3, GLOW_D)
c.circle(32, 26, 2, GLOW)
for x, y in [(32, 25), (31, 26), (32, 26), (33, 26), (32, 27)]:
    c.set(x, y, CORE)

# faint glow halo bleeding onto the iris
for x, y in [(26, 26), (38, 26), (32, 31), (28, 30), (36, 30)]:
    c.set(x, y, GLOW_D)

# ---- heavy eyelid (drawn after the eye so it hoods the top) ----
# cast-shadow crescent dipping lower than the lid itself
c.path("M 16 20 A 14 14 0 0 1 44 20 Q 30 27 16 20 Z", LID_SH, fill=True)
# the lid, dipping slightly at the centre
c.path("M 16 20 A 14 14 0 0 1 44 20 Q 30 23 16 20 Z", FLESH_D, fill=True)

# lash spikes hanging from the lid
c.poly([(21, 20), (23, 25), (25, 20)], FLESH_D)
c.poly([(27, 20), (28, 24), (29, 20)], FLESH_D)
c.poly([(36, 20), (37, 24), (38, 20)], FLESH_D)
c.poly([(39, 20), (41, 25), (43, 20)], FLESH_D)

# specular spark on the upper-left iris, just under the lid
c.set(27, 22, HILITE)
c.set(28, 22, HILITE)
c.set(27, 23, HILITE)

print(c.stats_text())
print(c.matrix_text())
view(c)
save("void-eye", c)
finish(c)
