# Create output canvas as a copy of input
output = input_canvas.copy(name='output')

# Register colors for vines (various greens)
vine_mid = output.color('#4a7a4a')   # Medium green for main vines
vine_light = output.color('#6b9b6b') # Light green for highlights
vine_leaf = output.color('#3d6b3d')  # Leaf green

# Register colors for the mage
cloak_dark = output.color('#1a1a2e')    # Dark cloak (dark blue-purple)
cloak_mid = output.color('#2d2d44')     # Medium cloak
cloak_light = output.color('#4a4a6a')   # Light cloak highlights
staff_wood = output.color('#8b6914')    # Brown wooden staff
staff_glow = output.color('#ffff80')    # Yellow glow from staff
staff_glow_outer = output.color('#ffcc00')  # Outer glow

# Draw vines on the tower walls - scattered organic patterns
# Vines on left side of tower (x=15-35, y=60-180)
# Main vine stem going down
output.line(18, 60, 22, 120, vine_mid)
output.line(22, 120, 25, 150, vine_mid)
output.line(25, 150, 28, 180, vine_mid)

# Branching vines
output.line(18, 70, 15, 80, vine_mid)
output.line(22, 90, 28, 95, vine_mid)
output.line(22, 110, 16, 120, vine_mid)
output.line(25, 140, 32, 145, vine_mid)
output.line(25, 160, 20, 170, vine_mid)

# Add some leaf clusters (small circles/ovals)
output.circle(15, 80, 2, vine_leaf, fill=True)
output.circle(28, 95, 2, vine_leaf, fill=True)
output.circle(16, 120, 2, vine_leaf, fill=True)
output.circle(32, 145, 2, vine_leaf, fill=True)
output.circle(20, 170, 2, vine_leaf, fill=True)
output.circle(25, 100, 1, vine_light, fill=True)
output.circle(19, 130, 1, vine_light, fill=True)

# Vines on right side of tower (x=45-65, y=70-160)
output.line(50, 70, 48, 100, vine_mid)
output.line(48, 100, 52, 130, vine_mid)
output.line(52, 130, 55, 160, vine_mid)

# Branching vines on right
output.line(50, 80, 56, 85, vine_mid)
output.line(48, 110, 42, 115, vine_mid)
output.line(52, 140, 58, 145, vine_mid)

# Leaf clusters on right
output.circle(56, 85, 2, vine_leaf, fill=True)
output.circle(42, 115, 2, vine_leaf, fill=True)
output.circle(58, 145, 2, vine_leaf, fill=True)
output.circle(49, 95, 1, vine_light, fill=True)
output.circle(53, 125, 1, vine_light, fill=True)

# Additional vine tendrils
output.line(30, 80, 35, 90, vine_mid)
output.line(35, 90, 38, 105, vine_mid)
output.circle(38, 105, 1, vine_leaf, fill=True)

# Draw the cloaked mage at the archway entrance
# Mage positioned at archway center, facing away (walking into tower)
mage_x = 75  # center x
mage_y = 225  # top of hood

# Draw cloak as a filled shape - back view of hooded figure
# Hood (top) - rounded
output.circle(mage_x, mage_y + 3, 3, cloak_dark, fill=True)

# Upper cloak body (shoulders)
output.rect(mage_x - 4, mage_y + 5, 9, 4, cloak_dark, fill=True)

# Lower cloak body (flowing down)
output.rect(mage_x - 3, mage_y + 9, 7, 10, cloak_dark, fill=True)

# Cloak folds/highlights to show it's fabric
output.set(mage_x - 2, mage_y + 7, cloak_mid)
output.set(mage_x + 2, mage_y + 8, cloak_mid)
output.set(mage_x - 1, mage_y + 12, cloak_mid)
output.set(mage_x + 1, mage_y + 14, cloak_mid)
output.set(mage_x, mage_y + 16, cloak_light)

# Bottom edge of cloak
output.set(mage_x - 3, mage_y + 18, cloak_mid)
output.set(mage_x + 3, mage_y + 18, cloak_mid)

# Staff - held in right hand (viewer's right since mage is facing away)
staff_x = mage_x + 5  # to the right of the mage
staff_top_y = mage_y + 6  # orb position (around shoulder height)
staff_bottom_y = mage_y + 20  # bottom of staff

# Staff wood (brown vertical line)
for y in range(staff_top_y + 2, staff_bottom_y + 1):
    output.set(staff_x, y, staff_wood)

# Glowing orb at top of staff - bright center
output.set(staff_x, staff_top_y, staff_glow)
output.set(staff_x, staff_top_y + 1, staff_glow)

# Glow halo around the orb
output.set(staff_x - 1, staff_top_y, staff_glow_outer)
output.set(staff_x + 1, staff_top_y, staff_glow_outer)
output.set(staff_x, staff_top_y - 1, staff_glow_outer)
output.set(staff_x - 1, staff_top_y + 1, staff_glow_outer)
output.set(staff_x + 1, staff_top_y + 1, staff_glow_outer)

# Additional glow pixels for brightness effect
output.set(staff_x - 2, staff_top_y, staff_glow)
output.set(staff_x + 2, staff_top_y, staff_glow)
output.set(staff_x, staff_top_y - 2, staff_glow)

# Hand holding staff (dark, barely visible)
output.set(staff_x - 1, staff_top_y + 3, cloak_dark)

# Submit the result
finish(output)
