from pixelbench_api import *

OUT = (34, 26, 38)        # dark outline
RED = (214, 69, 51)
ORANGE = (240, 130, 44)
YELLOW = (250, 205, 80)
PALE = (255, 240, 190)
ICE = (110, 190, 235)
ICE_D = (60, 130, 200)
WHITE = (235, 250, 255)
GREEN = (90, 200, 110)
GREEN_D = (50, 150, 80)
LIME = (190, 240, 160)
BOLT = (250, 220, 70)
BOLT_D = (230, 170, 40)

def base():
    return new_canvas(32, 32, name="icon")

def shield_body(c):
    # shield outline shape via poly
    pts = [(16, 3), (27, 7), (27, 16), (22, 25), (16, 29), (10, 25), (5, 16), (5, 7)]
    c.poly(pts, ICE)
    # darker right/bottom shading
    c.poly([(16,3),(27,7),(27,16),(22,25),(16,29),(16,26),(20,23),(25,16),(25,8)], ICE_D)
    # inner facet line
    c.line(16, 5, 16, 27, ICE_D)
    # snowflake-ish highlight
    c.line(10, 11, 22, 11, WHITE)
    c.line(16, 8, 16, 14, WHITE)
    c.set(12, 9, WHITE); c.set(20, 9, WHITE)
    c.set(12, 13, WHITE); c.set(20, 13, WHITE)
    return c

# fireball
c = base()
c.circle(17, 17, 9, RED)
c.circle(17, 17, 6, ORANGE)
c.circle(16, 16, 3, YELLOW)
# flame tail upper-left
c.poly([(8, 8), (13, 12), (9, 13), (12, 16), (6, 14)], ORANGE)
c.poly([(5, 5), (10, 9), (6, 9)], YELLOW)
c.set(4, 4, YELLOW)
# sparks
c.set(26, 8, YELLOW); c.set(28, 12, ORANGE); c.set(9, 25, ORANGE)
fire = c

# ice shield
c = base()
shield_body(c)
ice = c

# healing cross
c = base()
c.rect(12, 5, 8, 22, GREEN)
c.rect(5, 12, 22, 8, GREEN)
# shading
c.rect(12, 5, 3, 22, GREEN_D)
c.rect(5, 12, 3, 8, GREEN_D)
# shine
c.rect(17, 7, 2, 8, LIME)
c.rect(10, 14, 6, 2, LIME)
c.set(24, 14, LIME); c.set(25, 15, LIME)
heal = c

# lightning bolt
c = base()
c.poly([(19, 2), (9, 17), (15, 17), (11, 30), (24, 13), (17, 13), (24, 2)], BOLT)
# darker edge on left of bolt
c.poly([(19,2),(9,17),(15,17),(11,30),(13,30),(17,15),(12,15),(21,2)], BOLT_D)
c.set(20, 4, PALE); c.set(19, 5, PALE)
# sparks
c.set(27, 6, BOLT); c.set(6, 22, BOLT); c.set(5, 10, BOLT)
bolt = c

for icon in (fire, ice, heal, bolt):
    icon.outline(OUT)

result = new_canvas(64, 64, name="skill-icon-set")
result.blit(fire, 0, 0)
result.blit(ice, 32, 0)
result.blit(heal, 0, 32)
result.blit(bolt, 32, 32)

print(result.stats_text())
save("skill-icon-set", result)
finish(result)
