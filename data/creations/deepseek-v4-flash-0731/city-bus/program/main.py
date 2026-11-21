from pixelbench_api import new_canvas, finish

OUT    = "#12283F"  # dark outline
ROOF   = "#E9F2FA"  # white roof
MAIN   = "#2E6DB4"  # body blue
STRIPE = "#9CC8E8"  # accent stripe
SKIRT  = "#3B4A5E"  # dark skirt
GLASS  = "#1D4E7A"  # dark glass
GLASSHI= "#7FD0F0"  # glass highlight
DOOR   = "#3D7BBF"  # door tone
WHEEL  = "#131820"  # tire
HUB    = "#96A2AE"  # wheel hub
RIM    = "#D9E2EA"  # bright rim
HL     = "#F6E9A8"  # headlight
HLB    = "#FFFBE6"  # bright light
TAIL   = "#C62F2F"  # taillight
SBG    = "#0F1822"  # route sign background
SON    = "#FFD23F"  # route sign amber

c = new_canvas(64, 32)

# --- body silhouette ---
c.rect(1, 8, 63, 16, OUT)          # dark frame: x=1..63, y=8..23
c.rect(2, 9, 61, 1, ROOF)          # roof stripe  y=9
c.rect(2, 10, 61, 11, MAIN)        # main body   y=10..20
c.rect(2, 21, 61, 2, SKIRT)         # skirt       y=21..22

# --- row of side windows ---
for x in (12, 18, 24, 30, 36, 42):
    c.rect(x, 10, 5, 5, GLASS)      # glass band y=10..14
    c.rect(x + 1, 11, 3, 1, GLASSHI)

# --- front and rear doors (two leaves each) ---
for x in (5, 51):
    c.rect(x, 13, 5, 8, DOOR)       # x..x+4, y=13..20
    c.rect(x + 1, 14, 3, 3, GLASS)  # door glass y=14..16
    c.rect(x + 2, 13, 1, 7, OUT)    # centre split
    c.set(x, 17, OUT)               # handles
    c.set(x + 4, 17, OUT)

# --- accent stripe across body/doors ---
c.rect(2, 16, 61, 1, STRIPE)

# --- slanted windshield at the front ---
c.poly([(56, 9), (61, 9), (63, 14), (58, 14)], GLASS)
c.line(57, 11, 61, 13, GLASSHI)

# --- electronic route display on the front roof ---
c.rect(47, 7, 13, 7, SBG)
c.text(48, 7, "42", SON, font="5x7")
c.set(55, 12, SON)
c.set(56, 13, SON)

# --- lights ---
c.rect(59, 17, 4, 3, HL)            # headlights x=59..62, y=17..19
c.set(60, 18, HLB)
c.set(61, 18, HLB)
c.set(63, 18, HL)
c.rect(1, 17, 2, 3, TAIL)           # taillight   x=1..2,  y=17..19
c.set(2, 18, HLB)

# --- wheels ---
for cx in (12, 51):
    c.circle(cx, 25, 4, WHEEL)
    c.circle(cx, 25, 2, HUB)
    c.set(cx, 25, RIM)
    c.set(cx, 24, RIM)

print(c.stats_text())
finish(c)
