from pixelbench_api import new_canvas, finish

# Create a 32x32 canvas with transparent background
c = new_canvas(32, 32, background=None, name="usb_drive")

# Define colors - limited palette for clean pixel art
dark_outline = c.color((20, 20, 25), "dark_outline")
metal_light = c.color((195, 200, 210), "metal_light")
metal_mid = c.color((145, 150, 165), "metal_mid")
metal_dark = c.color((75, 80, 90), "metal_dark")
usb_gold = c.color((210, 180, 95), "usb_gold")
usb_gold_dark = c.color((155, 125, 55), "usb_gold_dark")
strap_color = c.color((55, 65, 80), "strap")
highlight = c.color((230, 235, 245), "highlight")

# USB Flash Drive layout - centered vertically
conn_x = 4
conn_y = 11
body_x = conn_x + 7
body_y = 10
body_w = 18
body_h = 14

# === USB CONNECTOR (the plug part) ===
# Outer metal shell - 8 wide x 10 tall
c.rect(conn_x, conn_y, 8, 10, metal_mid, fill=True)

# Connector dark outline
c.rect(conn_x, conn_y, 8, 1, dark_outline, fill=True)  # top
c.rect(conn_x, conn_y + 9, 8, 1, dark_outline, fill=True)  # bottom
c.rect(conn_x, conn_y, 1, 10, dark_outline, fill=True)  # left

# Inner plastic area
c.rect(conn_x + 1, conn_y + 1, 6, 8, usb_gold_dark, fill=True)
c.rect(conn_x + 2, conn_y + 2, 4, 6, usb_gold, fill=True)

# Gold contact pins (4 pins)
for i in range(4):
    c.rect(conn_x + 3 + i, conn_y + 3, 1, 4, highlight, fill=True)

# === MAIN BODY (metal casing) ===
c.rect(body_x, body_y, body_w, body_h, metal_mid, fill=True)

# Body outlines
c.rect(body_x, body_y, body_w, 1, dark_outline, fill=True)  # top
c.rect(body_x, body_y + body_h - 1, body_w, 1, dark_outline, fill=True)  # bottom
c.rect(body_x + body_w - 1, body_y, 1, body_h, dark_outline, fill=True)  # right

# Metallic highlight band (upper portion)
c.rect(body_x + 2, body_y + 2, body_w - 6, 2, highlight, fill=True)
c.rect(body_x + 2, body_y + 4, body_w - 5, 1, metal_light, fill=True)

# Shadow band (lower portion)
c.rect(body_x + 2, body_y + body_h - 4, body_w - 4, 2, metal_dark, fill=True)

# Decorative horizontal line
c.line(body_x + 3, body_y + 8, body_x + body_w - 4, body_y + 8, metal_dark)

# === KEYCHAIN LOOP ===
# Loop center position
loop_cx = body_x + body_w - 2
loop_cy = body_y + body_h // 2

# Draw the loop ring manually for better control
# Top of loop
c.set(loop_cx, loop_cy - 3, metal_dark)
c.set(loop_cx - 1, loop_cy - 3, metal_dark)
c.set(loop_cx + 1, loop_cy - 3, metal_dark)
# Upper sides
c.set(loop_cx - 2, loop_cy - 2, metal_dark)
c.set(loop_cx + 2, loop_cy - 2, metal_dark)
# Middle sides
c.set(loop_cx - 3, loop_cy - 1, metal_dark)
c.set(loop_cx - 3, loop_cy, metal_dark)
c.set(loop_cx - 3, loop_cy + 1, metal_dark)
c.set(loop_cx + 3, loop_cy - 1, metal_dark)
c.set(loop_cx + 3, loop_cy, metal_dark)
c.set(loop_cx + 3, loop_cy + 1, metal_dark)
# Lower sides
c.set(loop_cx - 2, loop_cy + 2, metal_dark)
c.set(loop_cx + 2, loop_cy + 2, metal_dark)
# Bottom of loop
c.set(loop_cx, loop_cy + 3, metal_dark)
c.set(loop_cx - 1, loop_cy + 3, metal_dark)
c.set(loop_cx + 1, loop_cy + 3, metal_dark)

# Inner hole (transparent) - make a 3x3 hole
c.set(loop_cx, loop_cy - 2, None)
c.set(loop_cx - 1, loop_cy - 1, None)
c.set(loop_cx, loop_cy - 1, None)
c.set(loop_cx + 1, loop_cy - 1, None)
c.set(loop_cx - 1, loop_cy, None)
c.set(loop_cx, loop_cy, None)
c.set(loop_cx + 1, loop_cy, None)
c.set(loop_cx - 1, loop_cy + 1, None)
c.set(loop_cx, loop_cy + 1, None)
c.set(loop_cx + 1, loop_cy + 1, None)
c.set(loop_cx, loop_cy + 2, None)

# Keychain strap attachment
c.set(loop_cx + 4, loop_cy - 2, strap_color)
c.set(loop_cx + 4, loop_cy - 1, strap_color)
c.set(loop_cx + 4, loop_cy, strap_color)
c.set(loop_cx + 4, loop_cy + 1, strap_color)
c.set(loop_cx + 4, loop_cy + 2, strap_color)

# === CONNECTOR TO BODY SEAM ===
c.line(body_x, body_y, body_x, body_y + body_h, dark_outline)

print(c.stats_text())
print(c.matrix_text())

finish(c)
