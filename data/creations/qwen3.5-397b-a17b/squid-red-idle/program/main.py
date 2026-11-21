# Create 3 frames for the squid idle animation
# Simple whole-sprite bobbing motion - clean and effective for breathing idle
# Frame 1: neutral/original position
# Frame 2: bobbed up (inhale)
# Frame 3: bobbed down (exhale)

CANVAS_W = 58
CANVAS_H = 64  # Extra space for movement (3px up + 3px down from neutral)

# Frame 1: neutral position (4px top padding)
f1 = new_canvas(CANVAS_W, CANVAS_H, name="frame1")
f1.blit(input_canvas, 0, 4)

# Frame 2: bob up by 2 pixels (2px top padding)
f2 = new_canvas(CANVAS_W, CANVAS_H, name="frame2")
f2.blit(input_canvas, 0, 2)

# Frame 3: bob down by 2 pixels from neutral (6px top padding)
f3 = new_canvas(CANVAS_W, CANVAS_H, name="frame3")
f3.blit(input_canvas, 0, 6)

print("Frame 1 stats:", f1.stats_text())
print("Frame 2 stats:", f2.stats_text())
print("Frame 3 stats:", f3.stats_text())

# Verify all frames have same pixel count
s1 = f1.stats()['visible_pixels']
s2 = f2.stats()['visible_pixels']
s3 = f3.stats()['visible_pixels']
print(f"Pixel counts: {s1}, {s2}, {s3}")
assert s1 == s2 == s3, "All frames should have same pixel count"

# Submit the 3 frames
finish([f1, f2, f3])
