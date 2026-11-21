# quick inspection of the seaside canvas regions
c = canvas("seaside")
print(c.stats_text())
print("---- umbrella region ----")
print(c.matrix_text(region=(10, 28, 55, 62)))
print("---- horizon/foam ----")
print(c.matrix_text(region=(0, 50, 40, 90)))
