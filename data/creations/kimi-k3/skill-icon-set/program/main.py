# Skill icon set: 2x2 grid on 64x64, transparent background.
# Fireball (TL), Ice Shield (TR), Healing (BL), Lightning (BR).
# Shared style: 1px dark outline, light from upper-left, shade lower-right.

c = new_canvas(64, 64, background=None, name="skill_icons")

# ---------- palette ----------
OUT   = '#1b1226'   # shared dark outline
WHITE = '#ffffff'

FIRE_HI   = '#ffe9a3'
FIRE_MID  = '#ff9a3d'
FIRE_DEEP = '#e0481f'

ICE_HI   = '#eafcff'
ICE_MID  = '#7fd0f0'
ICE_DEEP = '#3b8bd4'
ICE_DARK = '#274e8a'

HEAL_HI   = '#d9ffd9'
HEAL_MID  = '#53d97e'
HEAL_DEEP = '#22a052'

LIT_HI   = '#fff6ad'
LIT_MID  = '#ffd23e'
LIT_DEEP = '#f0961f'


def spark(x, y, col):
    """Small 5-pixel diamond sparkle (drawn after outlines)."""
    c.set(x, y - 1, col)
    c.set(x - 1, y, col)
    c.set(x, y, col)
    c.set(x + 1, y, col)
    c.set(x, y + 1, col)


# ---------- 1. FIREBALL (top-left, quadrant 0,0) ----------
ox, oy = 0, 0
c.circle(ox + 14, oy + 18, 9, FIRE_MID)                     # fireball body
c.poly([(ox + 11, oy + 12), (ox + 15, oy + 3), (ox + 18, oy + 8),
        (ox + 22, oy + 2), (ox + 25, oy + 8), (ox + 27, oy + 12),
        (ox + 22, oy + 15)], FIRE_MID)                       # flame tongues up-right
c.outline(OUT)
c.circle(ox + 17, oy + 21, 3, FIRE_DEEP)                     # lower-right shade
c.circle(ox + 13, oy + 16, 4, FIRE_HI)                       # hot core upper-left
c.set(ox + 12, oy + 14, WHITE)                               # hot spot
c.set(ox + 13, oy + 14, WHITE)

# ---------- 2. ICE SHIELD (top-right, quadrant 32,0) ----------
ox, oy = 32, 0
c.poly([(ox + 8, oy + 5), (ox + 24, oy + 5), (ox + 24, oy + 17),
        (ox + 16, oy + 27), (ox + 8, oy + 17)], ICE_MID)     # shield silhouette
c.outline(OUT)
c.poly([(ox + 10, oy + 7), (ox + 22, oy + 7), (ox + 22, oy + 16),
        (ox + 16, oy + 24), (ox + 10, oy + 16)], ICE_DEEP)   # inner panel
c.poly([(ox + 10, oy + 7), (ox + 16, oy + 7), (ox + 16, oy + 24),
        (ox + 10, oy + 16)], ICE_MID)                        # left light facet
c.line(ox + 10, oy + 7, ox + 22, oy + 7, ICE_HI)             # frosted top edge
c.line(ox + 22, oy + 8, ox + 22, oy + 16, ICE_DARK)          # right depth edge
c.line(ox + 22, oy + 16, ox + 17, oy + 23, ICE_DARK)

# ---------- 3. HEALING (bottom-left, quadrant 0,32) ----------
ox, oy = 0, 32
cross = [(13, 6), (19, 6), (19, 12), (25, 12), (25, 19), (19, 19),
         (19, 26), (13, 26), (13, 19), (7, 19), (7, 12), (13, 12)]
c.poly([(ox + x, oy + y) for x, y in cross], HEAL_MID)       # healing cross
c.outline(OUT)
c.rect(ox + 14, oy + 7, 5, 5, HEAL_HI)                       # top arm light
c.rect(ox + 8, oy + 13, 5, 5, HEAL_HI)                       # left arm light
c.rect(ox + 14, oy + 20, 5, 6, HEAL_DEEP)                    # bottom arm shade
c.rect(ox + 20, oy + 13, 5, 6, HEAL_DEEP)                    # right arm shade

# ---------- 4. LIGHTNING (bottom-right, quadrant 32,32) ----------
ox, oy = 32, 32
bolt = [(19, 3), (9, 17), (15, 17), (11, 28), (23, 13), (16, 13), (24, 3)]
c.poly([(ox + x, oy + y) for x, y in bolt], LIT_MID)         # bolt silhouette
c.outline(OUT)
c.poly([(ox + 16, oy + 17), (ox + 11, oy + 28), (ox + 19, oy + 17)],
       LIT_DEEP)                                             # lower shade
inner = [(18, 5), (13, 14), (17, 14), (14, 23), (20, 13), (16, 13), (21, 5)]
c.poly([(ox + x, oy + y) for x, y in inner], LIT_HI)         # bright core

# ---------- sparkles (after all outlines so they stay clean) ----------
spark(5, 5, WHITE)            # fireball
spark(32 + 27, 5, ICE_HI)     # ice shield
spark(5, 32 + 27, WHITE)      # healing
spark(32 + 27, 32 + 27, LIT_HI)
spark(32 + 5, 32 + 6, WHITE)  # lightning

print(c.stats_text())
view(c)
finish(c)
