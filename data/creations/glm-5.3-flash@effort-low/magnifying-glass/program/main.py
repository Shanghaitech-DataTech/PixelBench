c = new_canvas(16, 16, name="magnifier")

# ring: circle outline centered ~ (7,7), radius 5
c.circle(7, 7, 5, "#2b3a67", fill=False)
c.circle(7, 7, 4, "#9fd8ef", fill=False)  # inner glass tint ring
c.circle(7, 7, 3, "#d9f2ff", fill=True)   # glass fill
# highlight
c.set(5, 5, "#ffffff")
c.set(6, 5, "#ffffff")
c.set(5, 6, "#ffffff")

# handle from ring edge (11,11) to bottom-right
c.line(11, 11, 14, 14, "#8a5a2b")
c.set(11, 10, "#8a5a2b")
c.set(10, 11, "#8a5a2b")
c.set(14, 15, "#5c3a1a")
c.set(15, 14, "#5c3a1a")
c.set(15, 15, "#5c3a1a")

print(c.stats_text())
print(c.matrix_text())
save("magnifier", c)
finish(c)
