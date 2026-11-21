import math
from pixelbench_api import new_canvas, finish

BLACK = "#121212"
DARK = "#3b3b3b"
MID = "#4e4e4e"
SILVER = "#a8a8a8"
LIGHT = "#d8d8d8"
RED = "#e01f1f"
TARED = "#ff2a2a"
HUB = "#6d6d6d"
WHITE = "#ededed"
RIM = "#8f8f8f"

c = new_canvas(128, 128)


def wheel(cx, cy):
    c.circle(cx, cy, 24, BLACK)          # thick black tire
    c.circle(cx, cy, 15, RIM)            # rim
    for i in range(8):
        a = math.pi / 4 * i
        c.line(cx + round(7 * math.cos(a)), cy + round(7 * math.sin(a)),
               cx + round(14 * math.cos(a)), cy + round(14 * math.sin(a)), WHITE)
    c.circle(cx, cy, 7, HUB)             # gray hub
    c.circle(cx, cy, 2, BLACK)


wheel(26, 88)
wheel(100, 88)

# --- silver tubular frame -- swingarm to headstock
for dx, dy in [(-1, -1), (0, 0), (1, 1)]:
    c.line(82 + dx, 44 + dy, 42 + dx, 58 + dy, SILVER)   # main frame spars
for dx, dy in [(-1, -1), (0, 0), (1, 1)]:
    c.line(82 + dx, 60 + dy, 34 + dx, 74 + dy, SILVER)   # swingarm

# --- exhaust pipe + under-tail muffler
c.line(44, 62, 30, 56, SILVER)
c.line(45, 63, 31, 57, SILVER)
c.rect(16, 50, 13, 7, SILVER)
c.rect(13, 52, 3, 4, BLACK)

# --- wide dark gray fairing, streamlined, upswept tail
body = [(97, 52), (89, 44), (74, 37), (58, 34), (42, 33), (28, 30),
        (16, 26), (12, 28), (20, 33), (28, 37), (38, 44), (50, 53),
        (66, 60), (82, 63), (92, 59)]
c.poly(body, DARK)

# --- black lower cowl wedge (front belly)
c.poly([(92, 58), (76, 61), (60, 58), (48, 53), (56, 46), (72, 45), (84, 49)], BLACK)

# --- red accent swoosh along the fairing
c.poly([(92, 52), (82, 45), (64, 40), (44, 38), (28, 33), (20, 31),
        (14, 28), (19, 34), (34, 43), (54, 46), (74, 49)], RED)

# --- round silver gray engine cover
c.circle(58, 58, 8, SILVER)
c.circle(58, 58, 5, MID)
c.circle(58, 58, 2, BLACK)

# --- tilted small black windscreen
c.poly([(87, 47), (80, 33), (70, 35), (75, 45)], BLACK)

# --- small dark fender arching over the front wheel
c.poly([(87, 65), (99, 58), (110, 63), (103, 67), (91, 67)], MID)

# --- silver front fork from wheel to steering head
c.line(99, 88, 85, 50, SILVER)
c.line(101, 88, 87, 52, SILVER)
c.rect(83, 46, 7, 5, SILVER)
c.line(84, 47, 74, 42, SILVER)     # handlebar
c.rect(70, 41, 6, 3, BLACK)       # bar grip

# --- red tail light at the upswept tail tip
c.rect(8, 25, 5, 6, TARED)

print(c.stats_text())
print("---- tail/mid ----")
print(c.matrix_text(region=(0, 20, 60, 80)))
print("---- front ----")
print(c.matrix_text(region=(66, 28, 117, 80)))
print("---- lower ----")
print(c.matrix_text(region=(0, 56, 117, 114)))
finish(c)
