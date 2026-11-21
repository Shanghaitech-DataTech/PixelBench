c = new_canvas(32, 32, name="pear")

OUT  = c.color("#2b5420", "outline")
DARK = c.color("#4e8c2f", "dark")
MID  = c.color("#7cb342", "mid")
LIT  = c.color("#a8d758", "lit")
PALE = c.color("#dcf08f", "pale")
STEM = c.color("#6b4423", "stem")

body = ("M16 5 C17.6 5.6 18.7 9 18.2 12 C17.8 14.2 20 15 22 17 "
        "C25.2 20 25.5 26.2 21 28.6 C18 30.2 14 30.2 11 28.6 "
        "C6.6 26.2 6.8 20 10 17 C12 15 14.2 14.2 13.8 12 "
        "C13.3 9 14.4 5.6 16 5 Z")

c.path(body, MID)

# lit area on the upper-left of the bulb and the neck
c.ellipse(13, 21, 4, 5, LIT)
c.ellipse(15, 13, 2, 3, LIT)
for (px, py) in [(11,19),(12,19),(13,19),(11,20),(12,20),(13,20),
                 (11,21),(12,21),(12,22),(15,12),(15,13)]:
    c.set(px, py, PALE)

# shade crescent down the right side
c.path("M21.5 16 C25 20 25 27 19.5 29.4 C23.5 26 23.5 20 19 17 Z", DARK)
c.path("M12 28.6 C15 30 19 30 21.5 28.4 C19 30.6 14 30.6 12 28.6 Z", DARK)

c.outline(OUT)

# leaf
leaf = "M17 5 C19 1.5 23 0.6 25.5 2.2 C23 5.6 19 6.6 17 5 Z"
c.path(leaf, LIT)
c.path("M18 5 C20 2.6 23 1.4 25 2.2 C22.5 3 20 4 18 5 Z", MID)
c.path(leaf, OUT, fill=False)

# stem
c.line(16, 5, 16, 3, STEM)
c.set(17, 2, STEM)

view(c)
finish(c)
