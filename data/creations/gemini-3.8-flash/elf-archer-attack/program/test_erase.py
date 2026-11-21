from pixelbench_api import *

W, H = 48, 48
dx, dy = 5, 0

# Base canvases
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, dx, dy)

f2 = new_canvas(W, H, name="f2")

# Let's inspect what pixels from input_canvas can be transferred to f2,
# and what needs to be redrawn.
# Let's write a python function to build f2 carefully.

# Color shortcuts
TRANSPARENT = 0
C0  = 1   # #422110
C1  = 2   # #7b4231
C2  = 3   # #c5956a
C3  = 4   # #ffffff
C4  = 5   # #949473
C5  = 6   # #f3f4b6
C6  = 7   # #ffe75a
C7  = 8   # #c30074
C8  = 9   # #df9859
C9  = 10  # #55002a
C10 = 11  # #ef5ba1
C11 = 12  # #f6d39b
C12 = 13  # #e0c89e
C13 = 14  # #faf3c9
C14 = 15  # #f1d8b3
C15 = 16  # #a9794f
C16 = 17  # #8e7058
C17 = 18  # #907859
C18 = 19  # #fcc44c
C19 = 20  # #121311
C20 = 21  # #9e005d
C21 = 22  # #529439
C22 = 23  # #f6adcd
C23 = 24  # #304915
C24 = 25  # #14110e
C25 = 26  # #9cde5a
C26 = 27  # #bc6c0c
C27 = 28  # #252a23
C28 = 29  # #f1f7f7
C29 = 30  # #4f7229
C30 = 31  # #3c3c3c
C31 = 32  # #687862
C32 = 33  # #a4b496
C33 = 34  # #e1d4c2
C34 = 35  # #ffffce
C35 = 36  # #534338
C36 = 37  # #74341c
C37 = 38  # #48382f
C38 = 39  # #313b31
C39 = 40  # #5d422f
C40 = 41  # #d1b6a2
C41 = 42  # #17003599

# Let's start by copying f1 into f2, but selectively:
# 1. Lower body (y >= 26) can be mostly kept, but clean up the old bow tip at bottom right.
# 2. Quiver and hair bun (y <= 15, x <= 26) can be kept.
# 3. Old arms, old bow, old string are removed.

# Let's copy f1 into f2
for y in range(H):
    for x in range(W):
        c = f1.get(x, y)
        f2.set(x, y, c)

# Now, erase the old bow and string from f2:
# The old bow was in cols 27+dx to 34+dx (x = 32 to 39), y = 1 to 40.
# Let's inspect which pixels belong to the bow vs body in f1.
for y in range(1, 41):
    for x in range(27 + dx, W):
        # In rows 40-45, x=26..32 is the right foot! Don't erase the foot!
        if y >= 40:
            continue
        # Also, check if this is the left arm / body in rows 20-25:
        # We will replace left arm anyway.
        f2.set(x, y, TRANSPARENT)

# Also erase old bow tip at y=36..39:
for y in range(36, 40):
    for x in range(22 + dx, 27 + dx):
        # In f1, col 22..26 at y=36..39 has bow tip
        f2.set(x, y, TRANSPARENT)

# Also erase old string in y=4..20:
for y in range(4, 20):
    for x in range(25 + dx, 29 + dx):
        f2.set(x, y, TRANSPARENT)

# Also erase the old resting right arm on the left side:
# In f1, old right arm is around x = 5+dx to 12+dx (x=10..17), y = 16..24.
for y in range(16, 25):
    for x in range(5 + dx, 12 + dx):
        f2.set(x, y, TRANSPARENT)

# Also erase old left arm in y=20..25, x = 18+dx to 27+dx (x=23..32):
for y in range(20, 26):
    for x in range(18 + dx, 28 + dx):
        f2.set(x, y, TRANSPARENT)

comp = new_canvas(W * 2 + 4, H, name="comp")
comp.blit(f1, 0, 0)
comp.blit(f2, W + 4, 0)
view(comp)
