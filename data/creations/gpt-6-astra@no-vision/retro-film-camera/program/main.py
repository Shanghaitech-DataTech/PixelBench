# 32x32 retro film camera item sprite
c = new_canvas(32, 32, name="retro-film-camera")

ink = "#171923"
shadow = "#292a31"
leather = "#75452f"
leather_hi = "#a6653e"
leather_lo = "#543327"
metal = "#c2a66b"
metal_hi = "#f0d796"
steel = "#79828a"
glass = "#315267"
glass_hi = "#78a6ac"
black = "#101820"

# Main body silhouette and stepped top plate
c.rect(3, 10, 26, 17, ink)
c.rect(5, 8, 22, 2, ink)
c.rect(7, 6, 7, 4, ink)
c.rect(18, 7, 8, 3, ink)
# Leather front panel
c.rect(5, 12, 22, 13, leather)
c.rect(7, 10, 18, 2, leather)
c.rect(5, 25, 22, 1, shadow)
# Leather texture / side panels
c.rect(5, 13, 2, 10, leather_lo)
c.rect(25, 13, 2, 10, leather_lo)
c.rect(8, 13, 2, 1, leather_hi)
c.rect(11, 13, 2, 1, leather_hi)
c.rect(8, 23, 2, 1, leather_hi)
c.rect(22, 23, 2, 1, leather_hi)
c.rect(7, 15, 1, 7, shadow)
c.rect(24, 15, 1, 7, shadow)
# Top finder / flash housing
c.rect(8, 7, 5, 2, steel)
c.set(9, 7, metal_hi)
c.rect(19, 8, 6, 2, metal)
c.rect(20, 8, 4, 1, metal_hi)
# Shutter button
c.rect(15, 6, 3, 2, ink)
c.rect(15, 5, 3, 2, metal)
c.set(16, 5, metal_hi)
# Lens bezel and concentric glass
c.rect(10, 14, 13, 11, ink)
c.rect(11, 13, 11, 13, ink)
c.rect(12, 14, 9, 11, metal)
c.rect(13, 15, 7, 9, shadow)
c.rect(14, 16, 5, 7, steel)
c.rect(15, 17, 3, 5, glass)
c.rect(16, 17, 2, 3, glass_hi)
c.set(15, 18, black)
c.set(18, 21, black)
c.set(16, 17, "#b4d0c3")
# Small lens rim highlights
c.line(12, 15, 13, 14, metal_hi)
c.line(20, 23, 21, 22, metal_hi)
# Front badges and control details
c.rect(7, 11, 4, 1, metal)
c.rect(22, 11, 3, 1, metal_hi)
c.rect(7, 24, 4, 1, metal_hi)
c.rect(22, 24, 3, 1, metal)
c.rect(26, 15, 1, 6, steel)
c.set(27, 16, metal_hi)
# subtle edge glints
c.line(4, 11, 6, 9, shadow)
c.line(27, 9, 29, 11, shadow)

print(c.stats_text())
print(c.matrix_text(region=(2, 4, 30, 28)))
finish(c)
