from pixelbench_api import *

# ============================================================
# PALADIN ATTACK - 2 frames, both 50x65
# ============================================================

W, H = 50, 65

# Frame 1: exact copy of input
f1 = new_canvas(W, H, background=None, name="frame1")
f1.blit(input_canvas, 0, 0)

# Frame 2: same size
f2 = new_canvas(W, H, background=None, name="frame2")
f2.blit(input_canvas, 0, 0)

def hx(cv, x, y):
    pi = cv.get(x, y)
    if pi is None:
        return None
    rgba = cv.palette()[pi]['rgba']
    if rgba[3] == 0:
        return None
    return f"#{rgba[0]:02x}{rgba[1]:02x}{rgba[2]:02x}"

# ============================================================
# FRAME 2: Heavy downward attack swing
# ============================================================

# PART 1: Replace the raised blade (upper-right) with white motion trail
blade_colors = {
    '#c67b02', '#9e7c4f', '#734a29', '#c9886d', '#d1b563',
    '#daa088', '#5b461a', '#c08008'
}

for y in range(10, 28):
    for x in range(28, 43):
        cval = hx(f2, x, y)
        if cval in blade_colors:
            f2.set(x, y, None)

# Clear white/cream pixels from the old blade
for y in range(12, 28):
    for x in range(30, 43):
        cval = hx(f2, x, y)
        if cval in ['#ffffff', '#ffffd5', '#f3d887']:
            f2.set(x, y, None)

# PART 2: White motion trail 
trail_w = f2.color('#ffffff')
trail_c = f2.color('#ffffd5')

# Trail sweeping down from upper right
trail_arc = [
    (33, 11, trail_w), (35, 10, trail_c), (37, 10, trail_w),
    (39, 11, trail_c), (41, 12, trail_w), (42, 13, trail_c),
    (42, 15, trail_w), (41, 17, trail_c), (42, 14, trail_c),
    (41, 16, trail_w), (40, 13, trail_w), (38, 12, trail_w),
    (40, 14, trail_c), (41, 15, trail_c),
]

for tx, ty, tc in trail_arc:
    f2.set(tx, ty, tc)

# Trail streaking down behind the swing
f2.set(40, 18, trail_c)
f2.set(39, 20, trail_c)
f2.set(38, 22, trail_c)
f2.set(37, 24, trail_c)
f2.set(39, 19, trail_c)
f2.set(38, 21, trail_c)

# PART 3: Draw the sword in the downward swing position
# The sword has been swung down. A thick blade goes from the body
# down-right at an angle. The blade tip points down.

# The grip/hands have come down with the sword.
# The blade descends through the swing.

# Main blade going down-right
blade_body = [
    # Handle/crossguard at the top of the down blade
    (28, 21, '#c67b02'), (29, 21, '#ffcc43'), (30, 21, '#c67b02'),
    (29, 22, '#9e7c4f'), (30, 22, '#c67b02'), (31, 22, '#c67b02'),
    
    # Blade going down-right
    # Blade edge (dark)
    (30, 23, '#101010'), (31, 24, '#101010'), (32, 25, '#101010'),
    (33, 27, '#101010'), (34, 29, '#101010'), (35, 31, '#101010'),
    
    # Lower blade edge
    (32, 23, '#2f1010'), (33, 24, '#2f1010'), (34, 25, '#2f1010'),
    (35, 27, '#2f1010'),
    
    # Blade body (tan/steel)
    (30, 24, '#9e7c4f'), (31, 25, '#c9886d'), (32, 26, '#c9886d'),
    (33, 27, '#734a29'), (34, 28, '#c9886d'), (34, 29, '#9e7c4f'),
    (35, 30, '#734a29'), (36, 31, '#734a29'), (36, 32, '#101010'),
    (37, 33, '#101010'),
    
    # Gold accent on blade
    (31, 24, '#c67b02'), (32, 26, '#ffcc43'), (34, 28, '#ffcc43'),
    
    # White highlight
    (32, 25, '#ffffff'), (34, 28, '#ffffff'), (35, 30, '#ffffff'),
]

for bx, by, bc in blade_body:
    f2.set(bx, by, f2.color(bc))

# PART 4: Left foot steps forward
# The character's left foot steps forward, shifting weight.
# The left leg and foot move forward (right) and slightly down.

# IMPORTANT: I will NOT clear the original left leg.
# Instead, I'm going to gently move the left FOOT forward.
# The original left foot/boot was around (1-12, 47-53).
# The character steps forward with the left foot.

# The left boot (dark #2f1010 pixels) in rows 47-52, cols 2-12
# moves forward (right) to approximately rows 48-54, cols 5-16

# Let me more carefully only clear the BOOT (foot) part, not the leg.
# The leg goes from the hip down. The boot is at the bottom.
# Looking at the original leg, the boot area is roughly rows 47-53.

# The left boot pixels from the original:
# Around rows 47-52, the #2f1010 and #101010 pixels at columns ~0-14 form the boot.
# But the leg also has #101010 pixels.

# Safer: keep the original left leg AND add a forward foot,
# creating a stride/forward-step look.
# The foot extends forward from the body.

# Let me also add the forward-shifted left weight.

# The existing left foot stays, and I add a forward foot extension.
# This creates the visual of the left foot stepping forward.

# Forward foot extension - the foot sticks out toward the target
forward_foot = [
    # The left foot pushed forward (right and slightly down)
    # Shin going forward
    (12, 47, '#2f1010'), (13, 47, '#101010'), (14, 47, '#2f1010'),
    (12, 48, '#101010'), (13, 48, '#2f1010'), (14, 48, '#101010'),
    
    # Forward foot planted
    (13, 49, '#2f1010'), (14, 49, '#101010'), (15, 49, '#2f1010'),
    (14, 50, '#101010'), (15, 50, '#2f1010'),
    (15, 51, '#2f1010'), (16, 51, '#101010'),
    
    # Boot sole
    (14, 52, '#2f1010'), (15, 52, '#101010'),
    
    # Gold trim on the forward boot  
    (13, 49, '#c67b02'),
]

for fx, fy, fc in forward_foot:
    f2.set(fx, fy, f2.color(fc))

print("Frame 2:", f2.stats())

print("\nFrame 2 matrix:")
print(f2.matrix_text())

save("paladin_attack_f1", f1)
save("paladin_attack_f2", f2)

finish([f1, f2])
