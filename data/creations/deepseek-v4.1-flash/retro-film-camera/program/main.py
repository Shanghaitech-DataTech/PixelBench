import math

# ---------------- palette ----------------
OUT     = "#141110"
LEATH_D = "#232329"
LEATH   = "#34343d"
LEATH_L = "#4a4a54"
SILV_D  = "#6b7079"
SILV    = "#a8adb7"
SILV_L  = "#e2e7ec"
RING_D  = "#1b1d22"
RING    = "#3a3f47"
GL0     = "#0e1a24"
GL1     = "#17303f"
GL2     = "#2a5a72"
GL3     = "#5d9cb8"
GL4     = "#c3ecf7"
RED_D   = "#7d211c"
RED     = "#b8342c"
RED_L   = "#e26450"
WIN     = "#26313a"

CX, CY = 15, 18

c = new_canvas(32, 32, background=None, name="result")

# ---------------- leather body (x 1..30, y 10..26) ----------------
c.rect(1, 10, 30, 17, LEATH)
for y in range(10, 27):
    for x in range(1, 31):
        if (x * 3 + y * 5) % 7 == 0:
            c.set(x, y, LEATH_D)
        elif (x * 5 + y * 11) % 13 == 0:
            c.set(x, y, LEATH_L)

# soft dithered shadow on the leather under the lens
for y in range(10, 27):
    for x in range(1, 31):
        dx, dy = x - CX, y - CY
        if 7.8 < math.hypot(dx, dy) <= 9.9 and dy >= 2 and (x + y) % 2 == 0:
            c.set(x, y, LEATH_D)

# ---------------- bottom plate (y 27..28) ----------------
c.rect(1, 27, 30, 2, SILV)
c.line(1, 27, 30, 27, SILV_L)
c.line(1, 28, 30, 28, SILV_D)

# ---------------- top plate (y 7..9) ----------------
c.rect(1, 7, 30, 3, SILV)
c.line(1, 7, 30, 7, SILV_L)
c.line(1, 9, 30, 9, SILV_D)

# ---------------- pentaprism hump ----------------
c.poly([(9, 9), (12, 3), (19, 3), (22, 9)], SILV)
c.line(13, 4, 18, 4, SILV_L)
c.line(12, 4, 9, 9, SILV_L)
c.line(19, 4, 22, 9, SILV_D)
c.rect(14, 5, 4, 2, WIN)
c.line(14, 5, 17, 5, GL2)

# ---------------- rewind knob (left) ----------------
c.rect(3, 3, 6, 5, RING_D)
c.rect(4, 4, 4, 3, SILV_D)
c.line(4, 4, 7, 4, SILV)
c.line(3, 7, 8, 7, RING_D)
c.set(5, 5, SILV)
c.set(6, 6, SILV)

# ---------------- shutter button (right, red) ----------------
c.rect(23, 4, 5, 4, SILV_D)
c.rect(24, 4, 3, 3, RED_D)
c.rect(24, 5, 3, 2, RED)
c.line(24, 5, 26, 5, RED_L)

# ---------------- film counter window (right of lens) ----------------
c.rect(24, 13, 5, 5, SILV_D)
c.rect(25, 14, 3, 3, WIN)
c.set(26, 15, GL2)
c.set(26, 16, RED)

# ---------------- lens ----------------
c.circle(CX, CY, 8, OUT)       # dark halo separating lens from body
c.circle(CX, CY, 7, SILV_D)    # knurled focus ring
c.circle(CX, CY, 6, RING_D)    # barrel gap
c.circle(CX, CY, 5, GL1)       # glass

for deg in range(0, 360, 22):
    a = math.radians(deg)
    c.set(int(round(CX + 6.6 * math.cos(a))),
          int(round(CY + 6.6 * math.sin(a))), RING)   # knurl ticks

for y in range(32):
    for x in range(32):
        dx, dy = x - CX, y - CY
        d = math.hypot(dx, dy)
        if 5.7 < d <= 7.4 and dx <= -1 and dy <= -1:
            c.set(x, y, SILV)              # chrome light, upper-left of ring
        elif d <= 5.3:
            if dx + dy >= 3:
                c.set(x, y, GL0)           # shadowed lower-right of glass
            elif dx + dy <= -2:
                c.set(x, y, GL2)           # lit upper-left rim of glass

# glass specular
c.circle(CX - 3, CY - 3, 1, GL3)
c.set(CX - 3, CY - 3, GL4)
c.set(CX + 1, CY + 3, GL2)

# red mount-alignment dot on the ring
c.set(CX + 7, CY, RED)

# ---------------- dark outline ----------------
c.outline(OUT)

print(c.stats_text())
print(c.matrix_text(region=(0, 1, 31, 31)))
print(c.palette())

save("retro_film_camera", c)
finish(c)
