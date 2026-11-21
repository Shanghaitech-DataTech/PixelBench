from pixelbench_api import new_canvas, view, finish

# 48x48 vintage mechanical sewing machine sprite on transparency.
c = new_canvas(48, 48, background=None, name="vintage-sewing-machine")

# Palette
outline = "#171a1d"
deep = "#24282a"
metal = "#343a3b"
mid = "#4a5250"
light = "#69716b"
high = "#a7aa96"
shine = "#d5d2ae"
brass = "#b78337"
brass_hi = "#e0b95f"
red_dark = "#6f1e26"
red = "#b52f35"
red_hi = "#e05a4e"
thread = "#e4d99f"

# Cast-iron base, slightly angled in perspective.
c.poly([(4,37),(34,36),(44,39),(43,44),(9,45),(3,42)], outline)
c.poly([(6,38),(34,37),(41,39),(40,42),(9,43),(5,41)], metal)
c.line(9,43,40,42, light)
c.line(10,44,38,43, deep)
c.set(5,42, high).set(42,40, high)

# Red cloth passing beneath the foot, with a folded near edge.
c.poly([(21,36),(38,36),(44,39),(29,40)], red_dark)
c.poly([(20,35),(37,35),(43,38),(28,39)], red)
c.line(22,36,37,36, red_hi)
c.line(30,38,41,37, red_hi)
c.set(27,37, red_dark).set(36,37, red_dark)

# Main pillar rising from the base.
c.poly([(8,14),(17,12),(20,15),(20,33),(18,37),(8,38),(6,35),(7,18)], outline)
c.poly([(10,15),(16,14),(18,16),(18,32),(16,35),(9,36),(8,34),(9,18)], metal)
c.poly([(10,16),(14,15),(16,17),(16,31),(14,34),(10,34)], mid)
c.line(10,17,10,32, light)
c.set(11,17, high).set(11,18, high).set(15,16, light)

# Upper arm: long horizontal housing, tapering toward needle end.
c.poly([(10,10),(17,7),(35,8),(40,11),(39,17),(34,20),(17,19),(13,17),(8,17),(6,14)], outline)
c.poly([(11,11),(17,9),(34,10),(38,12),(37,15),(33,18),(17,17),(14,15),(9,15),(8,14)], metal)
c.poly([(17,10),(33,11),(36,12),(35,14),(17,14),(13,13)], mid)
c.line(17,10,33,11, light)
c.line(18,15,34,15, deep)
c.set(13,11, high).set(14,10, high).set(18,11, high)

# Decorative gold badge and floral dots on the body.
c.rect(12,20,4,7, deep)
c.rect(13,20,2,6, brass)
c.set(14,20, brass_hi).set(13,23, brass_hi).set(14,26, outline)
c.set(11,29, brass).set(14,30, brass_hi).set(12,32, brass)
c.line(18,12,27,12, brass)
c.set(20,11, brass_hi).set(25,13, brass_hi)

# Handwheel behind the right end, with hollow center and spokes.
c.circle(39,17,8, outline)
c.circle(39,17,6, brass)
c.circle(39,17,4, None)
c.circle(39,17,2, outline)
c.line(39,11,39,15, brass_hi)
c.line(39,19,39,23, brass_hi)
c.line(33,17,37,17, brass_hi)
c.line(41,17,45,17, brass_hi)
c.line(35,13,38,16, brass_hi)
c.line(40,18,43,21, brass_hi)
c.circle(39,17,1, shine)
c.set(44,12, outline).set(45,12, brass_hi).set(46,13, brass)

# Face plate and needle bar at the front/right end.
c.poly([(31,17),(37,15),(38,18),(35,23),(32,23)], outline)
c.poly([(33,17),(36,16),(36,20),(34,22),(33,21)], light)
c.set(34,17, high).set(35,17, shine)
c.rect(32,21,3,2, outline)

# Needle bar, clamp, needle, and thread.
c.rect(32,22,2,10, outline)
c.rect(33,22,1,9, high)
c.rect(31,28,4,3, brass)
c.set(32,28, brass_hi).set(34,30, outline)
c.line(33,31,33,37, shine)
c.set(33,37, outline)
c.line(30,12,31,12, thread)
c.line(31,12,33,22, thread)

# Presser foot, visibly gripping the fabric.
c.rect(30,33,5,2, outline)
c.rect(31,34,2,3, high)
c.line(29,37,35,37, outline)
c.line(30,36,34,36, shine)
c.set(29,36, metal).set(35,36, metal)

# Bobbin plate and base controls.
c.poly([(12,36),(27,35),(29,37),(15,39)], deep)
c.line(14,36,27,36, light)
c.rect(17,37,8,1, high)
c.set(25,36, shine)
c.rect(8,39,7,2, deep)
c.line(9,39,14,39, light)

# Small mechanical details and crisp isolated highlights.
c.circle(18,16,1, brass)
c.set(18,16, brass_hi)
c.rect(22,16,6,1, deep)
c.set(23,16, light).set(27,16, light)
c.set(7,20, outline).set(7,26, outline).set(7,32, outline)
c.set(9,34, light).set(16,34, high)

# Thread spool and pin on top.
c.line(19,5,19,9, outline)
c.rect(16,3,6,3, outline)
c.rect(17,3,4,2, thread)
c.set(17,3, shine).set(21,4, brass)
c.set(19,2, brass_hi)

# A few stitches continue out from under the presser foot.
c.set(36,37, thread).set(39,37, thread).set(42,38, thread)

view(c, scale=10, margin=1, edges="all")
finish(c)
