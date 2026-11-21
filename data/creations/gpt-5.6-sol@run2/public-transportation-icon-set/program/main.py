from pixelbench_api import new_canvas, view, finish

# 64x64 public transportation icon set
c = new_canvas(64, 64, background="#10283a", name="public-transportation-icon-set")

NAVY = "#10283a"
PANEL = "#173b4f"
FRAME = "#2b6070"
INK = "#f2ead3"
SHADOW = "#92b7b6"
TEAL = "#27c4aa"
YELLOW = "#f6c453"
CORAL = "#ee6f5d"

# Shared pixel-cut panel frame.
def panel(x, y):
    c.rect(x + 2, y, 24, 28, FRAME)
    c.rect(x, y + 2, 28, 24, FRAME)
    c.rect(x + 2, y + 2, 24, 24, PANEL)
    # inset corner ticks establish a consistent transit-sign frame
    c.rect(x + 3, y + 3, 4, 2, SHADOW)
    c.rect(x + 3, y + 3, 2, 4, SHADOW)
    c.rect(x + 21, y + 3, 4, 2, SHADOW)
    c.rect(x + 23, y + 3, 2, 4, SHADOW)

panel(3, 3)
panel(33, 3)
panel(3, 33)
panel(33, 33)

# BUS — front elevation, top-left.
# destination cap and body
c.rect(10, 9, 14, 2, YELLOW)
c.rect(8, 11, 18, 15, INK)
c.rect(10, 9, 14, 3, INK)
c.rect(12, 9, 10, 2, PANEL)
# windshield with central mullion
c.rect(10, 13, 14, 6, NAVY)
c.rect(16, 13, 2, 6, INK)
c.rect(11, 14, 4, 1, SHADOW)
c.rect(19, 14, 4, 1, SHADOW)
# belt, bumper, lights
c.rect(8, 20, 18, 2, TEAL)
c.rect(10, 23, 3, 2, YELLOW)
c.rect(21, 23, 3, 2, YELLOW)
c.rect(10, 26, 4, 2, NAVY)
c.rect(20, 26, 4, 2, NAVY)
c.rect(9, 25, 16, 2, INK)

# SUBWAY — rounded tunnel train, top-right.
# route marker and roof silhouette
c.rect(43, 8, 10, 2, CORAL)
c.rect(40, 11, 16, 2, INK)
c.rect(38, 13, 20, 11, INK)
c.rect(40, 11, 16, 15, INK)
# twin front windows
c.rect(41, 14, 6, 6, NAVY)
c.rect(49, 14, 6, 6, NAVY)
c.rect(42, 15, 4, 1, SHADOW)
c.rect(50, 15, 4, 1, SHADOW)
# nose band, lights and rails
c.rect(40, 21, 16, 2, CORAL)
c.rect(42, 23, 3, 2, YELLOW)
c.rect(51, 23, 3, 2, YELLOW)
c.rect(42, 26, 3, 2, INK)
c.rect(51, 26, 3, 2, INK)
c.line(44, 25, 41, 28, SHADOW)
c.line(52, 25, 55, 28, SHADOW)

# BICYCLE — side profile, bottom-left.
# Compact ring wheels respect the same two-pixel inset as every other icon.
c.circle(10, 52, 4, INK, fill=False)
c.circle(24, 52, 4, INK, fill=False)
c.circle(10, 52, 2, PANEL, fill=False)
c.circle(24, 52, 2, PANEL, fill=False)
# hubs
c.rect(9, 51, 2, 2, YELLOW)
c.rect(23, 51, 2, 2, YELLOW)
# angular teal frame
c.line(10, 52, 15, 44, TEAL)
c.line(15, 44, 19, 52, TEAL)
c.line(19, 52, 10, 52, TEAL)
c.line(19, 52, 22, 44, TEAL)
c.line(22, 44, 24, 52, TEAL)
c.line(15, 44, 22, 44, TEAL)
c.rect(13, 42, 6, 2, INK)
c.rect(20, 41, 2, 4, INK)
c.rect(21, 40, 5, 2, INK)

# PEDESTRIAN — dynamic walking figure, bottom-right.
# square pixel head with highlight
c.rect(46, 39, 6, 6, INK)
c.rect(48, 40, 3, 2, YELLOW)
# torso with accent vest
c.rect(45, 46, 8, 8, INK)
c.rect(47, 46, 4, 7, CORAL)
# bent arms
c.rect(41, 47, 5, 3, INK)
c.rect(40, 49, 3, 6, INK)
c.rect(52, 47, 4, 3, INK)
c.rect(55, 49, 3, 5, INK)
# separated walking legs
c.rect(45, 53, 4, 4, INK)
c.rect(43, 56, 6, 3, INK)
c.rect(50, 53, 4, 4, INK)
c.rect(53, 56, 5, 3, INK)
# shoe soles stay within the shared lower inset.
c.rect(42, 58, 7, 1, TEAL)
c.rect(53, 58, 6, 1, TEAL)

view(c, scale=8, margin=0)
finish(c)
