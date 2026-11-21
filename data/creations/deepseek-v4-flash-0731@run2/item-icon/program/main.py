from pixelbench_api import *

c = new_canvas(32, 32, name="golden_compass")

outline = c.color("#241708")
gold = c.color("#c9993f")
goldLight = c.color("#e8c468")
face = c.color("#f6df9c")
bronze = c.color("#6b4a12")
red = c.color("#b03a2e")
redLight = c.color("#d96a52")
blueDark = c.color("#1e4fa8")
blue = c.color("#3572d6")
blueLight = c.color("#6fa4f5")
whiteHi = c.color("#eef4ff")

# --- Body: thick dark outline + golden ring ---
c.circle(16, 16, 15, outline)      # outer dark disc (rows/cols 1..31)
c.circle(16, 16, 13, gold)         # gold ring behind the dark rim (2px thick outline)
c.circle(16, 16, 12, goldLight)    # lighter inner band
c.circle(16, 16, 10, face)         # pale dial face

# --- Compass ticks on the band (8 directions) ---
c.line(16, 3, 16, 5, outline)
c.line(16, 27, 16, 29, outline)
c.line(27, 16, 29, 16, outline)
c.line(3, 16, 5, 16, outline)
c.line(24, 8, 25, 7, outline)
c.line(24, 24, 25, 25, outline)
c.line(8, 24, 7, 25, outline)
c.line(8, 8, 7, 7, outline)

# --- Needle (north = red, south = pale gold) ---
c.poly([(16, 5), (20, 15), (12, 15)], red)
c.poly([(16, 25), (20, 16), (12, 16)], goldLight)
c.line(16, 6, 16, 9, redLight)

# --- Blue crystal center ---
c.poly([(16, 11), (20, 16), (16, 21), (12, 16)], blueDark)
c.poly([(16, 12), (19, 16), (16, 20), (13, 16)], blue)
c.poly([(16, 13), (18, 16), (16, 19), (14, 16)], blueLight)
# glint + shading
c.set(16, 13, whiteHi)
c.set(15, 14, whiteHi)
c.set(16, 14, whiteHi)
c.set(16, 15, whiteHi)
c.set(17, 17, blueDark)

print(c.stats_text())
finish(c)
