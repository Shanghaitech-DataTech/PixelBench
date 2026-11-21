# draw-sword-slash edit
# Frame 1: original content on a slightly larger canvas (room for the slash).
# Frame 2: sword swung from lower-left to upper-right, black slash trail.

W, H = 76, 84
DX, DY = 0, 12

f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, DX, DY)

f2 = f1.copy(name="f2")

# --- erase the old blade that pointed to the lower-left corner ---
# (boxes chosen to avoid the body edge, verified against the pixel map)
f2.clear(0, 54, 28, 2)   # rows 54-55, cols 0-27
f2.clear(0, 56, 28, 1)   # row 56
f2.clear(0, 57, 29, 1)   # row 57
f2.clear(0, 58, 26, 1)   # row 58
f2.clear(0, 59, 25, 8)   # rows 59-66

# --- black slash trail: tapered crescent from lower-left, over the top, hooking
# down at upper-right where the blade tip ends ---
f2.path("M 2 64 C -4 0 64 -2 58 36 C 56 4 0 10 2 64 Z", "#000000", fill=True)

# --- re-stamp the head over the trail so the crescent passes behind the hair ---
input_canvas.select(30, 0, 32, 17).copy_to(30, 12, f2, mode="over")

# --- sword at the end of the swing: blade from the gripping hand (waist)
# pointing up-right; dark blade with a bright edge so it reads over the torso ---
f2.poly([(38, 58), (64, 31), (34, 56)], "#1b0202", fill=True)
f2.line(35, 55, 63, 32, "#b2aeb1")

# --- re-stamp the left (gripping) hand over the blade base so it holds it ---
input_canvas.select(32, 41, 11, 7).copy_to(32, 53, f2)

view(f1)
view(f2)

finish([f1, f2])
