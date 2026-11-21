c = new_canvas(64, 32, background=None, name="city-bus")

BODY = "#2f8fd8"      # bus body blue
BODY_D = "#1f6ba8"    # darker blue shade
ROOF = "#e8eef4"      # light roof
WIN = "#9fd4ee"       # window glass
WIN_D = "#5b9cc4"
TIRE = "#20242a"
RIM = "#8a929c"
DOOR = "#c8d6e0"
LIGHT = "#ffe9a8"
RED = "#d84a3a"
DARK = "#17262f"

# Body: y 8..25, x 2..61
c.rect(2, 8, 60, 18, BODY)
c.rect(2, 8, 60, 2, ROOF)          # roof strip
c.rect(2, 24, 60, 2, BODY_D)       # lower skirt
c.rect(2, 8, 1, 18, BODY_D)        # rear edge shade
c.rect(61, 8, 1, 18, BODY_D)       # front edge shade

# Windshield (front = right side)
c.rect(56, 10, 5, 8, WIN)
c.rect(60, 10, 1, 8, WIN_D)

# Electronic route display above windshield
c.rect(52, 9, 9, 3, DARK)
c.text(53, 9, "42", "#7ff0a0", font="5x7")

# Row of windows x 6..50
for i in range(5):
    x = 6 + i * 9
    c.rect(x, 11, 7, 7, WIN)
    c.rect(x, 11, 7, 1, WIN_D)

# Doors: front door (x 50..54) and rear door (x 27..31)
c.rect(50, 11, 5, 13, DOOR)
c.rect(50, 11, 5, 1, BODY_D)
c.line(52, 11, 52, 23, BODY_D)
c.rect(27, 11, 5, 13, DOOR)
c.rect(27, 11, 5, 1, BODY_D)
c.line(29, 11, 29, 23, BODY_D)

# Belt line
c.rect(3, 20, 47, 1, BODY_D)

# Headlight (front, right) and taillight (rear, left)
c.rect(61, 21, 1, 2, LIGHT)
c.rect(60, 21, 1, 2, "#f0c060")
c.rect(2, 21, 1, 2, RED)

# Wheels
for wx in (14, 42):
    c.circle(wx, 26, 4, TIRE)
    c.circle(wx, 26, 2, RIM)
    c.set(wx, 26, DARK)

# Wheel arches (erase body below wheels)
c.clear(10, 25, 9, 7)
c.clear(38, 25, 9, 7)
for wx in (14, 42):
    c.circle(wx, 26, 4, TIRE)
    c.circle(wx, 26, 2, RIM)
    c.set(wx, 26, DARK)

print(c.stats_text())
save("city-bus", c)
finish(c)
