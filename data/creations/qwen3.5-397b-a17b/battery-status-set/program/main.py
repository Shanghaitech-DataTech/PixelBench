from pixelbench_api import new_canvas, finish

# Create 64x64 canvas
c = new_canvas(64, 64, background=None)

# Define colors
c.color("#2d2d2d", name="outline")      # Dark gray for outline
c.color("#4a4a4a", name="terminal")      # Slightly lighter for terminal
c.color("#4CAF50", name="full")          # Green for 100%
c.color("#8BC34A", name="medium")        # Light green for 60%
c.color("#FFC107", name="low")           # Yellow/amber for 20%
c.color("#2196F3", name="charging")      # Blue for charging indicator

# Battery dimensions
# Body: 10 wide x 6 tall
# Terminal: 2 wide x 3 tall, centered vertically
battery_body_w = 10
battery_body_h = 6
terminal_w = 2
terminal_h = 3

# Positions for 4 batteries (x, y)
# Total width per battery slot: 14 pixels (10 body + 2 terminal + 2 gap)
# Starting x positions: 2, 16, 30, 44
# Centered vertically: (64 - 6) / 2 = 29
batteries = [
    {"x": 2, "y": 29, "fill": "full", "level": 1.0},
    {"x": 16, "y": 29, "fill": "medium", "level": 0.6},
    {"x": 30, "y": 29, "fill": "low", "level": 0.2},
    {"x": 44, "y": 29, "fill": "charging", "level": 0.5},
]

def draw_battery_outline(canvas, bx, by):
    """Draw the battery outline (body + terminal)"""
    # Battery body outline (hollow rectangle)
    # Top edge
    canvas.line(bx, by, bx + battery_body_w - 1, by, "outline")
    # Bottom edge
    canvas.line(bx, by + battery_body_h - 1, bx + battery_body_w - 1, by + battery_body_h - 1, "outline")
    # Left edge
    canvas.line(bx, by, bx, by + battery_body_h - 1, "outline")
    # Right edge (partial, for terminal gap)
    # Top part of right edge (above terminal)
    canvas.set(bx + battery_body_w - 1, by, "outline")
    canvas.set(bx + battery_body_w - 1, by + 1, "outline")
    # Bottom part of right edge (below terminal)
    canvas.set(bx + battery_body_w - 1, by + 4, "outline")
    canvas.set(bx + battery_body_w - 1, by + 5, "outline")
    
    # Terminal (filled)
    tx = bx + battery_body_w  # terminal starts right after body
    ty = by + 1  # centered: (6-3)/2 = 1.5, round to 1
    canvas.rect(tx, ty, terminal_w, terminal_h, "terminal", fill=True)

def draw_battery_fill(canvas, bx, by, fill_type, level):
    """Draw the battery fill based on type and level"""
    # Fill area: inside the body, from left edge
    # Inner fill area: bx+1 to bx+8 (8 pixels wide), by+1 to by+4 (4 pixels tall)
    fill_start_x = bx + 1
    fill_end_x = bx + 8  # inclusive
    fill_top = by + 1
    fill_bottom = by + 4  # inclusive
    fill_width = 8
    fill_height = 4
    
    if fill_type == "full":
        # Fill entire battery
        color = "full"
        canvas.rect(fill_start_x, fill_top, fill_width, fill_height, color, fill=True)
    elif fill_type == "medium":
        # Fill 60% - about 5 of 8 pixels
        color = "medium"
        fill_pixels = int(fill_width * level)  # 8 * 0.6 = 4.8 -> 4 or 5
        fill_pixels = max(1, fill_pixels)
        canvas.rect(fill_start_x, fill_top, fill_pixels, fill_height, color, fill=True)
    elif fill_type == "low":
        # Fill 20% - about 1-2 of 8 pixels
        color = "low"
        fill_pixels = max(1, int(fill_width * level))  # 8 * 0.2 = 1.6 -> 1 or 2
        canvas.rect(fill_start_x, fill_top, fill_pixels, fill_height, color, fill=True)
    elif fill_type == "charging":
        # Half fill with lightning bolt
        color = "charging"
        # Fill bottom half (2 rows)
        canvas.rect(fill_start_x, by + 3, fill_width, 2, color, fill=True)
        
        # Draw lightning bolt in center
        # Lightning bolt: zigzag shape
        center_x = bx + 5
        bolt_top = by + 1
        bolt_bottom = by + 4
        
        # Simple lightning: diagonal down-right, then down-left, then down-right
        # Using set for pixel art lightning
        canvas.set(center_x, bolt_top, "charging")
        canvas.set(center_x + 1, bolt_top + 1, "charging")
        canvas.set(center_x, bolt_top + 1, "charging")
        canvas.set(center_x - 1, bolt_top + 2, "charging")
        canvas.set(center_x, bolt_top + 2, "charging")
        canvas.set(center_x + 1, bolt_top + 3, "charging")
        canvas.set(center_x, bolt_top + 3, "charging")

# Draw all batteries
for bat in batteries:
    draw_battery_outline(c, bat["x"], bat["y"])
    draw_battery_fill(c, bat["x"], bat["y"], bat["fill"], bat["level"])

# Check stats
print(c.stats_text())
print(c.matrix_text())

# Submit
finish(c)
