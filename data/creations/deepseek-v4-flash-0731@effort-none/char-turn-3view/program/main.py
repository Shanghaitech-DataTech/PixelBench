from pixelbench_api import *

input_canvas = canvas('input')
W, H = 66, 119

# Extract pixel data
px = {}
for y in range(H):
    for x in range(W):
        idx = input_canvas.get(x, y)
        if idx > 0:
            px[(x, y)] = idx

pal = input_canvas.palette()
color_by_idx = {}
for p in pal:
    color_by_idx[p['index']] = (p['rgba'][0], p['rgba'][1], p['rgba'][2])

f1 = new_canvas(66, 119, name='f1')
f2 = new_canvas(66, 119, name='f2')
f3 = new_canvas(66, 119, name='f3')

# =====================================================
# Build 3/4 views (frames 1 and 2)
# The character is symmetric front view.
# Frame 1: character turned 45° LEFT
# Frame 2: character turned 45° RIGHT (mirror of frame 1)
# =====================================================

def build_3q(orientation):
    """Build a 3/4 view from the front view."""
    result = {}
    
    for y in range(H):
        row_pixels = [(x, px[(x,y)]) for x in range(W) if (x,y) in px]
        if not row_pixels:
            continue
        
        left = min(x for x, _ in row_pixels)
        right = max(x for x, _ in row_pixels)
        cx = (left + right) / 2.0
        
        near_s = 0.92
        far_s = 0.58
        
        new_cx = cx
        
        new_row = {}
        
        for x, idx in sorted(row_pixels, key=lambda x: abs(x[0] - cx)):
            if orientation == 'left':
                if x <= cx:
                    nx = new_cx - (cx - x) * near_s
                else:
                    nx = new_cx + (x - cx) * far_s
            else:
                if x >= cx:
                    nx = new_cx + (x - cx) * near_s
                else:
                    nx = new_cx - (cx - x) * far_s
            nx = round(nx)
            if 0 <= nx < 66:
                result[(nx, y)] = idx
    
    return result

f1_map = build_3q('left')
f2_map = build_3q('right')

for (x, y), idx in f1_map.items():
    f1.set(x, y, idx)
for (x, y), idx in f2_map.items():
    f2.set(x, y, idx)

# =====================================================
# Frame 3: REAR VIEW (character seen from behind)
# =====================================================

# The character from behind shows:
# - Same twin buns at the top
# - Back of head with hair (where the face was)
# - Back of neck and shoulders
# - Back of body/outfit

f3_map = {}

def get_back_color(x, y, orig_idx):
    """Determine what color a pixel should be in the rear view."""
    # Buns area (rows 0-21): same from behind
    if y <= 21:
        return orig_idx
    
    # Head area (rows 22-48): back of head showing hair
    # The face features are replaced with hair colors
    
    # For the hair covering the back of the head:
    # Use alternating brown hair tones based on position
    if y <= 24:
        # Upper transition area
        if orig_idx in [7, 8]:  # skin in face
            return 2  # dark hair
        return orig_idx
    elif y <= 45:
        # Main back of head - hair covers the skull
        # Face features (skin, eyes) become hair
        if orig_idx in [7, 8, 10, 11, 12, 13, 14]:
            # Hair pattern on back of head
            pattern = [3, 4, 3, 2, 3]
            return pattern[(x + y) % 5]
        elif orig_idx in [9]:  # i (dark) - already hair
            return orig_idx
        else:
            return orig_idx
    elif y <= 52:
        # Neck/shoulder from behind
        if orig_idx in [7, 8, 10, 14]:
            return 3  # hair/neck from behind
        return orig_idx
    else:
        # Body from behind - same as front
        return orig_idx

for (x, y), idx in px.items():
    back_idx = get_back_color(x, y, idx)
    if y <= 48 and 12 <= x <= 54 and idx in [7, 8, 10, 11, 12, 13, 14]:
        # Make the back of head consistent
        pattern = [3, 4, 3, 2]
        f3_map[(x, y)] = pattern[(x + y) % 4]
    elif y <= 52 and 14 <= x <= 52:
        if idx in [7, 8, 10, 14]:
            f3_map[(x, y)] = 3
        else:
            f3_map[(x, y)] = idx
    else:
        f3_map[(x, y)] = idx

# Apply frame 3
for (x, y), idx in f3_map.items():
    f3.set(x, y, idx)

# Final check
print("Frame 1:", f1.stats())
print("Frame 2:", f2.stats())
print("Frame 3:", f3.stats())

# Submit all three frames
finish([f1, f2, f3])
