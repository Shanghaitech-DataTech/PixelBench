# Seamless carpet pattern, 32x32.
# Everything is computed from (x % 16, y % 16), so the pattern has period 16
# in both axes -> tiles seamlessly at 32 in all directions.

OUT  = '#3a1b14'   # dark brown outline
GOLD = '#d9a13b'   # border gold
A1   = '#b8472e'   # terracotta fill (light)
A2   = '#a03a26'   # terracotta fill (dark, weave)
B1   = '#7c2a23'   # deep red background diamond (light)
B2   = '#6b231e'   # deep red background diamond (dark, weave)
PET  = '#e9c66c'   # petal cream-gold
FC   = '#e0762a'   # flower center orange
LEAF = '#7d5f26'   # dark gold leaf
CRM  = '#f2e2b2'   # bright cream dots

c = new_canvas(32, 32, background=B1, name="carpet")

for y in range(32):
    for x in range(32):
        cx = (x % 16) - 8
        cy = (y % 16) - 8
        m = abs(cx) + abs(cy)          # manhattan distance from diamond centre
        axis = (cx == 0 or cy == 0)    # on a diamond tip axis
        chk = ((x + y) % 2) == 0       # woven checker

        if m <= 1:
            col = FC                                # flower centre
        elif m == 2 and not axis:
            col = LEAF                              # diagonal leaves
        elif axis and m <= 4:
            col = PET                               # 4 petals
        elif m <= 5:
            col = A1 if chk else A2                 # diamond A fill, woven
        elif m == 6:
            col = GOLD                              # A gold border
        elif m == 7:
            col = CRM if axis else OUT              # dark separator + cream tips
        elif m == 8:
            col = CRM if axis else GOLD             # B gold border + knot dots
        elif m == 13 and axis:
            col = GOLD                              # mini-flower petals around bg centre
        elif m <= 13:
            col = B1 if chk else B2                 # background diamond fill
        elif m == 14:
            col = GOLD                              # small motif ring
        else:
            col = CRM                               # background-diamond centre
        c.set(x, y, col)

# Working preview: 2x2 tiling to verify seamlessness (not submitted).
tile = new_canvas(64, 64, name="tile_check")
for dy in range(2):
    for dx in range(2):
        tile.blit(c, dx * 32, dy * 32)

view(tile)
view(c)
finish(c)
