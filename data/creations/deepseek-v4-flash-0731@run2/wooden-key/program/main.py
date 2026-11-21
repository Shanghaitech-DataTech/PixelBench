from pixelbench_api import *

a = '#2B1A0F'   # dark wood outline
b = '#A06A3C'   # wood
c = '#D39C64'   # light wood
d = '#6E421F'   # dark wood shade
e = '#EFD9A7'   # pale highlight
f = '#C0392B'   # red ribbon

cv = new_canvas(16, 16, name="wooden_key")

# --- wooden ring head ---
cv.circle(4, 8, 3, a)          # outer outline  x1..7  y5..11
cv.circle(4, 8, 2, b)          # wood band      x2..6  y6..10
cv.circle(4, 8, 1, None)       # hole           x3..5  y7..9
# wood grain & lighting on the head
cv.set(3, 6, e)                # glint top-left
cv.set(4, 6, e)
cv.set(2, 7, c)                # left side light
cv.set(5, 10, d)               # bottom-right shade
cv.set(5, 9, c)

# --- shaft ---
cv.rect(7, 7, 6, 3, a)        # outline  x7..12  y7..9
cv.rect(8, 7, 4, 2, b)        # wood     x8..11  y7..8
cv.rect(9, 7, 2, 1, c)        # light    x9..10  y7
cv.set(10, 8, d)               # grain

# --- teeth at the right end ---
cv.rect(9, 10, 2, 2, a)       # short tooth x9..10 y10..11
cv.rect(9, 11, 1, 1, b)
cv.set(9, 10, c)
cv.rect(11, 10, 2, 3, a)      # long tooth  x11..12 y10..12
cv.rect(11, 11, 2, 1, b)
cv.set(12, 11, d)

# --- small red ribbon at the neck ---
cv.rect(6, 7, 2, 2, f)        # knot x6..7 y7..8
cv.set(6, 9, f)                # tail

# center the sprite (bbox x1..12, y5..12 -> shift +2,+0)
cv.shift(2, 0)

finish(cv)

print(cv.stats_text())
print(cv.matrix_text())
