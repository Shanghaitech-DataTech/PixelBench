from pixelbench_api import *

# ---------- country-road background ----------
bg = new_canvas(64, 64, background=None, name='bg')

sky = bg.color('#9cd7ff', 'sky')
white = bg.color('#ffffff')  # reuses input white for clouds
hill_far = bg.color('#8fd06a', 'hill_far')
hill_near = bg.color('#63b23f', 'hill_near')
grass = bg.color('#7cc84a', 'grass')
road = bg.color('#8a8a92', 'road')
road_dark = bg.color('#5f5f68', 'road_dark')
shoulder = bg.color('#e8e8e8', 'shoulder')
line_yellow = bg.color('#ffd23e', 'line_yellow')

# sky
bg.rect(0, 0, 64, 64, sky)

# clouds
bg.ellipse(10, 6, 6, 3, white, fill=True)
bg.ellipse(17, 5, 4, 3, white, fill=True)
bg.ellipse(46, 9, 5, 3, white, fill=True)
bg.ellipse(52, 8, 4, 2, white, fill=True)

# distant hills
bg.poly([(0, 22), (10, 13), (22, 19), (36, 12), (52, 18), (63, 14), (63, 28), (0, 28)], hill_far, fill=True)

# nearer hills / horizon
bg.poly([(0, 26), (12, 20), (26, 24), (44, 19), (58, 24), (63, 23), (63, 32), (0, 32)], hill_near, fill=True)

# grass field below the hills
bg.rect(0, 26, 64, 38, grass)

# perspective country road: narrow at the horizon, wide at the viewer
bg.poly([(24, 28), (40, 28), (74, 64), (-10, 64)], road, fill=True)

# light road shoulders
bg.line(24, 28, -10, 64, shoulder)
bg.line(40, 28, 74, 64, shoulder)

# dashed yellow centre line
dash_y = 31
while dash_y <= 60:
    bg.line(32, dash_y, 32, dash_y + 3, line_yellow)
    dash_y += 7

# small contact shadows under the two wheels
bg.ellipse(14, 48, 7, 1, road_dark, fill=True)
bg.ellipse(50, 48, 8, 1, road_dark, fill=True)

# ---------- motorcycle layer (white background made transparent) ----------
moto = input_canvas.copy(name='moto')
white_idx = moto.color('#ffffffff')
for y in range(64):
    for x in range(64):
        if moto.get(x, y) == white_idx:
            moto.set(x, y, None)

# ---------- composite ----------
result = flatten([bg, moto], name='result')

print('bg stats:', bg.stats_text())
print('moto stats:', moto.stats_text())
print('result stats:', result.stats_text())
print(result.matrix_text(region=(0, 0, 63, 31)))

finish(result)
