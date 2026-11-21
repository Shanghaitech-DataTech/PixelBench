from pixelbench_api import new_canvas, finish

c = new_canvas(16, 16)

# --- palette ---
OUTLINE = (16, 34, 66)
HALO1 = (70, 175, 245, 42)     # outer faint glow ring
HALO2 = (95, 200, 255, 80)     # mid glow ring
BELL_LOW = (65, 150, 230, 190)
BELL_MID = (130, 210, 255, 215)
BELL_HI = (205, 242, 255, 235)
DOME = (235, 252, 255, 245)
TENT_DARK = (40, 100, 175, 200)
TENT = (105, 205, 255, 225)
TENT_LIGHT = (200, 240, 255, 225)
DEBRIS = (170, 225, 255, 120)

# --- glow halo behind the jelly ---
c.circle(7, 5, 5, HALO1, fill=False)
c.circle(7, 5, 4, HALO2, fill=False)

# --- translucent glowing bell ---
c.ellipse(7, 5, 4, 3, OUTLINE, fill=True)      # dark outline shell
c.ellipse(7, 5, 3, 2, BELL_LOW, fill=True)     # translucent body
c.ellipse(7, 5, 2, 1, BELL_MID, fill=True)     # brighter core
c.circle(6, 4, 1, DOME, fill=True)             # top dome highlight
c.set(8, 4, BELL_HI)                           # glint
# bottom rim light
for x in range(5, 10):
    c.set(x, 7, BELL_HI)

# --- short glowing tentacles ---
tents = [
    (4, 9), (5, 11), (6, 10), (7, 12), (8, 10), (9, 11), (10, 9),
]
for x, yend in tents:
    for y in range(8, yend + 1):
        c.set(x, y, TENT_DARK)
        if y < yend:
            c.set(x, y, TENT)
# light the inner half of each tentacle
for x, yend in tents:
    mid = (yend + 8) // 2
    for y in range(8, mid):
        c.set(x, y, TENT_LIGHT)

# tiny reflected glow dots in the deep water
for (dx, dy) in [(2, 10), (12, 11), (13, 6), (3, 12), (11, 13), (2, 5)]:
    c.set(dx, dy, DEBRIS)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 15, 15)))
finish(c)
