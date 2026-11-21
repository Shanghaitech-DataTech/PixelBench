from pixelbench_api import new_canvas, finish

W, H = 128, 64
c = new_canvas(W, H)

# Background
WHITE = "#f7f3ea"
c.rect(0, 0, W, H, WHITE)

# Colors by fruit
RED    = "#e53935"
YELLOW = "#fdd835"
ORANGE = "#fb8c00"
LIME   = "#c0ca33"
PURPLE = "#8e24aa"
BROWN  = "#6d4c41"

# (name, value, color)
data = [
    ("apple",  10, RED),
    ("banana", 5,  YELLOW),
    ("orange", 7,  ORANGE),
    ("lemon",  14, LIME),
    ("grape",  2,  PURPLE),
]

SCALE = 7     # pixels per unit
BAR_H = 8
X0 = 17       # bars start here

def hr(x0, y0, row, cols, col):
    for i, v in enumerate(cols):
        if v:
            c.set(x0+i, y0+row, col)

def icon_apple(ix, iy):
    ix -= 1; iy -= 1
    hr(ix,iy,0,[0,0,1,1,1,1,0,0],BROWN)
    hr(ix,iy,1,[0,1,1,1,1,1,0,0],BROWN)
    hr(ix,iy,2,[1,1,1,1,1,1,1,1],RED)
    hr(ix,iy,3,[1,1,1,1,1,1,1,1],RED)
    hr(ix,iy,4,[1,1,1,1,1,1,1,1],RED)
    c.set(ix+2, iy+3, "#ffeeee")
    hr(ix,iy,5,[1,1,1,1,1,1,1,1],RED)
    hr(ix,iy,6,[1,1,1,1,1,1,1,1],RED)
    hr(ix,iy,7,[0,1,1,1,1,1,1,0],RED)
    hr(ix,iy,8,[0,0,1,1,1,1,0,0],RED)

def icon_banana(ix, iy):
    ix -= 1; iy -= 1
    hr(ix,iy,0,[0,0,0,1,1,1,1,0],YELLOW)
    hr(ix,iy,1,[0,0,1,1,1,1,1,1],YELLOW)
    hr(ix,iy,2,[0,1,1,1,1,1,0,0],YELLOW)
    hr(ix,iy,3,[0,1,1,1,1,0,0,0],YELLOW)
    hr(ix,iy,4,[0,1,1,1,1,0,0,0],YELLOW)
    hr(ix,iy,5,[0,0,1,1,1,0,0,0],YELLOW)
    hr(ix,iy,6,[0,0,0,1,1,0,0,0],YELLOW)
    c.set(ix+1, iy+3, BROWN)

def icon_orange(ix, iy):
    ix -= 1; iy -= 1
    c.set(ix+3, iy, "#2e7d32")
    hr(ix,iy,1,[0,1,1,1,1,1,1,0],ORANGE)
    hr(ix,iy,2,[1,1,1,1,1,1,1,1],ORANGE)
    hr(ix,iy,3,[1,1,1,1,1,1,1,1],ORANGE)
    hr(ix,iy,4,[1,1,1,1,1,1,1,1],ORANGE)
    c.set(ix+2, iy+2, "#ffe0b2")
    hr(ix,iy,5,[1,1,1,1,1,1,1,1],ORANGE)
    hr(ix,iy,6,[0,1,1,1,1,1,1,0],ORANGE)
    hr(ix,iy,7,[0,0,1,1,1,1,0,0],ORANGE)

def icon_lemon(ix, iy):
    ix -= 1; iy -= 1
    c.set(ix+3, iy, "#2e7d32")
    hr(ix,iy,1,[0,1,1,1,1,1,1,0],LIME)
    hr(ix,iy,2,[1,1,1,1,1,1,1,1],LIME)
    hr(ix,iy,3,[1,1,1,1,1,1,1,1],LIME)
    c.set(ix+5, iy+2, "#f0f4c3")
    hr(ix,iy,4,[1,1,1,1,1,1,1,1],LIME)
    hr(ix,iy,5,[0,1,1,1,1,1,1,0],LIME)
    hr(ix,iy,6,[0,0,1,1,1,1,0,0],LIME)

def icon_grape(ix, iy):
    ix -= 1; iy -= 1
    c.set(ix+2, iy+0, "#2e7d32")
    c.set(ix+4, iy+0, "#2e7d32")
    hr(ix,iy,1,[0,1,1,1,1,0,0,0],PURPLE)
    hr(ix,iy,2,[1,1,1,1,1,1,0,0],PURPLE)
    hr(ix,iy,3,[1,1,1,1,1,1,0,0],PURPLE)
    hr(ix,iy,4,[0,1,1,1,1,1,0,0],PURPLE)
    hr(ix,iy,5,[0,0,1,1,1,0,0,0],PURPLE)
    c.set(ix+2, iy+2, "#ce93d8")

icons = [icon_apple, icon_banana, icon_orange, icon_lemon, icon_grape]

# Rows
y_top = 3
for i, (name, val, col) in enumerate(data):
    y = y_top + i * 12
    icons[i](6, y + 5)
    # value bar
    c.rect(X0, y, max(val * SCALE, 2), BAR_H, col)
    # subtle bar shading bottom
    c.rect(X0, y + BAR_H - 2, max(val * SCALE, 2), 2, "#00000022")
    # baseline
    c.set(X0 - 1, y + BAR_H - 1, "#c9c0ae")

# X axis baseline
c.line(X0 - 1, y_top + 4 * 12 + BAR_H - 1, X0 - 1, y_top - 2, "#c9c0ae")

print(c.stats_text())
finish(c)
