from pixelbench_api import *

c = new_canvas(64, 64, name="emotions")

OUTLINE = c.color("#1a1422", "outline")
SKIN = c.color("#f3ca9e", "skin")
HAIR = c.color("#6e4a30", "hair")
OUTFIT = c.color("#4678c8", "outfit")
WHITE = c.color("#ffffff", "white")
PINK = c.color("#f49696", "blush")


def ellipse_outline(c, cx, cy, rx, ry, colour):
    d = (f"M {cx - rx} {cy} "
         f"A {rx} {ry} 0 1 1 {cx + rx} {cy} "
         f"A {rx} {ry} 0 1 1 {cx - rx} {cy} Z")
    c.path(d, colour, fill=False)


def draw_head(cx, cy, mood):
    # neck and shoulders (behind the head)
    c.rect(cx - 3, cy + 10, 6, 6, SKIN, fill=True)
    c.poly([(cx - 12, cy + 17), (cx + 12, cy + 17),
            (cx + 9, cy + 13), (cx - 9, cy + 13)], OUTFIT, fill=True)
    c.poly([(cx - 12, cy + 17), (cx + 12, cy + 17),
            (cx + 9, cy + 13), (cx - 9, cy + 13)], OUTLINE, fill=False)

    # hair silhouette
    c.ellipse(cx, cy - 1, 12, 11, HAIR, fill=True)
    ellipse_outline(c, cx, cy - 1, 12, 11, OUTLINE)

    # face
    c.ellipse(cx, cy + 2, 9, 8, SKIN, fill=True)
    ellipse_outline(c, cx, cy + 2, 9, 8, OUTLINE)

    # fringe / bangs
    fringe = [
        (cx - 9, cy - 6), (cx + 9, cy - 6), (cx + 9, cy - 4),
        (cx + 6, cy - 2), (cx + 3, cy - 4), (cx, cy - 2),
        (cx - 3, cy - 4), (cx - 6, cy - 2), (cx - 9, cy - 4),
    ]
    c.poly(fringe, HAIR, fill=True)
    c.path(f"M {cx-9} {cy-4} L {cx-6} {cy-2} L {cx-3} {cy-4} "
           f"L {cx} {cy-2} L {cx+3} {cy-4} L {cx+6} {cy-2} "
           f"L {cx+9} {cy-4}", OUTLINE, fill=False)

    # tiny nose
    c.set(cx, cy + 5, OUTLINE)

    if mood == "calm":
        c.line(cx - 6, cy + 3, cx - 2, cy + 3, OUTLINE)
        c.line(cx + 2, cy + 3, cx + 6, cy + 3, OUTLINE)
        c.line(cx - 2, cy + 8, cx + 2, cy + 8, OUTLINE)

    elif mood == "smile":
        c.path(f"M {cx-7} {cy+3} Q {cx-4} {cy} {cx-1} {cy+3}",
               OUTLINE, fill=False)
        c.path(f"M {cx+1} {cy+3} Q {cx+4} {cy} {cx+7} {cy+3}",
               OUTLINE, fill=False)
        c.rect(cx - 7, cy + 5, 3, 2, PINK, fill=True)
        c.rect(cx + 4, cy + 5, 3, 2, PINK, fill=True)
        c.ellipse(cx, cy + 8, 3, 1, OUTLINE, fill=True)
        c.line(cx - 3, cy + 8, cx + 3, cy + 8, WHITE)

    elif mood == "angry":
        c.line(cx - 7, cy - 2, cx - 2, cy, OUTLINE)
        c.line(cx + 2, cy, cx + 7, cy - 2, OUTLINE)
        c.ellipse(cx - 4, cy + 3, 2, 2, WHITE, fill=True)
        ellipse_outline(c, cx - 4, cy + 3, 2, 2, OUTLINE)
        c.set(cx - 3, cy + 3, OUTLINE)
        c.ellipse(cx + 4, cy + 3, 2, 2, WHITE, fill=True)
        ellipse_outline(c, cx + 4, cy + 3, 2, 2, OUTLINE)
        c.set(cx + 3, cy + 3, OUTLINE)
        c.path(f"M {cx-3} {cy+8} Q {cx} {cy+10} {cx+3} {cy+8}",
               OUTLINE, fill=False)

    elif mood == "surprise":
        c.line(cx - 6, cy - 2, cx - 2, cy - 2, OUTLINE)
        c.line(cx + 2, cy - 2, cx + 6, cy - 2, OUTLINE)
        c.circle(cx - 4, cy + 3, 3, WHITE, fill=True)
        c.circle(cx - 4, cy + 3, 3, OUTLINE, fill=False)
        c.circle(cx - 4, cy + 3, 1, OUTLINE, fill=True)
        c.circle(cx + 4, cy + 3, 3, WHITE, fill=True)
        c.circle(cx + 4, cy + 3, 3, OUTLINE, fill=False)
        c.circle(cx + 4, cy + 3, 1, OUTLINE, fill=True)
        c.circle(cx, cy + 8, 2, OUTLINE, fill=True)


positions = [
    (16, 14, "calm"),
    (48, 14, "smile"),
    (16, 46, "angry"),
    (48, 46, "surprise"),
]
for cx, cy, mood in positions:
    draw_head(cx, cy, mood)

print(c.stats_text())
finish(c)
