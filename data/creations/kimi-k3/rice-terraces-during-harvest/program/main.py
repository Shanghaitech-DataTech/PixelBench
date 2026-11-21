import math

# ---------------- palette (value ramps, top of canvas -> bottom for depth) ----
goldA = ['#f6d35e', '#ecc245', '#e0b035', '#d3a129', '#c69420', '#b9871c']  # bright gold
goldB = ['#e9c24c', '#deb23a', '#d1a22c', '#c59424', '#b8861e', '#ab791a']  # deep gold
goldC = ['#f0cd70', '#e6c05c', '#dab34a', '#cfa63e', '#c39934', '#b78c2c']  # pale dry gold
green = ['#b9bc60', '#acb254', '#9da649', '#8f9a3f', '#818e37', '#748231']  # unharvested
water = ['#9db9ac', '#92aea2', '#87a398', '#7c988e', '#718d84', '#668278']  # flooded paddy
ridge = ['#8f6d38', '#826130', '#755629', '#684b22', '#5b411c', '#4e3817']  # narrow ridges
pathc = ['#e6d9b0', '#decfa2', '#d6c594', '#ccbb86', '#c2b17a', '#b8a76e']  # dirt road

W = H = 64
C1 = (74.0, -18.0)    # main hill, contours sweep from top-right
C2 = (-22.0, 82.0)    # second knoll, bottom-left
BH = 6.0              # terrace band height

c = new_canvas(64, 64, name="rice-terraces-harvest")


def hash2(x, y):
    n = (x * 374761393 + y * 668265263) & 0xFFFFFFFF
    n = (n ^ (n >> 13)) * 1274126177 & 0xFFFFFFFF
    return (n ^ (n >> 16)) & 0xFFFF


# ---------------- terraced ground ------------------------------------------
for y in range(64):
    z = min(5, (y * 6) // 64)          # depth zone: lighter far, darker near
    for x in range(64):
        dx1 = x - C1[0]; dy1 = y - C1[1]
        dx2 = x - C2[0]; dy2 = y - C2[1]
        d1 = math.sqrt(dx1 * dx1 + dy1 * dy1)
        d2 = math.sqrt(dx2 * dx2 + dy2 * dy2)
        d = d1 if d1 < d2 else d2
        band = int(d / BH)
        frac = d - band * BH
        h = hash2(x, y)
        if abs(d1 - d2) < 0.95:                     # valley road between hills
            col = pathc[z]
        elif frac < 1.2:                            # narrow ridge bund
            col = ridge[z]
        else:
            r = band % 8
            if r == 3:
                lst = water
            elif r == 6:
                lst = green
            elif r in (0, 2, 5):
                lst = goldB
            elif r == 7:
                lst = goldA
            else:
                lst = goldA
            edge = frac < 2.2 and lst is not water  # sunlit bund edge
            if lst is water:
                if h % 29 == 0:
                    col = '#f5faf8'                 # sun glint
                elif h % 4 == 0:
                    col = goldB[z]                  # stubble poking through
                else:
                    col = lst[z]
            else:
                if edge:
                    col = lst[max(0, z - 1)]
                elif h % 11 == 0:                   # rice texture speckle
                    col = lst[min(5, z + 1)]
                elif h % 23 == 0:
                    col = lst[max(0, z - 1)]
                else:
                    col = lst[z]
        c.set(x, y, col)

# ---------------- village in the distance (top-left) -----------------------
c.ellipse(11, 9, 8, 6, pathc[3])                    # packed-earth clearing
c.ellipse(11, 9, 8, 6, ridge[3], fill=False)


def house(x, y):
    c.rect(x, y, 6, 1, '#48545e')                   # shadowed eave
    c.rect(x, y + 1, 6, 2, '#5d6b78')               # roof
    c.line(x + 3, y, x + 3, y + 2, '#97a5b1')       # ridge line
    c.rect(x + 1, y + 3, 4, 2, '#c9b184')           # wall
    c.set(x + 3, y + 4, '#6b4f2a')                  # door


house(4, 4)
house(12, 3)
house(7, 11)
house(16, 13)


def tree(x, y, big=False):
    if big:
        c.circle(x, y, 2, '#4c6e2b')
        c.set(x - 1, y - 1, '#74993c')
        c.set(x, y - 2, '#74993c')
        c.set(x + 1, y + 1, '#3d5c22')
        c.set(x, y, '#3d5c22')
    else:
        c.circle(x, y, 1, '#4c6e2b')
        c.set(x, y - 1, '#74993c')


tree(17, 9, big=True)
tree(2, 14)
tree(20, 6)
tree(15, 17)
tree(52, 28, big=True)
tree(9, 34)
tree(47, 51)

# ---------------- haystacks -------------------------------------------------
def hay(x, y):
    c.set(x, y, '#f0d878')
    c.set(x - 1, y + 1, '#c89a34')
    c.set(x, y + 1, '#c89a34')
    c.set(x + 1, y + 1, '#a87e28')


hay(45, 35)
hay(30, 52)
hay(43, 17)
hay(55, 44)
hay(24, 24)

# ---------------- two farmers on the narrow ridges -------------------------
def farmer(x, y, shirt, pants='#4a3b28'):
    # feet stand at (x, y+4)
    c.set(x + 1, y + 4, '#3f2f16')              # cast shadow
    c.line(x - 1, y, x + 1, y, '#e9d69b')       # straw hat brim
    c.set(x, y - 1, '#d8c17a')                  # hat crown
    c.set(x, y + 1, '#a86f3f')                  # face
    c.line(x - 1, y + 2, x + 1, y + 2, shirt)   # arms / shoulders
    c.line(x - 1, y + 3, x, y + 3, shirt)       # torso
    c.set(x - 1, y + 4, pants)                  # legs
    c.set(x, y + 4, pants)


farmer(37, 25, '#b8402f')   # feet at (37,29): on a ridge of the main hill
farmer(20, 44, '#3f6fb0')   # feet at (20,48): on a ridge of the lower knoll

view(c)
finish(c)
