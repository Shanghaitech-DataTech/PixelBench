out = input_canvas.copy(name="output")

# Climbing vines over the tower's stone walls.
vine = '#274b32'
vine_light = '#3c7040'
leaf = '#4f8250'
for pts in [
    [(46, 209), (47, 198), (45, 190), (49, 181), (48, 172), (51, 164), (50, 155), (53, 147)],
    [(97, 213), (94, 204), (96, 196), (92, 187), (94, 179), (90, 171), (92, 161), (89, 153)],
    [(54, 187), (57, 181), (57, 174), (60, 169)],
    [(91, 197), (87, 191), (86, 184), (83, 179)],
]:
    for a, b in zip(pts, pts[1:]):
        out.line(a[0], a[1], b[0], b[1], vine)
for x, y in [(46,202),(43,194),(49,188),(45,179),(51,173),(47,163),(54,181),(58,174),(53,157),
              (96,207),(98,198),(91,192),(96,184),(90,176),(94,166),(87,187),(84,181),(90,157)]:
    out.set(x, y, leaf)
    out.set(x + (1 if x < 72 else -1), y - 1, vine_light)

# Rear-facing hood and cloak, stepping through the arch.
shadow = '#111b1c'
cloak = '#263033'
cloak_hi = '#3c4746'
hem = '#161f20'
# Hood silhouette and dark face opening point toward the doorway.
out.ellipse(73, 212, 4, 4, shadow)
out.ellipse(73, 211, 3, 3, cloak)
out.rect(71, 212, 5, 3, shadow)
out.rect(72, 212, 3, 2, '#172022')
# shoulders, tapered cloak and a forward step
out.poly([(69,216),(73,214),(77,216),(80,222),(79,232),(76,239),(66,238),(65,231),(66,222)], shadow)
out.poly([(70,217),(73,216),(76,218),(78,224),(77,231),(74,236),(68,235),(67,230),(68,222)], cloak)
out.line(73, 218, 72, 231, cloak_hi)
out.line(76, 220, 76, 232, shadow)
out.poly([(68,235),(73,236),(72,242),(68,243),(66,241)], hem)
out.poly([(73,236),(77,234),(79,239),(78,243),(73,242)], hem)
out.line(67, 243, 71, 243, '#0d1516')
out.line(74, 243, 79, 243, '#0d1516')
# arms angled forward toward the arch
out.line(68, 219, 64, 225, cloak)
out.line(78, 219, 81, 225, cloak_hi)
out.set(64, 225, '#c0a77a')
out.set(81, 225, '#c0a77a')
# staff held at the left, with a small luminous head
out.line(62, 213, 64, 234, '#6f573b')
out.line(62, 214, 63, 232, '#b28a4c')
out.circle(62, 211, 4, '#286b77')
out.circle(62, 211, 2, '#65d9e5')
out.set(62, 211, '#d5ffff')
out.set(62, 206, '#4aaeba')
out.set(57, 211, '#397f8a')
out.set(67, 211, '#397f8a')
out.set(62, 216, '#397f8a')

print(out.stats_text())
print(out.matrix_text(region=(42, 194, 101, 246)))
finish(out)
