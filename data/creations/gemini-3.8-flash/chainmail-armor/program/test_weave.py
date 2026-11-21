from pixelbench_api import *

c = new_canvas(32, 32)
c.rect(0, 0, 32, 32, "#0a0d14")

def draw_ring(c, rx, ry, col_hi, col_mid, col_shad, col_hole):
    # Top highlight
    c.set(rx + 1, ry, col_hi)
    c.set(rx + 2, ry, col_hi)
    # Left rim
    c.set(rx, ry + 1, col_mid)
    # Right rim
    c.set(rx + 3, ry + 1, col_shad)
    # Hole
    c.set(rx + 1, ry + 1, col_hole)
    c.set(rx + 2, ry + 1, col_hole)
    # Bottom rim
    c.set(rx + 1, ry + 2, col_shad)
    c.set(rx + 2, ry + 2, col_shad)

# Test with lighting variation:
# Light from top-left:
# x=0..31, y=0..31
# Intensity depends on x and y
for r in range(12):
    ry = 2 + r * 2
    ox = 2 if (r % 2 == 1) else 0
    for cx in range(-1, 8):
        rx = cx * 4 + ox
        
        # Calculate local brightness factor (0.0 to 1.0)
        # top-left is brightest, bottom-right is darkest
        # chest center has a round highlight
        lx = rx / 30.0
        ly = ry / 30.0
        bright = 1.0 - 0.5 * lx - 0.4 * ly
        
        # Choose colors based on brightness:
        if bright > 0.75:
            hi = "#ffffff"
            mid = "#cbd5e1"
            shad = "#64748b"
            hole = "#1e293b"
        elif bright > 0.55:
            hi = "#e2e8f0"
            mid = "#94a3b8"
            shad = "#475569"
            hole = "#18202c"
        elif bright > 0.40:
            hi = "#cbd5e1"
            mid = "#64748b"
            shad = "#334155"
            hole = "#111622"
        else:
            hi = "#94a3b8"
            mid = "#475569"
            shad = "#1e293b"
            hole = "#0d1117"
            
        draw_ring(c, rx, ry, hi, mid, shad, hole)

view(c)
