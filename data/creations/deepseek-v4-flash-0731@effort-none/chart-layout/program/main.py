from pixelbench_api import *

# 128x64 pixel art bar chart
c = new_canvas(128, 64, background=None, name="chart")

# Background
c.rect(0, 0, 128, 64, "#1a1a2e")

# Fruit colors
apple_color = "#e74c3c"    # red apple
apple_leaf = "#27ae60"     # green leaf
banana_color = "#f1c40f"   # yellow
banana_tip = "#8f7a1f"     # darker banana tip
orange_color = "#e67e22"   # orange
lemon_color = "#f9e74a"    # light yellow lemon
lemon_tip = "#8f7a1f"
grape_color = "#8e44ad"    # purple
grape_leaf = "#2ecc71"     # green leaf
stem_color = "#5d4037"     # brown

# Title
c.text(3, 3, "FRUIT DATA", "#ffffff", font="5x7")

# Chart background
c.rect(1, 11, 126, 50, "#16213e")

# Grid lines at value positions (0,2,4,6,8,10,12,14)
grid_color = "#1e2f52"
for v in [0, 2, 4, 6, 8, 10, 12, 14]:
    gx = 18 + int(v * 100 / 14)
    c.line(gx, 12, gx, 60, grid_color)

# Horizontal separators between rows
for gy in [20, 30, 40, 50]:
    c.line(8, gy, 127, gy, grid_color)

# === Fruit icons ===
# Icons positioned at x=2..15, bars start at x=18

# --- Apple icon: simple red apple with leaf (8x8) ---
def draw_apple_icon(x, y):
    # Stem
    c.set(x+3, y, stem_color)
    c.set(x+4, y, stem_color)
    # Leaf (small green leaf on top right)
    c.set(x+5, y, apple_leaf)
    c.set(x+6, y+1, apple_leaf)
    # Body
    c.set(x+2, y+1, apple_color)
    c.set(x+3, y+1, apple_color)
    c.set(x+4, y+1, apple_color)
    c.set(x+5, y+1, apple_color)
    c.set(x+1, y+2, apple_color)
    c.set(x+2, y+2, apple_color)
    c.set(x+3, y+2, apple_color)
    c.set(x+4, y+2, apple_color)
    c.set(x+5, y+2, apple_color)
    c.set(x+6, y+2, apple_color)
    # Lower body
    c.set(x+0, y+3, apple_color)
    c.set(x+1, y+3, apple_color)
    c.set(x+2, y+3, apple_color)
    c.set(x+5, y+3, apple_color)
    c.set(x+6, y+3, apple_color)
    c.set(x+7, y+3, apple_color)
    c.set(x+0, y+4, apple_color)
    c.set(x+1, y+4, apple_color)
    c.set(x+2, y+4, apple_color)
    c.set(x+5, y+4, apple_color)
    c.set(x+6, y+4, apple_color)
    c.set(x+7, y+4, apple_color)
    c.set(x+1, y+5, apple_color)
    c.set(x+2, y+5, apple_color)
    c.set(x+3, y+5, apple_color)
    c.set(x+4, y+5, apple_color)
    c.set(x+5, y+5, apple_color)
    c.set(x+6, y+5, apple_color)
    c.set(x+2, y+6, apple_color)
    c.set(x+3, y+6, apple_color)
    c.set(x+4, y+6, apple_color)
    c.set(x+5, y+6, apple_color)
    c.set(x+3, y+7, apple_color)
    c.set(x+4, y+7, apple_color)

# --- Banana icon: clear crescent (8x8) ---
def draw_banana_icon(x, y):
    # Stem tip
    c.set(x+7, y, banana_tip)
    c.set(x+7, y+1, banana_tip)
    # Banana curve - outer arch
    c.set(x+6, y+1, banana_color)
    c.set(x+5, y+2, banana_color)
    c.set(x+4, y+3, banana_color)
    c.set(x+3, y+4, banana_color)
    c.set(x+2, y+5, banana_color)
    c.set(x+1, y+5, banana_color)
    c.set(x+1, y+6, banana_tip)
    # Fill inner
    c.set(x+6, y+2, banana_color)
    c.set(x+6, y+3, banana_color)
    c.set(x+5, y+3, banana_color)
    c.set(x+5, y+4, banana_color)
    c.set(x+4, y+4, banana_color)
    c.set(x+3, y+5, banana_color)
    c.set(x+2, y+6, banana_color)
    c.set(x+2, y+4, banana_color)
    # Inner shadow edge
    c.set(x+6, y+4, banana_color)
    c.set(x+7, y+2, banana_tip)
    c.set(x+3, y+6, banana_tip)
    c.set(x+2, y+7, banana_tip)

# --- Orange icon: circle with leaf (8x7) ---
def draw_orange_icon(x, y):
    # Leaf
    c.set(x+5, y, apple_leaf)
    c.set(x+6, y+1, apple_leaf)
    # Circle body
    c.set(x+2, y+1, orange_color)
    c.set(x+3, y+1, orange_color)
    c.set(x+4, y+1, orange_color)
    c.set(x+5, y+1, orange_color)
    c.set(x+1, y+2, orange_color)
    c.set(x+2, y+2, orange_color)
    c.set(x+5, y+2, orange_color)
    c.set(x+6, y+2, orange_color)
    c.set(x+0, y+3, orange_color)
    c.set(x+1, y+3, orange_color)
    c.set(x+6, y+3, orange_color)
    c.set(x+7, y+3, orange_color)
    c.set(x+0, y+4, orange_color)
    c.set(x+1, y+4, orange_color)
    c.set(x+6, y+4, orange_color)
    c.set(x+7, y+4, orange_color)
    c.set(x+1, y+5, orange_color)
    c.set(x+2, y+5, orange_color)
    c.set(x+5, y+5, orange_color)
    c.set(x+6, y+5, orange_color)
    c.set(x+2, y+6, orange_color)
    c.set(x+3, y+6, orange_color)
    c.set(x+4, y+6, orange_color)
    c.set(x+5, y+6, orange_color)
    # Star/bottom
    c.set(x+3, y+7, orange_color)
    c.set(x+4, y+7, orange_color)

# --- Lemon icon: oval (8x7) ---
def draw_lemon_icon(x, y):
    # Small stem
    c.set(x+3, y, lemon_tip)
    c.set(x+4, y, lemon_tip)
    # Body
    c.set(x+2, y+1, lemon_color)
    c.set(x+3, y+1, lemon_color)
    c.set(x+4, y+1, lemon_color)
    c.set(x+5, y+1, lemon_color)
    c.set(x+1, y+2, lemon_color)
    c.set(x+2, y+2, lemon_color)
    c.set(x+5, y+2, lemon_color)
    c.set(x+6, y+2, lemon_color)
    c.set(x+1, y+3, lemon_color)
    c.set(x+2, y+3, lemon_color)
    c.set(x+5, y+3, lemon_color)
    c.set(x+6, y+3, lemon_color)
    c.set(x+1, y+4, lemon_color)
    c.set(x+2, y+4, lemon_color)
    c.set(x+5, y+4, lemon_color)
    c.set(x+6, y+4, lemon_color)
    c.set(x+2, y+5, lemon_color)
    c.set(x+3, y+5, lemon_color)
    c.set(x+4, y+5, lemon_color)
    c.set(x+5, y+5, lemon_color)
    c.set(x+3, y+6, lemon_color)
    c.set(x+4, y+6, lemon_color)

# --- Grape icon: bunch of grapes (8x7) ---
def draw_grape_icon(x, y):
    # Leaf
    c.set(x+3, y, grape_leaf)
    c.set(x+4, y, grape_leaf)
    c.set(x+5, y, grape_leaf)
    c.set(x+2, y+1, grape_leaf)
    c.set(x+3, y+1, grape_leaf)
    c.set(x+4, y+1, grape_leaf)
    # Top berries
    c.set(x+1, y+2, grape_color)
    c.set(x+2, y+2, grape_color)
    c.set(x+3, y+2, grape_color)
    c.set(x+4, y+2, grape_color)
    c.set(x+5, y+2, grape_color)
    c.set(x+2, y+3, grape_color)
    c.set(x+3, y+3, grape_color)
    c.set(x+4, y+3, grape_color)
    c.set(x+5, y+3, grape_color)
    c.set(x+6, y+3, grape_color)
    c.set(x+1, y+4, grape_color)
    c.set(x+2, y+4, grape_color)
    c.set(x+4, y+4, grape_color)
    c.set(x+5, y+4, grape_color)
    c.set(x+2, y+5, grape_color)
    c.set(x+3, y+5, grape_color)
    c.set(x+4, y+5, grape_color)
    c.set(x+5, y+5, grape_color)
    c.set(x+3, y+6, grape_color)
    c.set(x+4, y+6, grape_color)

# Draw icons at left side
draw_apple_icon(4, 12)
draw_banana_icon(4, 22)
draw_orange_icon(4, 32)
draw_lemon_icon(4, 42)
draw_grape_icon(4, 52)

# Bars (horizontal), x from 18, height 4px within each row
scale_factor = 100.0 / 14.0  # 14 -> 100px

# Apple: value 10
apple_w = int(10 * scale_factor)
c.rect(18, 15, apple_w, 4, apple_color)

# Banana: value 5
banana_w = int(5 * scale_factor)
c.rect(18, 25, banana_w, 4, banana_color)

# Orange: value 7
orange_w = int(7 * scale_factor)
c.rect(18, 35, orange_w, 4, orange_color)

# Lemon: value 14
lemon_w = int(14 * scale_factor)
c.rect(18, 45, lemon_w, 4, lemon_color)

# Grape: value 2
grape_w = int(2 * scale_factor)
c.rect(18, 55, grape_w, 4, grape_color)

# Axis line
c.line(18, 12, 18, 60, "#4a6fa5")

# Value labels at the end of each bar
c.text(90, 15, "10", "#ffffff", font="5x7")
c.text(55, 25, "5", "#ffffff", font="5x7")
c.text(69, 35, "7", "#ffffff", font="5x7")
c.text(100, 45, "14", "#ffffff", font="5x7")
c.text(33, 55, "2", "#ffffff", font="5x7")

print(c.stats_text())

finish(c)
