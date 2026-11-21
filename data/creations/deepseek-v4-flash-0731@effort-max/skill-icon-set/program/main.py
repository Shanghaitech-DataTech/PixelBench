from pixelbench_api import new_canvas, finish

DARK = "#242936"

# ---------------- Fireball (32x32) ----------------
def make_fireball():
    c = new_canvas(32, 32)
    # outer flame silhouette
    c.poly([(16, 2), (10, 13), (22, 13)], "#ff8c1a")
    c.circle(16, 13, 5, "#ff8c1a")
    c.circle(16, 19, 8, "#ff6a00")
    # inner core
    c.circle(16, 19, 5, "#ffb02e")
    c.circle(16, 13, 3, "#ffd15e")
    # highlights
    c.circle(15, 17, 2, "#ffecb3")
    c.circle(15, 11, 1, "#fff3d6")
    c.outline(DARK)
    return c

# ---------------- Ice shield (32x32) ----------------
def make_ice():
    c = new_canvas(32, 32)
    c.poly([(8, 5), (24, 5), (24, 16), (16, 28), (8, 16)], "#1f8fe0")
    c.poly([(11, 8), (21, 8), (21, 15), (16, 25), (11, 15)], "#6cc9ff")
    # snowflake
    c.line(16, 10, 16, 24, "#eaf6ff")
    c.line(11, 13, 21, 19, "#eaf6ff")
    c.line(11, 19, 21, 13, "#eaf6ff")
    c.line(13, 9, 19, 9, "#eaf6ff")
    c.circle(16, 17, 2, "#eaf6ff")
    c.outline(DARK)
    return c

# ---------------- Healing (32x32) ----------------
def make_heal():
    c = new_canvas(32, 32)
    c.circle(16, 17, 10, "#1fa855")
    c.circle(16, 17, 7, "#4fe08a")
    c.rect(13, 9, 6, 16, "#f2fff6")   # vertical cross arm
    c.rect(8, 14, 16, 6, "#f2fff6")   # horizontal cross arm
    c.circle(16, 17, 2, "#a7f0c0")     # green core
    c.outline(DARK)
    return c

# ---------------- Lightning (32x32) ----------------
def make_bolt():
    c = new_canvas(32, 32)
    c.poly([(19, 3), (11, 18), (15, 18), (13, 29), (24, 17), (19, 17), (21, 3)], "#ffd21f")
    c.poly([(17, 9), (14, 16), (16, 16), (15, 23), (20, 16), (17, 16), (18, 9)], "#ffe873")
    c.outline(DARK)
    return c

# ---------------- Assemble 64x64 ----------------
result = new_canvas(64, 64)
result.blit(make_fireball(), 0, 0)
result.blit(make_ice(), 32, 0)
result.blit(make_heal(), 0, 32)
result.blit(make_bolt(), 32, 32)

print(result.stats_text())
for name, x, y in [("fireball", 0, 0), ("ice", 32, 0), ("heal", 0, 32), ("bolt", 32, 32)]:
    print("=== " + name + " ===")
    print(result.matrix_text((x, y, x + 31, y + 31)))

finish(result)
