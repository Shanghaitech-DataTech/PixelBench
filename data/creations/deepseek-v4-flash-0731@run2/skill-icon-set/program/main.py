from pixelbench_api import *

DARK = (26, 28, 40)
WHITE = (255, 255, 255)


def icon_canvas():
    return new_canvas(32, 32)


# ================= FIREBALL (top-left) =================
fb = icon_canvas()
# core ball
fb.circle(16, 18, 10, DARK)
fb.circle(16, 18, 9, (232, 74, 24))      # outer red-orange
fb.circle(16, 19, 7, (255, 128, 0))      # orange
fb.circle(16, 18, 4, (255, 196, 0))      # yellow
fb.circle(16, 17, 2, (255, 244, 170))    # hot core
# flame tongue on top
fb.poly([(16, 3), (20, 11), (12, 11)], DARK)
fb.poly([(16, 5), (19, 10), (13, 10)], (255, 128, 0))
fb.poly([(16, 6), (18, 9), (14, 9)], (255, 196, 0))
# flame tongue on right side
fb.poly([(28, 15), (32, 18), (27, 21)], DARK)
fb.poly([(28, 16), (31, 18), (27, 20)], (255, 128, 0))
# sparks
fb.set(6, 9, DARK)
fb.set(7, 10, (255, 244, 170))
fb.set(27, 23, DARK)
fb.set(28, 24, (255, 244, 170))

# ================= ICE SHIELD (top-right) =================
sh = icon_canvas()
outer = [(16, 3), (25, 6), (26, 13), (24, 20), (16, 28), (8, 20), (6, 13), (7, 6)]
sh.poly(outer, DARK)
body = [(16, 6), (23, 8), (24, 13), (22, 19), (16, 26), (10, 19), (8, 13), (9, 8)]
sh.poly(body, (96, 190, 245))
panel = [(16, 10), (21, 11), (21, 14), (19, 18), (16, 22), (13, 18), (11, 14), (11, 11)]
sh.poly(panel, (170, 220, 252))
# central ice crystal
sh.poly([(16, 13), (19, 16), (16, 20), (13, 16)], DARK)
sh.poly([(16, 14), (18, 16), (16, 19), (14, 16)], (233, 247, 255))
# facet shines
sh.line(12, 10, 15, 9, (233, 247, 255))
sh.line(21, 12, 23, 13, (90, 180, 240))
sh.line(12, 20, 10, 22, (90, 180, 240))

# ================= HEALING (bottom-left) =================
he = icon_canvas()
# dark rounded cross
he.rect(5, 12, 22, 8, DARK)
he.rect(12, 5, 8, 22, DARK)
he.circle(9, 16, 4, DARK)
he.circle(23, 16, 4, DARK)
he.circle(16, 9, 4, DARK)
he.circle(16, 23, 4, DARK)
# green fill
he.rect(7, 14, 18, 4, (46, 204, 113))
he.rect(14, 7, 4, 18, (46, 204, 113))
he.circle(9, 16, 2, (46, 204, 113))
he.circle(23, 16, 2, (46, 204, 113))
he.circle(16, 9, 2, (46, 204, 113))
he.circle(16, 23, 2, (46, 204, 113))
# shine
he.rect(8, 13, 8, 2, (150, 240, 190))
he.rect(15, 8, 2, 6, (150, 240, 190))
# white plus at center
he.rect(15, 14, 2, 4, WHITE)
he.rect(14, 15, 4, 2, WHITE)
# sparkles
he.set(5, 6, DARK); he.set(5, 7, DARK); he.set(6, 6, (150, 240, 190))
he.set(25, 24, DARK); he.set(27, 24, DARK); he.set(26, 23, (150, 240, 190)); he.set(26, 25, WHITE)

# ================= LIGHTNING (bottom-right) =================
li = icon_canvas()
bolt = [(17, 3), (8, 18), (13, 17), (11, 28), (24, 10), (18, 12)]
li.poly(bolt, DARK)
inner = [(16, 6), (10, 17), (13, 16), (12, 26), (22, 12), (17, 13)]
li.poly(inner, (255, 214, 42))
# highlights along the upper and lower arms
li.line(15, 10, 12, 16, (255, 244, 170))
li.line(17, 19, 21, 13, (255, 244, 170))
# sparkles
li.set(6, 10, DARK); li.set(7, 11, (255, 244, 170))
li.set(26, 22, DARK); li.set(27, 23, (255, 244, 170))

# ================= COMPOSE 2x2 =================
c = new_canvas(64, 64)
c.blit(fb, 0, 0)
c.blit(sh, 32, 0)
c.blit(he, 0, 32)
c.blit(li, 32, 32)

print(fb.stats_text())
print(sh.stats_text())
print(he.stats_text())
print(li.stats_text())
print(c.stats_text())
print("--- fireball ---")
print(fb.matrix_text(region=(0, 0, 31, 31), indices=False))
print("--- shield ---")
print(sh.matrix_text(region=(0, 0, 31, 31), indices=False))
print("--- healing ---")
print(he.matrix_text(region=(0, 0, 31, 31), indices=False))
print("--- lightning ---")
print(li.matrix_text(region=(0, 0, 31, 31), indices=False))

finish(c)
