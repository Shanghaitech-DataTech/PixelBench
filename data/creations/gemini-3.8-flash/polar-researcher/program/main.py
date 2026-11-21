from pixelbench_api import *
from build_researcher import build_polar_researcher

c = new_canvas(48, 48, name="polar_researcher")
build_polar_researcher(c)

print(c.stats_text())
finish(c)
