from pixelbench_api import *

c = new_canvas(64, 64, background="#d8e4ea", name="lab")

WALL = "#d8e4ea"
WALL2 = "#c3d3dc"
BENCH = "#b98a5a"
BENCH_D = "#96693f"
BENCH_L = "#d0a374"
OUT = "#2b2b33"

# wall panel line
c.rect(0, 0, 64, 40, WALL)
c.rect(0, 36, 64, 4, WALL2)
c.rect(0, 38, 64, 2, "#8fa3ae")

# bench top (y 40..64)
c.rect(0, 40, 64, 8, BENCH)
c.rect(0, 40, 64, 1, BENCH_L)
c.rect(0, 47, 64, 1, BENCH_D)
c.rect(0, 48, 64, 16, BENCH_D)
c.rect(0, 48, 64, 2, "#7d5530")

# ---- microscope (left, biggest object) ----
# base
c.rect(8, 52, 16, 3, "#3a3f4a")
c.rect(8, 55, 16, 1, "#22252c")
# arm curve
c.line(20, 52, 20, 40, "#4a505e")
c.line(21, 52, 21, 40, "#4a505e")
c.line(22, 44, 22, 40, "#4a505e")
c.line(20, 40, 22, 40, "#4a505e")
# stage
c.rect(12, 44, 9, 2, "#5a6170")
c.rect(13, 46, 7, 1, "#3a3f4a")
# slide
c.rect(14, 43, 6, 1, "#9fd8e8")
# body tube + eyepiece
c.rect(15, 33, 5, 4, "#4a505e")
c.rect(16, 30, 3, 3, "#2f333c")
c.rect(16, 29, 3, 1, "#8fd0e0")
# objective lens
c.rect(16, 37, 3, 3, "#2f333c")
c.rect(17, 40, 1, 4, "#2f333c")
c.set(17, 44, "#8fd0e0")
# focus knob
c.circle(24, 47, 1, "#8892a3")
# light mirror under stage
c.set(17, 50, "#f2e6a0")

# ---- test-tube rack (right of microscope) ----
# rack base and back
c.rect(30, 50, 14, 2, "#c9a06a")
c.rect(30, 44, 14, 1, "#c9a06a")
c.rect(30, 45, 1, 5, "#c9a06a")
c.rect(43, 45, 1, 5, "#c9a06a")
# tubes (x centers 33,37,41)
for i, (x, liquid) in enumerate([(33, "#6ec46e"), (37, "#e0b040"), (41, "#d05a6a")]):
    c.rect(x, 42, 3, 9, "#bfe6f0")       # glass
    c.rect(x, 46, 3, 5, liquid)          # liquid
    c.set(x, 42, "#dff5fa")
    c.set(x + 2, 42, "#9fd4e2")
    c.set(x, 51, "#dff5fa")
# rack front lip
c.rect(30, 51, 14, 1, "#a87f4c")

# ---- labeled bottles (right side) ----
# big reagent bottle
c.rect(48, 42, 8, 11, "#7fae7a")
c.rect(48, 42, 2, 11, "#5f8f5c")
c.rect(50, 39, 4, 3, "#5f8f5c")          # neck
c.rect(49, 38, 6, 1, "#3f6f3e")          # cap
# label band
c.rect(48, 46, 8, 4, "#f2eee0")
c.line(49, 47, 55, 47, "#555555")
c.line(49, 49, 55, 49, "#555555")
c.line(49, 48, 52, 48, "#888888")

# small flask/beaker
c.rect(58, 46, 5, 7, "#cfe8f0")
c.rect(58, 50, 5, 3, "#8a7fd0")
c.rect(58, 46, 1, 7, "#e8f6fa")
c.rect(57, 45, 7, 1, "#cfe8f0")

# ---- dropper (leaning, front-center) ----
c.line(27, 40, 30, 53, "#e8e8f0")
c.line(28, 40, 31, 53, "#e8e8f0")
c.rect(26, 38, 3, 3, "#d05a6a")          # rubber bulb
c.rect(30, 53, 2, 2, "#8fd0e0")          # tip liquid

# ---- open laboratory notebook (front, center-bottom) ----
c.rect(6, 56, 24, 8, "#f5f2e8")          # pages
c.rect(6, 56, 24, 1, "#ffffff")
c.rect(17, 56, 1, 8, "#d8d4c4")          # spine
c.rect(5, 56, 1, 8, "#b06040")           # left cover edge
c.rect(30, 56, 1, 8, "#b06040")          # right cover edge
# ruled lines
for yy in (58, 60, 62):
    c.line(8, yy, 15, yy, "#9ab4c8")
    c.line(19, yy, 29, yy, "#9ab4c8")
# scribble "text" as short dashes (readable as writing, not tiny text)
c.line(9, 57, 14, 57, "#556070")
c.line(20, 57, 26, 57, "#556070")
# a small diagram on right page
c.circle(24, 61, 2, "#556070", fill=False)

# pencil on notebook
c.line(10, 62, 22, 59, "#e0a030")
c.line(10, 63, 22, 60, "#c08020")
c.set(23, 59, "#333333")

# ---- shelf detail on wall: hanging chart ----
c.rect(50, 8, 10, 14, "#f2eee0")
c.rect(50, 8, 10, 1, "#b06040")
c.line(52, 12, 58, 12, "#8898a8")
c.line(52, 15, 58, 15, "#8898a8")
c.line(52, 18, 56, 18, "#8898a8")

# dark outline pass: outline the bench front bottom
c.rect(0, 63, 64, 1, "#5f3f22")

print(c.stats_text())
save("lab_workbench", c)
finish(c)
