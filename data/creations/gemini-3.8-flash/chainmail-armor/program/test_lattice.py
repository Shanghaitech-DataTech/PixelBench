from pixelbench_api import *

c = new_canvas(32, 32)
c.rect(0, 0, 32, 32, "#11141a")

# Let's test the diamond lattice where:
# (x + y) % 2 == 0 is the HOLE of a ring!
# (x + y) % 2 == 1 is the METAL WIRE!
# But how does metal wire have structure?
# Some wires go / (top-right to bottom-left), some go \ (top-left to bottom-right).
# Also, top of each hole has a highlight, bottom of each hole has shadow!
# Let's see:
for y in range(4, 28):
    for x in range(4, 28):
        if (x + y) % 2 == 0:
            # Hole of the ring
            c.set(x, y, "#161b24")
        else:
            # Wire!
            # Which wire is it?
            # If x % 2 == 0 (and y % 2 == 1): wire between (x, y-1) and (x, y+1)
            # That's a vertical connection (top/bottom rim)
            # If y % 2 == 0 (and x % 2 == 1): horizontal connection (left/right rim)
            if x % 2 == 0:
                # Top rim of hole (x, y+1), or bottom rim of hole (x, y-1)
                # If top-lit: top rim gets light, bottom rim gets shadow
                # For hole at (x, y+1), this pixel (x, y) is its TOP RIM!
                # So it should be bright highlight!
                c.set(x, y, "#e2e8f0")
            else:
                # Left/right rim:
                # Left of hole (x+1, y) -> gets light-mid
                # Right of hole (x-1, y) -> gets shadow
                if (x // 2 + y // 2) % 2 == 0:
                    c.set(x, y, "#94a3b8")
                else:
                    c.set(x, y, "#475569")

view(c)
