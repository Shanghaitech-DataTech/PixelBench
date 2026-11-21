from pixelbench_api import new_canvas, finish

c = new_canvas(16, 16)

DARK = "#3a2310"   # dark wood outline
MID = "#8a5a2e"    # mid wood
LIGHT = "#c9924e"  # light wood
GLOW = "#e8c07a"   # highlight

# --- key bow (circular head) ---
# interior first, outline on top
c.circle(7, 4, 2, MID, fill=True)
c.set(6, 3, GLOW)
c.set(7, 3, GLOW)
c.set(6, 4, GLOW)
c.circle(7, 4, 3, DARK, fill=False)

# --- shaft ---
c.rect(6, 6, 4, 8, DARK, fill=True)          # outline block (x6..9, y6..13)
c.rect(10, 8, 2, 2, DARK, fill=True)         # tooth 1 outline
c.rect(10, 11, 2, 2, DARK, fill=True)        # tooth 2 outline
c.rect(7, 7, 2, 6, MID, fill=True)           # shaft inner
c.rect(10, 8, 1, 2, MID, fill=True)          # tooth 1 inner
c.rect(10, 11, 1, 2, MID, fill=True)         # tooth 2 inner

# --- wood grain / highlight ---
c.rect(7, 7, 1, 3, LIGHT, fill=True)
c.set(7, 11, LIGHT)
c.set(7, 12, LIGHT)
c.set(8, 10, LIGHT)

print(c.stats_text())
print(c.matrix_text())
finish(c)
