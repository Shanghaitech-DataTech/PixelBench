from pixelbench_api import *
import random

output = input_canvas.copy(name='output')

c_vine1 = output.color('#1a3320', 'vine1')
c_vine2 = output.color('#264d30', 'vine2')
c_vine3 = output.color('#377045', 'vine3')

c_cloak_dark = output.color('#16101c', 'cloak_dark')
c_cloak_mid = output.color('#251e2e', 'cloak_mid')
c_cloak_light = output.color('#362a42', 'cloak_light')
c_cloak_hi = output.color('#453854', 'cloak_hi')

c_staff = output.color('#4a2e1b', 'staff')
c_glow_core = output.color('#ffffff', 'glow_core')
c_glow_mid = output.color('#00ffff', 'glow_mid')
c_glow_out = output.color('#006688', 'glow_out')
c_glow_faint = output.color('#003344', 'glow_faint')

mage = new_canvas(30, 36)

# Shadow on ground
mage.ellipse(12, 33, 6, 1, 'cloak_dark')

# Glow on ground
mage.ellipse(20, 33, 4, 1, 'glow_faint')
mage.ellipse(20, 33, 2, 0, 'glow_out')

# Hood
mage.rect(10, 6, 5, 5, 'cloak_mid')
mage.rect(9, 8, 7, 4, 'cloak_mid')
mage.rect(11, 5, 3, 2, 'cloak_mid')

# Body
for y in range(12, 32):
    w = 6 + int((y - 12) / 1.5)
    x1 = int(12 - w/2)
    x2 = int(12 + w/2)
    mage.line(x1, y, x2, y, 'cloak_mid')

# Dark folds
mage.line(11, 12, 9, 31, 'cloak_dark')
mage.line(12, 12, 11, 31, 'cloak_dark')
mage.line(14, 14, 15, 31, 'cloak_dark')
mage.line(10, 19, 8, 31, 'cloak_dark')

# Highlight from the staff on the right side
for y in range(10, 32):
    w = 6 + int((y - 12) / 1.5) if y >= 12 else 6
    x2 = int(12 + w/2)
    if y < 12: x2 = 15
    
    mage.set(x2, y, 'glow_out')
    mage.set(x2-1, y, 'cloak_hi')
    mage.set(x2-2, y, 'cloak_light')
    if y % 2 == 0:
        mage.set(x2-3, y, 'cloak_light')

# Staff Glow
mage.circle(20, 9, 6, 'glow_faint')
mage.circle(20, 9, 4, 'glow_out')
mage.circle(20, 9, 2, 'glow_mid')
mage.circle(20, 9, 1, 'glow_core')

# Staff
mage.line(20, 10, 20, 32, 'staff')
mage.line(19, 11, 19, 32, 'staff')

output.blit(mage, 43, 182)

# Vines
random.seed(42)

def draw_vine(c, start_x, start_y, length, dir_x):
    x, y = start_x, start_y
    pts = [(x, y)]
    for i in range(length):
        x += dir_x + random.uniform(-1, 1)
        y += random.uniform(0.5, 2.0)
        pts.append((x, y))
    
    # draw main stem
    for i in range(len(pts)-1):
        c.line(int(pts[i][0]), int(pts[i][1]), int(pts[i+1][0]), int(pts[i+1][1]), 'vine1')
        
    # draw leaves
    for px, py in pts:
        if random.random() < 0.6:
            lx = int(px) + random.choice([-2, -1, 1, 2])
            ly = int(py) + random.choice([-1, 0, 1])
            c.rect(lx, ly, 2, 2, random.choice(['vine2', 'vine3']))
            if random.random() < 0.4:
                c.set(lx, ly, 'vine1')

vine_layer = new_canvas(144, 256)

# Top vines
for _ in range(15):
    sx = random.randint(45, 65)
    sy = random.randint(45, 60)
    length = random.randint(20, 50)
    draw_vine(vine_layer, sx, sy, length, random.uniform(-0.2, 0.4))

for _ in range(10):
    sx = random.randint(70, 85)
    sy = random.randint(55, 75)
    length = random.randint(15, 40)
    draw_vine(vine_layer, sx, sy, length, random.uniform(-0.4, 0.2))

# Lower roof vines
for _ in range(8):
    sx = random.randint(45, 85)
    sy = random.randint(150, 155)
    length = random.randint(10, 25)
    draw_vine(vine_layer, sx, sy, length, random.uniform(-0.3, 0.3))

output.blit(vine_layer, 0, 0)

finish(output)
