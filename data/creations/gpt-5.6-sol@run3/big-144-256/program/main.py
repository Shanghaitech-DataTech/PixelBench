from pixelbench_api import *

output = input_canvas.copy(name="output")

# Palette tuned to the existing blue-green dusk masonry.
vine_shadow = output.color("#173f3b", name="vine_shadow")
vine_mid = output.color("#24564a", name="vine_mid")
vine_light = output.color("#3b6a54", name="vine_light")
vine_tip = output.color("#568064", name="vine_tip")
cloak_deep = output.color("#171e2a", name="cloak_deep")
cloak = output.color("#252c3d", name="cloak")
cloak_mid = output.color("#34394b", name="cloak_mid")
cloak_edge = output.color("#485064", name="cloak_edge")
boot = output.color("#111923", name="boot")
staff_dark = output.color("#4a3324", name="staff_dark")
staff_wood = output.color("#806043", name="staff_wood")
glow_dim = output.color("#9b7238", name="glow_dim")
glow = output.color("#e0aa4c", name="staff_glow")
glow_hot = output.color("#ffe18a", name="glow_hot")

# Ivy climbing the round tower: irregular stems follow mortar and curve around the wall.
output.line(41, 188, 43, 171, vine_shadow)
output.line(43, 171, 39, 157, vine_mid)
output.line(39, 157, 44, 144, vine_mid)
output.line(44, 144, 41, 132, vine_shadow)
output.line(42, 167, 50, 160, vine_mid)
output.line(50, 160, 53, 149, vine_shadow)
output.line(44, 146, 51, 139, vine_mid)
output.line(51, 139, 49, 129, vine_shadow)
output.line(40, 158, 34, 151, vine_shadow)

# Angular leaf clusters, kept small enough to preserve the original stone texture.
for pts, col in [
    ([(39,181),(35,178),(36,174),(42,176)], vine_mid),
    ([(43,173),(47,168),(50,170),(47,175)], vine_light),
    ([(40,164),(35,161),(36,157),(42,160)], vine_light),
    ([(45,157),(49,153),(53,155),(49,159)], vine_mid),
    ([(39,153),(34,149),(35,146),(41,149)], vine_tip),
    ([(44,146),(47,141),(52,141),(49,146)], vine_light),
    ([(42,138),(37,135),(38,131),(43,134)], vine_mid),
    ([(49,134),(53,130),(56,132),(52,136)], vine_light),
    ([(52,151),(56,147),(59,149),(55,153)], vine_mid),
]:
    output.poly(pts, col)

# Older growth climbs the cylindrical upper wall in broken patches.
output.line(91, 143, 88, 130, vine_shadow)
output.line(88, 130, 91, 117, vine_mid)
output.line(91, 117, 87, 104, vine_shadow)
output.line(87, 104, 90, 91, vine_mid)
output.line(89, 125, 80, 119, vine_shadow)
output.line(89, 111, 98, 105, vine_shadow)
output.line(88, 99, 81, 94, vine_mid)
output.line(90, 92, 98, 87, vine_shadow)
for pts, col in [
    ([(88,133),(83,129),(84,125),(90,129)], vine_mid),
    ([(90,121),(94,116),(99,118),(95,122)], vine_light),
    ([(86,113),(80,109),(81,105),(87,109)], vine_mid),
    ([(90,105),(95,100),(100,102),(96,106)], vine_light),
    ([(87,98),(82,94),(83,90),(89,94)], vine_tip),
    ([(91,91),(96,86),(101,88),(97,92)], vine_mid),
    ([(80,120),(75,116),(77,112),(82,116)], vine_light),
    ([(98,105),(103,101),(107,103),(103,107)], vine_mid),
]:
    output.poly(pts, col)
# Small gripping tendrils branch over nearby stones.
output.line(88, 130, 80, 133, vine_mid)
output.line(91, 117, 100, 121, vine_mid)
output.line(87, 104, 78, 101, vine_shadow)
output.set(79, 132, vine_tip)
output.set(101, 120, vine_tip)
output.set(77, 100, vine_tip)

# A second trailing strand spreads across the right side of the entrance wall.
output.line(91, 181, 88, 166, vine_shadow)
output.line(88, 166, 93, 153, vine_mid)
output.line(93, 153, 89, 140, vine_shadow)
output.line(89, 140, 94, 129, vine_mid)
output.line(90, 157, 82, 151, vine_shadow)
output.line(88, 168, 80, 163, vine_mid)
output.line(91, 145, 99, 139, vine_shadow)
for pts, col in [
    ([(89,176),(84,172),(85,169),(91,171)], vine_mid),
    ([(88,166),(92,161),(96,163),(92,168)], vine_light),
    ([(86,159),(80,156),(81,152),(87,155)], vine_tip),
    ([(92,153),(96,148),(100,150),(96,154)], vine_mid),
    ([(89,145),(84,142),(85,138),(91,141)], vine_light),
    ([(94,137),(98,132),(102,134),(98,139)], vine_tip),
]:
    output.poly(pts, col)

# Sparse hanging tendrils below the tower ledge.
output.line(73, 153, 74, 169, vine_shadow)
output.line(74, 169, 71, 177, vine_mid)
output.poly([(73,160),(68,157),(69,154),(74,157)], vine_mid)
output.poly([(74,170),(78,166),(81,168),(77,172)], vine_light)

# Back-facing mage entering the archway. The hood and shoulders overlap the dark doorway.
output.poly([(57,207),(59,203),(63,201),(67,203),(69,208),(67,213),(59,213),(56,210)], cloak_deep)
output.poly([(59,206),(62,203),(66,204),(68,209),(66,211),(60,210)], cloak_mid)
output.set(61, 204, cloak_edge)
output.set(66, 206, cloak_edge)

# Cloak body tapers into the doorway; asymmetric hem and separated boots imply a forward step.
output.poly([(57,210),(61,208),(68,209),(72,216),(72,230),(68,235),(61,234),(55,231),(55,219)], cloak_deep)
output.poly([(59,211),(64,210),(69,213),(69,229),(65,232),(59,230),(57,220)], cloak)
output.line(60, 213, 58, 228, cloak_mid)
output.line(67, 213, 69, 227, cloak_mid)
output.line(58, 229, 63, 232, cloak_edge)
output.set(57, 217, cloak_edge)
output.set(68, 216, cloak_edge)
# Arm reaching toward the staff.
output.poly([(68,213),(72,215),(74,220),(72,222),(69,218)], cloak)
output.set(72, 219, cloak_edge)
# Feet: one already forward into shadow, one trailing behind.
output.rect(61, 232, 3, 5, boot)
output.rect(68, 231, 3, 4, boot)
output.set(60, 236, boot)
output.set(64, 235, cloak_mid)

# Staff held on the mage's right, with a hooked crown and a compact magical glow.
output.line(74, 205, 74, 233, staff_dark)
output.line(75, 205, 75, 232, staff_wood)
output.line(75, 205, 78, 201, staff_wood)
output.line(78, 201, 76, 198, staff_wood)
# Pixel halo, bright crystal and reflected highlights.
output.set(76, 196, glow_dim)
output.set(79, 197, glow_dim)
output.set(81, 200, glow_dim)
output.set(79, 203, glow_dim)
output.set(73, 200, glow_dim)
output.poly([(77,196),(80,198),(80,201),(77,204),(74,201),(74,198)], glow)
output.rect(76, 198, 3, 4, glow_hot)
output.set(75, 199, glow_hot)
output.set(79, 199, glow_hot)
output.set(73, 214, glow_dim)
output.set(72, 216, glow_dim)

view(output)
finish(output)
