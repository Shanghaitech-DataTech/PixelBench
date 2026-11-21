from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, background=None, name="skill-icons")

OUTLINE = "#262638"
FIRE_ORANGE = "#f0582d"
FIRE_YELLOW = "#ffd23e"
FIRE_LIGHT = "#ffee96"
ICE_BLUE = "#4cb9e8"
ICE_LIGHT = "#9ee0ff"
ICE_WHITE = "#eafaff"
HEAL_GREEN = "#42c15c"
HEAL_WHITE = "#f4fff7"
BOLT_YELLOW = "#ffd23e"
BOLT_LIGHT = "#fff4b0"

for col in [OUTLINE, FIRE_ORANGE, FIRE_YELLOW, FIRE_LIGHT, ICE_BLUE, ICE_LIGHT, ICE_WHITE, HEAL_GREEN, HEAL_WHITE, BOLT_YELLOW, BOLT_LIGHT]:
    c.color(col)

# Fireball (top-left)
c.poly([(16, 4), (12, 12), (20, 12)], FIRE_ORANGE, fill=True)
c.circle(16, 18, 10, FIRE_ORANGE, fill=True)
c.circle(16, 19, 6, FIRE_YELLOW, fill=True)
c.circle(12, 14, 3, FIRE_LIGHT, fill=True)

# Ice shield (top-right)
outer = [(7, 4), (25, 4), (26, 11), (24, 17), (20, 23), (16, 28), (12, 23), (8, 17), (6, 11)]
c.poly([(x + 32, y) for x, y in outer], ICE_BLUE, fill=True)
inner = [(10, 7), (22, 7), (23, 11), (21, 16), (18, 21), (16, 24), (14, 21), (11, 16), (9, 11)]
c.poly([(x + 32, y) for x, y in inner], ICE_LIGHT, fill=True)
cx, cy = 48, 15
for dx, dy in [(0, -6), (0, 6), (-6, 0), (6, 0), (-4, -4), (4, 4), (-4, 4), (4, -4)]:
    c.line(cx, cy, cx + dx, cy + dy, ICE_WHITE)

# Healing (bottom-left)
g = HEAL_GREEN
c.rect(12, 40, 9, 17, g, fill=True)
c.rect(8, 44, 17, 9, g, fill=True)
c.circle(16, 40, 4, g, fill=True)
c.circle(16, 56, 4, g, fill=True)
c.circle(8, 48, 4, g, fill=True)
c.circle(24, 48, 4, g, fill=True)
w = HEAL_WHITE
c.rect(14, 42, 5, 13, w, fill=True)
c.rect(10, 46, 13, 5, w, fill=True)

# Lightning (bottom-right)
bolt = [(52, 35), (40, 50), (47, 50), (43, 61), (56, 46), (48, 46)]
c.poly(bolt, BOLT_YELLOW, fill=True)
c.circle(47, 53, 1, BOLT_LIGHT, fill=True)

c.outline(OUTLINE)

finish(c)
