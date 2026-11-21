# 48x48 transparent pixel-art teleport portal
c = new_canvas(48, 48, name="teleport_portal")

# Palette
ink = "#170d35"
shadow = "#32105e"
deep = "#57169a"
purple = "#8d2de0"
bright = "#c45bff"
pale = "#f0baff"
blue = "#4b9cff"
cyan = "#9cecff"
white = "#f4ffff"

# Floating energy motes behind the ring
for x, y, col in [(7,11,blue),(10,7,purple),(38,8,cyan),(41,14,purple),
                  (6,31,purple),(9,39,blue),(39,38,purple),(42,29,cyan),
                  (13,5,bright),(34,5,bright),(5,21,bright),(43,22,bright)]:
    c.set(x, y, col)
c.set(8, 16, purple); c.set(40, 33, bright)
c.set(12, 42, purple); c.set(36, 43, blue)

# Halo: cool outer glow, electric highlights and dark outer silhouette
c.ellipse(24, 24, 16, 21, blue)
c.ellipse(24, 24, 15, 20, cyan, fill=False)
c.ellipse(24, 24, 14, 19, white, fill=False)
c.ellipse(24, 24, 13, 18, purple)
c.ellipse(24, 24, 11, 16, bright, fill=False)

# Inner aperture and deep violet depth
c.ellipse(24, 24, 10, 15, ink)
c.ellipse(24, 24, 9, 14, shadow, fill=False)
c.ellipse(24, 24, 8, 13, deep)

# Rotating vortex ribbons, winding inward through the aperture
c.path("M 15 14 C 18 10 27 9 32 13 C 36 16 35 21 31 23 C 27 25 19 22 17 26 C 15 30 20 35 26 34 C 30 33 32 30 31 27", purple, fill=False)
c.path("M 14 17 C 19 13 27 12 31 15 C 34 18 32 21 28 21 C 24 21 20 19 18 22", bright, fill=False)
c.path("M 33 32 C 29 37 21 38 17 34 C 14 31 16 27 20 26 C 24 25 29 28 31 25 C 34 22 31 17 26 16", blue, fill=False)
c.path("M 17 30 C 19 34 24 35 28 32 C 31 30 30 27 27 26", pale, fill=False)

# Sharp energy flecks and light-catching breaks in the halo
for x, y, col in [(22,14,pale),(25,13,white),(29,15,bright),(17,19,bright),
                  (30,19,cyan),(20,22,pale),(27,23,white),(16,27,blue),
                  (23,29,bright),(28,31,pale),(20,33,cyan),(32,28,bright),
                  (13,9,white),(35,10,white),(11,24,cyan),(37,25,white),
                  (17,42,white),(31,43,white)]:
    c.set(x, y, col)

# Small sparks emphasize a rotating, two-pose energy field
c.line(4, 17, 6, 18, cyan)
c.line(41, 10, 43, 9, white)
c.line(39, 40, 41, 41, cyan)
c.set(5, 26, bright); c.set(42, 26, bright)
c.set(14, 4, cyan); c.set(33, 44, pale)

print(c.stats_text())
finish(c)
