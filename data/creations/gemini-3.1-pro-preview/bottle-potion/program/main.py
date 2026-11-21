import sys

def main():
    output = input_canvas.copy(name="output")

    very_dark_purple = output.color((50, 10, 80, 255))
    dark_purple = output.color((80, 20, 120, 255))
    main_purple = output.color((140, 40, 180, 255))
    high_purple1 = output.color((155, 55, 195, 255))
    high_purple2 = output.color((165, 65, 205, 255))
    high_purple3 = output.color((175, 75, 215, 255))

    color_map = {
        5: dark_purple,
        6: main_purple,
        7: high_purple1,
        8: high_purple2,
        9: very_dark_purple,
        10: high_purple3
    }

    for y in range(64):
        for x in range(64):
            c = output.get(x, y)
            if c in color_map:
                output.set(x, y, color_map[c])

    # Bubbles
    bubble_color = output.color((230, 180, 255, 255))
    bubble_edge = output.color((200, 120, 230, 255))
    
    def draw_bubble(cx, cy, r):
        if r == 1:
            output.set(cx, cy, bubble_color)
        elif r == 2:
            output.rect(cx, cy, 2, 2, bubble_color)
        elif r == 3:
            output.set(cx, cy-1, bubble_color)
            output.set(cx, cy+1, bubble_color)
            output.set(cx-1, cy, bubble_color)
            output.set(cx+1, cy, bubble_color)
            output.set(cx, cy, bubble_color)
        elif r == 4:
            output.set(cx, cy-1, bubble_edge)
            output.set(cx, cy+1, bubble_edge)
            output.set(cx-1, cy, bubble_edge)
            output.set(cx+1, cy, bubble_edge)
            output.set(cx-1, cy-1, bubble_color)
    
    bubbles = [
        (22, 44, 2),
        (28, 52, 1),
        (35, 46, 3),
        (42, 54, 4),
        (45, 42, 1),
        (25, 56, 1),
        (32, 58, 2),
        (18, 48, 4),
        (38, 38, 2),
        (20, 36, 1),
        (48, 48, 1),
        (30, 40, 4),
    ]
    
    for bx, by, br in bubbles:
        draw_bubble(bx, by, br)
        
    def draw_surface_bubble(cx, cy, size):
        if size == 1:
            output.set(cx, cy-1, bubble_edge)
            output.set(cx-1, cy, bubble_edge)
            output.set(cx+1, cy, bubble_edge)
            output.set(cx-1, cy-1, bubble_color)
        elif size == 2:
            output.set(cx-1, cy-1, bubble_edge)
            output.set(cx, cy-1, bubble_edge)
            output.set(cx-2, cy, bubble_edge)
            output.set(cx+1, cy, bubble_edge)
            output.set(cx-1, cy-1, bubble_color)
            
    draw_surface_bubble(26, 28, 1)
    draw_surface_bubble(34, 29, 2)
    draw_surface_bubble(45, 28, 1)
    draw_surface_bubble(18, 29, 1)
    
    # some small droplets above surface
    output.set(26, 25, bubble_color)
    output.set(34, 26, bubble_color)
    output.set(35, 24, bubble_edge)
    output.set(45, 26, bubble_color)
    output.set(18, 26, bubble_edge)

    finish(output)

main()