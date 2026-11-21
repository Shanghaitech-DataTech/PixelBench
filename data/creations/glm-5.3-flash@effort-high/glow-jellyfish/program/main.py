from pixelbench_api import *

c = new_canvas(16, 16, background=None, name="glow-jellyfish")

OUT  = c.color("#141c33", name="outline")     # dark navy outline
EDGE = c.color("#3fd6e8", name="bell_edge")   # cyan bell rim
BODY = c.color("#8ef2ff", name="bell_body")   # translucent body
GLOW = c.color("#dfffff", name="glow_core")   # bright core
TENT = c.color("#35b8cc", name="tentacle")    # tentacle
TDIM = c.color("#1f7a8c", name="tentacle_dim")
SPARK= c.color("#9ff0ff", name="spark")       # ambient glow dots

# --- Bell outline (dome) ---
for x in range(6, 10):
    c.set(x, 1, OUT)
for x in (4, 5, 10, 11):
    c.set(x, 2, OUT)
for x in (3, 12):
    c.set(x, 3, OUT)
    c.set(x, 4, OUT)
    c.set(x, 5, OUT)
for x in (4, 5, 10, 11):
    c.set(x, 6, OUT)

# --- Bell interior ---
c.rect(6, 2, 4, 1, BODY)                 # y2: 6..9
c.rect(5, 3, 6, 1, BODY)                 # y3
c.rect(5, 4, 6, 1, BODY)                 # y4
c.rect(5, 5, 6, 1, BODY)                 # y5
c.rect(6, 6, 4, 1, BODY)                 # y6

# bright core
c.set(7, 3, GLOW); c.set(8, 3, GLOW)
c.set(6, 4, GLOW); c.set(7, 4, GLOW); c.set(8, 4, GLOW); c.set(9, 4, GLOW)
c.set(7, 5, GLOW); c.set(8, 5, GLOW)

# rim highlight just inside the outline
c.set(4, 3, EDGE); c.set(11, 3, EDGE)
c.set(4, 4, EDGE); c.set(11, 4, EDGE)
c.set(4, 5, EDGE); c.set(11, 5, EDGE)
c.set(6, 2, EDGE); c.set(9, 2, EDGE)

# --- Bottom rim / frill ---
c.set(3, 6, OUT)
c.set(12, 6, OUT)
for x in range(5, 11):
    c.set(x, 7, EDGE)
c.set(4, 7, OUT); c.set(11, 7, OUT)

# --- Tentacles (short, wavy) ---
# left
c.set(4, 8, TENT); c.set(4, 9, TENT); c.set(3, 10, TDIM); c.set(3, 11, TDIM)
# mid-left
c.set(6, 8, TENT); c.set(6, 9, TENT); c.set(5, 10, TENT); c.set(5, 11, TDIM)
# mid-right
c.set(9, 8, TENT); c.set(9, 9, TENT); c.set(10, 10, TENT); c.set(10, 11, TDIM)
# right
c.set(11, 8, TDIM); c.set(12, 9, TDIM); c.set(12, 10, TDIM)

# --- Ambient glow sparks around the bell ---
c.set(2, 2, SPARK); c.set(13, 3, SPARK)
c.set(1, 5, SPARK); c.set(14, 6, SPARK)
c.set(2, 8, SPARK); c.set(13, 12, SPARK)

print(c.stats_text())
print(c.matrix_text())
view(c, scale=24)
save("glow-jellyfish", c)
finish(c)
