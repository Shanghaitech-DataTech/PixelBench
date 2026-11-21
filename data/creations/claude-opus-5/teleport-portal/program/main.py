import math

# dark -> light purple ramp
PAL = ["#190333", "#28064f", "#3a0a6e", "#4e108f", "#6418b0", "#7d26cd",
       "#9540e8", "#ad63f2", "#c48cf7", "#dbb6fb", "#f0dcff", "#ffffff"]

CX = CY = 23.5
R = 21.0
ARMS = 3
TWIST = 5.0


def swirl(r, theta, phase):
    """0..1 wave that follows a logarithmic spiral."""
    p = ARMS * theta - TWIST * math.log(max(r, 0.8)) + phase
    w = 0.5 + 0.5 * math.sin(p)
    return w


def draw_vortex(c, phase, halo=False):
    n = len(PAL) - 1
    for y in range(48):
        dy = y - CY
        for x in range(48):
            dx = x - CX
            r = math.hypot(dx, dy)
            if r > R + (4.2 if halo else 0.0):
                continue
            theta = math.atan2(dy, dx)
            w = swirl(r, theta, phase)
            if r <= R:
                rn = r / R
                arm = w ** 2.2
                level = 0.07 + 0.78 * arm * (1.0 - 0.40 * rn)
                level += max(0.0, 1.0 - r / 5.5) * 0.95      # hot core
                if rn > 0.90:
                    level += 0.32                            # rim ring
                level = min(1.0, max(0.0, level))
                c.set(x, y, PAL[int(level * n + 0.5)])
            else:
                # wispy outer halo, only in the halo frame
                t = (r - R) / 4.2
                a = (1.0 - t) * (0.45 + 0.55 * arm_wisp(w))
                a = int(a * 190 / 32.0 + 0.5) * 32
                if a > 0:
                    c.set(x, y, (178, 110, 250, min(a, 192)))


def arm_wisp(w):
    return w ** 1.6


def sparkles(c, pts):
    for x, y in pts:
        c.set(x, y, "#ffffff")


# frame 1 - purple energy vortex
f1 = new_canvas(48, 48, name="frame1")
draw_vortex(f1, 0.0)
sparkles(f1, [(23, 10), (34, 30), (13, 27)])

# frame 2 - vortex rotated, with a glowing halo
f2 = new_canvas(48, 48, name="frame2")
draw_vortex(f2, 2.1, halo=True)
sparkles(f2, [(30, 12), (16, 33), (36, 24)])
# halo accent ring
for i in range(72):
    a = i / 72.0 * 2 * math.pi
    rr = R + 1.6
    x = int(round(CX + rr * math.cos(a)))
    y = int(round(CY + rr * math.sin(a)))
    w = swirl(rr, a, 2.1)
    if w > 0.35:
        f2.set(x, y, (214, 170, 255, 160))

save("portal_frame1", f1)
save("portal_frame2", f2)
view(f1)
view(f2)
print(f1.stats_text())
print(f2.stats_text())

# single deliverable: the rotated vortex with its glowing halo
result = f2
finish(result)
