# 64x32 city bus, side view, facing right
c = new_canvas(64, 32, background=None, name="city_bus")

OUT      = "#23272e"
BODY     = "#eef1f4"
BODY_D   = "#c3ccd4"
STRIPE   = "#1790d6"
STRIPE_D = "#0f6ca6"
GLASS    = "#2b4157"
GLASS_L  = "#8fc3dd"
TIRE     = "#191d22"
HUB      = "#a9b2bb"
HUB_D    = "#78828c"
LIGHT    = "#ffd94f"
IND      = "#ff9d2e"
TAIL     = "#e5483f"
DISP     = "#16130c"
AMBER    = "#ffb42a"
BUMP     = "#454d56"
SHADOW   = (20, 24, 30, 70)

# ground shadow
c.ellipse(32, 30, 27, 1, SHADOW)

# roof AC pod
c.rect(24, 5, 17, 2, BODY)

# main body silhouette (front slopes down to the right)
c.poly([(4, 7), (57, 7), (61, 10), (62, 15), (62, 22), (60, 26),
        (4, 26), (3, 25), (3, 8)], BODY)
c.outline(OUT)

# pod vents
for x in (27, 32, 37):
    c.rect(x, 6, 2, 1, BODY_D)

# side route display (amber dot-matrix on black)
c.rect(44, 8, 8, 3, DISP)
for x in (46, 47, 49, 50):
    c.set(x, 9, AMBER)

# window band with highlight and pillars
c.rect(5, 11, 46, 5, GLASS)
c.rect(5, 11, 46, 1, GLASS_L)
for x in (9, 14, 19, 24, 29, 41, 46):
    c.rect(x, 11, 1, 5, BODY)

# windshield (sloped front)
c.poly([(59, 10), (61, 12), (61, 15), (59, 15)], GLASS)
c.set(59, 11, GLASS_L)
c.set(60, 12, GLASS_L)

# livery stripe + lower skirt shading
c.rect(4, 17, 58, 2, STRIPE)
c.rect(4, 19, 58, 1, STRIPE_D)
c.rect(4, 24, 57, 1, BODY_D)

# rear + front double doors
for x0 in (30, 52):
    c.rect(x0, 11, 7, 13, OUT)          # frame
    c.rect(x0 + 1, 12, 5, 8, GLASS)     # glass
    c.rect(x0 + 1, 12, 5, 1, GLASS_L)   # glass highlight
    c.rect(x0 + 3, 12, 1, 8, OUT)       # centre seam
    c.rect(x0 + 1, 20, 5, 3, BODY)      # lower panel

# rear engine grille
c.rect(5, 20, 4, 2, BODY_D)

# wheels (arch, tire, hub)
for cx in (16, 44):
    c.circle(cx, 25, 5, OUT)
    c.circle(cx, 26, 4, TIRE)
    c.circle(cx, 26, 2, HUB)
    c.set(cx, 26, HUB_D)

# lights and bumpers
c.rect(61, 20, 2, 2, LIGHT)   # headlight
c.rect(61, 18, 2, 1, IND)     # front indicator
c.rect(60, 23, 3, 3, BUMP)    # front bumper
c.rect(3, 18, 1, 3, TAIL)     # taillight
c.set(3, 17, IND)
c.rect(3, 23, 3, 3, BUMP)     # rear bumper

# side mirror
c.set(62, 10, OUT)
c.set(63, 10, OUT)
c.set(63, 11, OUT)

view(c)
finish(c)
