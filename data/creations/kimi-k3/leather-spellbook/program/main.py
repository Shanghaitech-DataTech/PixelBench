# Closed leather spellbook - 32x32 RPG item portrait, 8 colors, transparent bg
book = new_canvas(32, 32, None, name="spellbook")

OUT = '#221419'  # dark outline
L1  = '#8a4526'  # leather base
L2  = '#5a2a1a'  # leather shadow / spine
L3  = '#c07a45'  # leather highlight
M1  = '#7a6436'  # brass dark
M2  = '#d9b45f'  # brass bright
P   = '#e8d9b0'  # page cream
G   = '#b03030'  # gem red

# --- silhouette / outline ---
book.rect(4, 5, 24, 22, OUT)          # x4..27, y5..26

# --- spine (left) ---
book.rect(5, 6, 3, 20, L2)            # x5..7, y6..25
book.rect(5, 9, 3, 1, L3)             # raised band
book.rect(5, 17, 3, 1, L3)            # raised band
book.line(8, 6, 8, 25, OUT)           # spine/cover divider

# --- cover base + bevel light ---
book.rect(9, 6, 18, 19, L1)           # x9..26, y6..24
book.rect(9, 6, 18, 1, L3)            # top light
book.line(9, 7, 9, 23, L3)            # left light
book.rect(9, 24, 18, 1, L2)           # bottom shadow
book.line(26, 7, 26, 23, L2)          # right shadow

# --- page block along bottom edge ---
book.rect(9, 25, 18, 1, P)
for tx in (11, 14, 17, 20, 23):       # page seams
    book.set(tx, 25, L2)

# --- tooled inner border + brass studs ---
book.rect(11, 9, 14, 12, OUT, fill=False)   # x11..24, y9..20
for sx, sy in ((11, 9), (24, 9), (11, 20), (24, 20)):
    book.set(sx, sy, M2)

# --- metal corner plates (3x3, inset) ---
for px, py, hx, hy in ((5, 6, 5, 6), (23, 6, 25, 6),
                       (5, 22, 5, 24), (23, 22, 25, 24)):
    book.rect(px, py, 3, 3, M1)
    book.set(hx, hy, M2)              # corner glint
    book.set(px + 1, py + 1, M2)      # rivet

# --- center gem (small diamond) ---
book.set(17, 11, M2)                  # glint tip
book.rect(16, 12, 3, 1, G)
book.set(17, 13, G)

# --- clasp strap across right edge ---
book.rect(20, 15, 8, 2, M1)           # x20..27, wraps over edge
book.line(20, 15, 27, 15, M2)         # top highlight
book.set(20, 16, M2)                  # rivet

view(book)
finish(book)
