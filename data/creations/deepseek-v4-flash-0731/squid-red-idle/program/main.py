from pixelbench_api import *

src = input_canvas
W, H = 58, 59  # 1px slack above and below the original 57-row sprite

def place(dy):
    c = new_canvas(W, H)
    c.blit(src, 0, dy)
    return c

# Frame 1: original picture content, kept on the new canvas.
f1 = place(1)
# Frames 2 & 3: the squid idling — the sprite bobs gently up (f2) and down (f3).
f2 = place(0)
f3 = place(2)

for i, f in enumerate((f1, f2, f3), 1):
    print(f"frame {i}: {f.stats_text()}")

finish([f1, f2, f3])
