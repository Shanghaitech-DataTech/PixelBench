f1 = input_canvas.copy(name="frame1")
f2 = input_canvas.copy(name="frame2")

BLACK = f2.color("#0b0b0eff")
EDGE = f2.color("#3a3f4dff")
BLADE = f2.color("#dfe4ecff")

# --- sword blade held in the LEFT hand (hand around x=40-50, y=13-21) ---
gx, gy = 45, 17
f2.line(gx - 4, gy + 4, gx + 2, gy - 2, EDGE)      # crossguard
f2.line(gx + 1, gy - 1, 58, 4, BLADE)              # blade up-right
f2.line(gx + 2, gy - 1, 59, 5, EDGE)
f2.line(gx, gy, 57, 5, EDGE)

# --- black slash trail: lower left -> upper right ---
def thick(x0, y0, x1, y1, w, col):
    for o in range(w):
        f2.line(x0, y0 + o, x1, y1 + o, col)

thick(3, 62, 55, 10, 3, BLACK)
f2.line(55, 10, 60, 5, BLACK)
f2.line(56, 11, 59, 7, BLACK)
f2.line(1, 65, 3, 62, BLACK)
f2.line(2, 66, 4, 63, BLACK)

finish([f1, f2])
