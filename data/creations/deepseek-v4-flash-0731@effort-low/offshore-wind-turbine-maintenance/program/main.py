from pixelbench_api import new_canvas, flatten, finish, save, view, input_canvas

W = 64
H = 64
c = new_canvas(W, H)

# ---------- Sky gradient ----------
sky = [
    "#5FA6DC", "#6DB1E2", "#7DBDE8", "#8CC7EE",
    "#9BD1F2", "#ABDBF6", "#BCE4FA", "#CBECFC",
]
for y in range(0, 32):
    idx = min(7, y // 4)
    for x in range(0, 64):
        c.set(x, y, sky[idx])

# clouds
cloud_col = "#F2F9FF"
c.ellipse(11, 5, 4, 2, cloud_col)
c.ellipse(16, 6, 3, 2, cloud_col)
c.ellipse(48, 10, 5, 2, cloud_col)
c.ellipse(55, 11, 3, 1, cloud_col)

# ---------- Sea ----------
sea = [
    "#3D76A8", "#366B9E", "#2F6093", "#285587",
    "#214A7A", "#1A3F6E",
]
for y in range(32, 64):
    idx = min(5, (y - 32) // 6)
    for x in range(0, 64):
        c.set(x, y, sea[idx])

# ---------- Distance turbines ----------
haze_tower = "#9FB2C6"
haze_blade = "#C3D2E0"
haze_nac  = "#A8BACB"

# turbine 1 (left, farther)
c.rect(5, 26, 2, 7, haze_tower)
c.rect(3, 25, 7, 2, haze_nac)
c.line(5, 25, 5, 21, haze_blade)
c.line(5, 25, 3, 22, haze_blade)
c.line(5, 25, 7, 22, haze_blade)

# turbine 2 (right)
c.rect(57, 28, 2, 5, haze_tower)
c.rect(54, 27, 7, 2, haze_nac)
c.line(58, 27, 58, 24, haze_blade)
c.line(58, 27, 56, 24, haze_blade)
c.line(58, 27, 60, 24, haze_blade)

# ---------- Main turbine ----------
steel_d  = "#39434E"   # dark outline
steel   = "#AEB9C5"   # tower light
shade   = "#8FA0AD"   # tower shadow
blade_c = "#D7E0E8"
nac     = "#AEBAC6"
nac_d   = "#5C6B79"

# blades (drawn behind nacelle)
c.poly([(23,10),(25,10),(24,0)], blade_c)     # up
c.poly([(23,9),(24,12),(12,4)], blade_c)     # up-left
c.poly([(25,9),(24,12),(35,4)], blade_c)     # up-right
# hub
c.set(24, 10, nac_d)

# tower
c.poly([(20,13),(29,13),(30,33),(16,33)], steel)
# tower shadow (right side)
c.line(27,13,29,15, shade)
c.line(28,16,29,30, shade)
c.line(26,13,28,14, shade)
# tower outline left
c.line(20,13,16,33, steel_d)
c.line(29,13,30,33, steel_d)
c.line(20,13,29,13, nac_d)

# nacelle
c.rect(16,8,14,5, nac)
c.rect(16,8,14,1, nac_d)
c.rect(16,8,1,5, nac_d)
c.rect(29,8,1,5, nac_d)
# nacelle highlight
c.rect(17,9,12,1, "#CBD6E0")

# ---------- Maintenance platform (catwalk) at sea level ----------
deck   = "#6E7E8E"
deck_h = "#9CADBC"
rail   = "#4A5561"

# deck extending right from tower at water line
c.rect(20,30,26,2, deck)       # x 20-45, y 30-31
c.rect(20,30,26,1, deck_h)
# railing posts
for px in range(20, 46, 3):
    c.rect(px, 27, 1, 3, rail)
# top rail
c.rect(20,27,26,1, rail)
# post tops
for px in range(20, 46, 3):
    c.set(px, 26, rail)
# left end post
c.set(20,27,rail)

# ---------- Ladder on tower ----------
rung = steel_d
c.rect(27,22,2,10, steel_d)   # rails
c.rect(25,21,2,1, steel_d)    # rail top (upper)
for ry in (22,24,26,28,30):
    c.rect(25,ry,4,1, steel_d)  # rungs x25-28

# ---------- Technician climbing ladder ----------
helmet = "#26303C"
skin   = "#E7BE93"
vest   = "#F59E2B"
vest_d = "#C97E14"
suit   = "#2E3A49"
boot   = "#1C242E"
# head + helmet
c.set(24,19,helmet); c.set(25,19,helmet); c.set(26,19,helmet)
c.set(24,20,skin);   c.set(25,20,skin)
c.set(23,20,helmet)
# torso/hi-vis
c.set(23,21,helmet); c.set(24,21,vest); c.set(25,21,vest); c.set(26,21,vest)
c.set(24,22,vest); c.set(25,22,vest_d)
# arms gripping ladder rung
c.set(26,23,vest_d); c.set(27,23,suit)
# legs
c.set(23,23,helmet); c.set(25,23,suit)
c.set(24,24,suit);   c.set(26,24,vest)
c.set(24,25,boot);   c.set(26,25,boot)

# ---------- Foreground wave highlights & whitecaps ----------
wave = "#5F9ECB"
foam = "#CBE7F7"
for x in range(0,64):
    if x % 3 == 1:
        c.set(x, 34, wave)
    if x % 4 == 2:
        c.set(x, 38, wave)
for x in range(0,64):
    if x % 5 == 0:
        c.set(x, 43, wave)
    if x % 6 == 3:
        c.set(x, 48, wave)
# foam near base
for x in range(13,34):
    c.set(x, 33, foam)

result = flatten([c], name="turbine")
print(result.stats_text())

finish(result)
