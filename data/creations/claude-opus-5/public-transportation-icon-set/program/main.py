"""64x64 - 2x2 grid of public transport icons: bus, subway, bicycle, pedestrian."""

c = new_canvas(64, 64, background="#161d2b", name="transit")

BG = c.color("#161d2b", "bg")
GRID = c.color("#283348", "grid")
ICON = c.color("#f2f6fb", "icon")
GLASS = c.color("#5bb7e8", "glass")
ACCENT = c.color("#ffc14d", "accent")
WHEEL = c.color("#46536b", "wheel")


def frame(c):
    c.rect(0, 0, 64, 64, GRID, fill=False)
    c.line(32, 1, 32, 62, GRID)
    c.line(1, 32, 62, 32, GRID)


def ground(c, ox, oy):
    for x in range(4, 27, 3):
        c.rect(ox + x, oy + 25, 2, 1, ACCENT)


def bus(c, ox, oy):
    c.rect(ox + 5, oy + 7, 20, 15, ICON)
    c.set(ox + 5, oy + 7, BG)
    c.set(ox + 24, oy + 7, BG)
    for wx in (7, 12, 17):
        c.rect(ox + wx, oy + 9, 4, 4, GLASS)
    c.rect(ox + 22, oy + 9, 2, 4, GLASS)
    c.rect(ox + 5, oy + 15, 20, 1, ACCENT)
    c.rect(ox + 23, oy + 18, 2, 2, ACCENT)
    for cx in (8, 19):
        c.rect(ox + cx, oy + 21, 4, 4, ICON)
        c.rect(ox + cx + 1, oy + 22, 2, 2, WHEEL)


def subway(c, ox, oy):
    c.rect(ox + 8, oy + 6, 16, 16, ICON)
    c.rect(ox + 9, oy + 5, 14, 1, ICON)
    c.set(ox + 8, oy + 6, BG)
    c.set(ox + 23, oy + 6, BG)
    c.rect(ox + 10, oy + 8, 12, 5, GLASS)
    c.rect(ox + 8, oy + 14, 16, 1, ACCENT)
    c.rect(ox + 15, oy + 16, 2, 6, BG)
    c.rect(ox + 9, oy + 17, 3, 2, ACCENT)
    c.rect(ox + 20, oy + 17, 3, 2, ACCENT)
    for wx in (10, 18):
        c.rect(ox + wx, oy + 21, 4, 4, ICON)
        c.rect(ox + wx + 1, oy + 22, 2, 2, WHEEL)


def tube(c, x0, y0, x1, y1, col, ox=0, oy=0):
    """2px-wide frame tube; thickness added across the shorter axis."""
    c.line(ox + x0, oy + y0, ox + x1, oy + y1, col)
    if abs(x1 - x0) >= abs(y1 - y0):
        c.line(ox + x0, oy + y0 + 1, ox + x1, oy + y1 + 1, col)
    else:
        c.line(ox + x0 + 1, oy + y0, ox + x1 + 1, oy + y1, col)


def bicycle(c, ox, oy):
    # wheels: 2px rims
    for cx in (8, 23):
        c.circle(ox + cx, oy + 18, 6, ICON)
        c.circle(ox + cx, oy + 18, 4, BG)
        c.set(ox + cx, oy + 18, ACCENT)                  # hub
    c.line(ox + 15, oy + 20, ox + 13, oy + 11, ICON)     # seat tube
    c.line(ox + 13, oy + 11, ox + 21, oy + 11, ICON)     # top tube
    c.line(ox + 15, oy + 20, ox + 21, oy + 11, ICON)     # down tube
    c.line(ox + 8, oy + 18, ox + 15, oy + 20, ICON)      # chain stay
    c.line(ox + 8, oy + 18, ox + 13, oy + 12, ICON)      # seat stay
    c.line(ox + 21, oy + 11, ox + 23, oy + 17, ICON)     # fork
    c.set(ox + 21, oy + 10, ICON)                        # stem
    c.rect(ox + 20, oy + 9, 3, 1, ACCENT)                # handlebar
    c.rect(ox + 11, oy + 9, 4, 1, ACCENT)                # saddle
    c.set(ox + 13, oy + 10, ICON)                        # seat post
    c.set(ox + 15, oy + 20, ACCENT)                      # bottom bracket


def thick(c, x0, y0, x1, y1, col, ox=0, oy=0):
    """Two-pixel-wide limb, offset horizontally."""
    c.line(ox + x0, oy + y0, ox + x1, oy + y1, col)
    c.line(ox + x0 + 1, oy + y0, ox + x1 + 1, oy + y1, col)


def pedestrian(c, ox, oy):
    # head, 4x4 with clipped corners
    c.rect(ox + 13, oy + 4, 4, 4, ICON)
    for px, py in ((13, 4), (16, 4), (13, 7), (16, 7)):
        c.set(ox + px, oy + py, BG)
    c.rect(ox + 14, oy + 8, 2, 1, ICON)       # neck
    c.rect(ox + 13, oy + 9, 4, 8, ICON)       # torso
    c.rect(ox + 13, oy + 14, 4, 1, ACCENT)    # belt
    thick(c, 12, 10, 9, 15, ICON, ox, oy)     # rear arm
    thick(c, 16, 10, 19, 14, ICON, ox, oy)    # front arm
    thick(c, 13, 17, 10, 23, ICON, ox, oy)    # rear leg
    thick(c, 15, 17, 18, 23, ICON, ox, oy)    # front leg
    c.rect(ox + 8, oy + 24, 3, 1, ICON)       # rear foot
    c.rect(ox + 19, oy + 24, 3, 1, ICON)      # front foot


frame(c)
# per-cell nudge keeps every icon on the same optical centre
for ox, oy, nudge, draw in ((0, 0, 1, bus), (32, 0, 0, subway),
                            (0, 32, 1, bicycle), (32, 32, 1, pedestrian)):
    ground(c, ox, oy)
    draw(c, ox + nudge, oy)

view(c)
save("transit-icons", c)
print(c.stats_text())
finish(c)
