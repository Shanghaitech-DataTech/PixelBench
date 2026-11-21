from pixelbench_api import new_canvas, view, finish

# Four-color mushroomling sprite on transparency.
result = new_canvas(16, 16, background=None, name="mushroomling")

dark = result.color("#241b22", name="outline")
red = result.color("#d9363e", name="cap_red")
white = result.color("#fff4df", name="spot_white")
tan = result.color("#d89b62", name="body_tan")

# Cap silhouette and red interior.
result.poly([(6, 1), (10, 1), (10, 2), (12, 2), (12, 3),
             (14, 3), (14, 5), (15, 5), (15, 7), (14, 7),
             (14, 8), (2, 8), (2, 7), (1, 7), (1, 5),
             (2, 5), (2, 4), (4, 4), (4, 2), (6, 2)], dark)
result.poly([(6, 2), (10, 2), (10, 3), (12, 3), (12, 4),
             (14, 4), (14, 7), (13, 7), (13, 8), (3, 8),
             (3, 7), (2, 7), (2, 5), (4, 5), (4, 3), (6, 3)], red)

# Cap spots, deliberately chunky and asymmetric.
result.rect(6, 2, 2, 2, white)
result.set(5, 3, white)
result.rect(11, 4, 2, 2, white)
result.rect(3, 6, 2, 1, white)
result.rect(8, 6, 2, 2, white)

# Body, feet, and stubby arms in the dark silhouette.
result.rect(5, 7, 6, 6, dark)
result.rect(3, 9, 3, 3, dark)
result.set(2, 10, dark)
result.rect(10, 9, 3, 3, dark)
result.set(13, 10, dark)
result.rect(4, 12, 4, 3, dark)
result.rect(8, 12, 4, 3, dark)

# Warm body fill and limbs.
result.rect(6, 8, 4, 4, tan)
result.set(4, 10, tan)
result.set(3, 10, tan)
result.set(11, 10, tan)
result.set(12, 10, tan)
result.rect(5, 12, 2, 2, tan)
result.rect(9, 12, 2, 2, tan)

# Paired high-contrast eyes and a tiny centered mouth.
result.set(6, 9, white)
result.set(9, 9, white)
result.set(7, 11, dark)
result.set(8, 11, dark)

view(result, scale=24, margin=1, edges="all")
finish(result)
