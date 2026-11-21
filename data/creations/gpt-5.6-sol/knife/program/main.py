from pixelbench_api import *

W, H = 224, 128
result_base = new_canvas(W, H, background=None, name="action_base")
trails = new_canvas(W, H, background=None, name="afterimages")
slash = new_canvas(W, H, background=None, name="slash_effect")
main_layer = new_canvas(W, H, background=None, name="knife")

# Rotate the original diagonal sprite into a clean rightward thrust pose.
main_sprite = input_canvas.select(0, 0, 93, 128).rotate(122, algorithm="rotsprite").preview("main_sprite")
trail_sprite_1 = input_canvas.select(0, 0, 93, 128).rotate(119, algorithm="rotsprite").preview("trail_sprite_1")
trail_sprite_2 = input_canvas.select(0, 0, 93, 128).rotate(115, algorithm="rotsprite").preview("trail_sprite_2")

palette = input_canvas.palette()
def alpha_of(c, x, y):
    return palette[c.get(x, y)]["rgba"][3]

def silhouette(src, colour, name):
    out = new_canvas(src.stats()["size"][0], src.stats()["size"][1], background=None, name=name)
    sw, sh = src.stats()["size"]
    for y in range(sh):
        for x in range(sw):
            if alpha_of(src, x, y) > 0:
                out.set(x, y, colour)
    return out

# Ghosts sit behind and slightly lower, describing acceleration toward the right.
ghost_far = silhouette(trail_sprite_2, "#7385d13a", "far_ghost")
ghost_near = silhouette(trail_sprite_1, "#a7b8ff66", "near_ghost")
trails.blit(ghost_far, 5, -8)
trails.blit(ghost_near, 26, -11)

# Broken motion accents keep the effect crisp and directional.
trails.path("M18 84 C49 92 76 92 106 84", "#9db4ff3d", fill=False)
trails.path("M32 92 C61 99 90 97 119 87", "#7188e02b", fill=False)
trails.line(7, 74, 48, 79, "#d3ddff47")
trails.line(18, 99, 67, 96, "#9fb3ff33")
trails.line(45, 105, 91, 98, "#879ee82e")

# Tapered slash hugs the downward-facing edge and converges at the tip.
slash.path("M39 89 C87 103 139 99 182 84 C198 78 211 70 223 62 L223 68 C211 77 198 85 183 91 C137 108 84 108 36 94 Z", "#b8c9ff42")
slash.path("M46 91 C94 102 142 97 184 81 C200 75 213 68 223 61 L221 66 C210 74 198 80 183 86 C141 102 93 106 44 95 Z", "#ffffffd6")
slash.path("M66 94 C107 101 148 94 184 80 C201 74 212 67 222 61 L220 64 C208 72 197 77 183 83 C146 97 107 104 66 97 Z", "#ffffffff")
slash.line(190, 77, 221, 60, "#ffffffff")
slash.set(220, 59, "#ffffffff")
slash.set(216, 62, "#ffffffff")

# Place the final knife so its edge rides immediately above the slash.
main_layer.blit(main_sprite, 63, -13)
result = flatten([result_base, trails, slash, main_layer], name="knife_thrust_right")
print(result.stats_text())
view(result, scale=3, margin=0)
finish(result)
