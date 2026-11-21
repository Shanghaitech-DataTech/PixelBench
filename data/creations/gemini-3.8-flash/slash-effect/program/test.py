import math
from pixelbench_api import new_canvas

c = new_canvas(48, 48)
cx2, cy2 = 22.0, 24.0
R2_out = 23.5
T2 = 3.6
theta2_max = math.radians(65)

for y in range(48):
    for x in range(24, 48):
        dx = x - cx2
        dy = y - cy2
        r = math.hypot(dx, dy)
        theta = math.atan2(dy, dx)
        
        if abs(theta) <= theta2_max and dx > 0:
            t_norm = math.cos((math.pi / 2.0) * (theta / theta2_max))
            
            # Trailing Streak 2 (inner streak)
            theta_s2_max = math.radians(44)
            if abs(theta) <= theta_s2_max:
                t_s2 = math.cos((math.pi / 2.0) * (theta / theta_s2_max))
                r_s2_out = R2_out - (T2 * t_norm) - 4.6
                r_s2_in = r_s2_out - 2.8 * t_s2
                if r_s2_in <= r <= r_s2_out:
                    c.set(x, y, '#002f80')

for y in range(48):
    for x in range(24, 48):
        if c.get(x, y) != 0:
            if x <= 26:
                print(f"drawn at ({x}, {y})")
