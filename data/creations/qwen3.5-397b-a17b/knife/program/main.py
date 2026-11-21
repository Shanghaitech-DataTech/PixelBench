from pixelbench_api import *

# Create the main canvas - make it slightly wider to avoid clipping
canvas = new_canvas(320, 200, name='main')

# Select and rotate the knife
sel = input_canvas.select(0, 0, 93, 128)
rotated_sel = sel.rotate(315, algorithm="rotsprite")
rotated_preview = rotated_sel.preview()

# The knife bbox is [3, 63, 153, 99]
# Position the main knife centered
main_knife_x = 120
main_knife_y = 80
offset_x = main_knife_x - 3
offset_y = main_knife_y - 63

# Create afterimages FIRST (they go in the back)
def create_afterimage(source, offset_dx, offset_dy, alpha, dest_canvas, base_x, base_y):
    """Create an afterimage by copying source pixels with modified alpha"""
    stats = source.stats()
    bbox = stats['bbox']
    if bbox is None:
        return
    x0, y0, x1, y1 = bbox
    
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            idx = source.get(x, y)
            if idx != 0:  # not transparent
                pal = source.palette()
                color_info = pal[idx]
                r, g, b, _ = color_info['rgba']
                dest_canvas.set(base_x + x + offset_dx, base_y + y + offset_dy, (r, g, b, alpha))

# Afterimage 3: -45px offset, 20% alpha (furthest back)
create_afterimage(rotated_preview, -45, 0, 51, canvas, offset_x, offset_y)

# Afterimage 2: -30px offset, 40% alpha
create_afterimage(rotated_preview, -30, 0, 102, canvas, offset_x, offset_y)

# Afterimage 1: -15px offset, 60% alpha (closest to main knife)
create_afterimage(rotated_preview, -15, 0, 153, canvas, offset_x, offset_y)

# Now draw the main knife ON TOP (opaque)
canvas.blit(rotated_preview, offset_x, offset_y)

# Add white slash effect at the front of the knife
# The knife tip is around x=153+120-3=270
# Draw a prominent white streak extending to the right

# Register white color
white = canvas.color('#ffffff', name='white')

# Draw slash effect - multiple lines for a dynamic slash
slash_start_x = 265
slash_start_y = 95

# Main slash lines - curved and dynamic, extending to the right
canvas.line(slash_start_x, slash_start_y, slash_start_x + 45, slash_start_y - 5, white)
canvas.line(slash_start_x, slash_start_y + 5, slash_start_x + 40, slash_start_y, white)
canvas.line(slash_start_x, slash_start_y + 10, slash_start_x + 35, slash_start_y + 5, white)

# Add shorter accent lines
canvas.line(slash_start_x + 10, slash_start_y - 8, slash_start_x + 30, slash_start_y - 12, white)
canvas.line(slash_start_x + 10, slash_start_y + 15, slash_start_x + 28, slash_start_y + 18, white)

# Add sparkle dots
canvas.set(slash_start_x + 18, slash_start_y - 10, white)
canvas.set(slash_start_x + 28, slash_start_y - 5, white)
canvas.set(slash_start_x + 23, slash_start_y + 8, white)
canvas.set(slash_start_x + 35, slash_start_y + 2, white)

print("Final canvas stats:", canvas.stats_text())

# View to check the result
view(canvas, scale=2)

# Submit the result
finish(canvas)
