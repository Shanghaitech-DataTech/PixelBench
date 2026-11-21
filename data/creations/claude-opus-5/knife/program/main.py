src = input_canvas
SW, SH = 93, 128

CW, CH = 240, 96

# --- 1. pose the knife: thrust to the right, cutting edge down -------------
rot = src.select(0, 0, SW, SH).flip("v").rotate(-124.0, "rotsprite").preview("rot")
knife = rot.select(3, 61, 154, 32).preview("knife")   # 154x32, tip at local (153, 15)
KW, KH = 154, 32
KX, KY = 58, 32                                        # tip lands at (211, 47)
TIPX, TIPY = KX + 153, KY + 15

kpal = {p['index']: p['rgba'] for p in knife.palette()}


def ghost(alpha, lift=0, cool=0):
    """Semi-transparent copy of the posed knife; lift brightens, cool tints blue."""
    g = new_canvas(KW, KH)
    for y in range(KH):
        for x in range(KW):
            r, gr, b, a = kpal[knife.get(x, y)]
            if a == 0:
                continue
            r = min(255, r + lift)
            gr = min(255, gr + lift)
            b = min(255, b + lift + cool)
            g.set(x, y, (r, gr, b, alpha))
    return g


def layer(name):
    return new_canvas(CW, CH, name=name)


# --- 2. dark backdrop so the white slash and the transparency both read ----
BG = (20, 22, 36, 255)
BG2 = (29, 32, 52, 255)
bg = new_canvas(CW, CH, background=BG, name="bg")
bg.dither(0, 26, CW, 42, [BG, BG2], pattern="bayer4")
bg.rect(0, 40, CW, 12, BG2)

# --- 3. speed streaks along the thrust line -------------------------------
streaks = layer("streaks")
W1 = (255, 255, 255, 130)
W2 = (255, 255, 255, 80)
W3 = (255, 255, 255, 40)
streaks.line(0, 34, 140, 34, W3)
streaks.line(6, 39, 176, 39, W2)
streaks.line(0, 44, 198, 44, W1)
streaks.line(4, 48, 202, 48, W2)
streaks.line(12, 53, 170, 53, W2)
streaks.line(0, 58, 150, 58, W3)
streaks.line(22, 63, 128, 63, W3)

# --- 4. afterimages: three fading copies trailing to the left --------------
trail = layer("trail")
for dx, alpha, lift, cool in ((-54, 38, 26, 22), (-36, 62, 16, 16), (-18, 102, 6, 10)):
    g = ghost(alpha, lift, cool)
    g.outline((190, 205, 255, max(30, alpha - 10)))
    trail.blit(g, KX + dx, KY)

blade = layer("blade")
blade.blit(knife, KX, KY)

# --- 5. white slash, hugging the tip and flaring ahead of it ---------------
slash = layer("slash")
WHITE = (255, 255, 255, 255)
# bright lens of light at the point of the thrust
slash.path("M %d 16 Q %d %d %d 78 Q %d %d %d 16 Z"
           % (TIPX - 5, TIPX + 25, TIPY, TIPX - 5, TIPX + 8, TIPY, TIPX - 5),
           WHITE, fill=True)
# outrider arcs, fading forward
slash.path("M %d 8 Q %d %d %d 85" % (TIPX - 12, TIPX + 20, TIPY, TIPX - 12),
           (255, 255, 255, 170), fill=False)
slash.path("M %d 2 Q %d %d %d 91" % (TIPX - 22, TIPX + 13, TIPY, TIPX - 22),
           (255, 255, 255, 85), fill=False)
# flare running along the cutting edge into the tip
slash.line(112, 62, TIPX - 14, 51, (255, 255, 255, 110))
slash.line(146, 63, TIPX - 8, 52, (255, 255, 255, 200))
slash.line(170, 60, TIPX - 4, 50, WHITE)
# faint spine highlight on the back of the blade
slash.line(96, 29, 180, 31, (255, 255, 255, 60))

result = flatten([bg, streaks, trail, blade, slash], name="output")
print(result.stats_text())
view(result)
save("knife_thrust", result)
finish(result)
