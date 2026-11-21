from pixelbench_api import new_canvas, finish

OUT = "#241f26"

c = new_canvas(64, 64, None, "combo")

# ---------------- tray ----------------
c.rect(3, 15, 58, 45, OUT, fill=False)
c.rect(4, 16, 56, 43, "#c3c9d4")
c.rect(6, 18, 52, 39, "#a9b0be")
# soften tray corners
for x, y in [(3,15),(60,15),(3,59),(60,59),(4,15),(59,15),(3,16),(60,16),
             (3,58),(60,58),(4,59),(59,59),(4,16),(59,16),(3,17),(60,17),
             (4,58),(59,58),(3,57),(60,57)]:
    c.set(x, y, None)

# ---------------- cheeseburger ----------------
b = new_canvas(64, 64, None, "burger")
cx, t = 16, 24
b.ellipse(cx, t + 4, 9, 4, "#e8a34c")          # top bun
b.ellipse(cx, t + 3, 7, 3, "#f2bc63")          # bun highlight
for dx, dy in [(-6, 0), (-3, -2), (1, -3), (5, -1), (-1, 1), (3, 2), (-5, 3), (6, 2)]:
    b.set(cx + dx, t + 4 + dy, "#fbecc4")      # sesame seeds
b.rect(cx - 9, t + 8, 19, 2, "#ffc32b")        # melted cheese
b.set(cx - 7, t + 10, "#ffc32b"); b.set(cx - 7, t + 11, "#f5a623")
b.set(cx + 2, t + 10, "#ffc32b"); b.set(cx + 2, t + 11, "#f5a623")
b.set(cx + 7, t + 10, "#ffc32b")
for x in range(cx - 10, cx + 11):              # lettuce frill
    b.set(x, t + 11, "#7ec850")
    if (x - cx) % 3 == 0:
        b.set(x, t + 12, "#5aa838")
b.rect(cx - 9, t + 13, 19, 3, "#6e4022")       # patty
b.rect(cx - 8, t + 13, 17, 1, "#7d4b28")
for dx in (-6, -1, 4, 8):
    b.set(cx + dx, t + 14, "#59341b")
b.rect(cx - 9, t + 16, 19, 2, "#e8a34c")       # bottom bun
b.rect(cx - 7, t + 18, 15, 1, "#d18f3c")
b.outline(OUT)
c.blit(b, 0, 0)

# ---------------- fries ----------------
f = new_canvas(64, 64, None, "fries")
for x, ty, col in [(29,18,"#f2bd45"),(31,14,"#f6ca55"),(33,17,"#e8ab38"),
                   (35,13,"#f6ca55"),(37,16,"#f2bd45"),(39,14,"#e8ab38"),
                   (41,18,"#f2bd45"),(30,22,"#e8ab38"),(34,21,"#f2bd45"),
                   (38,20,"#e8ab38"),(32,23,"#f2bd45")]:
    f.rect(x, ty, 2, 34 - ty, col)
    f.set(x, ty, "#fde9a8")
f.poly([(28,32),(43,32),(41,49),(30,49)], "#d8352f")     # carton
f.poly([(38,32),(43,32),(41,49),(37,49)], "#b02622")     # shade
f.line(28,32,43,32,"#8f1d1a")                            # rim
f.rect(33,38,4,4,"#f4f4f4")                              # logo mark
f.rect(34,39,2,2,"#d8352f")
f.outline(OUT)
c.blit(f, 0, 0)

# ---------------- cola cup ----------------
u = new_canvas(64, 64, None, "cup")
u.rect(54, 7, 2, 14, "#e04b3f")                          # straw
for yy in range(7, 20, 4):
    u.rect(54, yy, 2, 2, "#f4f4f4")
u.poly([(45,22),(59,22),(57,45),(47,45)], "#4a2413")     # cola body
u.rect(46, 23, 1, 20, "#6e3a1e")                         # highlight
u.rect(47,25,4,4,"#cfe9f2"); u.rect(48,26,2,1,"#ffffff") # ice
u.rect(52,28,4,4,"#bfe0ec"); u.rect(53,29,2,1,"#ffffff")
u.rect(49,33,4,4,"#cfe9f2"); u.rect(50,34,2,1,"#ffffff")
u.ellipse(52, 21, 8, 3, "#f4f4f4")                       # lid
u.ellipse(52, 20, 7, 2, "#ffffff")
u.line(45, 22, 59, 22, OUT)
u.outline(OUT)
c.blit(u, 0, 0)

# ---------------- nuggets ----------------
n = new_canvas(64, 64, None, "nuggets")
def nugget(x, y):
    n.ellipse(x + 4, y + 3, 4, 3, "#e2a94e")
    n.ellipse(x + 3, y + 2, 3, 2, "#f0c273")
    for dx, dy in [(-2, 1), (1, -1), (3, 2), (0, 2), (-3, -1)]:
        n.set(x + 4 + dx, y + 3 + dy, "#b97f2e")
    n.set(x + 2, y + 1, "#f8dda6")
nugget(26, 46)
nugget(36, 48)
nugget(30, 52)
n.outline(OUT)
c.blit(n, 0, 0)

# ---------------- dipping sauce cups ----------------
s = new_canvas(64, 64, None, "sauce")
def saucecup(x, y, sauce, hi):
    s.ellipse(x, y, 4, 3, "#f4f4f4")
    s.ellipse(x, y, 2, 1, sauce)
    s.set(x - 1, y - 1, "#ffffff")
    s.rect(x - 3, y + 2, 7, 1, "#d8d8dc")
    s.set(x + 1, y + 1, hi)
saucecup(11, 51, "#d0342c", "#e86a5a")
saucecup(19, 54, "#e8b23a", "#f4d070")
s.outline(OUT)
c.blit(s, 0, 0)

print(c.stats_text())
finish(c)
