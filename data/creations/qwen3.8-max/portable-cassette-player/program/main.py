from pixelbench_api import new_canvas, view, save, finish

c = new_canvas(32, 32, name="cassette_player")

# ---------------- palette ----------------
OUT    = '#1a1c2c'   # near-black outline
NAVY   = '#29366f'   # dark blue shade
BLUE   = '#3b5dc9'   # body blue
BLT    = '#41a6f6'   # body highlight
GREY   = '#c0cbdc'   # light grey
GREYM  = '#94b0c2'   # mid grey
GREYD  = '#566c86'   # dark grey / metal
SLATE  = '#333c57'   # reel + tape
RED    = '#b13e53'
ORANGE = '#ef7d57'

# ---------------- headphone cable ----------------
for p in [(24, 3), (24, 2), (23, 1), (22, 0), (21, 0), (20, 0), (19, 0),
          (18, 1), (17, 1), (16, 2), (15, 2), (14, 2), (13, 2)]:
    c.set(p[0], p[1], OUT)
# jack plug at the free end
c.rect(11, 1, 2, 3, GREYM)
c.set(11, 1, GREY); c.set(11, 2, GREY); c.set(11, 3, GREY)
c.set(10, 2, GREY)

# ---------------- body ----------------
c.rect(2, 4, 28, 28, OUT)                       # dark slab -> 1px outline
for p in [(2, 4), (3, 4), (2, 5), (29, 4), (28, 4), (29, 5),
          (2, 31), (3, 31), (2, 30), (29, 31), (28, 31), (29, 30)]:
    c.set(p[0], p[1], None)                     # rounded slab corners
c.rect(3, 5, 26, 26, BLUE)                      # shell
for p in [(3, 5), (4, 5), (3, 6), (28, 5), (27, 5), (28, 6),
          (3, 30), (4, 30), (3, 29), (28, 30), (27, 30), (28, 29)]:
    c.set(p[0], p[1], OUT)                      # rounded shell corners
# light from top-left
c.rect(5, 5, 22, 1, BLT)
c.set(4, 6, BLT)
c.rect(3, 7, 1, 22, BLT)
# shade bottom-right
c.rect(5, 30, 22, 1, NAVY)
c.set(27, 29, NAVY)
c.rect(28, 7, 1, 22, NAVY)

# ---------------- top panel: jack socket, LED, volume slider ----------------
c.rect(23, 5, 3, 2, GREYD)      # jack plate
c.set(24, 5, OUT)               # socket hole (cable enters here)

c.set(4, 7, ORANGE); c.set(5, 7, RED)
c.set(4, 8, RED);    c.set(5, 8, RED)

c.rect(8, 8, 14, 1, NAVY)       # slider track  x=8..21
c.rect(9, 8, 5, 1, GREYM)       # level filled so far
c.rect(14, 6, 3, 4, GREY)       # knob
c.rect(16, 6, 1, 4, GREYM)
c.rect(14, 9, 3, 1, GREYM)
c.set(9, 6, NAVY); c.set(11, 6, NAVY)
c.set(19, 6, NAVY)

# ---------------- cassette window (transparent) ----------------
c.rect(6, 10, 20, 12, OUT)      # bezel x=6..25 y=10..21
c.set(6, 10, BLUE); c.set(25, 10, BLUE)
c.set(6, 21, BLUE); c.set(25, 21, BLUE)
corners = {(7, 11), (24, 11), (7, 20), (24, 20)}
for y in range(11, 21):
    for x in range(7, 25):
        if (x, y) in corners:
            continue
        c.set(x, y, None)       # punch the see-through window

# two tape reels
for cx in (11, 20):
    c.circle(cx, 15, 3, SLATE)
    c.circle(cx, 15, 1, GREYM)
    c.set(cx, 15, GREY)
# tape running under the reels
c.line(9, 19, 22, 19, SLATE)
c.set(9, 18, SLATE); c.set(22, 18, SLATE)

# ---------------- playback controls ----------------
for x in (4, 9, 14, 19, 24):
    c.rect(x, 23, 4, 5, GREY)   # key cap
    c.rect(x, 28, 4, 1, NAVY)   # cast shadow

for p in [(5, 24), (7, 24), (4, 25), (5, 25), (6, 25), (7, 25),
          (5, 26), (7, 26)]:
    c.set(p[0], p[1], OUT)                                  # rewind
for p in [(9, 24), (10, 24), (9, 25), (10, 25), (11, 25),
          (9, 26), (10, 26)]:
    c.set(p[0], p[1], OUT)                                  # play
for p in [(14, 24), (16, 24), (14, 25), (15, 25), (16, 25), (17, 25),
          (14, 26), (16, 26)]:
    c.set(p[0], p[1], OUT)                                  # fast forward
c.rect(19, 24, 4, 3, OUT)                                   # stop
c.rect(25, 24, 2, 2, RED)                                   # record dot
c.set(25, 24, ORANGE)

print(c.stats_text())
print(c.matrix_text())
print(view(c, scale=16, margin=1))
save("cassette_player", c, indexed=True)
finish(c)
