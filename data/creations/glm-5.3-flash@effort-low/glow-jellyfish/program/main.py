from pixelbench_api import *

c = new_canvas(16, 16, background=None, name="glow-jellyfish")

OUT = "#1a1f3d"   # dark outline
BELL = "#7de8ff"  # translucent bell
GLOW = "#c9f7ff"  # bright glow core
TENT = "#5ab8e8"  # tentacles
DEEP = "#2a3f7a"  # inner shade

# Bell dome
c.line(5, 3, 10, 3, OUT)
c.line(4, 4, 11, 4, OUT)
c.line(3, 5, 12, 5, OUT)
c.line(3, 6, 12, 6, OUT)
c.line(4, 7, 11, 7, OUT)
c.line(5, 8, 10, 8, OUT)
c.line(6, 9, 9, 9, OUT)

# inner fill
c.rect(5, 4, 6, 1, GLOW)
c.rect(4, 5, 8, 1, BELL)
c.rect(4, 6, 8, 1, BELL)
c.rect(5, 7, 6, 1, BELL)
c.rect(6, 8, 4, 1, DEEP)

# highlight
c.set(6, 5, GLOW)
c.set(7, 5, GLOW)
c.set(6, 6, GLOW)

# rim glow pixels just outside outline
c.set(2, 5, BELL)
c.set(13, 5, BELL)
c.set(6, 2, BELL)
c.set(9, 2, BELL)

# tentacles
c.line(6, 10, 6, 13, TENT)
c.line(8, 10, 8, 12, TENT)
c.line(10, 9, 10, 13, TENT)
c.set(6, 13, TENT)
c.set(8, 12, TENT)
c.set(10, 13, TENT)
c.set(9, 10, TENT)
c.set(7, 11, TENT)

print(c.stats_text())
c.matrix_text()
save("glow-jellyfish", c, indexed=True)
finish(c)
