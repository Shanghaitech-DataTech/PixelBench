src = input_canvas
W, H = 64, 64

# ---------- Frame 1: original picture (canvas enlarged, content untouched) ----------
f1 = new_canvas(W, H, name="frame1")
f1.blit(src, 0, 0)

# ---------- Frame 2: thrust pose + flame flying forward ----------
f2 = new_canvas(W, H, name="frame2")
f2.blit(src, 0, 0)

# 1. remove the small flame burst that was sitting at the hand
f2.clear(35, 12, 12, 17)   # x=35..46, y=12..28
f2.clear(32, 12, 2, 2)     # stray sparks just above the hand

# 2. body leans in: head shifts 3px forward, torso/arm 2px forward
f2.select(8, 0, 27, 14).move_to(11, 0, f2)    # head + shoulders (y=0..13)
f2.select(8, 14, 27, 32).move_to(10, 14, f2)  # torso + arm (y=14..45)

# 3. left foot steps forward
f2.select(0, 54, 13, 9).move_to(6, 54, f2)

# 4. the spell: burst at the hand, fiery trail, fireball out front
ORANGE = '#f27219'
AMBER  = '#f4a30c'
YELLOW = '#fed32c'
HOT    = '#fff0a0'

# hand burst
f2.circle(38, 22, 2, AMBER)
f2.set(38, 22, YELLOW)
f2.set(39, 19, ORANGE); f2.set(38, 18, ORANGE)
f2.set(37, 25, ORANGE); f2.set(38, 26, ORANGE)

# trail, widening as it flies toward the ball
f2.line(42, 19, 51, 19, ORANGE)
f2.line(39, 20, 52, 20, AMBER)
f2.line(38, 21, 53, 21, AMBER)
f2.line(37, 22, 53, 22, AMBER)
f2.line(38, 23, 52, 23, AMBER)
f2.line(39, 24, 52, 24, AMBER)
f2.line(42, 25, 51, 25, ORANGE)
f2.line(45, 26, 50, 26, ORANGE)

# hot core of the trail
f2.line(44, 21, 52, 21, YELLOW)
f2.line(42, 22, 53, 22, YELLOW)
f2.line(44, 23, 52, 23, YELLOW)
f2.set(47, 22, HOT); f2.set(48, 22, HOT); f2.set(49, 21, HOT)

# fireball
f2.circle(57, 22, 5, ORANGE)
f2.circle(57, 22, 4, AMBER)
f2.circle(57, 22, 2, YELLOW)
f2.set(57, 21, HOT); f2.set(58, 22, HOT); f2.set(56, 22, HOT)

# sparks around the projectile
for (x, y, col) in [(50, 15, YELLOW), (55, 13, AMBER), (61, 15, ORANGE),
                    (63, 19, AMBER), (47, 28, ORANGE), (53, 29, AMBER),
                    (59, 30, ORANGE), (61, 27, ORANGE)]:
    f2.set(x, y, col)

print("f1:", f1.stats_text())
print("f2:", f2.stats_text())
print(f2.matrix_text(region=(0, 0, 40, 30)))

finish([f1, f2])
