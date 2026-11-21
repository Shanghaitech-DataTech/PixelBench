import math

W = H = 32
c = new_canvas(W, H, name="compass")
CX = CY = 15.5
SQ = math.sqrt(2.0)

# ---------------------------------------------------------------- palette
OUT    = '#120c06'   # thick dark outline
OUT2   = '#2e1f0e'   # warm near-black, recesses
GOLD_L = '#ffedb0'   # brightest gold
GOLD_1 = '#f4cf60'   # light gold
GOLD_2 = '#d9a633'   # mid gold
GOLD_3 = '#a9762a'   # shadow gold
GOLD_4 = '#77501d'   # deep shadow gold
FACE_1 = '#97692b'   # dial lit
FACE_2 = '#6a4418'   # dial mid
FACE_3 = '#4a2f10'   # dial shadow ring
ROSE_L = '#fdf5d6'   # compass rose lit face
ROSE_M = '#e6cd93'   # compass rose mid
ROSE_D = '#b78c48'   # compass rose shadow face
BLUE_1 = '#e6fdff'   # crystal specular
BLUE_2 = '#8fe4ff'   # crystal light facet
BLUE_3 = '#37a4e8'   # crystal table
BLUE_4 = '#1c68a8'   # crystal dark facet
BLUE_5 = '#123f6b'   # crystal deepest

# ---------------------------------------------------------------- geometry
R_OUT    = 14.6   # outside of dark outline
R_RIM    = 12.9   # outside of gold rim
R_SEP    = 10.9   # outside of dark separator ring
R_FACE   = 10.1   # outside of dial face
R_RING   = 4.6    # outside of dark ring around crystal
R_GEM    = 3.6    # outside of crystal
ROSE_TIP = 9.3    # cardinal points
ROSE_DIAG = 7.0   # diagonal points
ROSE_VAL = 5.1    # valley between points

STEP = math.pi / 4.0      # 45 deg between rose points
ALPHA = STEP / 2.0


def tip_len(phi):
    m = int(math.floor(phi / (math.pi / 4.0) + 0.5))
    return ROSE_TIP if m % 2 == 0 else ROSE_DIAG


def _pt(phi, rr):
    return (rr * math.cos(phi), rr * math.sin(phi))


def star_rad(theta):
    """Radius of the 8-point rose boundary at angle theta."""
    k = math.floor(theta / STEP)
    phi0 = k * STEP
    local = theta - phi0
    if local <= ALPHA:
        P1 = _pt(phi0, tip_len(phi0))
        P2 = _pt(phi0 + ALPHA, ROSE_VAL)
    else:
        P1 = _pt(phi0 + ALPHA, ROSE_VAL)
        P2 = _pt(phi0 + STEP, tip_len(phi0 + STEP))
    Dx, Dy = P2[0] - P1[0], P2[1] - P1[1]
    dxr, dyr = math.cos(theta), math.sin(theta)
    den = dxr * Dy - dyr * Dx
    if abs(den) < 1e-9:
        return ROSE_VAL
    s = (P1[0] * Dy - P1[1] * Dx) / den
    return s


def star_delta(theta):
    """Signed angular offset from the nearest tip (negative = lit side)."""
    phi = round(theta / STEP) * STEP
    d = theta - phi
    while d > ALPHA:
        d -= STEP
    while d < -ALPHA:
        d += STEP
    return d


for y in range(H):
    for x in range(W):
        dx = x - CX
        dy = y - CY
        r = math.hypot(dx, dy)
        if r > R_OUT:
            continue
        th = math.atan2(dy, dx)
        # light comes from the top-left
        a = (-dx - dy) / (r * SQ) if r > 0.01 else 1.0

        if r > R_RIM:
            # ---- thick dark outline, softened on the lit side
            c.set(x, y, OUT2 if (a > 0.55 and r < R_OUT - 0.7) else OUT)
        elif r > R_SEP:
            # ---- gold rim, bevelled
            t = (r - R_SEP) / (R_RIM - R_SEP)
            sc = a * 0.85 + (t - 0.5) * 0.55
            if sc > 0.72:
                col = GOLD_L
            elif sc > 0.34:
                col = GOLD_1
            elif sc > 0.0:
                col = GOLD_2
            elif sc > -0.40:
                col = GOLD_3
            else:
                col = GOLD_4
            c.set(x, y, col)
        elif r > R_FACE:
            # ---- dark separator ring between rim and dial
            c.set(x, y, OUT2 if a > 0.2 else OUT)
        elif r > R_RING:
            # ---- dial face
            if r > 9.3:
                col = FACE_3
            elif a > 0.45:
                col = FACE_1
            else:
                col = FACE_2
            # compass rose
            sr = star_rad(th)
            if r <= sr + 0.2:
                d = star_delta(th)
                if d < -0.02:
                    col = ROSE_L if r < sr - 1.2 else ROSE_M
                elif d > 0.02:
                    col = ROSE_D
                else:
                    col = ROSE_M
            else:
                # small engraved tick marks between the rose points
                va = (th - ALPHA) / STEP
                if abs(va - round(va)) < 0.055 and 8.2 < r < 9.25:
                    col = FACE_3
            c.set(x, y, col)
        elif r > R_GEM:
            c.set(x, y, OUT)
        else:
            # ---- blue crystal, radial facets
            if r > 2.1:
                b = math.cos(th + 0.75 * math.pi)   # lit from top-left
                if b > 0.4:
                    col = BLUE_2
                elif b < -0.4:
                    col = BLUE_4
                else:
                    col = BLUE_3
            else:
                col = BLUE_3
            c.set(x, y, col)

# ---------------------------------------------------------------- crystal detail
c.set(14, 13, BLUE_2)
c.set(13, 14, BLUE_2)
c.set(14, 14, BLUE_1)
c.set(16, 17, BLUE_4)
c.set(17, 16, BLUE_4)
c.set(17, 17, BLUE_5)

# ---------------------------------------------------------------- aged wear nicks
c.set(5, 9, GOLD_1)
c.set(26, 10, GOLD_4)
c.set(10, 25, GOLD_4)

save("ancient_compass", c)
view(c)
print(c.stats_text())
finish(c)
