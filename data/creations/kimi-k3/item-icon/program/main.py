import math

# API objects are preloaded; fall back to explicit import for helper runs.
try:
    new_canvas
except NameError:
    from pixelbench_api import *

# ---------------------------------------------------------------------------
# Ancient golden compass, top-down, 32x32 inventory icon.
#   - thick dark outline around a shaded brass ring
#   - parchment dial with degree ticks
#   - red / steel needle pointing north
#   - glowing blue crystal in the centre
# ---------------------------------------------------------------------------

C = new_canvas(32, 32, name="compass")

OUTLINE     = '#241505'
GOLD_BRIGHT = '#f7dd7e'
GOLD_LIGHT  = '#e8bd55'
GOLD_MID    = '#c69433'
GOLD_DARK   = '#94671d'
GOLD_DEEP   = '#6b4a12'
RING_SHADOW = '#54380d'

DIAL_LIGHT = '#e9d6a8'
DIAL_MID   = '#d2b87e'
DIAL_SHADE = '#ab8c52'
DIAL_EDGE  = '#82663a'
DIAL_RING  = '#c2a66c'
TICK       = '#3a2a10'

RED_LIGHT = '#e0593f'
RED_DARK  = '#8e241c'
STEEL_LIGHT = '#f0f3f5'
STEEL_DARK  = '#9aa1ab'

CR_GLINT   = '#eafcff'
CR_LIGHT   = '#6cc4f2'
CR_MID     = '#2e8fd8'
CR_DEEP    = '#155a96'
CR_DEEPEST = '#0c3a68'

cx = cy = 15.5
SQ2 = math.sqrt(2.0)

# rivet positions on the brass ring (diagonals), angle measured from north
studs = []
for k in range(4):
    a = math.radians(45 + 90 * k)
    studs.append((cx + 11.15 * math.sin(a), cy - 11.15 * math.cos(a)))

for y in range(32):
    for x in range(32):
        dx = x - cx
        dy = y - cy
        d = math.hypot(dx, dy)
        if d > 14.5:
            continue

        # --- thick dark outer outline ---
        if d > 12.6:
            C.set(x, y, OUTLINE)
            continue

        # --- brass ring ---
        if d > 9.7:
            L = (-dx - dy) / (d * SQ2)          # 1 = toward top-left light
            sd = min(math.hypot(x - sx, y - sy) for sx, sy in studs)
            if sd <= 1.55:                       # rivets
                if sd <= 1.0:
                    C.set(x, y, GOLD_BRIGHT if L > 0.1 else GOLD_DARK)
                else:
                    C.set(x, y, OUTLINE)
                continue
            if d > 12.0 and L > 0.5:
                col = GOLD_BRIGHT                # specular rim, top-left
            elif d < 10.5:
                col = RING_SHADOW if L < 0.4 else GOLD_DARK
            elif L > 0.45:
                col = GOLD_LIGHT
            elif L > -0.2:
                col = GOLD_MID
            elif L > -0.65:
                col = GOLD_DARK
            else:
                col = GOLD_DEEP
            C.set(x, y, col)
            continue

        # --- dark bezel line between ring and dial ---
        if d > 8.9:
            C.set(x, y, OUTLINE)
            continue

        # --- parchment dial ---
        L = (-dx - dy) / (d * SQ2) if d > 0 else 0.0
        if d > 7.9:
            col = DIAL_EDGE
        elif L > 0.35:
            col = DIAL_LIGHT
        elif L > -0.3:
            col = DIAL_MID
        else:
            col = DIAL_SHADE
        if 5.4 < d < 5.9:
            col = DIAL_RING                      # engraved degree circle

        # degree ticks (north is covered by the needle)
        ang = math.degrees(math.atan2(dx, -dy)) % 360.0
        m = ang % 90.0
        card = min(m, 90.0 - m)
        dd = (ang - 45.0) % 90.0
        diag = min(dd, 90.0 - dd)
        north = ang < 9.0 or ang > 351.0
        if card < 6.5 and 6.4 < d < 8.8 and not north:
            col = TICK
        elif diag < 5.5 and 7.5 < d < 8.8:
            col = TICK

        C.set(x, y, col)

# ---------------------------------------------------------------------------
# needle: dark outline diamonds, then lit faces (light from the top-left)
# ---------------------------------------------------------------------------
# north half - red
C.poly([(15.5, 7.9), (18.4, 15.5), (12.6, 15.5)], OUTLINE)
C.poly([(15.5, 8.9), (15.5, 15.5), (13.3, 15.5)], RED_LIGHT)
C.poly([(15.5, 8.9), (17.7, 15.5), (15.5, 15.5)], RED_DARK)
# south half - steel
C.poly([(15.5, 23.1), (18.4, 15.5), (12.6, 15.5)], OUTLINE)
C.poly([(15.5, 22.1), (15.5, 15.5), (13.3, 15.5)], STEEL_LIGHT)
C.poly([(15.5, 22.1), (17.7, 15.5), (15.5, 15.5)], STEEL_DARK)

# ---------------------------------------------------------------------------
# blue crystal centre
# ---------------------------------------------------------------------------
for y in range(11, 21):
    for x in range(11, 21):
        dx = x - cx
        dy = y - cy
        d = math.hypot(dx, dy)
        if d > 3.4:
            continue
        if d > 2.7:
            C.set(x, y, OUTLINE)
            continue
        L = (-dx - dy) / (d * SQ2) if d > 0 else 0.0
        dg = math.hypot(x - 14.2, y - 14.2)      # glint, top-left
        if dg <= 0.95:
            col = CR_GLINT
        elif L > 0.35:
            col = CR_LIGHT
        elif L > -0.2:
            col = CR_MID
        elif L > -0.6:
            col = CR_DEEP
        else:
            col = CR_DEEPEST
        C.set(x, y, col)

print(C.stats_text())
view(C)
finish(C)
