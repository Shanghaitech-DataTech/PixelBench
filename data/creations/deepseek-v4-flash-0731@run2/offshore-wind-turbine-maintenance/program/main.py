from pixelbench_api import *

W = H = 64
c = new_canvas(W, H, name="offshore_maintenance")

def fill_rows(y0, y1, col):
    for y in range(y0, y1 + 1):
        c.rect(0, y, W, 1, col)

# ---------------- SKY ----------------
fill_rows(0, 3, '#8FC9F5')
fill_rows(4, 7, '#7ABDEB')
fill_rows(8, 12, '#66B0E0')
fill_rows(13, 18, '#54A1D4')
fill_rows(19, 25, '#4592C8')
fill_rows(26, 33, '#3884BC')
fill_rows(34, 43, '#2E77B0')

# clouds
c.ellipse(14, 9, 7, 3, '#F4FAFE')
c.ellipse(19, 7, 4, 2, '#F4FAFE')
c.rect(8, 11, 13, 1, '#D9EEFB')
c.ellipse(48, 21, 5, 2, '#F4FAFE')
c.rect(44, 22, 9, 1, '#D9EEFB')
c.ellipse(28, 24, 4, 2, '#F4FAFE')
c.rect(25, 25, 7, 1, '#D9EEFB')

# ---------------- OCEAN ----------------
fill_rows(44, 47, '#3578AC')
fill_rows(48, 51, '#2D6C9F')
fill_rows(52, 54, '#265F92')
fill_rows(55, 57, '#215386')
fill_rows(58, 59, '#1D4A7B')
fill_rows(60, 63, '#194270')

# base ripples
for (y, x0, x1, col) in [
    (45, 4, 17, '#5FA6CE'), (45, 50, 60, '#5FA6CE'),
    (46, 30, 42, '#5FA6CE'),
    (47, 10, 15, '#8AC4E0'),
    (49, 40, 48, '#5FA6CE'),
    (51, 6, 12, '#8AC4E0'),
    (52, 24, 30, '#5FA6CE'),
    (53, 52, 60, '#8AC4E0'),
    (55, 14, 20, '#5FA6CE'),
    (56, 44, 50, '#8AC4E0'),
    (58, 30, 34, '#5FA6CE'),
    (59, 8, 14, '#8AC4E0'),
    (60, 54, 58, '#5FA6CE'),
    (61, 20, 26, '#8AC4E0'),
    (62, 40, 46, '#5FA6CE'),
    (63, 2, 8, '#8AC4E0'),
]:
    c.line(x0, y, x1, y, col)

# ---------------- DISTANT TURBINES ----------------
def distant_turbine(cx, base):
    c.rect(cx - 1, base - 6, 3, 6, '#6B84A3')      # tower
    c.rect(cx - 2, base - 9, 5, 3, '#5E7A99')      # nacelle
    c.line(cx, base - 8, cx - 5, base - 11, '#4E6B8C')
    c.line(cx, base - 8, cx + 5, base - 10, '#4E6B8C')
    c.line(cx, base - 8, cx + 2, base - 5, '#4E6B8C')

distant_turbine(11, 46)
distant_turbine(54, 45)

# ---------------- MAIN TURBINE ----------------
# tower
c.rect(36, 10, 3, 50, '#CDD6E0')   # y10..59
c.rect(39, 10, 5, 50, '#AAB6C4')
c.rect(44, 10, 1, 50, '#5D6E83')
# base flare (jacket transition)
c.rect(34, 60, 3, 4, '#CDD6E0')
c.rect(37, 60, 9, 4, '#5D6E83')
c.rect(46, 60, 2, 3, '#3E4D61')
c.rect(34, 60, 15, 1, '#3E4D61')

# nacelle
c.rect(33, 4, 18, 6, '#E7EDF3')
c.rect(33, 4, 18, 1, '#FDFEFF')
c.rect(33, 9, 18, 1, '#AEBBC9')
c.rect(35, 5, 2, 3, '#AEBBC9')

# blades + hub
c.line(42, 7, 22, 1, '#F0F4F8')
c.line(43, 8, 23, 2, '#C3CDD8')
c.line(42, 7, 61, 2, '#F0F4F8')
c.line(43, 8, 62, 3, '#C3CDD8')
c.line(42, 7, 46, 25, '#F0F4F8')
c.line(43, 8, 47, 26, '#C3CDD8')
c.circle(42, 7, 2, '#F0F4F8')
c.set(42, 8, '#C3CDD8')

# ---------------- MAINTENANCE PLATFORM ----------------
# deck
c.rect(16, 30, 37, 2, '#F6C344')
c.rect(16, 32, 37, 1, '#D9A51B')
c.rect(16, 33, 37, 1, '#A87D12')
for x in range(17, 53, 4):
    c.set(x, 32, '#A87D12')
# railing
c.rect(16, 26, 37, 1, '#B7C1CC')
for x in range(16, 53, 4):
    c.rect(x, 27, 1, 3, '#B7C1CC')
# cabinet on deck
c.rect(24, 27, 5, 3, '#D8DEE6')
c.rect(25, 28, 3, 1, '#8E9AA9')

# ---------------- LADDER + TECHNICIAN ----------------
c.rect(34, 12, 2, 18, '#EDB320')
for y in range(13, 30, 3):
    c.rect(34, y, 2, 1, '#A87D12')
# technician climbing (back view)
c.rect(34, 15, 3, 2, '#F2F5F8')   # helmet
c.rect(34, 17, 3, 2, '#F4891F')   # high-vis vest
c.rect(34, 19, 2, 2, '#2F3D52')   # legs/pants
c.rect(34, 21, 2, 1, '#1F2A3B')   # boots
c.set(36, 17, '#E05E0F')           # harness strap
c.set(34, 22, '#D1540C')           # hand on rung

# ---------------- SERVICE BOAT ----------------
c.rect(6, 55, 11, 4, '#C4572F')
c.rect(7, 55, 9, 1, '#D8DEE6')
c.rect(6, 58, 11, 1, '#8E3A1C')
c.set(15, 55, '#E7EDF3')
c.line(4, 57, 5, 57, '#C4E6F4')
c.line(17, 57, 19, 57, '#C4E6F4')
c.line(5, 58, 7, 58, '#8AC4E0')
c.line(16, 56, 18, 56, '#5FA6CE')

# ---------------- FOAM AT TOWER BASE ----------------
c.line(31, 56, 50, 56, '#8AC4E0')
c.line(33, 57, 48, 57, '#C4E6F4')
c.line(35, 58, 46, 58, '#EAF6FC')
c.line(36, 59, 45, 59, '#C4E6F4')
c.line(29, 57, 32, 57, '#5FA6CE')
c.set(49, 57, '#EAF6FC')
c.set(30, 55, '#8AC4E0')

print(c.stats_text())
print("--- far left ---")
print(c.matrix_text(region=(2, 30, 22, 46)))
print("--- boat + foam ---")
print(c.matrix_text(region=(28, 52, 53, 63)))

finish(c)
