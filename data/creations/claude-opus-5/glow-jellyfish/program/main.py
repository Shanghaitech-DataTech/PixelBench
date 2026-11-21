c = new_canvas(16, 16, name="jelly")

COLS = {
    "O": "#08122b",   # dark outline
    "D": "#1d4480",   # bell deep (shadow side)
    "M": "#3a7cc4",   # bell mid
    "L": "#7cc6ee",   # bell light / translucent sheen
    "G": "#b6eeff",   # glow
    "W": "#f6ffff",   # glow core
    "T": "#7fd0f0",   # tentacle light
    "t": "#2c66a6",   # tentacle dark
}
HALO = "#9fe6ff2b"    # faint bioluminescence bleeding into the water

# --- bell: rounded dome, lit upper-left, glow pooling in the lower centre ---
BODY = {
    2: (6, "LLLM"),
    3: (5, "LLLLMM"),
    4: (4, "LLLLGMMD"),
    5: (3, "LLLGGGMMDD"),
    6: (3, "MLGGWWGMDD"),
    7: (3, "MLGGWWGMDD"),
    8: (4, "DLGGGMDD"),
}
body = {}
for y, (x0, row) in BODY.items():
    for i, ch in enumerate(row):
        body[(x0 + i, y)] = ch

NEIGH8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
NEIGH4 = ((1, 0), (-1, 0), (0, 1), (0, -1))

# --- short tentacles trailing from the skirt, each with a glowing tip ---
TENTS = [
    [(5, 9), (5, 10), (4, 11), (4, 12)],
    [(7, 9), (7, 10), (7, 11), (7, 12), (7, 13)],
    [(9, 9), (9, 10), (9, 11), (10, 12)],
    [(11, 9), (11, 10), (11, 11)],
]
tent = {}
for strand in TENTS:
    last = len(strand) - 1
    for i, (x, y) in enumerate(strand):
        tent[(x, y)] = "G" if i == last else ("T" if i % 2 == 0 else "t")

# --- 1px dark outline around the bell, skipping the skirt cells the
#     tentacles grow out of so each strand reads as attached, not fenced in ---
outline = set()
for (x, y) in body:
    for dx, dy in NEIGH8:
        p = (x + dx, y + dy)
        if p in body or p in tent:
            continue
        if 0 <= p[0] < 16 and 0 <= p[1] < 16:
            outline.add(p)

# --- paint: halo under everything, then outline, bell, tentacles ---
lit = set(body) | outline | set(tent)
for (x, y) in lit:
    for dx, dy in NEIGH4:
        p = (x + dx, y + dy)
        if p not in lit and 0 <= p[0] < 16 and 0 <= p[1] < 16:
            c.set(p[0], p[1], HALO)

for (x, y) in outline:
    c.set(x, y, COLS["O"])
for (x, y), ch in body.items():
    c.set(x, y, COLS[ch])
for (x, y), ch in tent.items():
    c.set(x, y, COLS[ch])

print(c.stats_text())
view(c)
finish(c)
