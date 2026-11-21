import random
from pixelbench_api import *

random.seed(42)
c = new_canvas(128, 128)

# Palette definitions
sky = c.color("#0a0a14")
wall_mid = c.color("#151522")
wall_dark = c.color("#0d0d16")
ground = c.color("#11111a")

dist1 = c.color("#0a0a1a")
dist2 = c.color("#050510")
dist3 = c.color("#080815")
dist_light_y = c.color("#aaaa00")
dist_light_c = c.color("#00aaaa")
dist_light_m = c.color("#aa00aa")
back_ground = c.color("#08080c")

grid_col = c.color("#1a1a28")

vm_side = c.color("#441122")
vm_front = c.color("#ff2255")
vm_glass = c.color("#e0f7fa")
vm_red = c.color("#ff0000")
vm_green = c.color("#00ff00")
vm_blue = c.color("#0000ff")
vm_logo = c.color("#ff0055")
vm_slot = c.color("#000000")

sign_r_bg = c.color("#112233")
sign_r_neon = c.color("#00ffff")
sign_r_glow = c.color("#008888")

sign_l_bg = c.color("#331122")
sign_l_neon = c.color("#ff0077")
sign_l_glow = c.color("#880044")
sign_l_text = c.color("#ffffff")

ref_c_low = c.color("#0d333a")
ref_c_mid = c.color("#0a5560")
ref_m_low = c.color("#331122")
ref_m_mid = c.color("#551133")
ref_v_low = c.color("#3a1520")
ref_v_mid = c.color("#551a2a")

puddle = c.color("#1a1a24")
pud_c_high = c.color("#118899")
pud_m_high = c.color("#881155")
pud_v_high = c.color("#882244")

person_col = c.color("#000000")
person_ref = c.color("#0a0a10")
rim_c = c.color("#00aaaa")
rim_m = c.color("#aa0044")

cable = c.color("#000000")

rain1 = c.color("#445566")
rain2 = c.color("#778899")

trash1 = c.color("#555555")
trash2 = c.color("#888888")
trash3 = c.color("#444455")
trash_glow = c.color("#005555")

# 1. Base colors
c.rect(0, 0, 128, 128, sky)

# 2. Back wall / Distant buildings
c.rect(48, 48, 10, 32, dist1)
c.rect(58, 52, 14, 28, dist2)
c.rect(72, 45, 8, 35, dist3)

c.rect(50, 50, 2, 2, dist_light_y)
c.rect(54, 55, 2, 2, dist_light_c)
c.rect(74, 60, 2, 2, dist_light_m)
c.rect(48, 70, 32, 10, back_ground)

# 3. Left Wall
c.poly([(0, 0), (48, 48), (48, 80), (0, 128)], wall_mid)
for i in range(1, 5):
    x = i * 12
    c.line(x, x, x, 128 - x, wall_dark)

# 4. Right Wall
c.poly([(128, 0), (80, 48), (80, 80), (128, 128)], wall_mid)
for i in range(1, 5):
    x = 128 - i * 12
    c.line(x, 128 - x, x, x, wall_dark)

# 5. Ground
c.poly([(0, 128), (48, 80), (80, 80), (128, 128)], ground)
for y in range(84, 128, 6):
    left_x = int(48 - (y - 80) * (48 / 48))
    right_x = int(80 + (y - 80) * (48 / 48))
    c.line(left_x, y, right_x, y, grid_col)

# 6. Cyber City Sign (Background)
c.text(50, 36, "CYBER", sign_l_neon, font="5x7")
c.text(54, 44, "CITY", sign_r_neon, font="5x7")

# 7. Vending Machine (Left Wall)
c.poly([(24, 58), (36, 60), (36, 92), (24, 104)], vm_side)
c.poly([(36, 60), (46, 60), (46, 92), (36, 92)], vm_front)
c.poly([(38, 64), (44, 64), (44, 84), (38, 84)], vm_glass)
c.rect(39, 66, 2, 4, vm_red)
c.rect(42, 66, 2, 4, vm_green)
c.rect(39, 72, 2, 4, vm_blue)
c.poly([(28, 72), (32, 71), (32, 81), (28, 84)], vm_logo)
c.rect(40, 86, 4, 3, vm_slot)
c.line(45, 70, 45, 80, vm_green)

# 8. Right Neon Sign
c.poly([(104, 36), (94, 36), (94, 76), (104, 76)], sign_r_bg)
c.line(99, 40, 99, 72, sign_r_neon)
c.line(98, 40, 98, 72, sign_r_glow)
c.line(100, 40, 100, 72, sign_r_glow)
c.line(96, 45, 102, 47, sign_r_neon)
c.line(96, 62, 102, 64, sign_r_neon)

# 9. Left Neon Sign
c.poly([(20, 20), (30, 20), (30, 60), (20, 60)], sign_l_bg)
c.line(25, 24, 25, 56, sign_l_neon)
c.line(24, 24, 24, 56, sign_l_glow)
c.line(26, 24, 26, 56, sign_l_glow)
c.set(25, 28, sign_l_text)
c.set(25, 36, sign_l_text)
c.set(25, 44, sign_l_text)
c.set(25, 52, sign_l_text)

# 10. Ground Reflections
c.rect(96, 100, 6, 28, ref_c_low)
c.rect(98, 105, 2, 15, ref_c_mid)
c.rect(22, 100, 6, 28, ref_m_low)
c.rect(24, 105, 2, 15, ref_m_mid)
c.rect(36, 96, 8, 20, ref_v_low)
c.rect(38, 100, 4, 12, ref_v_mid)

# 11. Puddles
c.ellipse(64, 100, 20, 6, puddle)
c.ellipse(45, 115, 15, 4, puddle)
c.ellipse(90, 110, 18, 5, puddle)
c.ellipse(75, 88, 12, 3, puddle)
c.ellipse(25, 112, 10, 3, puddle)

# 12. Person reflection
c.rect(60, 102, 8, 10, person_ref)

# 13. Puddle Reflections
c.line(60, 98, 68, 98, pud_m_high)
c.line(62, 102, 66, 102, pud_c_high)
c.line(85, 108, 95, 108, pud_c_high)
c.line(88, 110, 92, 110, sign_r_neon)
c.line(40, 114, 50, 114, pud_v_high)
c.line(43, 115, 47, 115, vm_logo)
c.line(72, 87, 78, 87, pud_c_high)
c.line(20, 112, 30, 112, pud_m_high)
c.line(23, 113, 27, 113, sign_l_neon)

# 14. Trash
c.rect(30, 110, 3, 2, trash1)
c.rect(31, 109, 2, 1, trash2)
c.rect(100, 115, 4, 3, trash3)
c.rect(105, 116, 2, 2, trash_glow)

# 15. Cables
c.path("M 0 10 Q 64 30 128 0", cable, fill=False)
c.path("M 0 30 Q 64 50 128 20", cable, fill=False)
c.path("M 20 20 Q 64 60 104 36", cable, fill=False)
c.path("M 48 48 Q 64 64 80 48", cable, fill=False)
c.path("M 0 60 Q 40 80 80 48", cable, fill=False)

# 16. Person
c.rect(60, 80, 8, 25, person_col) # Body
c.rect(62, 73, 4, 6, person_col) # Head
c.rect(60, 100, 3, 10, person_col) # Leg 1
c.rect(65, 100, 3, 8, person_col) # Leg 2

# 17. Rim lights
c.line(67, 80, 67, 100, rim_c)
c.line(65, 73, 65, 78, rim_c)
c.line(60, 80, 60, 100, rim_m)
c.line(62, 73, 62, 78, rim_m)

# 18. Umbrella via blit
umb_c = new_canvas(128, 128)
umb_fill = c.color("#aaddff55")
umb_edge = c.color("#aaddffaa")
umb_hi = c.color("#ffffffcc")
umb_handle = c.color("#888888")

umb_c.path("M 48 75 Q 64 55 80 75 Q 64 70 48 75 Z", umb_fill, fill=True)
umb_c.path("M 48 75 Q 64 55 80 75", umb_edge, fill=False)
umb_c.path("M 48 75 Q 64 70 80 75", umb_edge, fill=False)
umb_c.path("M 52 70 Q 64 60 76 70", umb_hi, fill=False)
umb_c.line(64, 75, 64, 85, umb_handle)

c.blit(umb_c, 0, 0)

# 19. Rain
for _ in range(200):
    rx = random.randint(0, 127)
    ry = random.randint(0, 127)
    length = random.randint(2, 5)
    c.line(rx, ry, rx - length//2, ry + length, rain1 if random.random() > 0.2 else rain2)

for _ in range(30):
    rx = random.randint(10, 118)
    ry = random.randint(85, 125)
    c.line(rx-1, ry, rx+1, ry, rain2)
    c.set(rx, ry-1, rain2)

finish(c)
