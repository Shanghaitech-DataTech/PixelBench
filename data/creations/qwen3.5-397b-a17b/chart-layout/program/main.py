from pixelbench_api import new_canvas, finish

# Create canvas
c = new_canvas(128, 64, background=None)

# Define colors
RED = c.color("#e53935", "apple_red")
YELLOW = c.color("#fdd835", "banana_yellow")
ORANGE = c.color("#fb8c00", "orange_orange")
LEMON_YELLOW = c.color("#fff176", "lemon_yellow")
PURPLE = c.color("#8e24aa", "grape_purple")
GREEN = c.color("#43a047", "leaf_green")
BROWN = c.color("#795548", "stem_brown")
DARK_PURPLE = c.color("#5e35b1", "grape_dark")

# Fruit data
fruits = [
    {"name": "apple", "value": 10, "color": RED},
    {"name": "banana", "value": 5, "color": YELLOW},
    {"name": "orange", "value": 7, "color": ORANGE},
    {"name": "lemon", "value": 14, "color": LEMON_YELLOW},
    {"name": "grape", "value": 2, "color": PURPLE},
]

# Layout constants
ICON_X = 2
ICON_SIZE = 12
BAR_X = ICON_X + ICON_SIZE + 2  # 16
BAR_WIDTH = 110
Y_START = 4
ROW_HEIGHT = 10
BAR_HEIGHT_MAX = 8  # space for each bar

# Max value for scaling
max_value = 14
scale = BAR_HEIGHT_MAX / max_value  # pixels per unit

# Draw mini pixel art icons and bars for each fruit
for i, fruit in enumerate(fruits):
    y = Y_START + i * ROW_HEIGHT
    
    # Draw mini icon at (ICON_X, y)
    icon_x = ICON_X
    icon_y = y + 1  # center in row
    
    color = fruit["color"]
    
    if fruit["name"] == "apple":
        # Apple: round red shape with small stem
        c.set(icon_x + 4, icon_y, color)
        c.set(icon_x + 5, icon_y, color)
        c.set(icon_x + 6, icon_y, color)
        c.set(icon_x + 7, icon_y, color)
        c.set(icon_x + 3, icon_y + 1, color)
        c.set(icon_x + 4, icon_y + 1, color)
        c.set(icon_x + 5, icon_y + 1, color)
        c.set(icon_x + 6, icon_y + 1, color)
        c.set(icon_x + 7, icon_y + 1, color)
        c.set(icon_x + 8, icon_y + 1, color)
        c.set(icon_x + 2, icon_y + 2, color)
        c.set(icon_x + 3, icon_y + 2, color)
        c.set(icon_x + 4, icon_y + 2, color)
        c.set(icon_x + 5, icon_y + 2, color)
        c.set(icon_x + 6, icon_y + 2, color)
        c.set(icon_x + 7, icon_y + 2, color)
        c.set(icon_x + 8, icon_y + 2, color)
        c.set(icon_x + 9, icon_y + 2, color)
        c.set(icon_x + 2, icon_y + 3, color)
        c.set(icon_x + 3, icon_y + 3, color)
        c.set(icon_x + 4, icon_y + 3, color)
        c.set(icon_x + 5, icon_y + 3, color)
        c.set(icon_x + 6, icon_y + 3, color)
        c.set(icon_x + 7, icon_y + 3, color)
        c.set(icon_x + 8, icon_y + 3, color)
        c.set(icon_x + 9, icon_y + 3, color)
        c.set(icon_x + 3, icon_y + 4, color)
        c.set(icon_x + 4, icon_y + 4, color)
        c.set(icon_x + 5, icon_y + 4, color)
        c.set(icon_x + 6, icon_y + 4, color)
        c.set(icon_x + 7, icon_y + 4, color)
        c.set(icon_x + 8, icon_y + 4, color)
        c.set(icon_x + 5, icon_y - 1, BROWN)  # stem
        c.set(icon_x + 6, icon_y - 1, BROWN)
        c.set(icon_x + 5, icon_y - 2, GREEN)  # leaf
        c.set(icon_x + 6, icon_y - 2, GREEN)
        
    elif fruit["name"] == "banana":
        # Banana: curved yellow shape
        c.set(icon_x + 4, icon_y, YELLOW)
        c.set(icon_x + 5, icon_y, YELLOW)
        c.set(icon_x + 6, icon_y, YELLOW)
        c.set(icon_x + 3, icon_y + 1, YELLOW)
        c.set(icon_x + 4, icon_y + 1, YELLOW)
        c.set(icon_x + 5, icon_y + 1, YELLOW)
        c.set(icon_x + 6, icon_y + 1, YELLOW)
        c.set(icon_x + 7, icon_y + 1, YELLOW)
        c.set(icon_x + 2, icon_y + 2, YELLOW)
        c.set(icon_x + 3, icon_y + 2, YELLOW)
        c.set(icon_x + 4, icon_y + 2, YELLOW)
        c.set(icon_x + 5, icon_y + 2, YELLOW)
        c.set(icon_x + 6, icon_y + 2, YELLOW)
        c.set(icon_x + 7, icon_y + 2, YELLOW)
        c.set(icon_x + 8, icon_y + 2, YELLOW)
        c.set(icon_x + 2, icon_y + 3, BROWN)
        c.set(icon_x + 3, icon_y + 3, YELLOW)
        c.set(icon_x + 4, icon_y + 3, YELLOW)
        c.set(icon_x + 5, icon_y + 3, YELLOW)
        c.set(icon_x + 6, icon_y + 3, YELLOW)
        c.set(icon_x + 7, icon_y + 3, YELLOW)
        c.set(icon_x + 8, icon_y + 3, BROWN)
        c.set(icon_x + 3, icon_y + 4, BROWN)
        c.set(icon_x + 4, icon_y + 4, YELLOW)
        c.set(icon_x + 5, icon_y + 4, YELLOW)
        c.set(icon_x + 6, icon_y + 4, YELLOW)
        c.set(icon_x + 7, icon_y + 4, BROWN)
        
    elif fruit["name"] == "orange":
        # Orange: circle with segments
        c.set(icon_x + 4, icon_y, ORANGE)
        c.set(icon_x + 5, icon_y, ORANGE)
        c.set(icon_x + 6, icon_y, ORANGE)
        c.set(icon_x + 7, icon_y, ORANGE)
        c.set(icon_x + 3, icon_y + 1, ORANGE)
        c.set(icon_x + 4, icon_y + 1, ORANGE)
        c.set(icon_x + 5, icon_y + 1, ORANGE)
        c.set(icon_x + 6, icon_y + 1, ORANGE)
        c.set(icon_x + 7, icon_y + 1, ORANGE)
        c.set(icon_x + 8, icon_y + 1, ORANGE)
        c.set(icon_x + 2, icon_y + 2, ORANGE)
        c.set(icon_x + 3, icon_y + 2, ORANGE)
        c.set(icon_x + 4, icon_y + 2, "#ff9800")  # lighter segment
        c.set(icon_x + 5, icon_y + 2, ORANGE)
        c.set(icon_x + 6, icon_y + 2, "#ff9800")
        c.set(icon_x + 7, icon_y + 2, ORANGE)
        c.set(icon_x + 8, icon_y + 2, ORANGE)
        c.set(icon_x + 9, icon_y + 2, ORANGE)
        c.set(icon_x + 2, icon_y + 3, ORANGE)
        c.set(icon_x + 3, icon_y + 3, ORANGE)
        c.set(icon_x + 4, icon_y + 3, ORANGE)
        c.set(icon_x + 5, icon_y + 3, "#ff9800")
        c.set(icon_x + 6, icon_y + 3, ORANGE)
        c.set(icon_x + 7, icon_y + 3, ORANGE)
        c.set(icon_x + 8, icon_y + 3, ORANGE)
        c.set(icon_x + 9, icon_y + 3, ORANGE)
        c.set(icon_x + 3, icon_y + 4, ORANGE)
        c.set(icon_x + 4, icon_y + 4, ORANGE)
        c.set(icon_x + 5, icon_y + 4, ORANGE)
        c.set(icon_x + 6, icon_y + 4, ORANGE)
        c.set(icon_x + 7, icon_y + 4, ORANGE)
        c.set(icon_x + 8, icon_y + 4, ORANGE)
        c.set(icon_x + 5, icon_y - 1, GREEN)  # leaf
        
    elif fruit["name"] == "lemon":
        # Lemon: oval yellow shape
        c.set(icon_x + 4, icon_y, LEMON_YELLOW)
        c.set(icon_x + 5, icon_y, LEMON_YELLOW)
        c.set(icon_x + 6, icon_y, LEMON_YELLOW)
        c.set(icon_x + 7, icon_y, LEMON_YELLOW)
        c.set(icon_x + 3, icon_y + 1, LEMON_YELLOW)
        c.set(icon_x + 4, icon_y + 1, LEMON_YELLOW)
        c.set(icon_x + 5, icon_y + 1, LEMON_YELLOW)
        c.set(icon_x + 6, icon_y + 1, LEMON_YELLOW)
        c.set(icon_x + 7, icon_y + 1, LEMON_YELLOW)
        c.set(icon_x + 8, icon_y + 1, LEMON_YELLOW)
        c.set(icon_x + 2, icon_y + 2, LEMON_YELLOW)
        c.set(icon_x + 3, icon_y + 2, LEMON_YELLOW)
        c.set(icon_x + 4, icon_y + 2, LEMON_YELLOW)
        c.set(icon_x + 5, icon_y + 2, LEMON_YELLOW)
        c.set(icon_x + 6, icon_y + 2, LEMON_YELLOW)
        c.set(icon_x + 7, icon_y + 2, LEMON_YELLOW)
        c.set(icon_x + 8, icon_y + 2, LEMON_YELLOW)
        c.set(icon_x + 9, icon_y + 2, LEMON_YELLOW)
        c.set(icon_x + 2, icon_y + 3, LEMON_YELLOW)
        c.set(icon_x + 3, icon_y + 3, LEMON_YELLOW)
        c.set(icon_x + 4, icon_y + 3, LEMON_YELLOW)
        c.set(icon_x + 5, icon_y + 3, LEMON_YELLOW)
        c.set(icon_x + 6, icon_y + 3, LEMON_YELLOW)
        c.set(icon_x + 7, icon_y + 3, LEMON_YELLOW)
        c.set(icon_x + 8, icon_y + 3, LEMON_YELLOW)
        c.set(icon_x + 9, icon_y + 3, LEMON_YELLOW)
        c.set(icon_x + 3, icon_y + 4, LEMON_YELLOW)
        c.set(icon_x + 4, icon_y + 4, LEMON_YELLOW)
        c.set(icon_x + 5, icon_y + 4, LEMON_YELLOW)
        c.set(icon_x + 6, icon_y + 4, LEMON_YELLOW)
        c.set(icon_x + 7, icon_y + 4, LEMON_YELLOW)
        c.set(icon_x + 8, icon_y + 4, LEMON_YELLOW)
        c.set(icon_x + 5, icon_y - 1, GREEN)
        c.set(icon_x + 6, icon_y - 1, GREEN)
        
    elif fruit["name"] == "grape":
        # Grapes: cluster of circles
        c.set(icon_x + 5, icon_y, PURPLE)
        c.set(icon_x + 6, icon_y, PURPLE)
        c.set(icon_x + 4, icon_y + 1, PURPLE)
        c.set(icon_x + 5, icon_y + 1, DARK_PURPLE)
        c.set(icon_x + 6, icon_y + 1, PURPLE)
        c.set(icon_x + 7, icon_y + 1, PURPLE)
        c.set(icon_x + 3, icon_y + 2, PURPLE)
        c.set(icon_x + 4, icon_y + 2, DARK_PURPLE)
        c.set(icon_x + 5, icon_y + 2, PURPLE)
        c.set(icon_x + 6, icon_y + 2, DARK_PURPLE)
        c.set(icon_x + 7, icon_y + 2, PURPLE)
        c.set(icon_x + 8, icon_y + 2, PURPLE)
        c.set(icon_x + 4, icon_y + 3, PURPLE)
        c.set(icon_x + 5, icon_y + 3, PURPLE)
        c.set(icon_x + 6, icon_y + 3, DARK_PURPLE)
        c.set(icon_x + 7, icon_y + 3, PURPLE)
        c.set(icon_x + 5, icon_y + 4, PURPLE)
        c.set(icon_x + 6, icon_y + 4, PURPLE)
        c.set(icon_x + 5, icon_y - 1, BROWN)
        c.set(icon_x + 6, icon_y - 1, BROWN)
        c.set(icon_x + 5, icon_y - 2, GREEN)
        c.set(icon_x + 6, icon_y - 2, GREEN)
    
    # Draw bar
    bar_height = int(fruit["value"] * scale)
    bar_y = y + 1 + BAR_HEIGHT_MAX - bar_height  # align bottom
    c.rect(BAR_X, bar_y, BAR_WIDTH, bar_height, color, fill=True)

# Check stats
print(c.stats_text())

# Print matrix for verification
print(c.matrix_text(region=(0, 0, 127, 55)))

finish(c)
