from pixelbench_api import new_canvas, finish, save, view
import math
import random

# Create a 48x48 canvas with transparent background
c = new_canvas(48, 48, background=None, name="portal")

# Purple color palette - 9 colors for gradient depth
c.color('#0f051f', 'v0')  # darkest
c.color('#1a0833', 'v1')  
c.color('#2b0d52', 'v2')
c.color('#44167a', 'v3')
c.color('#6322a3', 'v4')  # mid purple
c.color('#8534c9', 'v5')
c.color('#a855e0', 'v6')
c.color('#c980f0', 'v7')  # light
c.color('#e8b8ff', 'v8')  # brightest
c.color('#ffffff', 'white')

center_x, center_y = 24, 24

# Draw filled spiral vortex using polar coordinates
# Each ring has a phase shift to create spiral effect
for ring in range(22, 0, -1):
    # Phase shift increases as we go inward (creates spiral)
    phase_shift = (22 - ring) * 0.25
    
    for angle_deg in range(0, 360, 1):
        rad = math.radians(angle_deg + math.degrees(phase_shift))
        x = int(center_x + ring * math.cos(rad))
        y = int(center_y + ring * math.sin(rad))
        
        if 0 <= x < 48 and 0 <= y < 48:
            # Color based on ring distance
            if ring > 18:
                color = 'v1'
            elif ring > 15:
                color = 'v2'
            elif ring > 12:
                color = 'v3' if (angle_deg // 15) % 2 == 0 else 'v4'
            elif ring > 9:
                color = 'v4' if (angle_deg // 12) % 2 == 0 else 'v5'
            elif ring > 6:
                color = 'v5' if (angle_deg // 10) % 2 == 0 else 'v6'
            elif ring > 3:
                color = 'v6' if (angle_deg // 8) % 2 == 0 else 'v7'
            else:
                color = 'v7'
            
            # Add gaps for spiral arm effect
            spiral_gap = math.sin(math.radians(angle_deg * 4 + ring * 15))
            if spiral_gap > -0.3 or ring < 5:
                c.set(x, y, color)

# Add distinct spiral arms (brighter)
random.seed(42)
num_arms = 4
for arm in range(num_arms):
    base_angle = arm * (360 / num_arms)
    for t in range(0, 100):
        progress = t / 100.0
        radius = 20 - progress * 16
        angle = base_angle + progress * 4.0  # spiral amount
        
        rad = math.radians(angle)
        x = int(center_x + radius * math.cos(rad))
        y = int(center_y + radius * math.sin(rad))
        
        if 0 <= x < 48 and 0 <= y < 48:
            if radius > 12:
                color = 'v5'
            elif radius > 8:
                color = 'v6'
            else:
                color = 'v7'
            
            # Draw thicker arm near center
            thickness = 2 if radius < 8 else 1
            for dx in range(-thickness, thickness+1):
                for dy in range(-thickness, thickness+1):
                    if dx*dx + dy*dy <= thickness*thickness + 1:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 48 and 0 <= ny < 48:
                            c.set(nx, ny, color)

# Glowing core
c.circle(center_x, center_y, 5, 'v8', fill=True)
c.circle(center_x, center_y, 3, 'white', fill=True)
c.circle(center_x, center_y, 1, 'v7', fill=True)

# Add sparkles/energy particles
random.seed(123)
for _ in range(60):
    angle = random.random() * 2 * math.pi
    dist = random.randint(7, 21)
    x = int(center_x + dist * math.cos(angle))
    y = int(center_y + dist * math.sin(angle))
    if 0 <= x < 48 and 0 <= y < 48:
        sparkle = random.choice(['v7', 'v8', 'white'])
        c.set(x, y, sparkle)

# Outer glow ring (sparse)
random.seed(456)
for angle_deg in range(0, 360, 10):
    rad = math.radians(angle_deg)
    for r in range(22, 24):
        x = int(center_x + r * math.cos(rad))
        y = int(center_y + r * math.sin(rad))
        if 0 <= x < 48 and 0 <= y < 48:
            if random.random() > 0.5:
                c.set(x, y, 'v7')

print(c.stats_text())
print(c.matrix_text(region=(6, 6, 42, 42)))

save("portal", c)
view(c, size=256)

finish(c)
