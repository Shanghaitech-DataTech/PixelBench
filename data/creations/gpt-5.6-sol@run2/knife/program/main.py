from pixelbench_api import *

# Rotate the supplied knife as one exact pixel patch: tip right, cutting edge down.
src = input_canvas
knife = src.select(0, 0, 93, 128).rotate(124, algorithm="nearest").preview()
W, H = 224, 160

# Repaint exact rotated silhouettes as cool translucent afterimages.
def ghost_from(source, alpha, name):
    g = new_canvas(source.stats()["size"][0], source.stats()["size"][1], background=None, name=name)
    pal = source.palette()
    for y in range(source.stats()["size"][1]):
        for x in range(source.stats()["size"][0]):
            idx = source.get(x, y)
            rgba = pal[idx]["rgba"]
            if rgba[3]:
                # Preserve value contrast while shifting the echoes toward icy blue.
                v = max(rgba[0], rgba[1], rgba[2])
                col = (min(205, 55 + v // 2), min(220, 65 + v // 2), min(245, 90 + v // 2), alpha)
                g.set(x, y, col)
    return g

far_knife = ghost_from(knife, 48, "far_afterimage")
mid_knife = ghost_from(knife, 82, "near_afterimage")

far = new_canvas(W, H, background=None, name="far echo")
mid = new_canvas(W, H, background=None, name="near echo")
far.blit(far_knife, 2, 17)
mid.blit(mid_knife, 20, 11)

# A broad, tapered crescent tracks the blade's thrust, with a bright white core.
slash = new_canvas(W, H, background=None, name="white slash")
slash.path("M 50 57 C 98 30 168 34 219 66 C 178 48 124 47 76 64 Z", "#dceeff36")
slash.path("M 68 59 C 116 40 176 44 219 68 C 177 52 125 53 81 68 Z", "#ffffff9a")
slash.path("M 67 96 C 118 113 181 105 220 78 C 178 99 125 101 81 89 Z", "#dceeff45")
slash.path("M 87 92 C 137 104 184 96 219 75 C 177 92 137 95 96 86 Z", "#ffffff90")
# Pixel-crisp speed streaks and spark fragments.
slash.line(9, 75, 57, 72, "#ffffff55")
slash.line(19, 84, 67, 80, "#dceeff70")
slash.line(33, 94, 78, 88, "#ffffff80")
slash.line(128, 42, 161, 46, "#ffffffb8")
slash.line(155, 106, 179, 91, "#ffffffa8")
slash.line(181, 54, 188, 58, "#ffffffff")
slash.set(189, 62, "#ffffffff")
slash.set(187, 68, "#ffffffff")

current = new_canvas(W, H, background=None, name="current knife")
current.blit(knife, 38, 6)

result = flatten([far, mid, slash, current], name="knife thrust right")
finish(result)
view(result, scale=3, margin=0)
