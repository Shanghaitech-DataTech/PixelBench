from pixelbench_api import *

# Both frames need the same canvas size
# Create a larger canvas (80x70) to accommodate the fire spell
# Frame 1: place original character on this canvas
frame1 = new_canvas(80, 70, background=None, name='frame1')
frame1.blit(input_canvas, 0, 0)

# Frame 2: same size canvas with fire spell animation
frame2 = new_canvas(80, 70, background=None, name='frame2')

# Copy the original character to frame2
frame2.blit(input_canvas, 0, 0)

# Register fire colors
fire_red = frame2.color('#ff3300')
fire_orange = frame2.color('#ff7700') 
fire_yellow = frame2.color('#ffbb00')
fire_white = frame2.color('#ffffaa')
fire_dark = frame2.color('#cc2200')

# Draw a large fire spell projectile extending forward
# Main fire ball at the front (around x=60-70)
frame2.circle(65, 30, 7, fire_orange, fill=True)
frame2.circle(65, 30, 5, fire_yellow, fill=True)
frame2.circle(65, 30, 3, fire_white, fill=True)

# Draw fiery trail connecting from character to fire ball
# Trail from x=45 to x=58, centered around y=30
for y in range(26, 36):
    for x in range(44, 60):
        dist_from_center = abs(y - 30)
        dist_from_ball = 58 - x
        
        # Trail shape - wider near ball, tapering back
        max_width = 5 - dist_from_ball // 4
        if dist_from_center <= max_width:
            # Color gradient
            if dist_from_ball < 3:
                frame2.set(x, y, fire_yellow)
            elif dist_from_ball < 6:
                frame2.set(x, y, fire_orange)
            elif dist_from_ball < 10:
                frame2.set(x, y, fire_red)
            else:
                frame2.set(x, y, fire_dark)

# Add flame flickers and sparks around the fire ball
frame2.set(71, 28, fire_white)
frame2.set(73, 30, fire_yellow)
frame2.set(71, 33, fire_orange)
frame2.set(68, 25, fire_yellow)
frame2.set(68, 36, fire_orange)
frame2.set(60, 26, fire_red)
frame2.set(60, 35, fire_red)

# Add spark particles flying outward
frame2.set(76, 29, fire_yellow)
frame2.set(77, 31, fire_orange)
frame2.set(75, 34, fire_red)
frame2.set(72, 24, fire_yellow)
frame2.set(73, 37, fire_orange)

# Modify the pose - show character thrusting forward
# Clear back foot area and redraw shifted forward
frame2.clear(x=5, y=48, w=18, h=18)

# Colors from original
robe = frame2.color('#7d423a')
dark = frame2.color('#0b0102')
skin = frame2.color('#dfb2ac')
hair = frame2.color('#4a222d')

# Redraw left foot stepped forward
frame2.rect(18, 58, 10, 4, dark, fill=True)  # shoe
frame2.rect(20, 55, 6, 4, robe, fill=True)   # lower robe

# Shift body forward slightly - redraw upper body area
frame2.clear(x=10, y=20, w=25, h=25)

# Redraw body leaning forward with extended arm
frame2.rect(15, 22, 18, 15, robe, fill=True)
frame2.rect(28, 24, 8, 5, skin, fill=True)  # extended arm/hand

# Head position adjusted for lean
frame2.rect(12, 8, 12, 10, skin, fill=True)  # face
frame2.rect(10, 6, 16, 5, hair, fill=True)   # hair

print("Frame 1 stats:", frame1.stats_text())
print("Frame 2 stats:", frame2.stats_text())

# Submit both frames
finish([frame1, frame2])
