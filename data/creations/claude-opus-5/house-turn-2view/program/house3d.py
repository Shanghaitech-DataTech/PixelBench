"""Fixed elevated camera renderer for the house turn-around."""
import math

# ---- palette (taken from the input image) ----
DARK = '#161c2e'
WOODD = '#6c513a'
WOOD = '#97763d'
WOODL = '#bda759'
SH = '#dcaa46'
SHM = '#c08f3f'
SHD = '#98694e'
GLOW = '#f9e279'
GLOW2 = '#e1d968'
PL = '#e1dca3'
PLM = '#cdc58c'
PLD = '#b3a987'
SHADOW = '#161c2e45'

# ---- house geometry (world units: x right, y depth away, z up) ----
W, D = 64, 56            # wall footprint
HW = 48                  # wall top
OX, OY = 8, 8            # roof overhang
WR = W / 2 + OX          # roof half span
ZE = 48                  # eave height
ZR = 76                  # ridge height (slope ~35deg, under the camera pitch
                         # so both roof planes stay visible)
YN, YF = -(D / 2 + OY), (D / 2 + OY)
ZG = ZR - (ZR - ZE) * (W / 2) / WR     # roof underside at the wall plane

PITCH = math.radians(45)                # camera elevation above the horizon
SP, CP = math.sin(PITCH), math.cos(PITCH)
VIEW = (0.0, CP, -SP)                   # unit vector from camera into the scene
LIGHT = (-0.40, -0.66, 0.64)            # from front-left, above
_ln = math.sqrt(sum(v * v for v in LIGHT))
LIGHT = tuple(v / _ln for v in LIGHT)


def rot(p, th):
    x, y, z = p
    c, s = math.cos(th), math.sin(th)
    return (x * c + y * s, -x * s + y * c, z)


def raw(p, th):
    x, y, z = rot(p, th)
    return (x, -(y * SP + z * CP))


def depth(p, th):
    x, y, z = rot(p, th)
    return y * CP - z * SP


def visible(n, th):
    return depth(n, th) < -1e-9


def bright(n, th):
    x, y, z = rot(n, th)
    m = math.sqrt(x * x + y * y + z * z)
    return (x * LIGHT[0] + y * LIGHT[1] + z * LIGHT[2]) / m


def lerp3(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t)


def bil(q, u, v):
    """q = (p00, p10, p11, p01); u left->right, v top->bottom."""
    a = lerp3(q[0], q[1], u)
    b = lerp3(q[3], q[2], u)
    return lerp3(a, b, v)


def arch(cu, hw, vtop, vbot, ar, n=16):
    """Arched opening outline in uv space; ar = face width / face height."""
    ah = hw * ar
    pts = [(cu - hw, vbot)]
    for i in range(n + 1):
        t = math.pi * i / n
        pts.append((cu - hw * math.cos(t), vtop + ah - ah * math.sin(t)))
    pts.append((cu + hw, vbot))
    return pts


# ---- faces ----
WALL_N = {'front': (0, -1, 0), 'back': (0, 1, 0), 'right': (1, 0, 0), 'left': (-1, 0, 0)}


def wall_quad(kind):
    if kind == 'front':
        y = -D / 2
        return ((-W / 2, y, HW), (W / 2, y, HW), (W / 2, y, 0), (-W / 2, y, 0))
    if kind == 'back':
        y = D / 2
        return ((W / 2, y, HW), (-W / 2, y, HW), (-W / 2, y, 0), (W / 2, y, 0))
    if kind == 'right':
        x = W / 2
        return ((x, D / 2, HW), (x, -D / 2, HW), (x, -D / 2, 0), (x, D / 2, 0))
    x = -W / 2
    return ((x, -D / 2, HW), (x, D / 2, HW), (x, D / 2, 0), (x, -D / 2, 0))


def wall_silhouette(kind):
    """Facade polygon; gable ends include the triangle up to the ridge."""
    if kind in ('front', 'back'):
        y = -D / 2 if kind == 'front' else D / 2
        return [(-W / 2, y, 0), (W / 2, y, 0), (W / 2, y, ZG),
                (0, y, ZR), (-W / 2, y, ZG)]
    q = wall_quad(kind)
    return [q[0], q[1], q[2], q[3]]


def gable_band(kind, t=6):
    """Chevron band following the two rake edges of a gable end."""
    y = -D / 2 if kind == 'front' else D / 2
    return [(-WR, y, ZE), (0, y, ZR + 3), (WR, y, ZE),
            (WR, y, ZE - t), (0, y, ZR + 3 - t), (-WR, y, ZE - t)]


def roof_quad(side):
    s = 1 if side == 'right' else -1
    return ((0, YF, ZR), (0, YN, ZR), (s * WR, YN, ZE), (s * WR, YF, ZE))


def roof_n(side):
    s = 1 if side == 'right' else -1
    return (s * (ZR - ZE), 0, WR)


class Render:
    def __init__(self, canvas, th, cx, cy):
        self.c = canvas
        self.th = th
        self.cx, self.cy = cx, cy

    def P(self, p):
        x, y = raw(p, self.th)
        return (int(round(x + self.cx)), int(round(y + self.cy)))

    def face(self, pts, colour, fill=True):
        self.c.poly([self.P(p) for p in pts], colour, fill=fill)

    def seg(self, a, b, colour):
        x0, y0 = self.P(a)
        x1, y1 = self.P(b)
        self.c.line(x0, y0, x1, y1, colour)

    def patch(self, q, u0, v0, u1, v1, colour, fill=True):
        self.face([bil(q, u0, v0), bil(q, u1, v0), bil(q, u1, v1), bil(q, u0, v1)],
                  colour, fill=fill)

    def uvpoly(self, q, uv, colour, fill=True):
        self.face([bil(q, u, v) for u, v in uv], colour, fill=fill)
