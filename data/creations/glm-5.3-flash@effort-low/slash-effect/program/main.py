c = new_canvas(48, 48, name="slash")

WHITE = "#FFFFFF"
LIGHT = "#DDEEFF"
MID = "#88BBEE"

# Frame 1 (left half, 24x48): small white arc slash
c.path("M 8 14 Q 18 18 20 30", WHITE, fill=False)
c.path("M 7 16 Q 16 20 18 31", LIGHT, fill=False)
c.set(6, 18, LIGHT)

# Frame 2 (right half): larger arc with trailing streak
c.path("M 30 8 Q 42 14 44 32", WHITE, fill=False)
c.path("M 29 11 Q 40 17 42 33", MID, fill=False)
c.path("M 28 14 Q 38 20 40 34", MID, fill=False)
# trailing streak behind the arc
c.line(24, 6, 28, 10, LIGHT)
c.line(23, 9, 26, 13, MID)
c.line(22, 12, 25, 16, MID)

print(c.stats_text())
finish(c)
