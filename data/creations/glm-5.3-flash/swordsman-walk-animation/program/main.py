from pixelbench_api import *

# ============================================================
# 16-bit RPG swordsman - 2-frame walk cycle on a 64x32 sheet
#   Frame A (left)  : contact  - near leg planted forward,
#                                far leg pushing off toe-down,
#                                body low, cape hanging
#   Frame B (right) : passing  - near leg under the body,
#                                far leg swinging through, knee up,
#                                body 1px higher, cape kicked back
#   The near leg is always bright, the far leg shaded, so the limbs
#   visibly scissor between the two frames.
# ============================================================

main = new_canvas(64, 32, background=None, name="swordsman_walk")

# ---------------- palette ----------------
OUT     = main.color("#221a2e", "outline")
SKIN    = main.color("#f4c896", "skin")
SKIN_S  = main.color("#cf9663", "skin_shade")
HAIR    = main.color("#d8441f", "hair")
HAIR_L  = main.color("#f47b2a", "hair_light")
HAIR_D  = main.color("#8e2410", "hair_dark")
CAPE    = main.color("#2c3f86", "cape")
CAPE_L  = main.color("#4d68bd", "cape_light")
CAPE_D  = main.color("#1a2550", "cape_dark")
TUN     = main.color("#9aa1ad", "tunic")
TUN_L   = main.color("#c3c9d2", "tunic_light")
TUN_D   = main.color("#666e7c", "tunic_shade")
BELT    = main.color("#6d4526", "belt")
PANTS   = main.color("#46536b", "pants")
PANTS_D = main.color("#303a4e", "pants_shade")
BOOT    = main.color("#5e3a20", "boot")
BOOT_D  = main.color("#38220f", "boot_dark")
BLADE   = main.color("#c6d7e6", "blade")
BLADE_L = main.color("#f4faff", "blade_light")
BLADE_D = main.color("#7e94ab", "blade_shade")
GOLD    = main.color("#e0ac3c", "gold")
GOLD_D  = main.color("#9c6d1c", "gold_dark")
SHADOW  = main.color((26, 20, 48, 120), "shadow")


def build_frame(pose):
    """Body pixels on a 36px-wide canvas, drawn at x+1 so the long
    sword and its outline fit; the caller shifts -2, putting the
    figure 1px left of the design grid inside the 32px cell."""
    bob = 0 if pose == "A" else 1
    f = new_canvas(36, 32, background=None)

    def S(x, y, col):
        f.set(x + 1, y, col)

    def R(x, y, w, h, col):
        f.rect(x + 1, y, w, h, col)

    def U(y):                      # upper body rides the bob
        return y - bob

    # ---------------- cape (behind everything) ----------------
    if pose == "A":
        R(8, 12, 5, 3, CAPE)       # x8-12  y12-14
        R(7, 15, 6, 3, CAPE)       # x7-12  y15-17
        R(6, 18, 6, 3, CAPE)       # x6-11  y18-20
        R(7, 21, 4, 1, CAPE)       # hem    y21
        S(10, 12, CAPE_L); S(11, 12, CAPE_L); S(11, 13, CAPE_L)
        for y in range(13, 18):    # core shadow against the torso
            S(12, y, CAPE_D)
        S(10, 15, CAPE_D); S(10, 16, CAPE_D); S(9, 17, CAPE_D)
        S(6, 19, CAPE_D); S(6, 20, CAPE_D); S(7, 20, CAPE_D)
        S(9, 19, CAPE_D); S(10, 20, CAPE_D); S(11, 20, CAPE_D)
        S(8, 21, CAPE_D); S(9, 21, CAPE_D)
    else:
        R(7, 11, 5, 3, CAPE)       # kicked back, riding the bob
        R(6, 14, 6, 3, CAPE)
        R(5, 17, 6, 3, CAPE)
        R(6, 20, 4, 1, CAPE)
        S(5, 20, CAPE_D)
        S(9, 11, CAPE_L); S(10, 11, CAPE_L); S(10, 12, CAPE_L)
        for y in range(12, 17):
            S(11, y, CAPE_D)
        S(9, 14, CAPE_D); S(9, 15, CAPE_D); S(8, 16, CAPE_D)
        S(5, 18, CAPE_D); S(5, 19, CAPE_D)
        S(8, 18, CAPE_D); S(9, 19, CAPE_D); S(10, 19, CAPE_D)
        S(7, 20, CAPE_D); S(8, 20, CAPE_D)
        # far arm swings back into view behind the torso
        for y in range(13, 17):
            S(11, y, SKIN_S); S(12, y, SKIN_S)
        S(11, 16, SKIN_S); S(12, 16, SKIN_S)

    # ---------------- head ----------------
    for x in range(13, 17):
        S(x, U(3), HAIR)                        # top spikes
    R(12, U(4), 7, 1, HAIR)
    R(11, U(5), 9, 1, HAIR)
    R(10, U(6), 10, 1, HAIR)
    for x in range(10, 17):                     # bangs
        S(x, U(7), HAIR)
    S(17, U(7), SKIN); S(18, U(7), SKIN)        # forehead
    S(10, U(8), HAIR_D); S(11, U(8), HAIR_D); S(12, U(8), HAIR)
    for x in range(13, 16):
        S(x, U(8), SKIN)
    S(16, U(8), OUT); S(17, U(8), OUT)          # eye
    S(18, U(8), SKIN); S(19, U(8), SKIN)        # nose
    S(10, U(9), HAIR_D); S(11, U(9), HAIR_D)
    for x in range(12, 16):
        S(x, U(9), SKIN)
    S(16, U(9), SKIN_S); S(17, U(9), SKIN_S)    # mouth / cheek
    S(18, U(9), SKIN)
    S(10, U(10), HAIR_D); S(11, U(10), HAIR_D)
    for x in range(12, 15):
        S(x, U(10), SKIN)
    S(15, U(10), SKIN_S); S(16, U(10), SKIN_S)  # chin
    S(14, U(11), SKIN); S(15, U(11), SKIN)      # neck
    S(13, U(4), HAIR_L); S(14, U(4), HAIR_L); S(15, U(4), HAIR_L)
    S(13, U(5), HAIR_L); S(14, U(5), HAIR_L)
    S(9, U(8), HAIR_D); S(9, U(9), HAIR_D)      # back tuft

    # ---------------- torso ----------------
    R(13, U(12), 6, 6, TUN)
    S(16, U(13), TUN_L); S(17, U(14), TUN_L)
    S(13, U(13), TUN_D); S(13, U(14), TUN_D); S(13, U(15), TUN_D)
    S(14, U(17), TUN_D); S(15, U(17), TUN_D); S(16, U(17), TUN_D)
    R(12, U(18), 7, 1, BELT)
    S(16, U(18), GOLD)

    # ---------------- sword arm (blade held level, ready) ----------------
    S(17, U(12), TUN_D)                          # shoulder
    S(18, U(13), TUN_D); S(18, U(14), TUN_D)     # upper arm
    S(19, U(15), SKIN); S(19, U(16), SKIN)       # forearm
    S(19, U(17), SKIN); S(20, U(17), SKIN)       # fist
    S(19, U(18), SKIN); S(20, U(18), GOLD_D)     # heel of hand + grip
    for y in range(16, 20):                      # crossguard bar
        S(21, U(y), GOLD if y < 19 else GOLD_D)
    for x in range(22, 32):                      # long blade, level
        S(x, U(17), BLADE_L)                     # lit upper edge
        if x < 29:                               # taper to a point
            S(x, U(18), BLADE_D if x > 26 else BLADE)

    # ---------------- pelvis ----------------
    R(13, U(19), 6, 2, PANTS)
    S(13, U(19) + 1, PANTS_D); S(14, U(19) + 1, PANTS_D)

    # ---------------- legs ----------------
    if pose == "A":
        # near leg: planted flat, striding forward
        for (x, y) in [(17, 21), (18, 21), (18, 22), (19, 22), (19, 23),
                       (20, 23), (20, 24), (20, 25)]:
            S(x, y, PANTS)
        S(18, 22, PANTS_D); S(19, 23, PANTS_D); S(20, 24, PANTS_D)
        R(19, 26, 4, 2, BOOT)
        S(23, 27, BOOT)                          # toe
        R(19, 28, 5, 1, BOOT_D)                  # sole on the ground
        # far leg: trailing, pushing off toe-down
        for (x, y) in [(14, 21), (13, 21), (13, 22), (12, 22), (11, 23),
                       (11, 24), (10, 24), (10, 25)]:
            S(x, y, PANTS_D)
        R(9, 25, 3, 2, BOOT)
        S(8, 26, BOOT); S(8, 27, BOOT); S(7, 27, BOOT)
        S(7, 28, BOOT_D); S(8, 28, BOOT_D)       # toe contact
        S(15, 21, PANTS_D); S(16, 21, PANTS_D)   # groin
    else:
        # near leg: support, straight under the body
        for y in range(20, 26):
            S(14, y, PANTS); S(15, y, PANTS)
        for y in (21, 23, 25):
            S(14, y, PANTS_D)
        R(13, 26, 4, 2, BOOT)
        R(13, 28, 5, 1, BOOT_D)
        # far leg: swinging through, knee forward, foot lifted
        for (x, y) in [(18, 20), (19, 20), (19, 21), (20, 21), (20, 22),
                       (21, 22), (21, 23)]:
            S(x, y, PANTS_D)
        R(21, 24, 4, 2, BOOT)
        R(21, 25, 4, 1, BOOT_D)                  # sole 3px above ground
        S(25, 25, BOOT)                          # toe
        S(15, 20, PANTS_D); S(16, 20, PANTS_D)   # groin
    return f


def make_frame(pose):
    """1px centred outline + contact shadow, cropped to the 32px cell."""
    body = build_frame(pose)

    rim = new_canvas(36, 32, background=None)
    w, h, data = body.to_rgba()
    for y in range(h):
        for x in range(w):
            if data[(y * w + x) * 4 + 3] == 0:
                continue
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 36 and 0 <= ny < 32:
                        rim.set(nx, ny, OUT)

    f = flatten([rim, body], name="frame_" + pose)
    f.shift(-2, 0)                               # design - 1 = final

    out = new_canvas(32, 32, background=None)
    for x in range(9, 23):                       # contact shadow
        out.set(x, 29, SHADOW)
    for x in range(7, 25):
        out.set(x, 30, SHADOW)
    out.blit(f, 0, 0)
    return out


def dump(c, x0, x1, y0, y1, label, indices=False):
    if indices:
        print(f"--- {label} (indices) ---")
        print(c.matrix_text(region=(x0, y0, x1, y1), indices=True))
        return
    print(f"--- {label} x[{x0}..{x1}] y[{y0}..{y1}] ---")
    print("    " + "".join(str((x0 + i) // 10 % 10) for i in range(x1 - x0 + 1)))
    print("    " + "".join(str((x0 + i) % 10) for i in range(x1 - x0 + 1)))
    w, h, data = c.to_rgba()
    for y in range(y0, y1 + 1):
        row = ""
        for x in range(x0, x1 + 1):
            row += "." if data[(y * w + x) * 4 + 3] == 0 else "#"
        print(f"{y:3d} " + row)


fa = make_frame("A")
fb = make_frame("B")
main.blit(fa, 0, 0)
main.blit(fb, 32, 0)

dump(main, 0, 31, 14, 21, "frame A sword", indices=True)
dump(main, 0, 31, 17, 31, "frame A lower")
dump(main, 32, 63, 17, 31, "frame B lower")
print(main.matrix_text(region=(32, 0, 63, 31)))

print(main.stats_text())
print(main.matrix_text(region=(0, 0, 31, 31)))
save("swordsman_walk", main)
finish(main)
