import sys
from pixelbench_api import new_canvas, view, finish
from render_utils import COLOR_MAP, render_view

def flip_row(row_str):
    tokens = [row_str[i:i+2] for i in range(0, len(row_str), 2)]
    return "".join(reversed(tokens))

def flip_view(grid):
    return [flip_row(row) for row in grid]

def validate_grid(name, grid):
    assert len(grid) == 32, f"{name} must have 32 rows, got {len(grid)}"
    for i, r in enumerate(grid):
        assert len(r) == 64, f"{name} row {i} has len {len(r)}, expected 64! Row: {r}"
        tokens = [r[j:j+2] for j in range(0, 64, 2)]
        for t in tokens:
            assert t in COLOR_MAP, f"Unknown token '{t}' in {name} row {i}"

# =============================================================================
# FRONT VIEW (Top-Left: 0..31, 0..31)
# =============================================================================
FRONT = [
# 0
"................................................................",
# 1: bow loops top
"....................OOOOOO............OOOOOO....................",
# 2: bow loops
"..................OOr0r0r1r1OO......OOr0r0r1r1OO................",
# 3: bow loops lower & knot top
"..................OOr1r1r2r2OOOOOOOOOOr2r2r1r1OO................",
# 4: bow knot & hair top
"....................OOOOOOr0r1r1r1r1r0OOOOOOOO..................",
# 5: hair top & bow base
"..................OOh0h0OOr1r2r2r2r2r1OOh0h0OO..................",
# 6: hair volume top
"................OOh0h0h0h1h1h1h1h1h1h1h1h0h0h0OO................",
# 7: bangs top
"..............OOh0h1h1h1h1h1h1h1h1h1h1h1h1h1h1h0OO..............",
# 8: bangs fringe with cute parted tips
"..............OOh1h0h1h0s1s1h0h1h1h0s1s1h0h1h0h1OO..............",
# 9: cute eyes upper - highlight at top-left of each eye
"................OOh1h1s1s1w0e1s1s1w0e1s1s1h1h1OO................",
# 10: lower eyes (blue iris), blush on cheeks, nose bridge between eyes
"................OOh2h2bls1e0e1s1s1e0e1s1blh2h2OO................",
# 11: cute smile below eyes, chin
"................OOh2s2s1s1s1s1mumus1s1s1s1s2h2OO................",
# 12: jawline & neck
"..................OOh3s2s1s1s1s1s1s1s1s1s2h3OO..................",
# 13: neck & shoulder line
"....................OOh3OOs1s1s1s1s1s1OOh3OO....................",
# 14: shoulders & cheer top straps
"..............OOOO..OOs1s1b1b0b0b0b0b1s1s1OO..OOOO..............",
# 15: upper chest chevron & bare arms
"............OOg0g0OOs1s1b0b1w0w0w0w0b1b0s1s1OOg0g0OO............",
# 16: white chevron V & arms/pompoms
"..........OOg0g1g1g0OOs1b1w0w0w0w0w0w0b1s1OOg0g1g1g0OO..........",
# 17: gold stripe & pompom center
"..........OOg1g2g1g1OOb2g1g1g0g0g0g0g1g1b2OOg1g1g2g1OO..........",
# 18: blue band & pompom center
"..........OOg1g2g2g1OOb0b1b1b1b1b1b1b1b1b0OOg1g2g2g1OO..........",
# 19: bare midriff & pompom bottom
"............OOg1g2OO....OOs1s1s0s0s1s1OO....OOg2g1OO............",
# 20: skirt waistband & hands
"..............OOOO......OOb1b1b1b1b1b1OO......OOOO..............",
# 21: pleated skirt upper
"......................OOb1w0b1b1b1b1w0b1OO......................",
# 22: pleated skirt flare
"....................OOb1b1w0b1b1b1b1w0b1b1OO....................",
# 23: skirt hem gold trim
"..................OOg1g0g1w0g1g1g1g1w0g1g0g1OO..................",
# 24: skirt shadow & upper thighs
"..................OOOOOOOOOOs2s1s1s2OOOOOOOOOO..................",
# 25: thighs
"..........................OOs1s1OOs1s1OO........................",
# 26: knees
"..........................OOs1s0OOs0s1OO........................",
# 27: calves
"..........................OOs2s1OOs1s2OO........................",
# 28: sock cuff (blue stripe)
"..........................OOb1b1OOb1b1OO........................",
# 29: socks (white)
"..........................OOw0w1OOw1w0OO........................",
# 30: sneakers white
"........................OOw0w0w1OOw1w0w0OO......................",
# 31: shoe soles
"........................OOt0t0t0OOt0t0t0OO......................",
]
validate_grid("FRONT", FRONT)

# =============================================================================
# BACK VIEW (Top-Right: 32..63, 0..31)
# =============================================================================
BACK = [
# 0
"................................................................",
# 1: bow loops top
"....................OOOOOO............OOOOOO....................",
# 2: bow loops
"..................OOr0r0r1r1OO......OOr0r0r1r1OO................",
# 3: bow loops lower & knot top
"..................OOr1r1r2r2OOOOOOOOOOr2r2r1r1OO................",
# 4: bow knot & ponytail tie
"....................OOOOOOr0r1r1r1r1r0OOOOOOOO..................",
# 5: hair top & ponytail start
"..................OOh0h0OOr1r2r2r2r2r1OOh0h0OO..................",
# 6: hair volume top & ponytail
"................OOh0h0h0h1h1h1h1h1h1h1h1h0h0h0OO................",
# 7: back of head & ponytail cascade
"..............OOh0h1h1h1h1h2h0h0h0h0h2h1h1h1h1h0OO..............",
# 8: back of head & ponytail
"..............OOh1h1h2h2h1h2h1h0h0h1h2h1h2h2h1h1OO..............",
# 9: back of head & ponytail
"................OOh2h2h3h2h3h1h1h1h1h3h2h3h2h2OO................",
# 10: back of head & ponytail
"................OOh3h3h3h2h3h1h2h2h1h3h2h3h3h3OO................",
# 11: back of hair base & ponytail
"................OOh3h3h3h2h3h2h2h2h2h3h2h3h3h3OO................",
# 12: neck & ponytail
"..................OOOO..OOs2h3h2h2h3s2OO..OOOO..................",
# 13: bare shoulders & racerback straps
"..............OOOO..OOs1s1b1h3h2h2h3b1s1s1OO..OOOO..............",
# 14: bare upper back & straps
"............OOg0g0OOs1s1b0b1h2h1h1h2b1b0s1s1OOg0g0OO............",
# 15: cheer top back chevron & ponytail tip
"..........OOg0g1g1g0OOs1b1w0h3h2h2h3w0b1s1OOg0g1g1g0OO..........",
# 16: cheer top back white band & pompom body
"..........OOg1g2g1g1OOb1w0w0w0w0w0w0w0w0b1OOg1g1g2g1OO..........",
# 17: cheer top back gold band & pompom center
"..........OOg1g2g2g1OOb2g1g1g0g0g0g0g1g1b2OOg1g1g2g1OO..........",
# 18: blue band & pompom center
"..........OOg1g2g2g1OOb0b1b1b1b1b1b1b1b1b0OOg1g2g2g1OO..........",
# 19: bare lower back & pompom bottom
"............OOg1g2OO....OOs2s1s0s0s1s2OO....OOg2g1OO............",
# 20: skirt waistband & hands
"..............OOOO......OOb1b1b1b1b1b1OO......OOOO..............",
# 21: pleated skirt upper
"......................OOb1w0b1b1b1b1w0b1OO......................",
# 22: pleated skirt flare
"....................OOb1b1w0b1b1b1b1w0b1b1OO....................",
# 23: skirt hem gold trim
"..................OOg1g0g1w0g1g1g1g1w0g1g0g1OO..................",
# 24: skirt shadow & upper thighs back
"..................OOOOOOOOOOs2s1s1s2OOOOOOOOOO..................",
# 25: thighs back
"..........................OOs1s2OOs2s1OO........................",
# 26: back of knees
"..........................OOs2s2OOs2s2OO........................",
# 27: calves back
"..........................OOs1s2OOs2s1OO........................",
# 28: sock cuff back
"..........................OOb1b1OOb1b1OO........................",
# 29: socks white back
"..........................OOw1w1OOw1w1OO........................",
# 30: sneakers heels
"........................OOw1w1w2OOw2w1w1OO......................",
# 31: shoe soles
"........................OOt0t0t0OOt0t0t0OO......................",
]
validate_grid("BACK", BACK)

# =============================================================================
# LEFT SIDE VIEW (Bottom-Left: 0..31, 32..63)
# =============================================================================
LEFT = [
# 0
"................................................................",
# 1: bow top
"..............................OOOOOO............................",
# 2: bow loops
"............................OOr0r0r1r1OO........................",
# 3: bow knot & tie
"..........................OOr1r1r2r1r2OO........................",
# 4: bow base & ponytail arch top
"..........................OOOOOOr0r1r2OO........................",
# 5: hair crown & ponytail cascade top
"......................OOOO..OOh0h0h1h1OO........................",
# 6: forehead bangs & ponytail cascade
"....................OOh0h0OO..OOh1h0h1h2OO......................",
# 7: bangs & side hair & ponytail cascade
"..................OOh0h1h1h0OOh1h1h0h1h2OO......................",
# 8: cute forehead profile & ponytail
"..................OOh1h0s1s1h1h2h1h0h1h3OO......................",
# 9: nose pointing left & eye & ponytail
"................OOs1w0e1s1s1h2h2h1h1h2OO........................",
# 10: lips/blush & ear & ponytail
"................OOs1mus1bls1s2h3h2h1h3OO........................",
# 11: chin & jaw & ponytail
"..................OOs1s2s1s2OOh3h2h3OO..........................",
# 12: neck & ponytail
"....................OOs1s1s2OOh3h2h3OO..........................",
# 13: shoulder & strap & ponytail tip
"..................OOb1b0b1s1s2OOh3OO............................",
# 14: chest chevron & bare arm
"................OOb0b1w0s1s1s1s2OO..............................",
# 15: chest front & pompom top
"..............OOb1w0w0b1s1s1s1s2OOg0g0OO........................",
# 16: gold stripe & pompom
"............OOg0g1b2g1g1s1s1s2OOg0g1g1g0OO......................",
# 17: blue band & pompom center
"..........OOg0g1g1b1b1b1s2s2OOg1g1g2g1g1OO......................",
# 18: bare midriff & pompom bottom
"..........OOg1g2g1OOs1s1s2OOOOg1g2g2g1g0OO......................",
# 19: skirt waistband & pompom bottom
"............OOg2OOOOb1b1b1b0OO..OOOOOOOO........................",
# 20: pleated skirt flare profile
"..................OOb1w0b1b1w0b1OO..............................",
# 21: pleated skirt flare profile
"................OOb1b1w0b1b1b1w0b1OO............................",
# 22: skirt hem gold trim
"..............OOg1g0g1w0g1g1g1w0g1g0g1OO........................",
# 23: skirt shadow & leg
"..............OOOOOOOOOOs2s1s2OOOOOOOOOO........................",
# 24: thigh profile
"......................OOs1s1s2OO................................",
# 25: knee profile (slight forward curve)
"....................OOs1s1s1s2OO................................",
# 26: calf profile (slight backward curve)
"....................OOs1s1s2s2OO................................",
# 27: sock cuff (blue stripe)
"......................OOb1b1b2OO................................",
# 28: sock (white)
"......................OOw0w1w2OO................................",
# 29: sneaker pointing left (toe at x=8)
"..................OOw0w0w0w1w2OO................................",
# 30: sneaker sole
"..................OOt0t0t0t0t0OO................................",
# 31
"................................................................",
]
validate_grid("LEFT", LEFT)

# RIGHT SIDE VIEW: mirror of LEFT SIDE VIEW
RIGHT = flip_view(LEFT)
validate_grid("RIGHT", RIGHT)

c = new_canvas(64, 64)
render_view(c, 0, 0, FRONT)
render_view(c, 32, 0, BACK)
render_view(c, 0, 32, LEFT)
render_view(c, 32, 32, RIGHT)

finish(c)
view(c)
