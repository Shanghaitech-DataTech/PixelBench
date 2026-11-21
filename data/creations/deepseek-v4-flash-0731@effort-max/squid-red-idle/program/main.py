from pixelbench_api import *

inp = input_canvas
w, h = 58, 57

f1 = new_canvas(58, 58)  # original content, whole sprite at offset +1
f2 = new_canvas(58, 58)  # upper body bobbed up 1px
f3 = new_canvas(58, 58)  # upper body bobbed down 1px

pal = inp.palette()

def blit_rows(dst, dy, y0, y1):
    for y in range(y0, y1 + 1):
        for x in range(w):
            idx = inp.get(x, y)
            rgba = pal[idx]['rgba'] if 0 <= idx < len(pal) else (0, 0, 0, 0)
            if rgba[3] > 0:
                dst.set(x, y + dy, rgba)

# Body/head (with arms) = rows 0..43, legs = rows 44..56.
blit_rows(f1, 1, 0, 56)      # frame 1: original picture content
blit_rows(f2, 0, 0, 43)      # head up
blit_rows(f2, 1, 44, 56)     # legs stay planted
blit_rows(f3, 2, 0, 43)      # head down
blit_rows(f3, 1, 44, 56)     # legs stay planted

for c in (f1, f2, f3):
    print(c.stats_text())

finish([f1, f2, f3])
