from pixelbench_api import new_canvas, view, finish

# 64x32 side-view city bus sprite on transparency.
c = new_canvas(64, 32, background=None, name="city_bus")

# Palette: cool modern transit livery with warm safety accents.
outline = "#172838"
deep = "#203848"
window = "#294c60"
window_hi = "#6fa2b2"
window_glint = "#a8ced3"
body_shadow = "#6f8790"
body = "#d7e2df"
body_hi = "#f0f5ef"
teal_dark = "#16727a"
teal = "#1f9ca0"
teal_hi = "#54bdba"
yellow = "#f0b83f"
red = "#d64e3c"
rubber = "#1b2229"
hub_dark = "#53656d"
hub = "#a8b7b6"
light = "#ffe291"
route = "#f5be48"

# Main stepped silhouette and lower shadow.
c.poly([(4,8),(7,6),(53,6),(58,8),(60,12),(60,23),(57,25),(6,25),(3,22),(3,11)], outline)
c.poly([(5,9),(8,7),(52,7),(56,9),(58,12),(58,21),(56,23),(6,23),(5,21)], body)
c.rect(5,18,53,5,body_shadow)
c.rect(6,18,51,3,body)
c.rect(6,21,51,2,teal_dark)
c.rect(7,20,49,2,teal)
c.rect(7,20,22,1,teal_hi)

# Dark continuous window band.
c.rect(7,8,47,8,deep)
c.rect(8,9,45,6,window)
# Rear destination/route display.
c.rect(8,9,8,4,outline)
c.rect(9,10,6,2,route)
c.set(10,10,outline).set(13,11,outline)

# Passenger windows with slim pillars and pixel reflections.
for x, w in [(17,6),(24,6),(31,6),(38,6),(45,7)]:
    c.rect(x,9,w,6,window)
    c.rect(x,9,w,1,window_hi)
    c.set(x+1,10,window_glint)
    if w > 6:
        c.set(x+2,10,window_glint)
# Pillars.
for x in [16,23,30,37,44,52]:
    c.rect(x,8,1,8,outline)

# Rear door, lower body cut and glazing.
c.rect(13,8,7,15,outline)
c.rect(14,9,5,13,body_shadow)
c.rect(15,10,3,7,window)
c.rect(15,10,3,1,window_hi)
c.rect(15,18,3,3,body_hi)
c.rect(18,9,1,13,deep)
c.set(14,22,yellow)

# Front door, wider and angled with paired glass panels.
c.poly([(48,8),(55,8),(57,11),(57,23),(48,23)], outline)
c.poly([(49,9),(54,9),(56,11),(56,22),(49,22)], body_shadow)
c.poly([(50,10),(53,10),(55,12),(55,17),(50,17)], window)
c.line(53,10,53,17,outline)
c.rect(50,18,5,3,body_hi)
c.rect(49,21,7,1,teal)
c.set(50,11,window_glint).set(54,12,window_hi)
# Door handles.
c.set(52,18,deep).set(53,18,deep)

# Driver windscreen and electronic route display above it.
c.poly([(53,8),(56,9),(58,12),(58,15),(55,15),(55,11)], window)
c.line(54,8,55,15,outline)
c.set(56,10,window_hi).set(57,12,window_glint)
c.rect(45,7,8,3,outline)
c.rect(46,8,6,1,route)
c.set(48,8,deep).set(51,8,deep)

# Body highlights, bumpers, lamps and small access details.
c.rect(7,17,5,1,body_hi)
c.rect(22,17,24,1,body_hi)
c.rect(4,19,2,3,deep)
c.rect(3,22,5,2,outline)
c.rect(57,21,4,3,outline)
c.rect(58,19,2,2,light)
c.set(59,18,light)
c.rect(4,16,2,2,red)
c.rect(8,22,3,1,yellow)
c.rect(28,19,10,1,"#b8c7c5")
c.set(32,19,deep).set(33,19,deep)

# Wheel arches are implied by wheels overlaying the lower body.
for cx in (15, 49):
    c.circle(cx,24,5,outline)
    c.circle(cx,25,4,rubber)
    c.circle(cx,25,2,hub_dark)
    c.circle(cx,25,1,hub)
    c.set(cx,25,body_hi)
    c.set(cx-2,23,"#34434a")

# Ground-facing chassis pixels and tiny mirror.
c.rect(23,24,18,2,deep)
c.rect(24,24,16,1,body_shadow)
c.rect(58,10,3,1,outline)
c.set(60,11,outline)

view(c, scale=12, margin=0)
finish(c)
