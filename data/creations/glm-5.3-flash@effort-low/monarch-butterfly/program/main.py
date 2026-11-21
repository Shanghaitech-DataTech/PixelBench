c = new_canvas(32, 32, name="monarch")

ORANGE = "#e8760c"
DARK = "#2b1a0e"
LIGHT = "#f5a623"
WHITE = "#f8f2e4"

# Wings: upper (forewing) and lower (hindwing) lobes, mirrored around x=16
def wing(cx, mirror):
    m = 1 if mirror else -1
    def X(x): return cx + m * x
    # forewing: big triangle-ish blob from body outward-up
    c.poly([(X(1), 16), (X(6), 4), (X(13), 6), (X(14), 14), (X(8), 19)], ORANGE)
    # hindwing
    c.poly([(X(1), 17), (X(6), 20), (X(12), 22), (X(13), 27), (X(8), 29), (X(3), 24)], ORANGE)

wing(16, False)
wing(16, True)

# black veins / borders: outline wings in dark
# forewing border
c.line(6, 4, 13, 6, DARK)
c.line(13, 6, 14, 14, DARK)
c.line(14, 14, 8, 19, DARK)
c.line(8, 19, 1, 16, DARK)
c.line(1, 16, 6, 4, DARK)
# hindwing border
c.line(1, 17, 6, 20, DARK)
c.line(6, 20, 12, 22, DARK)
c.line(12, 22, 13, 27, DARK)
c.line(13, 27, 8, 29, DARK)
c.line(8, 29, 3, 24, DARK)
c.line(3, 24, 1, 17, DARK)

# veins on forewing
c.line(2, 15, 11, 8, DARK)
c.line(3, 16, 12, 11, DARK)
c.line(4, 17, 12, 13, DARK)
# veins on hindwing
c.line(3, 19, 10, 24, DARK)
c.line(3, 21, 11, 26, DARK)

# white spots along outer forewing edge
for (x, y) in [(12, 7), (13, 9), (13, 11), (12, 13), (10, 15)]:
    c.set(x, y, WHITE); c.set(32 - x, y, WHITE)
# white spots hindwing edge
for (x, y) in [(11, 23), (12, 25), (11, 27), (8, 28)]:
    c.set(x, y, WHITE); c.set(32 - x, y, WHITE)

# body
c.rect(15, 8, 2, 18, DARK)
# antennae
c.line(15, 8, 12, 3, DARK)
c.line(16, 8, 19, 3, DARK)
c.set(12, 3, DARK); c.set(19, 3, DARK)
# head dots
c.set(14, 7, DARK); c.set(17, 7, DARK)

print(c.stats_text())
save("monarch", c)
finish(c)
