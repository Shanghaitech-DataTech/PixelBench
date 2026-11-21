c = new_canvas(64, 64, background=None, name="output")

bg = c.color("#26364F", name="bg")
white = c.color("#FFFFFF", name="white")

c.rect(0, 0, 64, 64, bg)


def hline(x0, x1, y, col):
    c.rect(x0, y, x1 - x0 + 1, 2, col)


def vline(x, y0, y1, col):
    c.rect(x, y0, 2, y1 - y0 + 1, col)


def thick_line(x0, y0, x1, y1, col):
    c.line(x0, y0, x1, y1, col)
    if abs(x1 - x0) >= abs(y1 - y0):
        c.line(x0, y0 + 1, x1, y1 + 1, col)
    else:
        c.line(x0 + 1, y0, x1 + 1, y1, col)


def rect_outline2(x, y, w, h, col):
    c.rect(x, y, w, h, col, fill=True)
    c.rect(x + 2, y + 2, w - 4, h - 4, bg, fill=True)


def circle_ring2(cx, cy, r, col):
    c.circle(cx, cy, r, col, fill=True)
    c.circle(cx, cy, r - 2, bg, fill=True)


def draw_bus(ox, oy):
    # Body outline (2px), with a 4px window band and 3 windows.
    rect_outline2(ox + 2, oy + 5, 20, 13, white)
    # Window sill.
    hline(ox + 4, ox + 19, oy + 11, white)
    # Window dividers.
    vline(ox + 8, oy + 7, oy + 10, white)
    vline(ox + 14, oy + 7, oy + 10, white)
    # Wheels.
    circle_ring2(ox + 7, oy + 20, 3, white)
    circle_ring2(ox + 16, oy + 20, 3, white)


def draw_subway(ox, oy):
    # Front-facing train: rounded roof and straight sides.
    c.ellipse(ox + 12, oy + 7, 9, 6, white, fill=True)
    c.rect(ox + 3, oy + 7, 18, 12, white, fill=True)
    # Hollow out the interior, leaving a 2px shell.
    c.ellipse(ox + 12, oy + 7, 7, 4, bg, fill=True)
    c.rect(ox + 5, oy + 7, 14, 10, bg, fill=True)
    # Central pillar and window sill: the dark shell interior becomes two windows.
    vline(ox + 11, oy + 4, oy + 12, white)
    hline(ox + 6, ox + 17, oy + 12, white)
    # Headlights.
    c.rect(ox + 6, oy + 15, 2, 2, white, fill=True)
    c.rect(ox + 16, oy + 15, 2, 2, white, fill=True)


def draw_bicycle(ox, oy):
    # Wheels as 2px rings.
    circle_ring2(ox + 6, oy + 15, 4, white)
    circle_ring2(ox + 17, oy + 15, 4, white)
    # Chain stay: rear hub to bottom bracket.
    hline(ox + 6, ox + 11, oy + 15, white)
    # Seat tube.
    thick_line(ox + 11, oy + 15, ox + 9, oy + 6, white)
    # Down tube.
    thick_line(ox + 11, oy + 15, ox + 16, oy + 5, white)
    # Top tube.
    thick_line(ox + 9, oy + 6, ox + 16, oy + 5, white)
    # Seat stay.
    thick_line(ox + 9, oy + 6, ox + 6, oy + 15, white)
    # Fork.
    thick_line(ox + 16, oy + 5, ox + 17, oy + 15, white)
    # Saddle and handlebar.
    hline(ox + 7, ox + 11, oy + 5, white)
    hline(ox + 15, ox + 19, oy + 4, white)


def draw_pedestrian(ox, oy):
    # Head.
    circle_ring2(ox + 12, oy + 5, 3, white)
    # Torso.
    vline(ox + 12, oy + 8, oy + 14, white)
    # Arms.
    thick_line(ox + 12, oy + 10, ox + 7, oy + 13, white)
    thick_line(ox + 12, oy + 10, ox + 17, oy + 13, white)
    # Legs.
    thick_line(ox + 12, oy + 14, ox + 7, oy + 21, white)
    thick_line(ox + 12, oy + 14, ox + 17, oy + 21, white)
    # Feet.
    hline(ox + 5, ox + 8, oy + 21, white)
    hline(ox + 16, ox + 19, oy + 21, white)


draw_bus(4, 2)
draw_subway(36, 6)
draw_bicycle(4, 36)
draw_pedestrian(36, 36)

finish(c)
