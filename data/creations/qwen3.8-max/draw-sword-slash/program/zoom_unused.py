src = open('main.py').read().replace('finish([f1, f2])', '')
exec(compile(src, 'main_inline', 'exec'), globals())

zoom = new_canvas(46, 40, name="zoom")
zoom.blit(f2, -62, -14)  # region x62..107, y14..53
view(zoom, scale=10, margin=0)
