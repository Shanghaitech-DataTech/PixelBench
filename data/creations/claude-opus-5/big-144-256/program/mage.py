"""Cloaked mage seen from behind, stepping through the archway."""

from pixelbench_api import new_canvas


def draw_mage(out, cx=55, top=182, floor=211):
    CL_S = out.color("#121a26", "cloak_shadow")
    CL_D = out.color("#1b2635", "cloak_dark")
    CL_M = out.color("#26364a", "cloak_mid")
    CL_H = out.color("#31455c", "cloak_hi")
    CL_R = out.color("#3e6d78", "cloak_rim")
    BOOT = out.color("#1a1a1e", "boot")
    BOOT_R = out.color("#39565c", "boot_rim")
    SOLE = out.color("#2b3a3a", "boot_sole")
    STF = out.color("#3a2e24", "staff")
    STF_L = out.color("#6b5340", "staff_lit")
    SH1 = out.color("#16242a", "mage_shadow")
    SH2 = out.color("#1d2f32", "mage_shadow2")

    # row -> half width left/right of the centre column
    prof = {
        0: (1, 1), 1: (2, 2),            # crown of the hood
        2: (2, 3), 3: (3, 3), 4: (3, 3), 5: (3, 3), 6: (3, 3),
        7: (3, 4),                       # hood meets the shoulders
        8: (4, 5), 9: (5, 5),
        10: (5, 5), 11: (5, 6), 12: (5, 6), 13: (5, 6),
        14: (5, 6), 15: (5, 6), 16: (6, 6), 17: (6, 6),
        18: (6, 6), 19: (6, 6), 20: (6, 6), 21: (6, 6),
        22: (6, 6), 23: (6, 6), 24: (6, 6), 25: (6, 6),
    }
    for dy, (lw, rw) in prof.items():
        y = top + dy
        xl, xr = cx - lw, cx + rw
        out.line(xl, y, xr, y, CL_D)
        out.set(xl, y, CL_S)
        out.set(xl + 1, y, CL_S if dy > 16 else CL_D)
        out.set(xr, y, CL_R)
        out.set(xr - 1, y, CL_H)

    hem = top + 26          # 208
    # ragged hem, split where the stride opens the cloak
    out.line(cx - 6, hem, cx - 3, hem, CL_D)
    out.set(cx - 6, hem, CL_S)
    out.line(cx - 5, hem + 1, cx - 4, hem + 1, CL_S)
    out.line(cx + 3, hem, cx + 6, hem, CL_D)
    out.set(cx + 6, hem, CL_R)
    out.line(cx + 4, hem + 1, cx + 5, hem + 1, CL_D)
    out.set(cx + 5, hem + 1, CL_R)

    # hood shading: lit from the staff on his left, dark on the far side
    out.set(cx, top, CL_M)
    out.set(cx + 1, top, CL_H)
    out.set(cx - 1, top + 1, CL_S)
    out.set(cx + 2, top + 1, CL_H)
    for dy in range(2, 7):
        out.set(cx - 2, top + dy, CL_M)
        out.set(cx + 2, top + dy, CL_H)
    out.line(cx - 4, top + 7, cx + 4, top + 7, CL_S)
    out.set(cx + 4, top + 7, CL_R)

    # centre seam of the cloak back plus two fold lines
    for dy in range(9, 26):
        out.set(cx, top + dy, CL_M)
    for dy in range(14, 25):
        out.set(cx - 3, top + dy, CL_M)
        out.set(cx + 3, top + dy, CL_H)

    # orb rim light catching the shoulder and the hood edge on the staff side
    out.set(cx + 3, top + 2, CL_R)
    out.set(cx + 3, top + 4, CL_R)
    out.set(cx + 4, top + 8, CL_R)
    out.set(cx + 5, top + 10, CL_R)

    # boots: trailing foot planted flat, leading foot lifted mid-stride
    out.rect(cx - 4, hem, 3, 4, BOOT)
    out.set(cx - 2, hem + 1, BOOT_R)
    out.line(cx - 4, hem + 3, cx - 2, hem + 3, SOLE)
    out.rect(cx + 1, hem - 1, 3, 3, BOOT)
    out.set(cx + 3, hem - 1, BOOT_R)
    out.line(cx + 1, hem + 1, cx + 3, hem + 1, SOLE)

    # contact shadow on the threshold
    out.line(cx - 6, floor + 1, cx + 5, floor + 1, SH1)
    out.line(cx - 4, floor + 2, cx + 3, floor + 2, SH2)

    # staff held at his left side, leaning back over the shoulder
    out.line(cx + 7, hem + 1, cx + 5, top + 1, STF)
    out.set(cx + 6, top + 14, STF_L)
    out.set(cx + 6, top + 9, STF_L)
    out.set(cx + 5, top + 4, STF_L)
    # sleeve and hand gripping the shaft
    out.rect(cx + 5, top + 11, 2, 3, CL_M)
    out.set(cx + 6, top + 11, CL_R)
    out.set(cx + 6, top + 13, CL_H)

    return cx + 5, top - 2      # orb position


def draw_glow(out, ox, oy, floor=211):
    st = out.stats()["size"]
    glow = new_canvas(st[0], st[1], name="glow")
    glow.circle(ox, oy, 15, "#86e4e40e")
    glow.circle(ox, oy, 11, "#92eded1a")
    glow.circle(ox, oy, 8, "#a6f2f22b")
    glow.circle(ox, oy, 5, "#c6f8f844")
    glow.circle(ox, oy, 3, "#ddfbfb66")
    glow.ellipse(ox - 3, floor, 9, 3, "#8fe8e818")
    glow.ellipse(ox - 3, floor + 1, 6, 2, "#9deeee24")
    out.blit(glow, 0, 0)

    out.circle(ox, oy, 2, out.color("#63c4c4", "orb_out"))
    out.circle(ox, oy, 1, out.color("#aef2f0", "orb_mid"))
    out.set(ox, oy, out.color("#f2ffff", "orb_core"))
    out.set(ox - 1, oy - 1, out.color("#f2ffff", "orb_core"))
