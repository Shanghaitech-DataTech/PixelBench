# squid-red-idle: 3-frame breathing idle
# f1 = original content; f2 = head/upper body bobbed up 1px; f3 = bobbed down 1px.

W, H = 58, 58
CUT = 42  # head keeps canvas rows 0..CUT-1 (sprite rows 0..40); body keeps rows CUT-1..57 (1px overlap)

# Frame 1: original picture content, 1px headroom on top for the up-bob
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, 0, 1)

# Build head / body layers from master
head = f1.copy(name="head")
head.clear(0, CUT, W, H - CUT)          # keep rows 0..41

body = f1.copy(name="body")
body.clear(0, 0, W, CUT - 1)            # keep rows 41..57 (overlap row 41, identical pixels)

# Frame 2: inhale — head raised 1px, lower body planted
head_up = head.copy(name="head_up")
head_up.shift(0, -1)                    # rows move up; vacated row 41 -> transparent
f2 = new_canvas(W, H, name="f2")
f2.blit(body, 0, 0)
f2.blit(head_up, 0, 0)

# Frame 3: exhale — head pressed down 1px, lower body planted
head_down = head.copy(name="head_down")
head_down.shift(0, 1)                   # rows move down; vacated row 0 -> transparent
f3 = new_canvas(W, H, name="f3")
f3.blit(body, 0, 0)
f3.blit(head_down, 0, 0)

print(f1.stats())
print(f2.stats())
print(f3.stats())
view(f1)
view(f2)
view(f3)
finish([f1, f2, f3])
