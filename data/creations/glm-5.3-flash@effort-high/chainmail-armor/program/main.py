# chainmail-armor: 32x32 RPG chainmail hauberk, interlocking rings, dark outline
LIGHT = '#ced4dc'   # specular highlight
MID   = '#9aa2ad'   # ring metal
DARK  = '#68707e'   # ring shadow / interior
OUT   = '#22252c'   # dark outline

W = H = 32

def px(arr, x, y):
    i = (y * W + x) * 4
    return arr[i:i + 4]

# ---- 1. silhouette of the mail shirt ----
s = new_canvas(W, H, name="silhouette")
s.rect(7, 5, 18, 2, MID)    # shoulders  x7-24, y5-6
s.rect(8, 7, 16, 20, MID)   # torso      x8-23, y7-26
s.rect(7, 25, 18, 3, MID)   # hem flare  x7-24, y25-27
s.rect(4, 7, 4, 7, MID)     # left sleeve  x4-7,  y7-13
s.rect(24, 7, 4, 7, MID)    # right sleeve x24-27, y7-13
s.clear(13, 5, 6, 3)        # neck opening
s.clear(7, 27, 2, 1)        # side slits at hem
s.clear(23, 27, 2, 1)

# ---- 2. interlocking ring texture ----
t = new_canvas(W, H, name="rings")
row = 0
for y in range(-2, H + 4, 4):
    off = 2 if (row % 2) else 0
    for x in range(-2 + off, W + 4, 4):
        t.circle(x, y, 2, DARK, fill=True)   # solid backing
        t.circle(x, y, 2, MID, fill=False)   # the ring itself
        t.set(x - 1, y - 1, LIGHT)           # specular glint
    row += 1

# ---- 3. clip texture to silhouette, dark ground between the rings ----
c = new_canvas(W, H, name="chainmail-armor")
sa = s.to_rgba()[2]
ta = t.to_rgba()[2]
for y in range(H):
    for x in range(W):
        if px(sa, x, y)[3] > 0:
            r, g, b, a = px(ta, x, y)
            c.set(x, y, (r, g, b) if a > 0 else DARK)

# ---- 4. shading: darker toward the right and the bottom ----
iM = c.color(MID)
iL = c.color(LIGHT)
iD = c.color(DARK)
for y in range(H):
    for x in range(W):
        idx = c.get(x, y)
        if idx < 0:
            continue
        if x >= 21 or y >= 25:
            if idx == iL:
                c.set(x, y, iM)
            elif idx == iM:
                c.set(x, y, iD)

# ---- 5. dark outline around the whole garment ----
c.outline(OUT)

print(c.stats_text())
print(c.matrix_text())
save("chainmail-armor", c)
finish(c)
