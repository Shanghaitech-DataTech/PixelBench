import math

# ---------- palette ----------
DARK   = '#4a3517'   # outline / dark bamboo
RIMSH  = '#8a6a35'   # rim shadow / binding strips
MID    = '#c99e5f'   # bamboo body
LIGHT  = '#e6c37c'   # rim highlight
INSIDE = '#6e4f26'   # basket interior shadow
JOINT  = '#a87c3e'   # horizontal slat lines
DFILL  = '#f6ecd6'   # dumpling body
DSHADE = '#e0cfa8'   # dumpling shade
DOL    = '#b89b6e'   # dumpling outline
DHIGH  = '#fff8ea'   # dumpling highlight
STEAM  = (232, 237, 241, 205)
STEAM2 = (232, 237, 241, 130)

out = new_canvas(32, 32, name='bamboo-steamer')

# ---------- basket interior (behind dumplings) ----------
out.rect(7, 13, 18, 1, RIMSH)    # back rim
out.rect(6, 14, 20, 1, INSIDE)
out.rect(5, 15, 22, 1, INSIDE)

# ---------- three dumplings ----------
DMP = [
    ".XXX.X.",
    "XFFFFFX",
    "XFFFFFX",
    "XSSSSSX",
    ".XXXXX.",
]

def dumpling(x, y):
    for r, row in enumerate(DMP):
        for c, ch in enumerate(row):
            if ch == '.':
                continue
            out.set(x + c, y + r, {'X': DOL, 'F': DFILL, 'S': DSHADE}[ch])
    out.set(x + 1, y + 1, DHIGH)            # highlight
    out.set(x + 2, y + 1, DSHADE)           # pleat marks
    out.set(x + 4, y + 1, DSHADE)

dumpling(5, 11)
dumpling(13, 10)
dumpling(21, 11)

# ---------- basket front ----------
out.rect(4, 16, 24, 1, LIGHT)               # rim top
out.set(4, 16, DARK); out.set(27, 16, DARK)
out.rect(4, 17, 24, 1, RIMSH)               # rim shadow band
out.set(4, 17, DARK); out.set(27, 17, DARK)
out.rect(5, 18, 22, 9, MID)                 # body fill rows 18-26
for y in range(18, 28):
    out.set(4, y, DARK)
    out.set(27, y, DARK)
out.rect(5, 21, 22, 1, JOINT)               # slat lines
out.rect(5, 24, 22, 1, JOINT)
for sx in (9, 15, 21):                      # vertical binding strips
    out.rect(sx, 18, 1, 9, RIMSH)
out.rect(5, 27, 22, 1, RIMSH)               # base band
out.rect(4, 28, 24, 1, DARK)                # bottom outline
out.rect(7, 29, 18, 1, DARK)                # rounded bottom

# ---------- lid: shallow dome lifted open, hinged left, rising right ----------
LPATH = "M 12 13 L 30 9 Q 21 1 12 13 Z"
out.path(LPATH, MID)
out.path(LPATH, DARK, fill=False)
out.path("M 14 11 Q 21 4.5 28 8", JOINT, fill=False)  # bamboo weave line
out.rect(20, 4, 2, 2, DARK)                           # knob
out.set(20, 4, LIGHT)

# ---------- rising steam ----------
def wisp(x0, ybot, h, phase):
    for i in range(h):
        dx = int(round(1.4 * math.sin(i * 0.85 + phase)))
        out.set(x0 + dx, ybot - i, STEAM)

wisp(7, 9, 8, 0.0)
wisp(9, 8, 6, 2.0)
wisp(6, 10, 5, 4.0)
out.set(7, 1, STEAM2)
out.set(8, 0, STEAM2)
out.set(9, 2, STEAM2)

view(out)
finish(out)
