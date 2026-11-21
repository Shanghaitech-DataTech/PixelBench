from pixelbench_api import *

# A compact, four-color public-transit pictogram set on a shared night-grid palette.
W = H = 64
bg = '#101a2b'
panel = '#18283c'
panel_hi = '#20364d'
frame = '#3c5a70'
ink = '#e8f1ef'
ink_dim = '#a8c0c5'
shadow = '#0b1320'
coral = '#f27662'
cyan = '#54c7d5'
yellow = '#f2c451'
green = '#79d48d'

c = new_canvas(W, H, bg, name='public_transportation_icon_set')

# Four identical framed cells: 28x28 with a 2px gutter and 3px outer margin.
def tile(x, y, accent):
    c.rect(x, y, 28, 28, panel, fill=True)
    c.rect(x, y, 28, 28, frame, fill=False)
    c.rect(x+2, y+2, 24, 1, panel_hi, fill=True)
    c.rect(x+2, y+25, 24, 1, shadow, fill=True)
    # tiny accent locator marks make the four cells read as one designed set
    c.rect(x+2, y+2, 4, 1, accent, fill=True)
    c.rect(x+22, y+25, 4, 1, accent, fill=True)

tile(3, 3, coral)
tile(33, 3, cyan)
tile(3, 33, yellow)
tile(33, 33, green)

# BUS, top left. Silhouette stays inside a 20x20 footprint.
# shadow/underbody
c.rect(8, 23, 18, 2, shadow, fill=True)
c.rect(8, 10, 18, 13, ink, fill=True)
c.rect(10, 8, 14, 3, ink, fill=True)
# rounded-ish roof corners cut into the block
c.rect(9, 9, 1, 2, panel, fill=True)
c.rect(24, 9, 1, 2, panel, fill=True)
# windshield and windows
c.rect(10, 11, 14, 5, coral, fill=True)
c.rect(11, 12, 5, 3, panel, fill=True)
c.rect(18, 12, 5, 3, panel, fill=True)
# window glints
c.rect(12, 12, 2, 1, panel_hi, fill=True)
c.rect(19, 12, 2, 1, panel_hi, fill=True)
# body stripe and lower body
c.rect(8, 17, 18, 2, coral, fill=True)
c.rect(10, 19, 14, 4, ink_dim, fill=True)
c.rect(8, 22, 18, 1, coral, fill=True)
# bumpers and wheels
c.rect(7, 21, 1, 3, ink_dim, fill=True)
c.rect(25, 21, 1, 3, ink_dim, fill=True)
c.rect(11, 22, 4, 4, shadow, fill=True)
c.rect(19, 22, 4, 4, shadow, fill=True)
c.rect(12, 23, 2, 2, ink_dim, fill=True)
c.rect(20, 23, 2, 2, ink_dim, fill=True)
# door divisions / lights
c.rect(17, 19, 1, 3, coral, fill=True)
c.rect(9, 19, 2, 1, yellow, fill=True)
c.rect(23, 19, 2, 1, yellow, fill=True)

# SUBWAY, top right. A front-facing train with track marks.
c.rect(38, 23, 18, 2, shadow, fill=True)
c.rect(38, 10, 18, 13, ink, fill=True)
c.rect(40, 8, 14, 3, ink, fill=True)
c.rect(39, 9, 1, 2, panel, fill=True)
c.rect(54, 9, 1, 2, panel, fill=True)
# single broad destination band and two windows
c.rect(40, 11, 14, 3, cyan, fill=True)
c.rect(41, 12, 5, 1, panel, fill=True)
c.rect(48, 12, 5, 1, panel, fill=True)
c.rect(41, 15, 5, 4, panel, fill=True)
c.rect(48, 15, 5, 4, panel, fill=True)
# reflected window pixels
c.rect(42, 15, 2, 1, panel_hi, fill=True)
c.rect(49, 15, 2, 1, panel_hi, fill=True)
# nose and doors
c.rect(39, 19, 16, 3, cyan, fill=True)
c.rect(46, 19, 2, 4, ink, fill=True)
c.rect(38, 22, 18, 1, cyan, fill=True)
# headlights and wheels
c.rect(40, 20, 2, 1, yellow, fill=True)
c.rect(52, 20, 2, 1, yellow, fill=True)
c.rect(42, 22, 4, 4, shadow, fill=True)
c.rect(50, 22, 4, 4, shadow, fill=True)
c.rect(43, 23, 2, 2, ink_dim, fill=True)
c.rect(51, 23, 2, 2, ink_dim, fill=True)
# rails / station signal underneath
c.rect(37, 26, 20, 1, frame, fill=True)
c.rect(40, 27, 1, 1, cyan, fill=True)
c.rect(53, 27, 1, 1, cyan, fill=True)

# BICYCLE, bottom left. Two exact pixel wheels and a bright frame.
# wheel rings: dark outside, ink rim, panel hub
c.circle(10, 48, 6, shadow, fill=True)
c.circle(10, 48, 5, ink_dim, fill=True)
c.circle(10, 48, 3, panel, fill=True)
c.circle(24, 48, 6, shadow, fill=True)
c.circle(24, 48, 5, ink_dim, fill=True)
c.circle(24, 48, 3, panel, fill=True)
# frame geometry
c.line(10, 48, 15, 40, yellow)
c.line(15, 40, 20, 48, yellow)
c.line(20, 48, 10, 48, yellow)
c.line(15, 40, 24, 48, yellow)
# crisp central joint and pedal accent
c.rect(14, 47, 3, 2, yellow, fill=True)
c.set(15, 48, ink)
c.line(15, 40, 19, 40, yellow)
# fork, seat post, handlebar
c.line(24, 48, 22, 39, yellow)
c.line(22, 39, 24, 38, yellow)
c.line(24, 38, 25, 39, yellow)
c.line(15, 40, 14, 37, yellow)
c.rect(12, 36, 5, 1, yellow, fill=True)
c.rect(20, 37, 4, 1, yellow, fill=True)
# frame highlights and hubs
c.set(15, 41, ink)
c.set(20, 47, ink)
c.set(10, 48, ink)
c.set(24, 48, ink)
# tiny ground shadow
c.rect(8, 55, 18, 1, shadow, fill=True)

# PEDESTRIAN, bottom right. Consistent bright 2px stroke and compact stance.
# head
c.circle(47, 38, 3, green, fill=True)
c.set(46, 37, ink,)
# neck, torso and shoulders, made as stepped pixel geometry
c.rect(46, 41, 3, 2, green, fill=True)
c.rect(45, 42, 5, 8, green, fill=True)
c.rect(43, 43, 2, 2, green, fill=True)
c.rect(50, 43, 2, 2, green, fill=True)
# negative separation to clarify limbs
c.rect(46, 47, 3, 1, panel, fill=True)
# arms angled in pixel steps
c.line(44, 44, 40, 49, green)
c.line(51, 44, 54, 48, green)
c.rect(39, 49, 3, 2, green, fill=True)
c.rect(53, 48, 3, 2, green, fill=True)
# legs, with sturdy feet
c.line(46, 49, 43, 55, green)
c.line(49, 49, 52, 55, green)
c.rect(41, 55, 4, 2, green, fill=True)
c.rect(51, 55, 4, 2, green, fill=True)
# subtle highlight makes the figure read at 64px
c.rect(46, 42, 1, 4, ink, fill=True)
c.rect(45, 53, 1, 2, ink, fill=True)
# ground baseline shared with the other pictograms
c.rect(39, 58, 16, 1, shadow, fill=True)

view(c)
finish(c)
