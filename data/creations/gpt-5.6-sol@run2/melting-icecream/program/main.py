# Build the edited sprite from an exact copy of the supplied image.
out = input_canvas.copy(name='output')

# Reuse the sprite's established outline family and add a compact chocolate ramp.
outline = out.color('#5e363e', name='melt_outline')
deep = out.color('#6f382f', name='chocolate_deep')
choc = out.color('#87483b', name='chocolate')
light = out.color('#a65b49', name='chocolate_light')
glint = out.color('#c87859', name='chocolate_glint')

# Softened chocolate lip over the top edge of the cone. The stepped edge keeps
# the original low-resolution style while establishing a continuous melt.
out.poly([(18,32),(34,32),(34,37),(32,37),(32,42),(29,42),(29,38),
          (27,38),(27,48),(24,48),(24,39),(22,39),(22,44),(19,44),(19,37),(18,37)],
         outline)
out.poly([(19,32),(33,32),(33,36),(31,36),(31,41),(30,41),(30,36),
          (27,36),(27,47),(25,47),(25,37),(22,37),(22,43),(20,43),(20,36),(19,36)],
         choc)

# Darker underside and rounded drip tips add weight and separation from cone.
out.rect(20,34,2,5,deep)
out.set(21,40,deep)
out.rect(25,35,2,9,deep)
out.set(26,46,deep)
out.rect(30,34,2,5,deep)
out.set(30,40,deep)

# Reflected warm light on the glossy moving chocolate.
out.rect(20,33,8,2,light)
out.rect(28,33,4,1,light)
out.rect(22,35,3,1,light)
out.rect(25,36,1,5,light)
out.set(26,35,glint)
out.set(21,34,glint)
out.set(25,42,glint)

# Restore a few crisp outline pixels at the outer silhouette.
out.set(18,33,outline)
out.set(18,34,outline)
out.set(19,43,outline)
out.set(22,44,outline)
out.set(24,47,outline)
out.set(27,47,outline)
out.set(29,41,outline)
out.set(32,41,outline)
out.set(33,36,outline)

print(out.stats_text())
print(out.matrix_text((15,29,38,51)))
view(out, scale=8, margin=0)
finish(out)
