OL   = "#3a3737"
G1   = "#b7b3b2"
G2   = "#827c7c"
WH   = "#efe9e7"

W, H = 40, 36

# ---------- frame 1 : original content on the shared stage ----------
f1 = new_canvas(W, H, name="frame1")
f1.blit(input_canvas, 5, 6)

# ---------- frame 2 : mid-leap ----------
# body tilted nose-up, reusing the original sprite
rot = input_canvas.select(0, 0, 26, 28).rotate(-15, "rotsprite").preview("rot")

body = new_canvas(W, H, name="body")
body.blit(rot, 3, 1)
body.clear(9, 29, 9, 7)        # drop the dangling hind foot

# far-side limbs (grey, tucked just behind the near ones)
far = new_canvas(W, H, name="far")
far.poly([(17,22),(13,25),(9,27),(8,29),(11,30),(15,27),(18,25)], G1)   # hind
far.poly([(26,21),(24,24),(27,28),(30,29),(31,27),(28,24),(27,21)], G1) # fore
far.outline(OL)

# near-side hind leg, stretched out behind the leap
near = new_canvas(W, H, name="near")
near.ellipse(18, 25, 4, 3, WH)                 # thigh
near.poly([(19,22),(13,26),(8,29),(4,30),(4,33),(9,33),
           (15,29),(20,26)], WH)               # shank
near.rect(2, 31, 9, 3, WH)                     # long foot
near.ellipse(3, 32, 2, 1, WH)
near.rect(2, 33, 9, 1, G1)                     # sole shading
near.line(12, 28, 16, 26, G1)
near.outline(OL)

f2 = flatten([far, near, body], name="frame2")
# haunch shading so the leg joins the body
f2.line(17, 25, 19, 27, G1)
f2.set(16, 26, G1)

view(f1)
view(f2)
finish([f1, f2])
