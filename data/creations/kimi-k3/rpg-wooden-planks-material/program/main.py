import math

W = H = 16
c = new_canvas(W, H, background="#a06632", name="wood_tile")

# ---- palette ----------------------------------------------------------
SEAM      = "#2e1c0c"   # dark groove between planks
KNOT_RING = "#54300f"
KNOT_CORE = "#38200a"

LIGHT = {"hi": "#b97f43", "base": "#a06632", "shadow": "#87522a",
         "grain": "#6b3f1a", "cap": "#c9975a"}
DARK  = {"hi": "#96602f", "base": "#7f4d24", "shadow": "#64401d",
         "grain": "#4f2f12", "cap": "#8a5a2c"}

planks = [LIGHT if p % 2 == 0 else DARK for p in range(4)]  # alternating boards

# ---- base columns + seam grooves --------------------------------------
# each plank: 3 wood columns (highlight / base / shadow) + 1 dark seam
for p, tone in enumerate(planks):
    for lx, col in enumerate([tone["hi"], tone["base"], tone["shadow"]]):
        for y in range(16):
            c.set(p * 4 + lx, y, col)
    for y in range(16):
        c.set(p * 4 + 3, y, SEAM)

# ---- wood-grain lines: sparse short strokes with a slight wobble ------
# (local_x, start_y, length, wobble_dx_at_end) per plank
grain_strokes = [
    [(0, 1, 3, 1), (2, 5, 3, -1), (1, 12, 3, 0)],
    [(2, 0, 3, 0), (0, 5, 4, 1), (1, 9, 2, 0), (2, 12, 3, -1)],
    [(0, 0, 2, 0), (2, 4, 3, 0), (0, 8, 3, 1), (2, 13, 2, 0)],
    [(2, 1, 3, -1), (0, 8, 3, 0), (2, 12, 3, 0)],
]
for p, tone in enumerate(planks):
    for x0, y0, ln, wob in grain_strokes[p]:
        for i in range(ln):
            x = x0 + (wob if i == ln - 1 else 0)
            x = max(0, min(2, x))
            c.set(p * 4 + x, (y0 + i) % 16, tone["grain"])

# ---- staggered horizontal board-end joints -----------------------------
joints = [4, 11, 7, 14]           # one end joint per plank, staggered
for p, tone in enumerate(planks):
    yj = joints[p]
    for lx in range(3):
        c.set(p * 4 + lx, yj - 1, tone["shadow"])  # worn bottom edge of board above
        c.set(p * 4 + lx, yj,     SEAM)            # the joint groove
        c.set(p * 4 + lx, yj + 1, tone["cap"])     # end grain of the new board

# ---- knots: concentric ring + dark core, staggered across planks -------
knots = [(0, 9), (2, 2), (3, 6)]
for p, y in knots:
    cx = p * 4 + 1
    for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
        c.set(cx + dx, y + dy, KNOT_RING)
    c.set(cx, y, KNOT_CORE)
# faint oval halo around each knot (grain bending around it)
for p, y in knots:
    tone = planks[p]
    cx = p * 4 + 1
    for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
        c.set(cx + dx, y + dy, tone["grain"])

# ---- seamlessness preview: 3x3 tiling ----------------------------------
preview = new_canvas(48, 48, name="tile_check")
for ty in range(3):
    for tx in range(3):
        preview.blit(c, tx * 16, ty * 16)

view(c, scale=16)
view(preview, scale=8)
print(c.stats_text())

finish(c)
