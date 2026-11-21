from pixelbench_api import *

# Create 32x32 canvas for seamless carpet pattern
c = new_canvas(32, 32, background=None, name="carpet")

# Warm carpet palette
BG = c.color("#8B4513")           # warm brown background  
DARK_BROWN = c.color("#5C2E0D")   # dark warm brown
RED = c.color("#B84A2A")          # terracotta red
DEEP_RED = c.color("#7A2E1B")     # deep red
GOLD = c.color("#D4A025")          # rich gold
LIGHT_GOLD = c.color("#E8C766")    # light gold
CREAM = c.color("#F5E6C8")         # cream
WARM_ORANGE = c.color("#C75B35")    # warm orange  
WEAVE = c.color("#6B3410")         # dark weave

# Fill background
c.rect(0, 0, 32, 32, BG)

# Full woven background texture
for y in range(32):
    for x in range(32):
        if (x + y) % 8 == 3 or (x + y) % 8 == 5:
            c.set(x, y, DARK_BROWN)
        elif (x + y) % 8 == 1:
            c.set(x, y, WEAVE)

# Draw the carpet pattern for each of the 4x4 cells
# Each 8x8 cell has a beautifully designed diamond and floral elements.

for gy in range(4):
    for gx in range(4):
        cx, cy = 4 + gx*8, 4 + gy*8  # diamond centers

# ============================================================
# DESIGN THE 8x8 CARPET UNIT:
# Each 8x8 cell has:
#   1. Large diamond outline at center
#   2. Intricate floral patterns inside
#   3. Connecting symbols between adjacent diamonds  
#   4. Decorative corner elements
# ============================================================

# All drawing uses %32 wrapping to guarantee seamlessness.

for gy in range(4):
    for gx in range(4):
        cx = 4 + gx*8
        cy = 4 + gy*8
        
        # ===== THE GRAND DIAMOND (radius 3) =====
        # Outer diamond outline, red
        for i in range(4):
            c.set((cx + i)%32, (cy - 3 + i)%32, RED)
            c.set((cx - i)%32, (cy - 3 + i)%32, RED)
            c.set((cx + i)%32, (cy + 3 - i)%32, RED)
            c.set((cx - i)%32, (cy + 3 - i)%32, RED)
        
        # Gold ring (radius 2)
        for i in range(3):
            c.set((cx + i)%32, (cy - 2 + i)%32, GOLD)
            c.set((cx - i)%32, (cy - 2 + i)%32, GOLD)
            c.set((cx + i)%32, (cy + 2 - i)%32, GOLD)
            c.set((cx - i)%32, (cy + 2 - i)%32, GOLD)
        
        # Light gold inner diamond
        for dy in range(-2, 3):
            w = 3 - abs(dy)
            for dx in range(-w+1, w):
                c.set((cx + dx)%32, (cy + dy)%32, LIGHT_GOLD)
        
        # Cream center pattern
        c.set(cx%32, cy%32, CREAM)
        c.set((cx+1)%32, cy%32, CREAM)
        c.set((cx-1)%32, cy%32, CREAM)
        c.set(cx%32, (cy+1)%32, CREAM)
        c.set(cx%32, (cy-1)%32, CREAM)
        
        # Red diagonal accents
        c.set((cx+1)%32, (cy-1)%32, RED)
        c.set((cx-1)%32, (cy+1)%32, RED)
        
        # Gold corner dots
        c.set((cx+2)%32, (cy+2)%32, CREAM)
        c.set((cx-2)%32, (cy+2)%32, CREAM)
        
        # WARM accent at base of diamond's core
        c.set((cx+1)%32, (cy+2)%32, WARM_ORANGE)

for gy in range(4):
    for gx in range(4):
        cx = 4 + gx*8
        cy = 4 + gy*8
        
        # ===== SMALL DIAMOND at each cell boundary midpoint =====
        # These connect the diamonds in a grid pattern
        
        # Horizontal edge diamonds (at (4+8gx, 8gy))
        ex = cx  # ex = 4+gx*8, ey = gy*8
        ey = gy*8
        c.set(ex%32, ey%32, WARM_ORANGE)
        c.set((ex+1)%32, ey%32, WARM_ORANGE)
        c.set((ex-1)%32, ey%32, WARM_ORANGE)
        c.set(ex%32, (ey+1)%32, WARM_ORANGE)
        c.set(ex%32, (ey-1)%32, WARM_ORANGE)
        c.set(ex%32, ey%32, CREAM)
        
        # Vertical edge diamonds (at (8gx, 4+8gy))
        ex2 = gx*8
        ey2 = 4 + gy*8
        c.set(ex2%32, ey2%32, WARM_ORANGE)
        c.set((ex2+1)%32, ey2%32, WARM_ORANGE)
        c.set((ex2-1)%32, ey2%32, WARM_ORANGE)
        c.set(ex2%32, (ey2+1)%32, WARM_ORANGE)
        c.set(ex2%32, (ey2-1)%32, WARM_ORANGE)
        c.set(ex2%32, ey2%32, CREAM)
        
        # ===== DECORATIVE CORNER dots =====
        # Small dots around each cell
        fx, fy = gx*8, gy*8
        c.set((fx+3)%32, (fy+3)%32, GOLD)
        c.set((fx+4)%32, (fy+2)%32, GOLD)
        c.set((fx+2)%32, (fy+4)%32, GOLD)

# Verify perfect periodicity
all_ok = True
for y in range(32):
    for x in range(32):
        if x+8 < 32 and c.get(x,y) != c.get(x+8,y):
            print(f"Break at ({x},{y})")
            all_ok = False
            break
if all_ok:
    for x in range(32):
        for y in range(32):
            if y+8 < 32 and c.get(x,y) != c.get(x,y+8):
                print(f"Y break at ({x},{y})")
                all_ok = False
                break
if all_ok:
    print("PERFECT SEAMLESS period-8 pattern!")

print(c.stats_text())
print(c.matrix_text(region=(0,0,31,31), indices=False))

finish(c)
