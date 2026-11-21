inp = input_canvas
W, H = 58, 57
SPLIT = 44  # rows 0..43 bob (head, eyes, mouth, upper arms); rows 44..56 anchored stems


def band(src, y0, y1):
    """Copy of src keeping only rows y0..y1 inclusive."""
    t = src.copy()
    if y0 > 0:
        t.clear(0, 0, W, y0)
    if y1 < H - 1:
        t.clear(0, y1 + 1, W, H - (y1 + 1))
    return t


upper = band(inp, 0, 43)      # bobbing part
lower = band(inp, 44, 56)     # tentacle stems, anchored
row43 = band(inp, 43, 43)     # seam filler row for the "up" frame

# Base position in frame coords: orig row i -> frame row i+1 (58x58, 1px headroom).

# ---- frame 1: original picture ----
f1 = new_canvas(58, 58, name='f1')
f1.blit(inp, 0, 1)

# ---- frame 2: upper body bobbed UP 1px, stems anchored ----
# orig 0..43 -> frame 0..43 ; seam frame 44 = orig 43 ; stems orig 44..56 -> frame 45..57
f2 = new_canvas(58, 58, name='f2')
f2.blit(upper, 0, 0)   # band content rows 0..43 -> frame 0..43
f2.blit(row43, 0, 1)   # band content row 43   -> frame 44 (seam filler)
f2.blit(lower, 0, 1)   # band content rows 44..56 -> frame 45..57

# ---- frame 3: upper body bobbed DOWN 1px, stems anchored (drawn in front) ----
# orig 0..43 -> frame 2..45 ; stems orig 44..56 -> frame 45..57 on top
f3 = new_canvas(58, 58, name='f3')
f3.blit(upper, 0, 2)   # band content rows 0..43 -> frame 2..45
f3.blit(lower, 0, 1)   # band content rows 44..56 -> frame 45..57

for c in (f1, f2, f3):
    print(c.name, c.stats_text())

for name, c in (('f1', f1), ('f2', f2), ('f3', f3)):
    print('===', name, 'rows 40-50 (seam) ===')
    print(c.matrix_text(region=(0, 40, 57, 50)))

# Frame 1: original picture content.
# Frames 2/3: breathing idle - the body/head/eyes/mouth/upper arms bob up and
# down by 1px while the tentacle stems stay anchored to the ground.
finish([f1, f2, f3])
