c = new_canvas(32, 32, background=None, name="pear")

dark = "#2e5c1e"    # outline
mid  = "#5a9e34"    # main green
lite = "#8cc63f"    # highlight
stem = "#6b4a2b"    # brown stem
leaf = "#3f7d28"    # leaf
shine= "#c9e88a"    # bright shine

# body: pear shape via ellipse bottom + narrower top
c.ellipse(16, 21, 8, 8, mid)          # bottom bulb rows 13-28
c.ellipse(16, 13, 5, 6, mid)          # upper bulb rows 7-18
# outline
c.ellipse(16, 21, 8, 8, dark, fill=False)
c.ellipse(16, 13, 5, 6, dark, fill=False)
# fill seams: repaint interior to merge
c.ellipse(16, 21, 7, 7, mid)
c.ellipse(16, 13, 4, 5, mid)
c.rect(12, 13, 9, 3, mid)             # join the two lobes

# stem
c.line(16, 6, 17, 2, stem)
c.set(15, 6, stem)

# leaf
c.ellipse(21, 4, 3, 1, leaf)
c.set(24, 4, leaf)

# highlight
c.ellipse(12, 18, 2, 3, lite)
c.set(11, 16, shine)
c.set(12, 15, shine)
c.set(13, 15, shine)

print(c.stats_text())
save("green-pear", c)
finish(c)
