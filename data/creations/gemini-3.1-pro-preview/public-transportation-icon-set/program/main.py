from pixelbench_api import new_canvas, finish

def draw_rounded_rect(c, x, y, w, h, bg, border):
    # Inner fill
    c.rect(x+1, y+1, w-2, h-2, bg)
    # Borders
    c.line(x+2, y, x+w-3, y, border)
    c.line(x+2, y+h-1, x+w-3, y+h-1, border)
    c.line(x, y+2, x, y+h-3, border)
    c.line(x+w-1, y+2, x+w-1, y+h-3, border)
    # Corners
    c.set(x+1, y+1, border)
    c.set(x+w-2, y+1, border)
    c.set(x+1, y+h-2, border)
    c.set(x+w-2, y+h-2, border)

def main():
    c = new_canvas(64, 64, '#1e1e24')

    box_bg = '#2b2d42'
    box_border = '#8d99ae'
    icon_color = '#edf2f4'
    accent_color = '#ef233c'

    # Draw 4 consistent framing boxes
    draw_rounded_rect(c, 2, 2, 28, 28, box_bg, box_border)
    draw_rounded_rect(c, 34, 2, 28, 28, box_bg, box_border)
    draw_rounded_rect(c, 2, 34, 28, 28, box_bg, box_border)
    draw_rounded_rect(c, 34, 34, 28, 28, box_bg, box_border)

    # --- 1. Bus (Top-Left) ---
    # Body
    c.rect(7, 8, 19, 15, icon_color, fill=False)
    c.line(9, 7, 23, 7, icon_color)
    c.set(8, 8, icon_color)
    c.set(24, 8, icon_color)
    c.set(7, 8, box_bg)
    c.set(25, 8, box_bg)
    # Windshield
    c.rect(9, 10, 15, 6, icon_color, fill=False)
    # Accent stripe
    c.line(7, 17, 25, 17, accent_color)
    # Headlights
    c.line(9, 20, 11, 20, icon_color)
    c.line(21, 20, 23, 20, icon_color)
    # Wheels
    c.rect(10, 23, 3, 3, icon_color, fill=False)
    c.rect(19, 23, 3, 3, icon_color, fill=False)
    # Mirrors
    c.line(5, 11, 7, 11, icon_color)
    c.line(5, 11, 5, 13, icon_color)
    c.line(25, 11, 27, 11, icon_color)
    c.line(27, 11, 27, 13, icon_color)

    # --- 2. Subway (Top-Right) ---
    # Body (sleeker top)
    c.rect(39, 8, 19, 15, icon_color, fill=False)
    c.line(42, 6, 54, 6, icon_color)
    c.set(41, 7, icon_color)
    c.set(55, 7, icon_color)
    c.set(40, 8, icon_color)
    c.set(56, 8, icon_color)
    c.set(39, 8, box_bg)
    c.set(57, 8, box_bg)
    # Windshield & Door line
    c.rect(41, 10, 15, 7, icon_color, fill=False)
    c.line(48, 10, 48, 16, icon_color)
    # Accent stripe
    c.line(39, 18, 57, 18, accent_color)
    # Headlights
    c.line(41, 21, 43, 21, icon_color)
    c.line(53, 21, 55, 21, icon_color)
    # Tracks
    c.line(37, 25, 59, 25, box_border)
    c.line(39, 24, 41, 26, box_border)
    c.line(48, 24, 48, 26, box_border)
    c.line(57, 24, 55, 26, box_border)

    # --- 3. Bicycle (Bottom-Left) ---
    # Wheels
    c.circle(9, 53, 4, icon_color, fill=False)
    c.circle(25, 53, 4, icon_color, fill=False)
    # Frame
    c.line(9, 53, 15, 53, icon_color) # Chainstay
    c.line(15, 53, 13, 43, icon_color) # Seat tube
    c.line(15, 53, 22, 43, icon_color) # Down tube
    c.line(13, 43, 22, 43, icon_color) # Top tube
    c.line(25, 53, 21, 39, icon_color) # Fork
    # Seat post
    c.line(13, 43, 13, 42, icon_color)
    # Seat
    c.line(11, 41, 15, 41, accent_color)
    c.line(12, 40, 14, 40, accent_color)
    # Handlebars
    c.line(21, 39, 19, 39, icon_color)
    c.line(21, 39, 24, 36, accent_color)

    # --- 4. Pedestrian (Bottom-Right) ---
    # Head
    c.circle(48, 38, 2, icon_color, fill=False)
    # Torso
    c.rect(46, 42, 5, 7, icon_color, fill=False)
    # Left arm (swinging forward)
    c.line(50, 43, 55, 48, icon_color)
    # Right arm (swinging back)
    c.line(46, 43, 41, 48, icon_color)
    # Left leg (stepping forward)
    c.line(49, 49, 53, 53, icon_color)
    c.line(53, 53, 53, 58, icon_color)
    # Right leg (stepping back)
    c.line(47, 49, 43, 53, icon_color)
    c.line(43, 53, 43, 58, icon_color)
    # Crosswalk
    c.line(40, 59, 44, 59, accent_color)
    c.line(46, 59, 50, 59, accent_color)
    c.line(52, 59, 56, 59, accent_color)

    finish(c)

if __name__ == "__main__":
    main()
