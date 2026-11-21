import math

# Teleport portal - 2 frames of 24x24 side by side on one 48x48 canvas.
W, H = 48, 48
c = new_canvas(W, H, background=None, name="portal_frames")

DEEP      = c.color("#160533", "void")
DARK      = c.color("#3b0a6b", "dark_purple")
PURPLE    = c.color("#6d28d9", "purple")
VIOLET    = c.color("#a855f7", "violet")
MAGENTA   = c.color("#d946ef", "magenta")
PINK      = c.color("#f0abfc", "pink")
NEARWHITE = c.color("#fdf4ff", "glow_white")
CYAN      = c.color("#67e8f9", "halo_cyan")
CYAN_D    = c.color("#22d3ee", "halo_cyan_dark")

def draw_portal(c, cx, cy, phase, halo):
    # base disc of void purple
    c.ellipse(cx, cy, 10, 10, DEEP, fill=True)
    # dark rim
    c.ellipse(cx, cy, 10, 10, DARK, fill=False)

    # three spiral arms of swirling energy
    for arm in range(3):
        i = 0
        while True:
            th = arm * (2 * math.pi / 3) + i * 0.17 + phase
            r = 1.2 + i * 0.135
            if r > 9.2:
                break
            x = cx + r * math.cos(th)
            y = cy + r * math.sin(th)
            if r < 2.6:
                col = PINK
            elif r < 4.8:
                col = MAGENTA
            elif r < 7.2:
                col = VIOLET
            else:
                col = PURPLE
            c.set(int(round(x)), int(round(y)), col)
            i += 1

    # bright energy core
    c.circle(cx, cy, 1, MAGENTA, fill=True)
    c.set(cx, cy, NEARWHITE)

    # orbiting sparkles on the swirl
    for k in range(6):
        a = k * (math.pi / 3) + phase * 1.7
        r = 6.0
        c.set(int(round(cx + r * math.cos(a))), int(round(cy + r * math.sin(a))), PINK)

    if halo:
        # glowing halo ring just outside the rim
        c.ellipse(cx, cy, 11, 11, CYAN, fill=False)
        # dashed outer shimmer
        for k in range(16):
            a = k * (math.pi / 8) + 0.13
            r = 11.6
            c.set(int(round(cx + r * math.cos(a))), int(round(cy + r * math.sin(a))), CYAN_D)
        # brighter core for the charged frame
        c.set(cx + 1, cy, NEARWHITE)
        c.set(cx - 1, cy, NEARWHITE)
        c.set(cx, cy + 1, NEARWHITE)
        c.set(cx, cy - 1, NEARWHITE)

# frame 1: purple energy vortex
draw_portal(c, 12, 24, phase=0.0, halo=False)
# frame 2: vortex rotated ~60 degrees with glowing halo
draw_portal(c, 36, 24, phase=math.pi / 3, halo=True)

print(c.stats_text())
finish(c)
