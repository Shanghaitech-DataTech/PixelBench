c = new_canvas(64, 32, name="output")

# ---- palette ----
BODY    = "#eef3f6"
BODY_D  = "#ccd8de"
PANEL   = "#d7e2e8"
SKIRT   = "#a7b7c2"
SKIRT_D = "#8695a0"
ACCENT  = "#2278bd"
ACCENT_D = "#13527f"
ROOF    = "#fbfdfe"
GLASS   = "#55b8da"
GLASS_D = "#2d86ad"
GLASS_L = "#a8e6f4"
FRAME   = "#262f36"
TIRE    = "#17191c"
RIM     = "#9aa5ac"
RIM_D   = "#5e676d"
HEAD    = "#ffe484"
HEAD_C  = "#fffbe4"
TAIL    = "#d8402f"
TAIL_D  = "#9c2a1e"
LED     = "#ffb833"
LEDBG   = "#12181d"

# ============ body shell: roof y5, body y6..25 ============
c.rect(2, 6, 60, 20, BODY)
c.rect(4, 5, 56, 1, ROOF)
c.set(3, 5, BODY)
c.set(60, 5, BODY)
c.rect(20, 6, 14, 1, BODY_D)       # roof AC unit

# ============ side windows, y8..15 ============
def win(x0, x1):
    w = x1 - x0 + 1
    c.rect(x0, 8, w, 8, GLASS)
    c.rect(x0, 8, w, 1, GLASS_L)
    c.rect(x0, 15, w, 1, GLASS_D)
    c.rect(x0, 9, 1, 6, GLASS_L)

for a, b in [(4, 9), (11, 16), (18, 22), (32, 37), (39, 43)]:
    win(a, b)

# ============ side band + skirt ============
c.rect(2, 20, 49, 2, ACCENT)
c.rect(2, 22, 49, 1, ACCENT_D)
c.rect(2, 23, 59, 3, SKIRT)
c.rect(2, 25, 59, 1, SKIRT_D)

# ============ electronic route display ============
c.rect(51, 6, 10, 5, LEDBG)
c.rect(52, 7, 3, 1, LED)           # "2"
c.set(54, 8, LED)
c.rect(52, 9, 3, 1, LED)
c.rect(56, 7, 3, 1, LED)           # "7"
c.set(58, 8, LED)
c.set(57, 9, LED)

# ============ windshield, y12..19 ============
c.rect(51, 12, 10, 8, GLASS)
c.rect(51, 12, 10, 1, GLASS_L)
c.rect(51, 19, 10, 1, GLASS_D)
c.line(53, 17, 56, 14, GLASS_L)    # small glint

# front lower face
c.rect(51, 20, 10, 2, PANEL)
c.rect(51, 22, 10, 3, SKIRT)
c.rect(51, 25, 10, 1, SKIRT_D)

# ============ doors: rear x24..29, front x45..50 ============
def door(x0, x1):
    w = x1 - x0 + 1
    c.rect(x0, 7, w, 17, FRAME)                 # dark door frame y7..23
    c.rect(x0 + 1, 8, w - 2, 9, GLASS)          # glass y8..16
    c.rect(x0 + 1, 8, w - 2, 1, GLASS_L)
    c.rect(x0 + 1, 16, w - 2, 1, GLASS_D)
    c.rect(x0 + 1, 18, w - 2, 5, PANEL)         # lower panel
    c.rect(x0 + 1, 22, w - 2, 1, SKIRT_D)       # step edge
    cx = x0 + w // 2
    c.line(cx, 8, cx, 22, FRAME)                # leaf split

door(24, 29)
door(45, 50)

# ============ lights ============
c.rect(55, 20, 6, 3, FRAME)        # lamp housing
c.rect(56, 20, 4, 2, HEAD)         # headlight cluster
c.rect(57, 20, 2, 1, HEAD_C)
c.rect(2, 20, 5, 3, FRAME)         # rear lamp housing
c.rect(3, 20, 4, 2, TAIL)
c.rect(3, 21, 4, 1, TAIL_D)

# silhouette
c.outline(FRAME)

# ============ wheel arches cut into the skirt ============
for cx in (14, 40):
    c.rect(cx - 4, 24, 9, 2, SKIRT_D)
    c.rect(cx - 3, 23, 7, 1, SKIRT_D)
    c.rect(cx - 3, 24, 7, 2, FRAME)
    c.rect(cx - 2, 22, 5, 2, FRAME)

# ============ wheels ============
for cx in (14, 40):
    c.circle(cx, 26, 4, FRAME)
    c.circle(cx, 26, 3, TIRE)
    c.circle(cx, 26, 1, RIM)
    c.set(cx, 26, RIM_D)

# ============ mirror ============
c.set(62, 11, FRAME)
c.set(62, 12, FRAME)
c.set(63, 10, FRAME)

view(c)
print(c.stats_text())
finish(c)
