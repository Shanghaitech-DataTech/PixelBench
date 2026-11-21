OUT = "#241812"

c = new_canvas(64, 64, name="fast-food-combo")

# ---------------- tray ----------------
c.rect(3, 14, 58, 46, "#3a3a44")
c.rect(5, 16, 54, 42, "#64646e")
c.rect(5, 16, 54, 1, "#7e7e8a")
c.rect(5, 17, 1, 40, "#74747e")
c.rect(5, 57, 54, 1, "#50505a")
for (x, y, w, h) in [(3, 14, 2, 2), (59, 14, 2, 2), (3, 58, 2, 2), (59, 58, 2, 2),
                     (5, 16, 1, 1), (58, 16, 1, 1), (5, 57, 1, 1), (58, 57, 1, 1)]:
    c.clear(x, y, w, h)

# ---------------- soft shadows on the tray ----------------
SH = "#54545e"
c.ellipse(11, 41, 7, 2, SH)
c.ellipse(32, 49, 12, 2, SH)
c.ellipse(51, 41, 8, 2, SH)
c.ellipse(12, 55, 9, 2, SH)

# ---------------- cola cup (back left) ----------------
cup = new_canvas(20, 38, name="cup")
for i in range(23):                      # tapered paper body
    y = 13 + i
    hw = 7 - (i * 2) // 22
    cup.rect(10 - hw, y, 2 * hw + 1, 1, "#eef0f4")
    cup.set(10 + hw, y, "#c2c6ce")
    cup.set(10 + hw - 1, y, "#d6dae1")
cup.rect(3, 21, 15, 8, "#d8281e")        # red label band
cup.rect(3, 28, 15, 1, "#a81612")
cup.line(13, 11, 15, 3, "#d8281e")       # straw
cup.line(14, 11, 16, 3, "#d8281e")
cup.ellipse(10, 13, 8, 3, "#c2c7d1")     # lid
cup.ellipse(10, 13, 6, 2, "#99a0ab")
cup.ellipse(10, 13, 5, 2, "#3c1e0d")     # cola
for (x, y) in [(8, 12), (12, 12), (10, 14), (7, 14)]:
    cup.set(x, y, "#d8ecf6")             # ice cubes
cup.outline(OUT)
c.blit(cup, 1, 5)

# ---------------- fries carton (back right) ----------------
fr = new_canvas(17, 34, name="fries")
for (x, ytop) in [(2, 9), (4, 4), (6, 7), (8, 2), (10, 5), (12, 3), (14, 8)]:
    ln = 18 - ytop
    fr.rect(x, ytop, 2, ln, "#ffd45e")
    fr.set(x + 1, ytop, "#f2bd45")
    fr.set(x, ytop + ln - 1, "#e8a832")
fr.rect(1, 15, 15, 2, "#7a0e0c")         # inside back of carton
for i in range(18):                      # tapered red front
    y = 16 + i
    xl = 1 + i // 9
    xr = 15 - i // 9
    fr.rect(xl, y, xr - xl + 1, 1, "#d8281e")
    fr.set(xr, y, "#a81612")
fr.rect(6, 21, 5, 2, "#ffc233")          # yellow arch
fr.rect(6, 23, 2, 4, "#ffc233")
fr.rect(9, 23, 2, 4, "#ffc233")
fr.outline(OUT)
fr.rect(6, 21, 5, 2, "#ffc233")          # re-stamp arch over outline
fr.rect(6, 23, 2, 4, "#ffc233")
fr.rect(9, 23, 2, 4, "#ffc233")
c.blit(fr, 43, 7)

# ---------------- cheeseburger (centre) ----------------
bg = new_canvas(24, 27, name="burger")
bg.ellipse(12, 6, 11, 5, "#dd9638")      # bun crown
bg.ellipse(11, 5, 8, 3, "#eeae4e")
for (x, y) in [(5, 4), (9, 3), (14, 3), (18, 5), (7, 7), (12, 6), (17, 8), (21, 7), (3, 7)]:
    bg.set(x, y, "#f8e4ae")              # sesame seeds
bg.rect(1, 11, 23, 3, "#cf8834")         # bun side
bg.rect(1, 13, 23, 1, "#b06f24")
bg.rect(1, 16, 23, 1, "#58b52e")         # lettuce
for x in range(1, 24):
    bg.set(x, 17, "#58b52e" if (x % 4) < 2 else "#3f8f20")
for x in (2, 3, 8, 9, 14, 15, 20, 21):
    bg.set(x, 18, "#3f8f20")
bg.rect(1, 14, 23, 2, "#ffc233")         # melted cheese
for x in (4, 5, 11, 12, 18, 19):
    bg.set(x, 16, "#ffc233")             # cheese drips
bg.rect(2, 19, 21, 5, "#6b4026")         # patty
for (x, y) in [(5, 20), (10, 21), (15, 20), (19, 22), (7, 22), (12, 23)]:
    bg.set(x, y, "#4e2c17")
for (x, y) in [(8, 20), (17, 21)]:
    bg.set(x, y, "#83502e")
bg.rect(2, 23, 21, 3, "#d99a4a")         # bottom bun
bg.rect(4, 26, 17, 1, "#c8873a")
bg.outline(OUT)
c.blit(bg, 20, 22)

# ---------------- chicken nuggets (front left) ----------------
def nugget():
    n = new_canvas(11, 9, name="nug")
    n.ellipse(5, 4, 4, 3, "#e8b054")
    n.set(3, 3, "#f6cd7e")
    n.set(4, 2, "#f6cd7e")
    n.set(6, 3, "#f6cd7e")
    n.set(7, 5, "#b57f2e")
    n.set(3, 6, "#b57f2e")
    n.outline(OUT)
    return n

c.blit(nugget(), 5, 45)
c.blit(nugget(), 15, 47)
c.blit(nugget(), 7, 50)

# ---------------- dipping sauce cups (front right) ----------------
sc = new_canvas(18, 12, name="sauce")
sc.ellipse(4, 4, 4, 3, "#eef0f4")
sc.ellipse(4, 4, 3, 2, "#c02818")        # ketchup
sc.set(3, 3, "#e86a5a")
sc.ellipse(13, 8, 4, 3, "#eef0f4")
sc.ellipse(13, 8, 3, 2, "#f0c020")       # mustard
sc.set(12, 7, "#f6da6a")
sc.outline(OUT)
c.blit(sc, 41, 46)

print(c.stats_text())
finish(c)
