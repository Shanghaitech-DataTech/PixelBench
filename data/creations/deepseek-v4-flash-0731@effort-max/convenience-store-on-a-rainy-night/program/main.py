from pixelbench_api import *

c = new_canvas(64, 64, name="store")

# ---------- palette ----------
SKY0   = "#0a0d24"; SKY1 = "#10143a"; SKY2 = "#1a2050"
RAIN   = "#7f92d6"; RAINL = "#a5b4ea"
ALLEY  = "#1d2140"
ROOF   = "#232748"; ROOFH = "#3a4170"; ROOFD = "#161a34"
FAS    = "#211f3d"
SF     = "#b83a2a"; ST   = "#f4ecd8"
WALL   = "#2c3050"; WALLD = "#242744"
FRAME  = "#5b3f22"
IB     = "#fdf3c8"; I2   = "#ffd77e"; I3  = "#f2bd5f"
SHELF  = "#d9a34f"
R1     = "#d8504f"; B1   = "#4f9fd8"; G1  = "#6fbf6f"; P1 = "#e8a0c8"
COOL   = "#b8ecf2"
DF     = "#262a4c"; DI   = "#ffe89a"
YC     = "#f2c53f"; YD   = "#d9a92e"; YS  = "#5fb98a"; BOOT = "#1c1f38"
RACK   = "#4a4f70"; RD   = "#3a3f5e"
U1     = "#c94f4f"; U2   = "#4f7fce"; UT  = "#d9d9e8"
BT     = "#4fc0a8"; BD   = "#3a9c88"; TIRE = "#171b33"; RIM  = "#4a5078"
SW     = "#4a5074"; CURB = "#3a3f5e"
PD     = "#23274a"; RY   = "#f2c55e"; RS  = "#9ec8e8"; SP   = "#c99b4f"
STREET = "#262a48"
POST   = "#3c4168"; PS   = "#e8734f"

# ---------- sky ----------
c.rect(0, 0, 64, 1, SKY0)
c.rect(0, 1, 64, 2, SKY1)
c.rect(0, 3, 64, 8, SKY2)
c.rect(0, 10, 3, 40, ALLEY)
c.rect(60, 10, 4, 40, ALLEY)

# ---------- building shell ----------
c.rect(3, 10, 58, 1, ROOFH)
c.rect(3, 11, 58, 2, ROOF)
c.rect(3, 13, 58, 1, ROOFD)
c.rect(4, 13, 56, 9, FAS)
c.rect(9, 14, 45, 8, SF)
c.text(22, 15, "STORE", ST)
c.rect(4, 22, 56, 29, WALL)

# ---------- big lit window ----------
c.rect(8, 23, 25, 25, FRAME)
c.rect(9, 24, 23, 6, IB)
c.rect(9, 30, 23, 9, I2)
c.rect(9, 39, 23, 8, I3)
c.rect(27, 39, 5, 7, COOL)
c.rect(9, 30, 23, 1, SHELF)
c.rect(9, 35, 23, 1, SHELF)
c.rect(9, 40, 23, 1, SHELF)
# goods on shelves
c.rect(10, 28, 2, 1, R1); c.rect(14, 28, 1, 1, G1)
c.rect(17, 28, 2, 1, P1); c.rect(21, 28, 2, 1, B1)
c.rect(11, 33, 2, 1, B1); c.rect(15, 34, 1, 1, R1)
c.rect(18, 33, 2, 1, G1); c.rect(22, 34, 2, 1, P1)
c.rect(10, 38, 2, 1, P1); c.rect(14, 38, 1, 1, B1)
c.rect(18, 38, 2, 1, R1); c.rect(12, 39, 2, 1, G1)
# glass glints
c.rect(11, 25, 5, 1, IB); c.rect(16, 26, 4, 1, IB); c.rect(12, 32, 3, 1, IB)
# mullions + sill
c.rect(14, 23, 1, 25, FRAME)
c.rect(20, 23, 1, 25, FRAME)
c.rect(26, 23, 1, 25, FRAME)
c.rect(34, 47, 26, 1, RD)

# ---------- door / doorway ----------
c.rect(35, 23, 14, 27, DF)
c.rect(36, 24, 12, 23, DI)
c.rect(36, 36, 12, 2, DF)
c.rect(36, 44, 12, 2, DF)
c.rect(44, 29, 1, 5, FRAME)
c.rect(58, 22, 1, 28, WALLD)
c.rect(59, 22, 1, 28, WALLD)

# ---------- poster on right wall ----------
c.rect(51, 25, 6, 9, POST)
c.rect(52, 26, 4, 7, PS)
c.set(53, 27, G1)

# ---------- sidewalk, curb, street ----------
c.rect(0, 50, 64, 8, SW)
c.rect(0, 58, 64, 2, CURB)
c.rect(0, 60, 64, 4, STREET)

# light spilling onto the wet walk
c.rect(8, 50, 25, 1, SP)
c.rect(36, 50, 12, 1, SP)
c.rect(12, 51, 5, 1, RY); c.rect(20, 51, 4, 1, RY)
c.rect(38, 51, 5, 1, RY); c.rect(42, 52, 4, 1, RY)

# ---------- reflective puddles ----------
c.ellipse(20, 55, 7, 2, PD)
c.rect(16, 54, 5, 1, RY)
c.rect(18, 56, 5, 1, RY)
c.set(15, 55, RS)
c.ellipse(41, 56, 6, 2, PD)
c.rect(38, 55, 4, 1, RY)
c.rect(41, 57, 3, 1, RS)
c.ellipse(30, 61, 13, 2, PD)
c.rect(24, 60, 8, 1, RY)
c.rect(20, 61, 4, 1, RS)
c.rect(32, 62, 7, 1, RY)
c.ellipse(51, 62, 6, 1, PD)
c.rect(48, 61, 4, 1, RS)

# ---------- umbrella rack ----------
c.rect(50, 33, 1, 13, RACK)
c.rect(55, 33, 1, 13, RACK)
c.rect(50, 32, 6, 1, RACK)
c.rect(50, 46, 6, 2, RACK)
c.rect(51, 34, 2, 13, U1)
c.rect(53, 34, 2, 12, U2)
c.set(52, 33, UT)
c.set(53, 35, UT)

# ---------- parked bicycle on the sidewalk in front of the store ----------
c.circle(11, 50, 4, TIRE)
c.circle(24, 50, 4, TIRE)
c.circle(11, 50, 1, RIM)
c.circle(24, 50, 1, RIM)
c.line(15, 44, 16, 48, BT)
c.line(16, 48, 11, 50, BT)
c.line(24, 45, 24, 50, BT)
c.line(16, 48, 24, 45, BT)   # top tube
c.line(24, 45, 27, 43, BT)   # handlebar
c.rect(14, 43, 4, 1, BD)
c.rect(27, 42, 2, 1, BD)
c.set(16, 48, BD)
c.set(17, 48, BD)
c.line(16, 48, 14, 54, RIM)  # kickstand

# ---------- person in a raincoat entering ----------
c.ellipse(41, 28, 2, 2, YD)
c.set(41, 28, BOOT)
c.set(42, 28, BOOT)
c.rect(39, 31, 2, 15, YC)
c.rect(41, 31, 3, 15, YD)
c.rect(40, 32, 1, 12, YS)
c.rect(39, 45, 2, 3, YC)
c.rect(41, 46, 2, 3, YC)
c.rect(38, 47, 2, 2, BOOT)
c.rect(42, 48, 2, 2, BOOT)

# ---------- rain ----------
for i in range(22):
    x = (i * 7 + 2) % 64
    y = (i * 5 + 2) % 8
    col = RAINL if i % 3 == 0 else RAIN
    c.line(x, y, x + 1, y + 2, col)
for i in range(7):
    x = (i * 9 + 4) % 64
    y = 51 + (i * 2) % 7
    c.line(x, y, x, y + 2, RAIN)

print(c.stats_text())
print(c.matrix_text(region=(8, 23, 33, 49)))
print(c.matrix_text(region=(0, 0, 63, 12)))
print(c.matrix_text(region=(0, 60, 63, 63)))

finish(c)
