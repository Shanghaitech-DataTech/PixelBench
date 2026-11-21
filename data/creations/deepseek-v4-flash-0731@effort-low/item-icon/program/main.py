from pixelbench_api import *

# palette
dark      = '#20170e'   # near-black dark outline
gold_deep = '#7a5416'
gold_mid  = '#c48a24'
gold_lt   = '#efc250'
gold_hi   = '#ffdf8a'
gold_hot  = '#fff0b8'
cry_dark  = '#14305e'
cry_mid   = '#2a63c6'
cry_lt    = '#5a9cf4'
cry_hi    = '#9fd0ff'
white     = '#eaf6ff'

c = new_canvas(32, 32)  # transparent

CX, CY = 16, 16

# --- thick dark outer outline ---
c.circle(CX, CY, 14, dark)

# --- outer gold band ---
c.circle(CX, CY, 12, gold_mid)
# shading on outer band: light top-left, deep bottom-right
c.circle(CX, CY, 12, gold_lt, fill=False)  # rim
c.circle(CX, CY, 11.2, gold_hot, fill=False).circle(CX, CY, 10.6, gold_lt, fill=False)

# --- dark inner ring ---
c.circle(CX, CY, 10, dark)

# --- inner gold band ---
c.circle(CX, CY, 8, gold_deep)
c.circle(CX, CY, 8, gold_mid, fill=False)
c.circle(CX, CY, 7.4, gold_hi, fill=False)

# --- crystal bezel (dark) ---
c.poly([(16, 9), (23, 16), (16, 23), (9, 16)], dark)
c.poly([(16, 10), (22, 16), (16, 22), (10, 16)], cry_dark)

# --- crystal facets: brighter bottom-right, dark top-left for gem depth ---
c.poly([(16, 11), (21, 16), (16, 21), (11, 16)], cry_mid)
c.poly([(16, 13), (19, 16), (16, 19), (13, 16)], cry_lt)
c.poly([(16, 14.5), (17.6, 16), (16, 17.6), (14.4, 16)], cry_hi)
c.set(15, 15, cry_hi)
c.set(14, 15, cry_lt)

# --- gold needle: thin diagonal cross + bright north arrow ---
# dark needle outline (thin diagonals)
c.line(16, 16, 24, 8, dark)
c.line(16, 16, 8, 8, dark)
c.line(16, 16, 24, 24, dark)
c.line(16, 16, 8, 24, dark)
# gold needle body (lighter in the SW pointing pair)
c.line(15, 16, 23, 8, gold_hi)
c.line(17, 16, 9, 8, gold_hi)
c.line(15, 16, 23, 24, gold_mid)
c.line(17, 16, 9, 24, gold_mid)
# north arrowhead (bright gold)
c.poly([(16, 10), (18, 13), (14, 13)], gold_hot)
# south arrowhead
c.poly([(16, 22), (18, 19), (14, 19)], cry_hi)
# center pivot
c.circle(CX, CY, 2, dark)
c.set(CX, CY, gold_hot)

# --- cardinal ticks on outer gold band ---
def tick(x, y):
    c.set(x, y, gold_hot)
c.set(16, 3, gold_hot); c.set(16, 4, gold_hot)
c.set(16, 28, gold_hot); c.set(16, 29, gold_hot)
c.set(3, 16, gold_hot); c.set(4, 16, gold_hot)
c.set(28, 16, gold_hot); c.set(29, 16, gold_hot)

# diagonal dots
c.set(8, 8, gold_hi); c.set(24, 8, gold_hi)
c.set(8, 24, gold_hi); c.set(24, 24, gold_hi)

print(c.stats_text())
print(c.matrix_text())
finish(c)

