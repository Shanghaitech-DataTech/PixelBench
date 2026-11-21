# RPG wooden magic staff with curved head + purple particles, 48x48.

c = new_canvas(48, 48, background=None, name="magic-staff")

# ---------------- palette ----------------
WK = "#2E1D0D"   # dark outline
WD = "#46290F"   # wood shadow
WM = "#7A4E28"   # wood mid
WL = "#A8743D"   # wood light
WH = "#D6A05C"   # wood highlight
WB = "#5C3A1E"   # wrap band dark
WBL = "#8A5A30"  # wrap band light

PD = "#5B2A86"   # purple deep
PM = "#8A4FC0"   # purple mid
PL = "#B987E6"   # purple light
PG = "#F0E2FF"   # glint
PP = "#C9A0F0"   # particle bright
PT = "#9A6FD0"   # particle dim
AU = (154, 79, 214, 70)    # aura
AU2 = (154, 79, 214, 36)   # faint aura

def rr(x, y, w, h, r, col):
    c.rect(x + r, y, w - 2 * r, h, col)
    c.rect(x, y + r, w, h - 2 * r, col)
    for cx, cy in ((x + r, y + r), (x + w - 1 - r, y + r),
                   (x + r, y + h - 1 - r), (x + w - 1 - r, y + h - 1 - r)):
        c.circle(cx, cy, r, col)

# ---------------- aura (behind everything) ----------------
c.circle(24, 7, 6, AU2)
c.circle(24, 7, 4, AU)

# ---------------- shaft ----------------
c.rect(22, 16, 4, 32, WK)          # outline, y16..47
c.line(23, 16, 23, 45, WL)         # light left grain
c.line(24, 16, 24, 45, WM)         # mid right grain

# ---------------- curved head: upward crescent ----------------
c.circle(24, 10, 7, WK)            # outer outline disc
c.circle(24, 10, 6, WM)            # wood body
c.circle(24, 6, 4, None)           # carve the bowl (orb cradles inside)
# inner bowl rim (dark) so the orb reads as cradled
for (x, y) in [(19,5),(19,6),(20,7),(20,8),(20,9),(21,10),
               (29,5),(29,6),(28,7),(28,8),(28,9),(27,10)]:
    c.set(x, y, WD)
# prong tip accents
c.set(20, 4, WH); c.set(19, 5, WL)
c.set(28, 4, WD); c.set(29, 5, WD)
# outer rim shading (light upper-left, dark lower-right)
for (x, y) in [(18,6),(17,8),(17,9),(17,10),(18,11),(19,12)]:
    c.set(x, y, WL)
for (x, y) in [(30,6),(31,8),(31,9),(30,10),(30,11),(29,12),(27,14),(25,16)]:
    c.set(x, y, WD)
# wood grain streaks on the knot
c.line(21, 12, 23, 14, WL)
c.line(26, 13, 28, 11, WD)

# ---------------- orb (cradled in the crescent) ----------------
c.circle(24, 7, 3, PM)
c.circle(23, 6, 2, PL)
c.set(22, 5, PG); c.set(23, 5, PG); c.set(22, 6, PG)
# bottom-right shading
c.set(26, 9, PD); c.set(25, 10, PD); c.set(27, 7, PD); c.set(27, 8, PM)
c.set(24, 10, PD)

# ---------------- collar below head ----------------
c.rect(21, 17, 6, 3, WK)
c.rect(22, 18, 4, 1, WBL)
c.rect(22, 19, 4, 1, WB)

# ---------------- shaft grain detail ----------------
c.line(23, 24, 23, 28, WH)
c.line(24, 20, 24, 24, WD)
c.line(23, 36, 23, 41, WM)
c.set(24, 30, WD); c.set(23, 31, WD)   # knot

# ---------------- wrap bands (grip) ----------------
for y in (26, 35):
    c.rect(22, y, 4, 2, WB)
    c.line(22, y, 25, y, WBL)

# ---------------- butt cap ----------------
rr(21, 44, 6, 4, 1, WK)
c.rect(22, 45, 4, 2, WM)
c.line(22, 45, 22, 46, WL)
c.set(25, 46, WD)
c.set(23, 45, WH)

# ---------------- purple particles ----------------
def sparkle(x, y, col, big=False):
    c.set(x, y, col)
    c.set(x - 1, y, col); c.set(x + 1, y, col)
    c.set(x, y - 1, col); c.set(x, y + 1, col)
    if big:
        c.set(x, y, PG)

sparkle(8, 14, PP, big=True)
sparkle(38, 4, PP)
sparkle(40, 15, PT)
sparkle(33, 24, PP)
sparkle(9, 27, PT)
sparkle(37, 33, PT, big=True)
sparkle(7, 39, PP)
sparkle(30, 41, PT)
sparkle(13, 7, PT)

# tiny dots
for (x, y, col) in [(4,6,PP),(33,1,PT),(43,9,PP),(15,21,PT),(41,22,PP),
                    (5,22,PT),(14,34,PP),(42,38,PT),(10,45,PP),(27,36,PT),
                    (17,17,PP),(35,45,PT),(44,29,PT),(3,33,PP),(36,10,PT)]:
    c.set(x, y, col)

# faint glow dots near the orb
for (x, y) in [(24,2),(16,6),(32,6)]:
    c.set(x, y, AU2)

print(c.stats_text())
view(c)
finish(c)
