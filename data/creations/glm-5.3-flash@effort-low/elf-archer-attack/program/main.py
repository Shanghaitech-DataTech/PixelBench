# Frame 1: original. Frame 2: fully drawn bow, side stance (facing right).
f1 = input_canvas.copy(name='frame1')

f2 = new_canvas(35, 47, name='frame2')
c = f2
f2.blit(input_canvas, 0, 0)

W = '#8a5a2b'   # bow wood
Ws = '#5e3a17'  # bow shade
S = '#121311'   # string
G = '#c5956a'   # glove/hand
Gd = '#7b4231'  # hand shade
wI = c.color(W); wS = c.color(Ws); sI = c.color(S)
gI = c.color(G); gdI = c.color(Gd)

# --- erase old bow (limb+string column x=25..34, y=0..35) ---
f2.clear(25, 0, 10, 36)

# --- erase old arms (x=19..24, y=17..26) ---
f2.clear(19, 17, 6, 10)

# --- new fully-open bow: limb tips (5,17) and (33,17), belly (19,35) ---
f2.line(5, 17, 12, 22, W)
f2.line(12, 22, 17, 28, W)
f2.line(17, 28, 19, 34, W)
f2.line(33, 17, 26, 22, W)
f2.line(26, 22, 21, 28, W)
f2.line(21, 28, 19, 34, W)
# limb tip nocks
f2.set(4, 17, Ws); f2.set(34, 17, Ws)
# belly thickening
f2.set(18, 34, W); f2.set(20, 34, W)

# --- string: tip to tip via draw hand (28,24) ---
f2.line(4, 17, 27, 24, S)
f2.line(27, 24, 34, 17, S)

# --- front arm: shoulder (19,20) -> hand at (12,22) ---
f2.line(19, 20, 15, 21, G)
f2.line(15, 21, 12, 22, G)
f2.set(11, 22, Gd); f2.set(12, 21, Gd)   # fist on string
f2.set(13, 23, Gd)

# --- draw arm: shoulder (20,22) -> elbow (24,25) -> hand (27,24) ---
f2.line(20, 22, 24, 25, G)
f2.line(24, 25, 27, 24, G)
f2.set(27, 23, Gd); f2.set(28, 24, Gd)   # draw hand at anchor
f2.set(28, 23, Gd)

print(f2.stats_text())
finish([f1, f2])
