from pixelbench_api import *
src = open('main.py').read()
src = src.replace("print(c.stats_text())", "").replace("view(c)", "").replace("finish(c)", "")
exec(src)
nc = new_canvas(150, 112, name="zoom_dragon")
nc.blit(c, -92, -28)
view(nc, scale=4)
