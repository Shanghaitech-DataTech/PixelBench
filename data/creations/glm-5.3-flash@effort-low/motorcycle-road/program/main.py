from pixelbench_api import input_canvas, new_canvas, finish, view, save

out = input_canvas.copy(name='output')
sky = out.color('#a9d7f2', name='sky')
cloud = out.color('#eef6fb', name='cloud')
grass = out.color('#6cbf3a', name='grass')
grass2 = out.color('#57a52e', name='grass_dark')
road = out.color('#6e6e74', name='road')
road2 = out.color('#5d5d63', name='road_dark')
dash = out.color('#e8d24a', name='dash')
white = out.color('#ffffff', name='white')

w, h = 64, 64
for y in range(h):
    for x in range(w):
        idx = out.get(x, y)
        if out.color_name(idx) == '#ffffffff':
            if y < 30:
                out.set(x, y, sky)
            elif y < 46:
                out.set(x, y, grass if (x * 7 + y * 13) % 5 else grass2)
            else:
                out.set(x, y, road if (x + y) % 7 else road2)

out.ellipse(12, 8, 6, 3, cloud)
out.ellipse(18, 9, 5, 2, cloud)
out.ellipse(46, 14, 7, 3, cloud)
out.ellipse(52, 15, 4, 2, cloud)
out.ellipse(10, 30, 14, 7, grass2)
out.ellipse(50, 31, 12, 6, grass2)

out.rect(0, 46, w, h - 46, road)
out.rect(0, 46, w, 2, road2)
for x in range(2, w, 10):
    out.rect(x, 55, 5, 2, dash)
out.rect(0, 49, w, 1, white)
out.rect(0, 61, w, 1, white)

print(out.stats_text())
view(out)
save('motorcycle_road', out)
finish(out)
