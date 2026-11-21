"""16x16 RPG wooden-planks material tile, seamless in both axes.

Layout: 4 vertical boards, 3 px wide, separated by 1 px dark grooves at
x = 3, 7, 11, 15 (the x = 15 groove is the left/right wrap seam).
Board joints (end grain) are staggered and their caps alternate:
  board A (x 0-2)   light cap y=10, joint y=11
  board B (x 4-6)   dark  cap y=2,  joint y=3
  board C (x 8-10)  light cap y=13, joint y=14
  board D (x 12-14) dark  cap y=4,  joint y=5
Knots (ring / core / ring) sit at A y=5, B y=8, D y=11.
Grain streaks run across the y = 15 / y = 0 wrap on every board.
"""

PAL = {
    "h": "#F7E3B0",  # highlight speck
    ".": "#DCA96B",  # light board body
    "e": "#EFD096",  # light end-grain cap
    "g": "#A06C36",  # grain line
    ",": "#B5834A",  # darker board body
    "d": "#8F6334",  # shade / knot ring
    "E": "#6B4526",  # dark end-grain cap
    "k": "#5A3A1E",  # knot core
    "G": "#46301E",  # seam groove and board joints
}

ROWS = [
    ".g.G,g,G..gG,,gG",
    ".g.G,,dG..gG,,dG",
    "..dGEEEG..dGd,,G",
    ".g.GGGGG.g.G,g,G",
    ".d.GdddG..gGEEEG",
    "dkdG,g,Gg..GGGGG",
    ".d.G,,gG...GdddG",
    "hg.G,d,G..dG,,gG",
    "..gGdkdG.g.G,g,G",
    ".g.G,d,Gg..G,d,G",
    "eeeG,g,G...G,dgG",
    "GGGG,,dG..gGdkdG",
    ".dgG,g,G.g.G,d,G",
    ".g.G,,gGeeeG,,gG",
    "..gG,g,GGGGGd,gG",
    "..gG,g,G..gG,,gG",
]

# --- structural self-checks before drawing ---
assert len(ROWS) == 16
for y, row in enumerate(ROWS):
    assert len(row) == 16, f"row {y} has {len(row)} chars"
    for x in (3, 7, 11, 15):
        assert row[x] == "G", f"groove broken at ({x},{y})"
wrap = [(x, ROWS[15][x], ROWS[0][x]) for x in range(16) if ROWS[15][x] != ROWS[0][x]]
print("y-wrap column changes (grain wander only):", wrap)

c = new_canvas(16, 16, background=None, name="wood_planks")
for y, row in enumerate(ROWS):
    for x, ch in enumerate(row):
        c.set(x, y, PAL[ch])

print(c.stats_text())
print(c.matrix_text())

# --- seam check: 2x2 tiling, inspect where four tiles meet ---
chk = new_canvas(32, 32, background=None, name="tiling_check")
for ox in (0, 16):
    for oy in (0, 16):
        chk.blit(c, ox, oy)
print("centre of 2x2 tiling (x 12-21, y 12-21):")
print(chk.matrix_text(region=(12, 12, 21, 21)))

save("wooden_planks_16", c, indexed=True)
finish(c)
