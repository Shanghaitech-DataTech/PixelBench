# Rightward knife thrust with layered motion echoes and a white slash trail.
W, H = 240, 112
result = new_canvas(W, H, background=None, name="output")

# Cool translucent afterimage ramps, split between metal and handle.
far_blade = result.color("#8199df2e", name="far_blade")
far_dark = result.color("#46578426", name="far_dark")
far_rim = result.color("#bfd0ff3b", name="far_rim")
near_blade = result.color("#9fb3ed48", name="near_blade")
near_dark = result.color("#53668f3c", name="near_dark")
near_rim = result.color("#d9e4ff5b", name="near_rim")
slash_soft = result.color("#cfe3ff68", name="slash_soft")
slash_white = result.color("#ffffffff", name="slash_white")
slash_hot = result.color("#f5fbffff", name="slash_hot")

# Preserve the source's blade/handle shading groups in each translucent echo.
def afterimage(angle, blade, dark, rim):
    src = input_canvas.select(0, 0, 93, 128).rotate(angle, algorithm="rotsprite").preview()
    sw, sh = src.stats()["size"]
    ghost = new_canvas(sw, sh, background=None)
    for y in range(sh):
        for x in range(sw):
            p = src.get(x, y)
            if p == 0:
                continue
            if p == 1:                 # dark source outline
                ghost.set(x, y, rim)
            elif 2 <= p <= 4:          # blade planes
                ghost.set(x, y, blade)
            else:                       # guard, grip and pommel
                ghost.set(x, y, dark)
    return ghost

far = afterimage(108, far_blade, far_dark, far_rim)
near = afterimage(117, near_blade, near_dark, near_rim)

# Ghosts mark two prior frames of the clockwise swing into the thrust.
result.blit(far, 17, -21)
result.blit(near, 39, -16)

# Tapered crescent below the cutting edge; a soft wake surrounds a white core.
result.path("M 57 96 C 112 101 185 87 235 57 C 193 91 118 106 57 99 Z", slash_soft, fill=True)
result.path("M 68 95 C 125 98 194 82 236 56 C 198 86 129 101 68 97 Z", slash_white, fill=True)
result.path("M 132 91 C 175 84 211 69 237 52 C 215 72 180 87 139 93 Z", slash_hot, fill=True)

# Detached speed cuts prevent the lower wake from reading as a single block.
result.poly([(92, 101), (126, 98), (108, 103)], slash_soft)
result.poly([(176, 84), (210, 70), (190, 83)], slash_white)
result.line(112, 104, 154, 99, slash_soft)

# Final full-colour pose: handle left, point right, cutting edge downward.
final_pose = input_canvas.select(0, 0, 93, 128).rotate(125, algorithm="rotsprite").preview()
result.blit(final_pose, 63, -9)

# White contact glints along the moving lower edge and at the point.
result.line(158, 78, 180, 79, slash_white)
result.line(181, 78, 199, 75, slash_hot)
result.set(222, 68, slash_white)
result.set(223, 68, slash_white)

print(result.stats_text())
view(result, scale=3, margin=0)
finish(result)
