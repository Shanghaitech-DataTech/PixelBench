from pixelbench_api import *

c = new_canvas(64, 64, name="laundromat")
C = {}
def col(k, hexv):
    C[k] = c.color(hexv)

col("CEIL", "#e2eaf2"); col("LGHT", "#f4faff"); col("GLOW", "#d7e5f1")
col("WALL", "#c6d3e0"); col("WALLS", "#a9bdcd"); col("BASE", "#5b6f83")
col("FLOOR", "#93a9bb"); col("FLOOR2", "#7f96aa"); col("FLOORD", "#6b8195")
col("MW", "#f6f9fc"); col("MS", "#ccd8e3")
col("PANEL", "#3c5266"); col("PANEL2", "#2b3d4e")
col("GLASS", "#1b2f40"); col("GLASSH", "#82a3c0"); col("SOAP", "#d7e6f2")
col("RING", "#b2c3d3"); col("RING2", "#8ba1b5")
col("KNOB", "#eef3f8"); col("LED", "#e0564f")
col("CLK", "#f8fbfd"); col("CLKR", "#31414f"); col("HAND", "#20303e")
col("BASK", "#e28a4c"); col("BASKS", "#c06a2c"); col("DARK", "#5a3d2b")
col("SHIRT", "#d9574e"); col("TOWEL", "#5fa860")
col("TAB", "#b6c5d2"); col("TABS", "#8fa3b4")
col("FOLD", "#f2eedb"); col("FOLDS", "#cfc5a8")

# ---- room shell ----
c.rect(0, 0, 64, 8, C["CEIL"])
c.rect(8, 0, 48, 2, C["PANEL2"])
c.rect(12, 2, 40, 2, C["LGHT"])
c.rect(16, 2, 32, 1, C["LGHT"])
c.rect(0, 8, 64, 32, C["WALL"])
c.rect(0, 8, 64, 5, C["GLOW"])
c.rect(0, 36, 64, 3, C["WALLS"])
c.rect(0, 39, 64, 2, C["BASE"])
c.rect(0, 41, 64, 23, C["FLOOR"])

# light pool on the floor under the fixture
c.rect(27, 42, 10, 6, C["GLOW"])

# floor tile grid
for yy in (47, 53, 59):
    c.line(0, yy, 63, yy, C["FLOOR2"])
for xx in (8, 16, 24, 32, 40, 48, 56):
    c.line(xx, 41, xx, 63, C["FLOOR2"])
c.rect(0, 60, 64, 3, C["FLOORD"])

# ---- washing machines: two rows ----
def machine(x, running=False):
    # body
    c.rect(x, 13, 12, 30, C["MW"])      # y13..42
    c.rect(x + 11, 13, 1, 29, C["MS"])
    # control panel
    c.rect(x, 13, 12, 6, C["PANEL"])
    c.rect(x, 13, 12, 1, C["PANEL2"])
    c.rect(x + 2, 15, 2, 1, C["KNOB"])
    c.set(x + 5, 15, C["LED"])
    c.rect(x + 7, 15, 2, 1, C["KNOB"])
    # front door
    c.circle(x + 5, 36, 6, C["RING"])
    if running:
        c.circle(x + 5, 36, 4, C["SOAP"])
        c.set(x + 6, 35, C["TOWEL"]); c.set(x + 8, 37, C["TOWEL"]); c.set(x + 7, 38, C["SHIRT"])
        c.set(x + 3, 34, C["GLASSH"])
    else:
        c.circle(x + 5, 36, 4, C["GLASS"])
        c.set(x + 2, 33, C["GLASSH"]); c.set(x + 3, 34, C["GLASSH"]); c.set(x + 2, 35, C["GLASSH"])
    c.circle(x + 5, 38, 1, C["RING2"])
    # base
    c.rect(x, 41, 12, 2, C["BASE"])

machine(2)
machine(16)
machine(35, running=True)
machine(50)

# grounding shadows under machines
for sx in (2, 16, 35, 50):
    c.rect(sx, 43, 12, 2, C["FLOORD"])

# ---- wall clock between the rows ----
c.circle(31, 22, 3, C["CLKR"])
c.circle(31, 22, 2, C["CLK"])
c.line(31, 22, 31, 19, C["HAND"])
c.set(32, 21, C["HAND"])

# ---- laundry basket (left side, in front) ----
c.rect(13, 43, 10, 2, C["SHIRT"])
c.set(15, 42, C["TOWEL"]); c.set(17, 42, C["TOWEL"])
c.set(19, 43, C["SHIRT"])
c.rect(9, 45, 18, 2, C["BASK"])
c.rect(11, 47, 14, 2, C["DARK"])
c.rect(10, 49, 16, 9, C["BASK"])
c.rect(13, 49, 1, 9, C["BASKS"])
c.rect(17, 49, 1, 9, C["BASKS"])
c.rect(21, 49, 1, 9, C["BASKS"])

# ---- folding table (right side, in front) ----
c.rect(39, 47, 3, 14, C["TAB"])
c.rect(56, 47, 3, 14, C["TAB"])
c.rect(37, 44, 25, 4, C["TAB"])
c.rect(37, 46, 25, 2, C["TABS"])

# folded laundry on the table
c.rect(42, 40, 14, 4, C["FOLD"])
c.rect(43, 41, 12, 1, C["FOLDS"])
c.set(45, 41, C["TOWEL"]); c.set(50, 41, C["TOWEL"])

print(c.stats_text())
print(c.canvas if False else c.stats())
finish(c)
