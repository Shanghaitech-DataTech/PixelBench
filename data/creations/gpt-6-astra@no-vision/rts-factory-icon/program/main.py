c = new_canvas(32, 32, name="factory")

# Palette
outline = "#202a35"
shadow = "#394651"
roof = "#596975"
roof_hi = "#82939a"
brick = "#ad4938"
brick_hi = "#d16a4e"
brick_shadow = "#7f352f"
vent = "#35434c"
vent_hi = "#b5c2b8"
window = "#e3bd69"
ground = "#26343d"

# Building silhouette and brick mass
c.rect(3, 13, 26, 17, outline)
c.rect(4, 14, 24, 15, brick)
c.rect(4, 14, 24, 2, brick_hi)
c.rect(4, 27, 24, 2, brick_shadow)

# Flat roof with a crisp stepped lip
c.rect(2, 11, 28, 3, outline)
c.rect(3, 11, 26, 2, roof)
c.rect(4, 11, 24, 1, roof_hi)
c.rect(5, 13, 22, 1, shadow)

# Tall chimney, integrated behind the roofline
c.rect(20, 3, 7, 10, outline)
c.rect(21, 4, 5, 8, brick)
c.rect(21, 4, 5, 2, brick_hi)
c.rect(21, 10, 5, 2, brick_shadow)
c.rect(19, 2, 9, 2, outline)
c.rect(20, 2, 7, 1, roof_hi)
c.rect(21, 6, 1, 3, brick_shadow)
c.rect(24, 7, 2, 1, brick_hi)

# Roof vents and machinery housings
c.rect(6, 7, 5, 4, outline)
c.rect(7, 8, 3, 3, vent)
c.rect(7, 8, 3, 1, vent_hi)
c.rect(13, 9, 4, 2, outline)
c.rect(14, 8, 2, 3, roof_hi)
c.rect(14, 9, 2, 1, vent)

# Recessed front windows
c.rect(7, 17, 5, 5, outline)
c.rect(8, 18, 3, 3, window)
c.rect(9, 18, 1, 3, brick_hi)
c.rect(16, 17, 5, 5, outline)
c.rect(17, 18, 3, 3, window)
c.rect(18, 18, 1, 3, brick_hi)

# Loading door and lintel
c.rect(23, 18, 3, 10, outline)
c.rect(24, 19, 1, 8, shadow)
c.rect(24, 20, 1, 1, roof_hi)
c.rect(22, 17, 5, 2, roof_hi)

# Brick courses, with staggered short highlights
c.rect(5, 16, 2, 1, brick_shadow)
c.rect(13, 15, 2, 1, brick_shadow)
c.rect(21, 15, 2, 1, brick_shadow)
c.rect(12, 19, 2, 1, brick_shadow)
c.rect(5, 23, 3, 1, brick_shadow)
c.rect(14, 23, 2, 1, brick_shadow)
c.rect(20, 24, 2, 1, brick_shadow)
c.rect(8, 25, 3, 1, brick_hi)
c.rect(16, 26, 3, 1, brick_hi)

# Foundation shadow and small ground feet
c.rect(3, 29, 26, 1, outline)
c.rect(5, 30, 4, 1, ground)
c.rect(23, 30, 4, 1, ground)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))
finish(c)
