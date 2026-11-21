# 48x48 two-frame slash-effect sprite sheet.
# Frame cells are 24x48: anticipation slash on the left, impact slash on the right.

result = new_canvas(48, 48, background=None, name="slash_effect_2_frames")

WHITE = "#fffef4"
HOT = "#ffffff"
PALE = "#dff6ff"
BLUE = "#8edfff"
FADE = "#55bde8"

# Frame 1: compact rising arc, thin at both tips.
# Outer pale-blue rim.
result.poly([(3,34),(4,29),(6,24),(9,20),(13,17),(17,16),(20,17),
             (17,18),(13,20),(10,23),(8,27),(7,31),(7,34)], PALE)
# Hollow the inside to leave a narrow crescent.
result.poly([(7,33),(8,29),(10,25),(13,22),(17,19),(20,18),
             (17,18),(13,20),(10,23),(8,27),(7,31)], None)
# Bright cutting edge, deliberately stepped.
result.poly([(3,34),(4,29),(6,24),(9,20),(13,17),(17,16),(20,17),
             (16,17),(12,19),(8,23),(6,27),(5,32),(5,34)], WHITE)
# Pinpoint glints around the small slash.
result.set(5,22, PALE).set(7,19, HOT).set(19,14, HOT)
result.set(3,27, BLUE).set(9,35, BLUE)

# Frame 2: broad impact arc sweeping from lower-left to upper-right.
# Blue outer wake gives the larger frame a readable motion silhouette.
result.poly([(25,39),(25,34),(27,28),(30,22),(34,17),(39,13),(44,11),(47,11),
             (47,15),(43,15),(39,17),(35,20),(32,24),(30,29),(29,34),(30,38)], FADE)
# Pale core laid inside the wake.
result.poly([(27,38),(27,33),(29,28),(32,23),(35,19),(39,16),(44,13),(47,13),
             (47,16),(43,16),(39,18),(36,21),(33,25),(31,30),(30,35),(31,38)], PALE)
# White cutting face.
result.poly([(29,37),(29,33),(31,28),(34,23),(38,19),(42,17),(47,15),
             (47,18),(43,18),(39,20),(36,24),(33,29),(32,34),(33,37)], WHITE)
# Hard-hot highlight segments along the edge.
result.line(32,31, 35,24, HOT)
result.line(36,22, 40,19, HOT)
result.line(42,18, 46,17, HOT)

# Trailing streaks peel away behind the main sweep.
result.poly([(25,39),(31,39),(35,41),(42,42),(46,42),(46,44),(40,44),(34,43),(29,41),(25,41)], PALE)
result.poly([(26,40),(32,40),(36,42),(44,43),(47,43),(47,44),(41,44),(35,43),(30,41),(26,41)], WHITE)
result.poly([(25,35),(28,36),(33,39),(38,40),(35,40),(30,38),(25,37)], BLUE)

# Breakup pixels and speed flecks in frame 2.
result.rect(26,29,1,3, BLUE)
result.rect(28,24,1,2, PALE)
result.set(31,20, BLUE).set(34,17, PALE)
result.rect(40,12,2,1, BLUE)
result.set(45,9, PALE).set(47,8, HOT)
result.rect(36,45,3,1, BLUE)
result.rect(43,46,2,1, FADE)
result.set(31,43, WHITE).set(28,42, PALE)

view(result, scale=10, margin=0)
finish(result)
