from pixelbench_api import *

# Slash effect, 48x48, single canvas combining the two-frame read:
# a small inner white arc (frame 1) and a larger outer arc with a
# trailing streak (frame 2), on a transparent background.

c = new_canvas(48, 48, background=None, name="slash_effect")

white = c.color('#FFFFFF', name='slash_core')
pale  = c.color('#CFE3FF', name='slash_glow')
dim   = c.color('#8FB4E8', name='trail')
faint = c.color('#5A7FB8', name='trail_far')

# --- Frame 2: large arc slash with trailing streak ---
# main bright edge, two nearly-parallel strokes for a 2px-thick blade
c.path("M 6 42 Q 12 13 40 7", white, fill=False)
c.path("M 8 43 Q 14 15 41 8", white, fill=False)

# trailing streak: fading echoes behind the blade
c.path("M 11 44 Q 17 20 43 10", pale, fill=False)
c.path("M 15 45 Q 21 25 45 13", dim, fill=False)
c.path("M 20 46 Q 26 31 46 17", faint, fill=False)

# --- Frame 1: small white arc slash (inner crescent) ---
c.path("M 17 33 Q 21 21 33 17", white, fill=False)
c.path("M 19 34 Q 23 23 34 19", pale, fill=False)

# a few spark pixels along the cut
for (x, y) in [(10, 36), (14, 27), (22, 16), (31, 12), (38, 9),
               (24, 30), (29, 25), (36, 20)]:
    c.set(x, y, pale)

print(c.stats_text())

result = c
finish(result)

