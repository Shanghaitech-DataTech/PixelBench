from pixelbench_api import new_canvas, flatten, finish, view

W, H = 128, 128

sky_colors = [
    "#0b1021",
    "#1b1b3a",
    "#32224f",
    "#50275d",
    "#753064",
    "#9c3f60",
    "#c25556",
    "#df734b",
    "#f29742",
    "#f8c255",
    "#fceb79"
]

sea_colors = [
    "#f8c255",
    "#df734b",
    "#9c3f60",
    "#50275d",
    "#1b1b3a",
    "#0b1021"
]

c_sky = new_canvas(W, H)
horizon = 85

for y in range(horizon):
    idx = int((y / horizon) ** 1.5 * (len(sky_colors) - 1))
    c_sky.line(0, y, W-1, y, sky_colors[idx])
    
for y in range(horizon, H):
    idx = int(((y - horizon) / (H - horizon)) ** 0.8 * (len(sea_colors) - 1))
    c_sky.line(0, y, W-1, y, sea_colors[idx])
    
c_sun = new_canvas(W, H)
sun_x, sun_y = 85, 75
c_sun.circle(sun_x, sun_y, 16, "#df734b")
c_sun.circle(sun_x, sun_y, 14, "#f29742")
c_sun.circle(sun_x, sun_y, 11, "#f8c255")

# Sun reflection
for y in range(horizon, H):
    if y % 2 == 0:
        w = int((y - horizon) * 0.5) + 3
        c_sun.line(sun_x - w, y, sun_x + w, y, "#f29742")
    elif y % 3 == 0:
        w = int((y - horizon) * 0.4) + 2
        c_sun.line(sun_x - w, y, sun_x + w, y, "#f8c255")
    elif y % 5 == 0:
        w = int((y - horizon) * 0.2) + 1
        c_sun.line(sun_x - w, y, sun_x + w, y, "#fceb79")
        
c_clouds = new_canvas(W, H)
def cloud(x, y, w, color):
    c_clouds.ellipse(x, y, w, 4, color)
    c_clouds.ellipse(x-int(w*0.5), y+1, int(w*0.6), 3, color)
    c_clouds.ellipse(x+int(w*0.5), y+1, int(w*0.6), 3, color)
    c_clouds.ellipse(x-int(w*0.2), y-2, int(w*0.5), 4, color)
    c_clouds.ellipse(x+int(w*0.2), y-1, int(w*0.4), 3, color)
    
cloud(30, 30, 20, sky_colors[4])
cloud(90, 20, 25, sky_colors[3])
cloud(60, 45, 30, sky_colors[6])
cloud(110, 55, 18, sky_colors[5])
cloud(25, 60, 22, sky_colors[7])
cloud(85, 65, 35, sky_colors[8])

c_cliff = new_canvas(W, H)
rock_base = "#141124"
rock_dark = "#0a0812"
rock_light = "#241d38"

# Cliff left
c_cliff.poly([(0, H-1), (0, 60), (10, 62), (20, 68), (35, 75), (45, 90), (55, H-1)], rock_base)
c_cliff.poly([(0, H-1), (0, 65), (8, 70), (15, 75), (25, 85), (35, 105), (40, H-1)], rock_dark)
c_cliff.poly([(10, 62), (20, 68), (22, 70), (12, 64)], rock_light)
c_cliff.poly([(20, 68), (35, 75), (37, 77), (22, 70)], rock_light)

# Castle base
c_cliff.rect(4, 45, 26, 15, rock_base)
# Left tower
c_cliff.rect(2, 25, 8, 35, rock_base)
# Right tower
c_cliff.rect(24, 30, 8, 30, rock_base)

# Parapets
for i in range(2, 10, 2):
    c_cliff.rect(i, 23, 1, 2, rock_base)
for i in range(24, 32, 2):
    c_cliff.rect(i, 28, 1, 2, rock_base)
for i in range(12, 24, 2):
    c_cliff.rect(i, 43, 1, 2, rock_base)
    
# Spires
c_cliff.poly([(1, 23), (6, 5), (11, 23)], rock_dark)
c_cliff.poly([(23, 28), (28, 13), (33, 28)], rock_dark)

# Flags
c_cliff.line(6, 5, 6, 0, rock_light)
c_cliff.poly([(6, 1), (16, 3), (6, 5)], "#c25556")
c_cliff.line(28, 13, 28, 5, rock_light)
c_cliff.poly([(28, 6), (36, 8), (28, 10)], "#c25556")

# Windows
c_cliff.rect(4, 30, 2, 4, "#fceb79")
c_cliff.rect(27, 35, 2, 4, "#fceb79")

# Gate
c_cliff.rect(12, 50, 6, 10, "#f8c255")
c_cliff.ellipse(14, 50, 3, 3, "#f8c255")
c_cliff.rect(13, 51, 4, 9, "#df734b")
c_cliff.ellipse(14, 51, 2, 2, "#df734b")

c_fg = new_canvas(W, H)
# Right rocks
c_fg.poly([(W-1, H-1), (W-1, 90), (115, 95), (100, 105), (85, 120), (75, H-1)], rock_base)
c_fg.poly([(W-1, H-1), (W-1, 100), (120, 105), (105, 115), (90, 125), (85, H-1)], rock_dark)
c_fg.poly([(115, 95), (100, 105), (102, 107), (117, 97)], rock_light)

# Left rocks foreground
c_fg.poly([(0, H-1), (0, 110), (15, 115), (30, H-1)], rock_dark)

# Birds
def bird(x, y):
    c_sky.set(x, y, rock_dark)
    c_sky.set(x-1, y-1, rock_dark)
    c_sky.set(x-2, y-2, rock_dark)
    c_sky.set(x+1, y-1, rock_dark)
    c_sky.set(x+2, y-2, rock_dark)

bird(90, 40)
bird(95, 35)
bird(82, 45)

final = flatten([c_sky, c_sun, c_clouds, c_cliff, c_fg])
finish(final)
