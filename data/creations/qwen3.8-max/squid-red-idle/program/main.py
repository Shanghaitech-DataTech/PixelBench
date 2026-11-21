from pixelbench_api import *

W, H = 58, 58  # one extra row of headroom so the bob never clips

# ---- base: original picture padded 1px at top ----
base = new_canvas(W, H, name="base")
base.blit(input_canvas, 0, 1)

# seam: original row 15 (canvas row 16) is a uniform red band across the dome
# head cap = canvas rows 0..15  (original rows 0..14) -> the bobbing part
# body     = canvas rows 16..57 (original rows 15..56) -> static part
head = base.copy(name="head")
head.clear(0, 16, W, H - 16)
body = base.copy(name="body")
body.clear(0, 0, W, 16)

# filler: seam row kept behind the head so no gap opens when the head rises
filler = base.copy(name="filler")
filler.clear(0, 0, W, 16)          # keep rows 16..
filler.clear(0, 17, W, H - 17)     # keep only row 16
filler.clear(0, 16, 10, 1)         # clip to the dome footprint cols 10..46
filler.clear(47, 16, W - 47, 1)
filler.shift(0, -1)                # sits at row 15, hidden under the head

# ---- frame 1: original content ----
f1 = flatten([body, filler, head], name="frame1")

# ---- frame 2: inhale - head cap bobs up 1px ----
h2 = head.copy(name="h2")
h2.shift(0, -1)
f2 = flatten([body, filler, h2], name="frame2")

# ---- frame 3: exhale - head cap bobs down 1px ----
h3 = head.copy(name="h3")
h3.shift(0, 1)
f3 = flatten([body, filler, h3], name="frame3")

# sanity: frame 1 must equal the original picture
w1, h1, b1 = f1.to_rgba()
w0, h0, b0 = base.to_rgba()
print("frame1 == original:", b1 == b0)
for f in (f1, f2, f3):
    print(f.stats_text())

view(f1, scale=8, margin=0)
view(f2, scale=8, margin=0)
view(f3, scale=8, margin=0)

finish([f1, f2, f3])
