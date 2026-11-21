from pixelbench_api import new_canvas, finish, view

# ---- palette ----
O       = "#241f2b"   # dark outline
SKIN    = "#f3c9a2"
SKIN_SH = "#d9a077"
HAIR    = "#5a3a26"
HAIR_D  = "#3a2415"
HAIR_L  = "#7d5436"
EYE_W   = "#ffffff"
IRIS    = "#4a7ab5"
MOUTH   = "#8c3b3b"
SHIRT   = "#3f6bb0"
SHIRT_D = "#2b4a80"
COLLAR  = "#e9e9ef"
BLUSH   = "#eb9a86"


def base_portrait():
    """Shared head + hair + outfit for all four emotions (32x32 tile)."""
    c = new_canvas(32, 32)
    # neck
    c.rect(13, 21, 6, 5, SKIN)
    c.rect(13, 24, 6, 2, SKIN_SH)
    # shirt / shoulders
    c.rect(5, 25, 22, 6, SHIRT)
    c.rect(3, 27, 26, 4, SHIRT)
    c.rect(3, 30, 26, 1, SHIRT_D)
    # collar
    c.rect(12, 25, 8, 2, COLLAR)
    # head
    c.rect(8, 6, 16, 17, SKIN)      # x8..23, y6..22
    c.rect(9, 23, 14, 1, SKIN)      # rounded chin
    c.rect(21, 9, 2, 13, SKIN_SH)   # cheek shading
    # hair
    c.rect(7, 2, 18, 4, HAIR)       # top, y2..5
    c.rect(7, 6, 18, 1, HAIR_D)     # dark fringe line
    c.rect(6, 4, 2, 12, HAIR)       # left lock
    c.rect(24, 4, 2, 12, HAIR)      # right lock
    for x in range(8, 24):          # zig-zag fringe tips
        c.set(x, 7, HAIR if (x % 4) < 2 else SKIN)
    c.rect(9, 3, 4, 1, HAIR_L)      # highlights
    c.rect(16, 3, 3, 1, HAIR_L)
    c.set(6, 6, HAIR_L)
    return c


def calm():
    c = base_portrait()
    for ex in (10, 18):
        c.rect(ex, 12, 4, 3, EYE_W)
        c.rect(ex + 1, 12, 2, 2, IRIS)
        c.set(ex + 1, 12, O)
        c.rect(ex - 1, 11, 6, 1, O)          # upper lid
    c.rect(10, 9, 4, 1, HAIR_D)              # flat brows
    c.rect(18, 9, 4, 1, HAIR_D)
    c.rect(15, 16, 1, 2, SKIN_SH)            # nose
    c.rect(13, 19, 5, 1, MOUTH)              # straight mouth
    c.outline(O)
    return c


def smiling():
    c = base_portrait()
    for ex in (10, 18):
        c.rect(ex, 12, 4, 3, EYE_W)
        c.rect(ex + 1, 12, 2, 2, IRIS)
        c.set(ex + 1, 12, O)
        c.rect(ex - 1, 11, 6, 1, O)
    c.rect(10, 8, 4, 1, HAIR_D)              # raised brows
    c.rect(18, 8, 4, 1, HAIR_D)
    c.rect(15, 16, 1, 2, SKIN_SH)
    # big open grin
    c.rect(13, 18, 6, 2, MOUTH)
    c.rect(14, 18, 4, 1, EYE_W)              # teeth
    c.set(12, 17, MOUTH)
    c.set(19, 17, MOUTH)
    c.rect(9, 16, 2, 1, BLUSH)               # blush
    c.rect(21, 16, 2, 1, BLUSH)
    c.outline(O)
    return c


def angry():
    c = base_portrait()
    c.line(9, 8, 13, 10, HAIR_D)             # brows slanting down-in
    c.line(18, 10, 22, 8, HAIR_D)
    for ex in (10, 18):
        c.rect(ex, 13, 4, 2, EYE_W)          # narrowed eyes
        c.rect(ex + 1, 13, 2, 2, IRIS)
        c.rect(ex - 1, 12, 6, 1, O)          # lowered lid
    c.rect(15, 16, 1, 2, SKIN_SH)
    # deep frown
    c.rect(13, 19, 6, 1, MOUTH)
    c.set(12, 20, MOUTH)
    c.set(19, 20, MOUTH)
    c.outline(O)
    return c


def surprised():
    c = base_portrait()
    for ex in (10, 18):
        c.rect(ex, 11, 4, 4, EYE_W)          # wide eyes
        c.rect(ex + 1, 12, 2, 2, IRIS)
        c.set(ex + 1, 12, O)
        c.rect(ex - 1, 10, 6, 1, O)          # lifted lid
    c.rect(10, 8, 4, 1, HAIR_D)              # brows shot up
    c.rect(18, 8, 4, 1, HAIR_D)
    c.rect(15, 15, 1, 2, SKIN_SH)
    c.circle(15, 20, 1, MOUTH)               # little "o" mouth
    c.outline(O)
    return c


tiles = [(calm(), 0, 0), (smiling(), 32, 0), (angry(), 0, 32), (surprised(), 32, 32)]

result = new_canvas(64, 64, name="result")
for t, dx, dy in tiles:
    result.blit(t, dx, dy)

print(result.stats_text())
print(result.matrix_text(region=(0, 0, 31, 31)))
finish(result)
