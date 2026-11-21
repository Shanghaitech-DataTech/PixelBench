c = new_canvas(32, 32, background="#e8f4ff", name="scooter")

R = c.color("#d93636", "helmet")      # helmet red
D = c.color("#a32222", "helmet_dark")
S = c.color("#f2c29b", "skin")
B = c.color("#2e6fd8", "shirt")
P = c.color("#37414f", "pants")
K = c.color("#1b1f26", "shoe")
G = c.color("#5a6472", "deck")
T = c.color("#8b95a3", "stem")
H = c.color("#2b2f36", "grip")
W = c.color("#20242b", "tire")
U = c.color("#9aa3b0", "hub")
L = c.color("#ffd75e", "light")

# --- scooter ---
# deck
c.rect(7, 23, 16, 2, G)
c.rect(7, 24, 16, 1, c.color("#454e5b", "deck_dark"))
# wheels (4x4 rounded)
for wx, wy in ((5, 25), (23, 25)):
    c.rect(wx, wy, 4, 4, W)
    c.set(wx, wy, None); c.set(wx+3, wy, None)
    c.set(wx, wy+3, None); c.set(wx+3, wy+3, None)
    c.rect(wx+1, wy+1, 2, 2, U)
# ground shadow
c.rect(5, 30, 23, 1, c.color("#c9dcec", "shadow"))
# stem (leaning forward)
c.line(24, 23, 27, 11, T)
c.line(25, 23, 27, 12, T)
# handlebar
c.line(25, 10, 29, 10, H)
c.set(29, 10, H)
c.set(24, 10, H)
# headlight on stem front
c.set(27, 12, L)

# --- rider ---
# back leg (straight)
c.line(12, 17, 11, 22, P)
# front leg (bent)
c.line(14, 17, 16, 19, P)
c.line(16, 19, 15, 22, P)
# shoes on deck
c.rect(10, 22, 3, 1, K)
c.rect(14, 22, 3, 1, K)
# torso leaning forward
c.rect(12, 12, 4, 5, B)
c.set(15, 12, B)
# arm to handlebar
c.line(15, 13, 24, 11, B)
c.line(15, 14, 24, 11, B)
# hand on grip
c.set(25, 11, S)
c.set(24, 11, S)
# neck + head
c.set(14, 11, S)
c.rect(13, 8, 3, 3, S)   # face
c.set(15, 9, c.color("#222", "eye"))
# helmet
c.rect(12, 6, 4, 2, R)
c.set(12, 8, R)
c.set(13, 8, R)
c.set(16, 7, R)
c.set(16, 8, D)
c.set(15, 10, c.color("#7fd4ff", "visor"))
c.set(16, 10, c.color("#7fd4ff", "visor"))
c.set(11, 7, R)   # back of helmet
# chin strap
c.set(14, 11, D)

print(c.stats_text())

finish(c)
print(c.matrix_text())
