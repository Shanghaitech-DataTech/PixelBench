from pixelbench_api import new_canvas, finish

# Create 64x64 canvas
c = new_canvas(64, 64, name="laundromat")

# Define colors (cool palette for laundromat)
# Background/walls
c.color("#e8e8e8", "wall")        # light gray wall
c.color("#c0c0c0", "wall_shadow")  # darker wall
c.color("#d0d8e0", "ceiling")      # cool white ceiling

# Floor tiles
c.color("#a0a0b0", "floor_dark")   # dark floor tile
c.color("#b8b8c8", "floor_light")  # light floor tile

# Washing machines
c.color("#f0f0f0", "machine_body") # white machine body
c.color("#d0d0d8", "machine_shadow") # machine shadow
c.color("#4060a0", "machine_door") # blue-tinted door glass
c.color("#6080c0", "door_highlight") # door highlight
c.color("#305080", "door_dark")    # door dark edge
c.color("#203050", "door_frame")   # door frame
c.color("#8090a0", "machine_top")  # machine top panel
c.color("#4080ff", "led_on")       # blue LED indicator
c.color("#ff6040", "led_off")      # red/off indicator
c.color("#606070", "control_knob") # control knob

# Folding table
c.color("#c8b8a0", "table_top")    # light wood table
c.color("#a08868", "table_leg")    # table leg
c.color("#887058", "table_shadow") # table shadow

# Laundry basket
c.color("#d0c0a0", "basket_light") # light basket weave
c.color("#a09070", "basket_dark")  # dark basket weave
c.color("#ffffff", "clothes_white") # white clothes
c.color("#80a0c0", "clothes_blue")  # blue clothes

# Wall clock
c.color("#ffffff", "clock_face")   # white clock face
c.color("#303030", "clock_frame")  # black clock frame
c.color("#202020", "clock_hands")  # clock hands

# Ceiling lights (cool white fluorescent)
c.color("#f8f8ff", "light_bright") # bright cool white
c.color("#e0e0f0", "light_dim")    # dimmer light area
c.color("#c0c0d0", "light_fixture") # light fixture

# === Draw background ===

# Ceiling (top 12 pixels)
c.rect(0, 0, 64, 12, "ceiling", fill=True)

# Back wall (next 30 pixels, from y=12 to y=42)
c.rect(0, 12, 64, 30, "wall", fill=True)

# Floor (bottom 22 pixels, from y=42 to y=64)
# Create tiled floor pattern
for y in range(42, 64, 4):
    for x in range(0, 64, 4):
        tile_color = "floor_light" if ((x // 4) + (y // 4)) % 2 == 0 else "floor_dark"
        c.rect(x, y, 4, 4, tile_color, fill=True)

# === Draw ceiling lights ===
# Three fluorescent light fixtures on ceiling
for lx in [8, 32, 56]:
    # Fixture housing
    c.rect(lx - 8, 2, 16, 4, "light_fixture", fill=True)
    # Light glow
    c.rect(lx - 6, 3, 12, 2, "light_bright", fill=True)
    c.rect(lx - 7, 5, 14, 1, "light_dim", fill=True)

# === Draw wall clock ===
# Position: upper right wall
clock_x, clock_y = 52, 18
# Clock frame (circle)
c.circle(clock_x, clock_y, 6, "clock_frame", fill=True)
# Clock face
c.circle(clock_x, clock_y, 5, "clock_face", fill=True)
# Clock hands (pointing to ~10:10)
c.line(clock_x, clock_y, clock_x - 2, clock_y - 3, "clock_hands")  # hour hand
c.line(clock_x, clock_y, clock_x + 3, clock_y - 2, "clock_hands")  # minute hand
c.set(clock_x, clock_y, "clock_hands")  # center dot

# === Draw washing machines - Row 1 (left side, closer) ===
# Machine 1
m1_x, m1_y = 4, 28
c.rect(m1_x, m1_y, 18, 22, "machine_body", fill=True)
c.rect(m1_x, m1_y, 18, 4, "machine_top", fill=True)
# Door (circular, front-loading)
c.circle(m1_x + 9, m1_y + 13, 7, "door_frame", fill=True)
c.circle(m1_x + 9, m1_y + 13, 6, "door_dark", fill=True)
c.circle(m1_x + 9, m1_y + 13, 5, "machine_door", fill=True)
c.circle(m1_x + 8, m1_y + 12, 2, "door_highlight", fill=True)
# Control panel
c.set(m1_x + 14, m1_y + 6, "control_knob")
c.set(m1_x + 16, m1_y + 6, "led_on")
# Machine shadow/separation line
c.line(m1_x + 18, m1_y, m1_x + 18, m1_y + 22, "machine_shadow")

# Machine 2
m2_x, m2_y = 24, 28
c.rect(m2_x, m2_y, 18, 22, "machine_body", fill=True)
c.rect(m2_x, m2_y, 18, 4, "machine_top", fill=True)
c.circle(m2_x + 9, m2_y + 13, 7, "door_frame", fill=True)
c.circle(m2_x + 9, m2_y + 13, 6, "door_dark", fill=True)
c.circle(m2_x + 9, m2_y + 13, 5, "machine_door", fill=True)
c.circle(m2_x + 8, m2_y + 12, 2, "door_highlight", fill=True)
c.set(m2_x + 14, m2_y + 6, "control_knob")
c.set(m2_x + 16, m2_y + 6, "led_off")
c.line(m2_x + 18, m2_y, m2_x + 18, m2_y + 22, "machine_shadow")

# Machine 3
m3_x, m3_y = 44, 28
c.rect(m3_x, m3_y, 16, 22, "machine_body", fill=True)
c.rect(m3_x, m3_y, 16, 4, "machine_top", fill=True)
c.circle(m3_x + 8, m3_y + 13, 6, "door_frame", fill=True)
c.circle(m3_x + 8, m3_y + 13, 5, "door_dark", fill=True)
c.circle(m3_x + 8, m3_y + 13, 4, "machine_door", fill=True)
c.circle(m3_x + 7, m3_y + 12, 2, "door_highlight", fill=True)
c.set(m3_x + 12, m3_y + 6, "control_knob")
c.set(m3_x + 14, m3_y + 6, "led_on")

# === Row 2 (right side, slightly further back - smaller) ===
# Machine 4
m4_x, m4_y = 6, 52
c.rect(m4_x, m4_y, 16, 10, "machine_body", fill=True)
c.rect(m4_x, m4_y, 16, 3, "machine_top", fill=True)
c.circle(m4_x + 8, m4_y + 6, 4, "door_frame", fill=True)
c.circle(m4_x + 8, m4_y + 6, 3, "machine_door", fill=True)
c.circle(m4_x + 7, m4_y + 5, 1, "door_highlight", fill=True)
c.set(m4_x + 12, m4_y + 4, "led_on")

# Machine 5
m5_x, m5_y = 26, 52
c.rect(m5_x, m5_y, 16, 10, "machine_body", fill=True)
c.rect(m5_x, m5_y, 16, 3, "machine_top", fill=True)
c.circle(m5_x + 8, m5_y + 6, 4, "door_frame", fill=True)
c.circle(m5_x + 8, m5_y + 6, 3, "machine_door", fill=True)
c.circle(m5_x + 7, m5_y + 5, 1, "door_highlight", fill=True)
c.set(m5_x + 12, m5_y + 4, "led_off")

# Machine 6
m6_x, m6_y = 46, 52
c.rect(m6_x, m6_y, 14, 10, "machine_body", fill=True)
c.rect(m6_x, m6_y, 14, 3, "machine_top", fill=True)
c.circle(m6_x + 7, m6_y + 6, 4, "door_frame", fill=True)
c.circle(m6_x + 7, m6_y + 6, 3, "machine_door", fill=True)
c.set(m6_x + 10, m6_y + 4, "led_on")

# === Folding table (against right wall) ===
table_x, table_y = 48, 38
# Table top
c.rect(table_x, table_y, 14, 3, "table_top", fill=True)
# Table legs
c.rect(table_x + 2, table_y + 3, 2, 8, "table_leg", fill=True)
c.rect(table_x + 10, table_y + 3, 2, 8, "table_leg", fill=True)
# Table shadow
c.rect(table_x + 1, table_y + 11, 12, 2, "table_shadow", fill=True)

# === Laundry basket (on floor near table) ===
basket_x, basket_y = 38, 56
# Basket shape (rounded rectangle)
c.rect(basket_x + 2, basket_y, 8, 6, "basket_light", fill=True)
c.rect(basket_x + 1, basket_y + 1, 10, 4, "basket_dark", fill=True)
# Weave pattern
for bx in range(basket_x + 2, basket_x + 10, 2):
    c.set(bx, basket_y + 2, "basket_light")
# Clothes in basket
c.set(basket_x + 4, basket_y + 1, "clothes_white")
c.set(basket_x + 6, basket_y + 1, "clothes_blue")
c.set(basket_x + 5, basket_y, "clothes_white")

# Add subtle wall shadow at floor junction
c.line(0, 41, 63, 41, "wall_shadow")

print(c.stats_text())

finish(c)
