from pixelbench_api import *

# 64x64 canvas, 2x2 grid of 32x32 portraits
w, h = 64, 64
c = new_canvas(w, h, name="emotion_set")

# Color definitions
SKIN = "#f2c48d"
SKIN_SHADOW = "#d9a56a"
HAIR = "#3d2b1f"
HAIR_DARK = "#2a1e15"
OUTLINE = "#1a1a1e"
SHIRT = "#4a86c8"
SHIRT_DARK = "#35689f"
BROW = "#2a1e15"
MOUTH = "#a04028"
MOUTH_DARK = "#6b2010"
BLUSH = "#e8907a"
SWEAT = "#7ac8e8"
WHITE = "#fafafa"


def draw_portrait(c, cx, cy, emotion):
    """Draw a 32x32 portrait at top-left (cx, cy)."""
    def P(x, y, col):
        c.set(cx + x, cy + y, col)

    # ===== HEAD outline =====
    c.ellipse(cx + 16, cy + 16, 11, 12, OUTLINE, fill=True)
    # Face skin
    c.ellipse(cx + 16, cy + 16, 10, 11, SKIN, fill=True)

    # ===== HAIR (mop-top covering upper head) =====
    # Hair arcs over the top of the head
    c.ellipse(cx + 16, cy + 9, 11, 6, HAIR, fill=True)
    # Dark top hair
    c.ellipse(cx + 16, cy + 6, 10, 4, HAIR_DARK, fill=True)

    # Side locks - a few pixels framing either side
    for sy in ((11, 12, 13, 14, 15)):
        P(5, sy, HAIR)
        P(26, sy, HAIR)
    P(6, 13, HAIR)
    P(6, 14, HAIR)
    P(25, 13, HAIR)
    P(25, 14, HAIR)
    P(7, 14, HAIR)
    P(24, 14, HAIR)
    # Small side at lower cheeks
    P(6, 16, HAIR)
    P(25, 16, HAIR)

    # ===== NECK =====
    P(14, 28, OUTLINE)
    P(15, 28, OUTLINE)
    P(16, 28, OUTLINE)
    P(17, 28, OUTLINE)
    P(14, 29, SKIN)
    P(15, 29, SKIN)
    P(16, 29, SKIN)
    P(17, 29, SKIN)
    P(14, 30, SKIN)
    P(15, 30, SKIN)
    P(16, 30, SKIN)
    P(17, 30, SKIN)

    # ===== EYES =====
    if emotion == "calm":
        # Small calm eyes
        P(11, 17, OUTLINE)
        P(12, 17, OUTLINE)
        P(11, 18, OUTLINE)
        P(12, 18, OUTLINE)
        P(19, 17, OUTLINE)
        P(20, 17, OUTLINE)
        P(19, 18, OUTLINE)
        P(20, 18, OUTLINE)
        # Relaxed flat brows
        for bx in [10, 11, 12, 13, 18, 19, 20, 21]:
            P(bx, 14, BROW)
        # Gentle smile
        P(13, 24, MOUTH)
        P(14, 24, MOUTH)
        P(15, 24, MOUTH)
        P(16, 24, MOUTH)
        P(17, 24, MOUTH)
        P(18, 24, MOUTH)
        P(19, 24, MOUTH)
        P(13, 23, MOUTH)
        P(19, 23, MOUTH)
        # Nose
        P(16, 21, SKIN_SHADOW)

    elif emotion == "smiling":
        # Happy closed eyes (curved up like ^)
        # Left eye - smile curve ((arc)
        P(10, 17, OUTLINE)
        P(11, 17, OUTLINE)
        P(12, 17, OUTLINE)
        P(13, 17, OUTLINE)
        P(14, 17, OUTLINE)
        P(10, 18, OUTLINE)
        P(14, 18, OUTLINE)
        # Right eye
        P(17, 17, OUTLINE)
        P(18, 17, OUTLINE)
        P(19, 17, OUTLINE)
        P(20, 17, OUTLINE)
        P(21, 17, OUTLINE)
        P(17, 18, OUTLINE)
        P(21, 18, OUTLINE)
        # Raised brows
        for bx in [10, 11, 12, 13, 18, 19, 20, 21]:
            P(bx, 13, BROW)
        # Big happy open smile
        P(11, 24, MOUTH)
        P(12, 24, MOUTH)
        P(13, 24, MOUTH)
        P(14, 24, MOUTH)
        P(15, 24, MOUTH)
        P(16, 24, MOUTH)
        P(17, 24, MOUTH)
        P(18, 24, MOUTH)
        P(19, 24, MOUTH)
        P(20, 24, MOUTH)
        P(12, 25, MOUTH_DARK)
        P(13, 25, MOUTH_DARK)
        P(14, 25, MOUTH_DARK)
        P(15, 25, MOUTH_DARK)
        P(16, 25, MOUTH_DARK)
        P(17, 25, MOUTH_DARK)
        P(18, 25, MOUTH_DARK)
        P(13, 26, MOUTH_DARK)
        P(14, 26, MOUTH_DARK)
        P(15, 26, MOUTH_DARK)
        P(16, 26, MOUTH_DARK)
        P(17, 26, MOUTH_DARK)
        # Blush
        for by in (23, 24):
            P(7, by, BLUSH)
            P(8, by, BLUSH)
            P(23, by, BLUSH)
            P(24, by, BLUSH)
        # Nose
        P(16, 21, SKIN_SHADOW)

    elif emotion == "angry":
        # Angry narrowed eyes (1px tall squares, squinted)
        P(11, 17, OUTLINE)
        P(12, 17, OUTLINE)
        P(19, 17, OUTLINE)
        P(20, 17, OUTLINE)
        P(11, 18, OUTLINE)
        P(12, 18, OUTLINE)
        P(19, 18, OUTLINE)
        P(20, 18, OUTLINE)
        # Angry slanted brows (thicker, more aggressive)
        # Left: long slanting brow going down toward center
        P(8, 12, BROW)
        P(9, 12, BROW)
        P(10, 13, BROW)
        P(11, 13, BROW)
        P(12, 14, BROW)
        P(13, 14, BROW)
        # Second row for thickness
        P(8, 13, BROW)
        P(9, 14, BROW)
        # Right: mirrored
        P(18, 14, BROW)
        P(19, 14, BROW)
        P(20, 13, BROW)
        P(21, 13, BROW)
        P(22, 12, BROW)
        P(23, 12, BROW)
        P(22, 13, BROW)
        P(23, 14, BROW)
        # Furrow lines between brows
        P(15, 14, BROW)
        # Deep frown
        P(12, 25, MOUTH)
        P(13, 25, MOUTH)
        P(14, 25, MOUTH)
        P(15, 25, MOUTH)
        P(16, 25, MOUTH)
        P(17, 25, MOUTH)
        P(18, 25, MOUTH)
        P(19, 25, MOUTH)
        # Frown extras - deeper corners
        P(12, 26, MOUTH_DARK)
        P(13, 26, MOUTH_DARK)
        P(18, 26, MOUTH_DARK)
        P(19, 26, MOUTH_DARK)
        # Nose scrunched in anger
        P(14, 21, SKIN_SHADOW)
        P(15, 21, SKIN_SHADOW)
        P(16, 21, SKIN_SHADOW)
        P(17, 21, SKIN_SHADOW)
        P(18, 21, SKIN_SHADOW)

    elif emotion == "surprised":
        # Huge surprised eyes with clear eye whites
        # Left eye - 4x4 opening with visible white and pupil
        c.rect(cx + 9, cy + 15, 5, 5, OUTLINE, fill=True)   # outer dark outline
        c.rect(cx + 10, cy + 16, 3, 3, WHITE, fill=True)     # eye whites
        c.rect(cx + 11, cy + 17, 1, 1, OUTLINE, fill=True)  # pupil

        # Right eye
        c.rect(cx + 18, cy + 15, 5, 5, OUTLINE, fill=True)
        c.rect(cx + 19, cy + 16, 3, 3, WHITE, fill=True)
        c.rect(cx + 20, cy + 17, 1, 1, OUTLINE, fill=True)

        # High shocked brows
        for bx in [9, 10, 11, 12, 13, 18, 19, 20, 21, 22]:
            P(bx, 11, BROW)
        # Small O mouth
        P(14, 23, MOUTH)
        P(15, 23, MOUTH)
        P(16, 23, MOUTH)
        P(17, 23, MOUTH)
        P(13, 24, MOUTH)
        P(18, 24, MOUTH)
        P(13, 25, MOUTH)
        P(18, 25, MOUTH)
        P(14, 26, MOUTH)
        P(15, 26, MOUTH)
        P(16, 26, MOUTH)
        P(17, 26, MOUTH)
        P(14, 24, MOUTH_DARK)
        P(15, 24, MOUTH_DARK)
        P(16, 24, MOUTH_DARK)
        P(17, 24, MOUTH_DARK)
        P(14, 25, MOUTH_DARK)
        P(15, 25, MOUTH_DARK)
        P(16, 25, MOUTH_DARK)
        P(17, 25, MOUTH_DARK)
        # Sweat drop
        P(27, 7, SWEAT)
        P(27, 8, SWEAT)
        P(28, 8, SWEAT)
        P(26, 8, SWEAT)
        # Nose
        P(16, 21, SKIN_SHADOW)

    # ===== SHOULDERS / SHIRT =====
    c.rect(cx + 2, cy + 30, 28, 2, OUTLINE, fill=True)
    c.rect(cx + 3, cy + 30, 26, 1, SHIRT, fill=True)
    c.rect(cx + 3, cy + 31, 26, 1, SHIRT_DARK, fill=True)


# Draw four portraits in 2x2 grid
draw_portrait(c, 0, 0, "calm")
draw_portrait(c, 32, 0, "smiling")
draw_portrait(c, 0, 32, "angry")
draw_portrait(c, 32, 32, "surprised")

print(c.stats_text())

finish(c)
