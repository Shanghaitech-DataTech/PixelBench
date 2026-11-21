from pixelbench_api import *

c = new_canvas(32, 32, name="output")

# palette
body = c.color('#6ecb4f')
outline = c.color('#2f5e2f')
shade = c.color('#4f9e3f')
highlight = c.color('#a9e870')
moss = c.color('#3d7a3a')
moss_dark = c.color('#2c5c2e')
eye_glow = c.color('#8ef5c8')
eye_core = c.color('#eaff5e')
sparkle = c.color('#ffffff')
mouth = c.color('#2a4a26')
tongue = c.color('#ff8fa3')
antler_col = c.color('#b98a5e')
antler_dark = c.color('#7c5134')
mush_cap = c.color('#e64539')
mush_cap_dark = c.color('#9e2b28')
mush_spot = c.color('#f8f1e0')
cheek = c.color('#ff9db0')

# main slime body: rounded dome with a soft bottom
c.path("M 6 25 C 6 14 10 8 16 8 C 22 8 26 14 26 25 C 23 27 20 28 16 28 C 12 28 9 27 6 25 Z", body)

# lower/edge shading
c.path("M 8 25 C 8 18 11 12 16 12 C 21 12 24 18 24 25 C 22 27 19 28 16 28 C 13 28 10 27 8 25 Z", shade)

# top-left specular highlight
c.ellipse(12, 13, 2, 2, highlight, fill=True)

# outline the body silhouette
c.outline(outline)

# moss tufts on head and shoulders
for x, y in [(11, 10), (12, 9), (14, 9), (16, 10), (18, 9), (20, 10),
             (8, 14), (9, 15), (10, 14), (23, 13), (24, 14), (22, 14)]:
    c.set(x, y, moss)
for x, y in [(12, 10), (15, 9), (18, 9), (9, 14), (23, 14)]:
    c.set(x, y, moss_dark)

# glowing eyes
c.ellipse(12, 16, 2, 2, eye_glow, fill=True)
c.ellipse(20, 16, 2, 2, eye_glow, fill=True)
c.ellipse(12, 16, 1, 1, eye_core, fill=True)
c.ellipse(20, 16, 1, 1, eye_core, fill=True)
c.set(11, 15, sparkle)
c.set(19, 15, sparkle)

# cute open mouth
c.rect(15, 21, 1, 1, mouth)
c.rect(17, 21, 1, 1, mouth)
c.rect(14, 22, 5, 1, mouth)
c.rect(15, 23, 3, 1, mouth)
c.rect(16, 22, 1, 1, tongue)

# cheeks
c.rect(9, 19, 2, 1, cheek)
c.rect(22, 19, 2, 1, cheek)

# tiny antlers
def draw_antler(x0, dirx):
    c.line(x0, 10, x0 - dirx, 6, antler_col)
    c.line(x0 - dirx, 6, x0 - dirx*2, 4, antler_col)
    c.line(x0 - dirx, 6, x0 - dirx, 4, antler_col)

draw_antler(11, 1)   # left: trunk leans left
draw_antler(21, -1)  # right: trunk leans right

# small red mushroom peeking over the right shoulder (on the back)
c.rect(23, 11, 3, 1, mush_cap)        # rounded top of cap
c.rect(22, 12, 5, 1, mush_cap)        # widest part of cap
c.rect(23, 13, 3, 1, mush_cap_dark)   # shaded bottom edge
c.set(23, 12, mush_spot)
c.set(25, 12, mush_spot)
c.set(24, 11, mush_spot)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))

finish(c)
