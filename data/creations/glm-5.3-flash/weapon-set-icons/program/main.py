# =====================================================================
#  WEAPON ICON SET -- 64x64 pixel art, 2x2 grid
#      top-left: SWORD        top-right: BOW
#      bottom-left: SHIELD    bottom-right: BATTLE AXE
#  One consistent style: chunky pixel masses, dark outlines,
#  steel / gold / wood / leather palette, transparent background.
#  Each icon is authored on a 24x24 cell, placed with a 4px margin
#  inside its 32x32 quadrant (cells at 4,4 / 36,4 / 4,36 / 36,36).
#  Light source: top-left. 13 colours total.
# =====================================================================

PALETTE = {
    "#": "#1a1c2c",  # dark outline
    "W": "#f4f4f8",  # bright edge highlight
    "S": "#b8c4d4",  # steel light
    "s": "#8b9bb4",  # steel mid
    "d": "#566c8c",  # steel shadow
    "G": "#eebf4d",  # gold
    "g": "#b97a2a",  # gold shadow
    "L": "#a9743f",  # wood light
    "l": "#7a4a28",  # wood shadow
    "B": "#4a2f1e",  # leather grip
    "R": "#cf3f4f",  # gem red
    "r": "#8e2a3c",  # gem shadow
    "t": "#d8d3c8",  # bowstring (deliberate 1px line, exempt from outline rule)
}

# ------------------------------- SWORD -------------------------------
SWORD = [
    "........................",
    "........................",
    "...........##...........",
    "..........#WS#..........",
    ".........#WSSs#.........",
    ".........#WSSs#.........",
    ".........#WSSs#.........",
    ".........#WSSs#.........",
    ".........#WSSs#.........",
    ".........#WSSs#.........",
    ".........#WSSs#.........",
    ".........#WSSs#.........",
    ".........#WSSs#.........",
    "......############......",
    "......#GGGGGGGGGG#......",
    "......#GGGGGGGggg#......",
    "......############......",
    "..........#lB#..........",
    "..........#lB#..........",
    "..........#lB#..........",
    ".........#GGGG#.........",
    ".........#gggg#.........",
    ".........######.........",
    "........................",
]

# -------------------------------- BOW --------------------------------
# C-shaped limb on the left, string anchored at both tips, arrow
# nocked at the string pointing right: leather nock, red fletching,
# wood shaft, steel broadhead.
BOW = [
    "........................",
    ".......####.............",
    "......#Ll#t.............",
    ".....#Ll#.t.............",
    ".....#Ll#.t.............",
    "....#Ll#..t.............",
    "....#Ll#..t.............",
    "...#Ll#...t.............",
    "...#Ll#...t.............",
    "...#Ll#...t........##...",
    "...#BB#...t########SS#..",
    "...#BB#...tBRRLLLLSSSS#.",
    "...#BB#...tBrrllllssss#.",
    "...#BB#...t########ss#..",
    "...#Ll#...t........##...",
    "...#Ll#...t.............",
    "...#Ll#...t.............",
    "....#Ll#..t.............",
    "....#Ll#..t.............",
    ".....#Ll#.t.............",
    ".....#Ll#.t.............",
    "......#Ll#t.............",
    ".......####.............",
    "........................",
]

# ------------------------------- SHIELD ------------------------------
# Heater shield: gold trim, steel face lit from the left, red gem.
SHIELD = [
    "........................",
    "........................",
    "........................",
    "......############......",
    ".....#GGGGGGGGGggg#.....",
    "....#GWWSSSSSSSsssG#....",
    "....#GWSSSSSSSSsssG#....",
    "....#GSSSSSSSSSsssG#....",
    "....#GSSSSSSSSSsssG#....",
    "....#GSSSSS##SSsssG#....",
    "....#GSSSS#RR#SsssG#....",
    ".....#GSS#RRrr#ssg#.....",
    ".....#GSS#Rrrr#ssg#.....",
    "......#GSS#rr#ssg#......",
    "......#GSSS##Sssg#......",
    ".......#GSSssssg#.......",
    ".......#Gssssssg#.......",
    "........#Gssssg#........",
    ".........#Gddg#.........",
    "..........#Gg#..........",
    "...........##...........",
    "........................",
    "........................",
    "........................",
]

# ----------------------------- BATTLE AXE ----------------------------
# Double-bitted axe: gold-capped haft, two crescent steel blades with
# bright outer cutting edges, long shaded haft with a gold butt.
AXE = [
    "........................",
    "........................",
    "..........####..........",
    "..........#GG#..........",
    "........###Ll###........",
    ".......#Ws#Ll#sW#.......",
    "......#WSs#Ll#sSW#......",
    ".....#WSSs#Ll#sSSW#.....",
    "....#WSSSs#Ll#sSSSW#....",
    "...#WSSSSs#Ll#sSSSSW#...",
    "...#WSSSSs#Ll#sSSSSW#...",
    "....#WSSSs#Ll#sSSSW#....",
    ".....#WSSs#Ll#sSSW#.....",
    "......##Ws#Ll#sW##......",
    "........###Ll###........",
    "..........#Ll#..........",
    "..........#Ll#..........",
    "..........#Ll#..........",
    "..........#Ll#..........",
    "..........#Ll#..........",
    "..........#gg#..........",
    "..........####..........",
    "........................",
    "........................",
]

ICONS = [
    ("sword", SWORD, 4, 4),
    ("bow", BOW, 36, 4),
    ("shield", SHIELD, 4, 36),
    ("battle axe", AXE, 36, 36),
]


def validate(art, name):
    assert len(art) == 24, f"{name}: {len(art)} rows (want 24)"
    for j, row in enumerate(art):
        assert len(row) == 24, f"{name} row {j}: {len(row)} chars (want 24)"
        for ch in row:
            assert ch == "." or ch in PALETTE, f"{name} row {j}: bad char {ch!r}"


def outline_leaks(art, exempt=("t",)):
    """Coloured (non-outline) pixels that touch transparency 4-way."""
    leaks = []
    for y in range(24):
        for x in range(24):
            ch = art[y][x]
            if ch in (".", "#") or ch in exempt:
                continue
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if not (0 <= nx < 24 and 0 <= ny < 24) or art[ny][nx] == ".":
                    leaks.append((x, y, ch))
                    break
    return leaks


def stamp(canvas, art, ox, oy):
    for j, row in enumerate(art):
        for i, ch in enumerate(row):
            if ch != ".":
                canvas.set(ox + i, oy + j, PALETTE[ch])


c = new_canvas(64, 64, background=None, name="weapon_icons")

for name, art, ox, oy in ICONS:
    validate(art, name)
    leaks = outline_leaks(art)
    print(f"[{name}] non-outline pixels touching transparency: {len(leaks)} {leaks if leaks else ''}")
    stamp(c, art, ox, oy)

print()
print(c.stats_text())
print()

for name, art, ox, oy in ICONS:
    print(f"--- {name} ---")
    print(c.matrix_text(region=(ox, oy, ox + 23, oy + 23)))
    print()

try:
    save("weapon_icons", c)
except Exception as e:
    print("save skipped:", e)

finish(c)
