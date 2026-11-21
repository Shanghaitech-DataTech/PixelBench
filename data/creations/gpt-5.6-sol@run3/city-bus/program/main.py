# 64x32 modern city bus side-view sprite
result = new_canvas(64, 32, background=None, name="city_bus")

# Compact transit palette
outline = "#16212b"
deep = "#233440"
window = "#294957"
window_light = "#3f6977"
glass_glint = "#79a5ad"
body = "#d9e1df"
body_hi = "#f3f5ed"
body_shadow = "#aab8b8"
teal = "#1e9696"
teal_dark = "#147274"
amber = "#f4aa32"
red = "#d94b3f"
rubber = "#15191d"
hub = "#73868a"
hub_hi = "#b7c4c1"

# Main silhouette: squared rear, softened stepped front.
result.poly([(3,8),(6,5),(55,5),(59,7),(62,12),(62,25),(59,28),(5,28),(2,25),(2,11)], outline)

# Body panels, including the high roof and lower skirt.
result.poly([(4,10),(7,7),(54,7),(58,9),(60,13),(60,23),(57,26),(5,26),(4,24)], body)
result.rect(5,19,54,6,body_hi)
result.rect(4,23,56,3,teal)
result.rect(6,26,51,2,teal_dark)
result.rect(7,7,45,1,body_hi)

# Rear cap and lamps.
result.rect(3,12,2,11,body_shadow)
result.rect(3,14,1,5,red)
result.set(3,13,"#f27b4f")
result.rect(3,21,1,2,amber)

# Window band, separated into clean passenger bays.
result.rect(6,9,43,10,outline)
result.rect(7,10,8,8,window)
result.rect(16,10,8,8,window)
result.rect(25,10,8,8,window)
result.rect(34,10,8,8,window)
result.rect(43,10,6,8,window)
# Cool reflected sky pixels.
result.rect(8,10,6,1,window_light)
result.rect(17,10,6,1,window_light)
result.rect(26,10,6,1,window_light)
result.rect(35,10,6,1,window_light)
result.line(8,12,11,12,glass_glint)
result.line(27,12,30,12,glass_glint)
result.set(44,11,glass_glint)

# Rear door assembly, behind the rear axle area.
result.rect(20,9,8,17,outline)
result.rect(21,10,3,9,window)
result.rect(25,10,2,9,window)
result.rect(21,20,3,5,body_shadow)
result.rect(25,20,2,5,body_shadow)
result.line(24,10,24,25,deep)
result.set(23,20,body_hi)
result.set(25,20,body_hi)

# Driver windshield and angled modern front mask.
result.poly([(50,8),(54,8),(57,10),(59,14),(59,18),(50,18)], outline)
result.poly([(51,9),(54,9),(56,11),(58,15),(58,17),(51,17)], window)
result.line(52,10,55,10,window_light)
result.set(57,14,glass_glint)

# Front double door, low floor style.
result.rect(50,18,9,8,outline)
result.rect(51,19,3,6,window)
result.rect(55,19,3,6,window)
result.line(54,19,54,25,deep)
result.set(53,22,glass_glint)
result.set(55,22,glass_glint)

# Electronic route display, kept intentionally generic.
result.rect(7,6,13,3,outline)
result.rect(8,7,11,1,"#573f20")
result.set(9,7,amber)
result.set(10,7,amber)
result.set(12,7,amber)
result.set(15,7,amber)
result.set(17,7,amber)

# Lower body articulation and utility panels.
result.rect(29,20,18,1,body_shadow)
result.line(31,21,46,21,"#c8d2d0")
result.rect(31,24,12,1,body_shadow)
result.rect(44,24,3,1,deep)
result.set(47,24,amber)
result.rect(6,23,2,1,deep)

# Front bumper and lighting.
result.rect(59,20,2,4,body_shadow)
result.rect(60,19,2,2,amber)
result.set(61,19,"#ffe28a")
result.rect(59,24,3,2,deep)
result.rect(60,24,2,1,body_shadow)

# Wheel wells overpaint the skirt, then tires and hubs define the wheels.
for cx in (14, 48):
    result.circle(cx,27,4,outline)
    result.circle(cx,27,3,rubber)
    result.circle(cx,27,2,hub)
    result.set(cx,26,hub_hi)
    result.set(cx-1,27,hub_hi)
    result.set(cx,28,deep)
# Flatten wheel tops slightly into the body for a grounded bus profile.
result.line(11,23,17,23,outline)
result.line(45,23,51,23,outline)

# Pixel accents and crisp chassis baseline.
result.rect(21,27,22,1,deep)
result.rect(4,26,4,1,outline)
result.rect(56,26,3,1,outline)
result.set(5,9,body_hi)
result.set(6,8,body_hi)

view(result, scale=12, margin=1, edges="all")
finish(result)
