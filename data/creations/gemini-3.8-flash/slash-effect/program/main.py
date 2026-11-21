import math
from pixelbench_api import new_canvas, flatten, view, finish

# Create 48x48 canvas with transparent background
c = new_canvas(48, 48)

# Palette
W = '#ffffff'      # Pure white cutting edge
ICE = '#e8fcff'    # Luminous ice white
C1 = '#8fe8ff'     # Bright electric cyan
C2 = '#38cbf5'     # Electric cyan mid
C3 = '#00a4f5'     # Vivid azure blue
C4 = '#0072d8'     # Medium blue
C5 = '#0048b0'     # Deep blue
C6 = '#002878'     # Navy streak tail
C7 = '#001448'     # Deepest shadow AA

# =========================================================================
# FRAME 1: A small white arc slash
# Box: x in [0, 23], centered around (12, 24)
# =========================================================================
cx1, cy1 = 5.0, 24.0
R1_out = 11.2
T1 = 2.8
theta1_max = math.radians(64)

for y in range(48):
    for x in range(24):
        dx = x - cx1
        dy = y - cy1
        r = math.hypot(dx, dy)
        theta = math.atan2(dy, dx)
        
        if abs(theta) <= theta1_max and dx > 0:
            t = math.cos((math.pi / 2.0) * (theta / theta1_max))
            r_in = R1_out - T1 * t
            
            if r_in <= r <= R1_out:
                c.set(x, y, W)
            elif (r_in - 0.6) <= r < r_in or R1_out < r <= R1_out + 0.4:
                c.set(x, y, ICE)


# =========================================================================
# FRAME 2: A larger arc slash with a trailing streak
# Box: x in [24, 47], centered around (36, 24)
# =========================================================================
cx2, cy2 = 24.0, 24.0
R2_out = 21.2
theta2_max = math.radians(72)

for y in range(48):
    for x in range(24, 48):
        dx = x - cx2
        dy = y - cy2
        r = math.hypot(dx, dy)
        theta = math.atan2(dy, dx)
        
        if dx <= 0:
            continue
            
        if abs(theta) <= theta2_max:
            t = math.cos((math.pi / 2.0) * (theta / theta2_max))
            
            # Trailing edge ribbon modulation
            ribbon_mod = 1.0 + 0.12 * math.sin(theta * 5.0)
            T_eff = 9.2 * (t ** 0.8) * ribbon_mod
            r_inner = R2_out - T_eff
            
            if r_inner <= r <= R2_out:
                d = R2_out - r
                
                # 1. Outer cutting edge (pure white)
                if d <= 1.4:
                    c.set(x, y, W)
                elif d <= 2.2:
                    c.set(x, y, ICE)
                elif d <= 3.2:
                    c.set(x, y, C1)
                # 2. Secondary embedded speed streak
                elif d <= 4.3:
                    if abs(theta) <= math.radians(45):
                        c.set(x, y, W)
                    else:
                        c.set(x, y, C1)
                # 3. Trailing energy layers
                elif d <= 5.3:
                    c.set(x, y, C2)
                elif d <= 6.8:
                    c.set(x, y, C3)
                elif d <= 8.0:
                    c.set(x, y, C4)
                elif d <= 9.0:
                    c.set(x, y, C5)
                else:
                    c.set(x, y, C6)
            elif R2_out < r <= R2_out + 0.5:
                c.set(x, y, ICE)

# Seamlessly connected trailing speed streamers on the inner edge:
streamers = [
    # Top streamer trailing behind
    (34, 15, C4), (33, 16, C5), (32, 16, C6), (31, 17, C7),
    (33, 18, C5), (32, 18, C6),
    # Mid streamer trailing behind
    (34, 23, C4), (33, 23, C5), (32, 23, C6), (31, 23, C7),
    (34, 24, C4), (33, 24, C5), (32, 24, C6),
    (34, 25, C4), (33, 25, C5), (32, 25, C6), (31, 25, C7),
    # Bottom streamer trailing behind
    (33, 30, C5), (32, 30, C6),
    (34, 33, C4), (33, 32, C5), (32, 32, C6), (31, 31, C7),
]

for x, y, col in streamers:
    if 24 <= x < 48 and 0 <= y < 48:
        if c.get(x, y) == 0:
            c.set(x, y, col)

# Submit the finished canvas
finish(c)
