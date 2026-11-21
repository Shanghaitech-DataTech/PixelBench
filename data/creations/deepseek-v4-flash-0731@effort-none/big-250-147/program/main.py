from pixelbench_api import *

c = input_canvas
output = c.copy(name='output')

# "Set the time to noon on a clear day. Because it is noon, the sun should not appear."
# The current sky is #fcf6e4 (very light warm cream) - needs to become blue for noon.
# The surrounding sunset/warm sky glow colors also need to change to cool noon blue tones.

# Get palette to map colors
pal = c.palette()
pal_by_rgba = {p['rgba']: p['index'] for p in pal}

# Sky-related colors currently in the image (warm sunset tones):
# Main sky: #fcf6e4 (warm cream)
# Sunset edge/glow colors near the sky

# Map of old sky colors to noon blue equivalents
# For a clear noon sky, using a pleasant light-medium blue family
color_map = {
    (252, 246, 228, 255): (120, 178, 232, 255),   # v/c21 - main sky #fcf6e4 -> light blue
    (252, 242, 220, 255): (130, 185, 235, 255),   # H/c33 - sky glow #fcf2dc -> light blue
    (244, 238, 220, 255): (125, 182, 233, 255),   # P/c41 - sky #f4eedc -> light blue
    (244, 230, 212, 255): (115, 175, 230, 255),   # L/c37 - warm sky #f4e6d4 -> blue
    (244, 230, 220, 255): (110, 172, 228, 255),   # K/c36 - warm sky #f4e6dc -> blue
    (236, 226, 212, 255): (105, 168, 226, 255),   # M/c38 - warm sky #ece2d4 -> blue
    (236, 218, 204, 255): (100, 165, 224, 255),   # u/c20 - warm #ecdacc -> blue
    (244, 248, 235, 255) : (135, 190, 238, 255),  # potential additional sky
    (252, 246, 228, 255): (120, 178, 232, 255),   # main sky
}

# Also handle the warm pink/rose colors at sky edges that represent sunset glow
# These appear in the sky region:
# E #dcbec4, B #e4c6c4, F #e4cec4, G #e4c2c4, A #dcb6bc, s #d4aab4, w #f4ded4
# J #ccaeb4, R #ccbabc, V #e4dad4, I #e4cac4, 3 #f4eadc, 4 #fceedc
# These are sunset warm colors surrounding the sky; change to lighter blue/cloud tones

color_map.update({
    (228, 202, 196, 255): (150, 200, 240, 255),  # I/c34 #e4cac4 -> light blue
    (220, 206, 204, 255): (140, 195, 238, 255),  # O/c40 #dccecc -> light blue
    (228, 210, 200, 255): (135, 192, 236, 255),  # E/c30 #dcbec4 -> blue
    (228, 198, 196, 255): (145, 198, 238, 255),  # B/c27 #e4c6c4 -> light blue
    (228, 206, 196, 255): (130, 188, 235, 255),  # F/c31 #e4cec4 -> blue
    (228, 194, 196, 255): (140, 195, 237, 255),  # G/c32 #e4c2c4 -> light blue
    (220, 182, 188, 255): (155, 202, 240, 255),  # A/c26 #dcb6bc -> light blue
    (212, 170, 180, 255): (165, 208, 242, 255),  # s/c18 #d4aab4 -> very light blue
    (204, 166, 180, 255): (170, 212, 244, 255),  # t/c19 #cca6b4 -> very light blue
    (244, 222, 212, 255): (128, 185, 234, 255),  # w/c22 #f4ded4 -> blue
    (204, 174, 180, 255): (175, 215, 245, 255),  # J/c35 #ccaeb4 -> light blue
    (228, 214, 212, 255): (120, 180, 232, 255),  # R/c43 #ccbabc -> blue
    (228, 218, 212, 255): (115, 176, 230, 255),  # V/c47 #e4dad4 -> blue
    (244, 234, 220, 255): (125, 184, 233, 255),  # 3/c55 #f4eadc -> light blue
    (252, 238, 220, 255): (130, 187, 234, 255),  # 4/c56 #fceedc -> light blue
})

# Apply the color mapping to all pixels
w, h = stats['size']
for y in range(h):
    for x in range(w):
        idx = output.get(x, y)
        rgba = tuple(output.palette()[idx]['rgba'])
        if rgba in color_map:
            new_col = color_map[rgba]
            output.set(x, y, new_col)

# Check if there's a sun that needs removal. 
# The task says "because it is noon, the sun should not appear"
# If there was a bright sun disc, it would have been in the warm bright area.
# After the sky color change, any remaining warm bright spots would still be there.
# Let me also check for bright warm colors that would be a sun:
# The warm colors Q (#ac6e8c), 9 (#b46e8c), 5 (#b4728c), D (#b4768c), ? (#bc7284)
# These are the sunset/sun colors. At noon, if any form a sun in the sky,
# they should be changed.
# Let me convert any remaining warm sky-region pixels to blue too.

# In the sky region, replace warm orange/bright tones with blue equivalents
# Check if there are any remaining bright warm colors in the original sky area
# Let's replace remaining sunset-colored warm pixels in the upper sky
# Specifically looking at the transition zone

# Additional warm-orange/pink tones that appear near the sky and might be sun or clouds
color_map2 = {
    (172, 110, 140, 255): (140, 190, 230, 255),   # Q/c42 #ac6e8c - was warm pink
    (180, 110, 140, 255): (148, 196, 234, 255),   # 9/c61 #b46e8c - was warm pink
    (180, 114, 140, 255): (155, 200, 238, 255),   # 5/c57 #b4728c - was warm pink
    (180, 118, 140, 255): (150, 198, 236, 255),   # D/c29 #b4768c - was warm pink
    (188, 114, 132, 255): (160, 205, 240, 255),   # ?/c62 #bc7284 - was warm pink
    (172, 114, 142, 255): (150, 197, 236, 255),   # z/c25 #ac728e - was warm pink
}

# Only apply color_map2 to pixels in the sky region (upper part of the image)
for y in range(h):
    for x in range(w):
        idx = output.get(x, y)
        rgba = tuple(output.palette()[idx]['rgba'])
        if rgba in color_map2:
            # Check if this pixel is in/near the sky area
            # The sky is roughly in the upper 2/3 of the image
            if y < 100:
                new_col = color_map2[rgba]
                output.set(x, y, new_col)

finish(output)
