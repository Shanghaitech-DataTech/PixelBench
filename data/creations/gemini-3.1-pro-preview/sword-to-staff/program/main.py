from pixelbench_api import input_canvas, view, finish

out = input_canvas.copy()

# Clear the sword area
for y in range(38, 60):
    for x in range(41, 50):
        out.set(x, y, '#ffffffff')
out.set(40, 39, '#ffffffff')
out.set(40, 40, '#ffffffff')

# Draw the staff
c_out = '#2e1f12ff'
c_wood1 = '#7a6248ff'
c_wood2 = '#4a3120ff'

# Top cap
out.set(44, 15, c_out)
out.set(45, 15, c_out)

# Staff body
for y in range(16, 56):
    out.set(43, y, c_out)
    out.set(44, y, c_wood1)
    out.set(45, y, c_wood2)
    out.set(46, y, c_out)

# Bottom cap
out.set(44, 56, c_out)
out.set(45, 56, c_out)

# Redraw the hand over the staff
c_skin = '#f2c49bff'

for y in range(35, 38): # 35, 36, 37
    out.set(43, y, c_skin)
    out.set(44, y, c_out)

# Hand bottom outline at y=38
out.set(40, 38, c_out)
out.set(41, 38, c_out)
out.set(42, 38, c_out)
out.set(43, 38, c_out)
out.set(44, 38, c_out)

finish(out)
