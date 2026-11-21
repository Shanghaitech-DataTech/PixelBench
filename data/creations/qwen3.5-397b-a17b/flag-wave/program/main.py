from pixelbench_api import *

# Recreate the frames with better wave handling
output_w, output_h = 64, 72
offset_x, offset_y = 8, 8

# Frame 1: original positioned
f1 = new_canvas(output_w, output_h, name="frame1")
f1.blit(input_canvas, offset_x, offset_y)

import math

def create_waved_flag_v2(frame_type):
    """Create a flag with wave effect using inverse mapping to avoid gaps"""
    canvas = new_canvas(output_w, output_h, name=f"flag_{frame_type}")
    
    # Copy the pole from original (columns 0-7) - unchanged
    for y in range(56):
        for x in range(8):
            color_idx = input_canvas.get(x, y)
            if color_idx is not None:
                canvas.set(offset_x + x, offset_y + y, color_idx)
    
    # For the flag portion, use inverse mapping
    flag_x_start = offset_x + 8
    flag_x_end = offset_x + 48
    
    for dst_y in range(output_h):
        for dst_x in range(flag_x_start, min(flag_x_end, output_w)):
            src_x_rel = dst_x - offset_x - 8
            src_x = src_x_rel + 8
            
            if src_x < 8 or src_x >= 48:
                continue
            
            dist = src_x - 8
            max_dist = 40
            
            if frame_type == 'high':
                progress = dist / max_dist
                wave = 4 * math.sin(progress * math.pi / 2)
                y_shift = -wave
            elif frame_type == 'low':
                progress = dist / max_dist
                wave = 4 * math.sin(progress * math.pi / 2)
                y_shift = wave
            else:
                y_shift = 0
            
            src_y = dst_y - offset_y - y_shift
            
            if 0 <= src_y < 56:
                src_y_int = int(round(src_y))
                if 0 <= src_y_int < 56:
                    color_idx = input_canvas.get(src_x, src_y_int)
                    if color_idx is not None:
                        canvas.set(dst_x, dst_y, color_idx)
    
    return canvas

f2 = create_waved_flag_v2('high')
f3 = create_waved_flag_v2('low')

# Verify canvas dimensions are the same
print(f"Frame 1 size: {f1.stats()['size']}")
print(f"Frame 2 size: {f2.stats()['size']}")
print(f"Frame 3 size: {f3.stats()['size']}")

# Check that all frames have same dimensions
assert f1.stats()['size'] == f2.stats()['size'] == f3.stats()['size'], "Frame sizes must match!"

# View the top portion to see wave differences
print("\n=== Frame 1 top-middle ===")
print(f1.matrix_text(region=(35, 8, 50, 25)))

print("\n=== Frame 2 top-middle (high) ===")
print(f2.matrix_text(region=(35, 5, 50, 22)))

print("\n=== Frame 3 top-middle (low) ===")
print(f3.matrix_text(region=(35, 12, 50, 29)))

# Check the visible pixel counts
print(f"\nVisible pixels: F1={f1.stats()['visible_pixels']}, F2={f2.stats()['visible_pixels']}, F3={f3.stats()['visible_pixels']}")

finish([f1, f2, f3])
