from pixelbench_api import *

# reload the drawing state that main.py produced is not persisted; instead rebuild by importing main's code is heavy.
# Simplest: re-run construction in this file by exec'ing main.py source, then print regions.
src = open("main.py").read()
# strip the finish call so nothing is declared here
src = src.replace("finish(c)", "pass")
src = src.replace('print(c.stats_text())', 'pass')
exec(src)

print("=== WALL/DOOR/GLOW (30,58)-(100,96) ===")
print(c.matrix_text((30,58,99,95)))
print("=== ROOF TOP (40,40)-(100,66) ===")
print(c.matrix_text((40,40,99,65)))
