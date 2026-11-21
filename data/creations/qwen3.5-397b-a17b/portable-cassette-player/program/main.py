from pixelbench_api import new_canvas, finish

# Create 32x32 canvas with transparent background
c = new_canvas(32, 32, background=None, name="cassette_player")

# Define colors
body_light = c.color("#C0C0C0", "body_light")      # Silver body
body_dark = c.color("#808080", "body_dark")        # Darker silver
body_shadow = c.color("#505050", "body_shadow")    # Shadow
window_bg = c.color("#1a1a1a", "window_bg")        # Cassette window background
reel_white = c.color("#FFFFFF", "reel_white")      # Tape reels
reel_center = c.color("#404040", "reel_center")    # Reel centers
button_play = c.color("#4CAF50", "button_play")    # Play button green
button_stop = c.color("#F44336", "button_stop")    # Stop button red
button_pause = c.color("#2196F3", "button_pause")  # Pause button blue
button_gray = c.color("#606060", "button_gray")    # Other buttons
volume_knob = c.color("#FFD700", "volume_knob")    # Volume knob gold
cable = c.color("#202020", "cable")                # Headphone cable
highlight = c.color("#E0E0E0", "highlight")        # Highlight
jack = c.color("#101010", "jack")                  # Headphone jack

# Main body - rounded rectangle (28x24, centered at x=2, y=4)
# Draw the base shape
c.rect(2, 4, 28, 24, body_light, fill=True)

# Darker bottom edge for depth
c.rect(2, 26, 28, 2, body_dark, fill=True)

# Top highlight edge
c.rect(3, 5, 26, 1, highlight, fill=True)

# Cassette window area
# Window outer frame
c.rect(4, 6, 24, 14, window_bg, fill=True)

# Window inner (darker background for transparent look)
c.rect(5, 7, 22, 12, "#0a0a0a", fill=True)

# Left tape reel
c.circle(11, 13, 4, reel_white, fill=True)
c.circle(11, 13, 2, reel_center, fill=True)
c.set(11, 13, reel_white)  # Center highlight

# Right tape reel
c.circle(21, 13, 4, reel_white, fill=True)
c.circle(21, 13, 2, reel_center, fill=True)
c.set(21, 13, reel_white)  # Center highlight

# Tape visible between reels
c.line(15, 11, 17, 11, "#333333")
c.line(15, 15, 17, 15, "#333333")

# Window label strip
c.rect(6, 8, 20, 2, "#2a2a2a", fill=True)

# Brand text area below window
c.rect(8, 18, 16, 2, "#3a3a3a", fill=True)

# Playback controls area (below window)
c.rect(4, 21, 24, 6, body_dark, fill=True)

# Play button (triangle pointing right) - green
c.set(7, 23, button_play)
c.set(7, 24, button_play)
c.set(7, 25, button_play)
c.set(8, 23, button_play)
c.set(8, 24, button_play)
c.set(8, 25, button_play)
c.set(9, 24, button_play)

# Stop button (square) - red
c.rect(11, 23, 3, 3, button_stop, fill=True)

# Pause button (two vertical bars) - blue
c.set(16, 23, button_pause)
c.set(16, 24, button_pause)
c.set(16, 25, button_pause)
c.set(18, 23, button_pause)
c.set(18, 24, button_pause)
c.set(18, 25, button_pause)

# Rewind button (triangle pointing left) - gray
c.set(21, 24, button_gray)
c.set(22, 23, button_gray)
c.set(22, 24, button_gray)
c.set(22, 25, button_gray)
c.set(23, 24, button_gray)

# Fast forward button (triangle pointing right) - gray
c.set(25, 24, button_gray)
c.set(26, 23, button_gray)
c.set(26, 24, button_gray)
c.set(26, 25, button_gray)
c.set(27, 24, button_gray)

# Volume control wheel on right side
c.rect(29, 10, 2, 10, body_shadow, fill=True)
c.set(30, 12, volume_knob)
c.set(30, 13, volume_knob)
c.set(30, 14, volume_knob)
c.set(30, 15, volume_knob)

# Headphone jack on top center
c.rect(14, 2, 4, 2, jack, fill=True)

# Headphone cable coming from jack going up
c.set(15, 1, cable)
c.set(16, 0, cable)
c.set(17, 1, cable)

# Side speaker grills (left and right edges)
for y in range(10, 18, 2):
    c.set(1, y, "#404040")
    c.set(30, y, "#404040")

# Add depth shading - left edge shadow
c.line(2, 4, 2, 27, body_shadow)

# Add highlight on right edge
c.line(29, 4, 29, 27, highlight)

# Corner rounding effect (top corners)
c.set(2, 4, highlight)
c.set(29, 4, highlight)

print(c.stats_text())
print(c.matrix_text())

finish(c)
