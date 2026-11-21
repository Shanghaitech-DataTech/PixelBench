# neighborhood-laundromat, 64x64

WALL = '#d7e1e8'
c = new_canvas(64, 64, background=WALL, name='laundromat')

# ---------- ceiling & fluorescent lights ----------
c.rect(0, 0, 64, 6, '#c6d3dc')
c.rect(7, 1, 20, 3, '#ffffff')
c.rect(37, 1, 20, 3, '#ffffff')
c.rect(7, 4, 20, 1, '#e6f1f8')
c.rect(37, 4, 20, 1, '#e6f1f8')
c.line(0, 6, 63, 6, '#9fb0bb')

# ---------- wall ----------
c.rect(8, 7, 18, 8, '#e0eaf1')    # cool light wash
c.rect(38, 7, 18, 8, '#e0eaf1')

# wall clock
c.circle(32, 10, 3, '#37424c', fill=False)
c.circle(32, 10, 2, '#ffffff')
c.set(32, 9, '#37424c')
c.set(32, 8, '#37424c')
c.set(33, 10, '#37424c')
c.set(32, 10, '#37424c')

# wall posters / signs
c.rect(9, 8, 6, 5, '#4fa3b8')
c.rect(10, 9, 4, 1, '#ffffff')
c.rect(10, 11, 4, 1, '#d7e1e8')
c.rect(49, 8, 6, 5, '#e8eef2')
c.rect(50, 9, 4, 1, '#7b8b97')
c.rect(50, 11, 4, 1, '#7b8b97')

c.line(0, 15, 63, 15, '#b9c6d0')  # wall shadow above machines

# ---------- back row of front-loading washers ----------
for x0 in (3, 13, 23, 33, 43, 53):
    c.rect(x0, 16, 8, 14, '#eef2f4')          # body
    c.rect(x0 + 7, 16, 1, 14, '#c3ced5')      # side shade
    c.rect(x0, 16, 8, 2, '#2e3942')           # control panel
    c.set(x0 + 1, 17, '#69d2e7')              # display
    c.set(x0 + 2, 17, '#69d2e7')
    c.set(x0 + 6, 17, '#7ee081')              # button
    c.circle(x0 + 4, 23, 3, '#37424c')        # door ring
    c.circle(x0 + 4, 23, 2, '#87a4b8')        # door glass
    c.set(x0 + 3, 22, '#b8d4e4')              # glass highlight
    c.set(x0 + 5, 24, '#62808f')              # drum shadow
    c.rect(x0, 29, 8, 1, '#a9b7c1')           # lower shade
    c.line(x0, 30, x0 + 7, 30, '#5c6873')     # kick plate
for gx in (11, 21, 31, 41, 51):               # divider shadows between machines
    c.line(gx, 16, gx, 30, '#5c6873')

# ---------- floor ----------
c.rect(0, 31, 64, 17, '#93a4b0')
c.rect(11, 33, 12, 5, '#a2b3bf')              # cool light reflections
c.rect(41, 33, 12, 5, '#a2b3bf')
c.line(0, 31, 63, 31, '#6e7d89')              # baseboard shadow
c.line(0, 39, 63, 39, '#8294a0')              # tile grout
c.line(0, 46, 63, 46, '#8294a0')
for x in (8, 24, 40, 56):
    c.line(x, 32, x, 38, '#8294a0')
for x in (16, 32, 48):
    c.line(x, 40, x, 45, '#8294a0')
c.line(0, 47, 63, 47, '#6e7d89')              # shadow in front of front row

# ---------- folding table ----------
c.rect(17, 37, 30, 2, '#f4f7f9')              # top
c.line(17, 39, 46, 39, '#b9c6d0')             # front edge
c.rect(19, 40, 2, 8, '#7f8d99')               # legs
c.rect(43, 40, 2, 8, '#7f8d99')
c.line(21, 44, 43, 44, '#7f8d99')             # crossbar

# folded laundry + detergent on the table
c.rect(22, 34, 7, 3, '#f0f4f7')
c.rect(23, 33, 5, 1, '#ffffff')
c.line(23, 35, 28, 35, '#4fa3b8')
c.rect(32, 34, 6, 3, '#7fc4d4')
c.rect(33, 33, 4, 1, '#a8dce6')
c.line(33, 35, 37, 35, '#ffffff')
c.rect(41, 34, 3, 3, '#f6a23b')               # detergent bottle
c.set(42, 33, '#ffffff')

# ---------- laundry basket ----------
c.set(49, 38, '#e8eef2')                      # clothes pile
c.set(50, 38, '#ffffff')
c.rect(51, 37, 3, 2, '#ffffff')
c.set(54, 38, '#ffffff')
c.set(55, 38, '#e8eef2')
c.set(56, 38, '#f0f4f7')
c.rect(48, 39, 10, 2, '#d17a28')              # rim
c.rect(49, 41, 8, 6, '#e8913f')               # body
for yy in (42, 44):                           # basket holes
    for xx in (50, 52, 54, 56):
        c.set(xx, yy, '#b0661f')
c.rect(49, 46, 8, 1, '#d17a28')               # base

# ---------- front row of front-loading washers ----------
for x0 in (2, 14, 26, 38, 50):
    c.rect(x0, 48, 11, 16, '#eef2f4')
    c.rect(x0 + 10, 48, 1, 16, '#c3ced5')
    c.rect(x0, 48, 11, 3, '#2e3942')
    c.rect(x0 + 2, 49, 3, 1, '#69d2e7')       # display
    c.set(x0 + 7, 49, '#7ee081')              # buttons
    c.set(x0 + 9, 49, '#f6d365')
    c.circle(x0 + 5, 56, 4, '#37424c')        # door ring
    c.circle(x0 + 5, 56, 3, '#87a4b8')        # door glass
    c.set(x0 + 4, 53, '#b8d4e4')              # highlight
    c.set(x0 + 3, 54, '#b8d4e4')
    c.set(x0 + 6, 58, '#62808f')              # laundry inside drum
    c.set(x0 + 7, 57, '#62808f')
    c.rect(x0, 61, 11, 1, '#a9b7c1')
    c.rect(x0, 62, 11, 2, '#5c6873')          # kick plate
for gx in (13, 25, 37, 49):                   # dividers between machines
    c.line(gx, 48, gx, 63, '#525f6a')
c.line(0, 48, 0, 63, '#525f6a')               # side walls
c.line(63, 48, 63, 63, '#525f6a')

save('laundromat', c)
view(c, scale=6, margin=0)
print(c.stats_text())
finish(c)
