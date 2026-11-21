# Modern city bus side-view sprite, 64x32, transparent background.
result = new_canvas(64, 32, background=None, name="city-bus")

# Palette
outline = "#172532"
deep = "#203443"
tire = "#111820"
rubber_hi = "#34444d"
hub = "#91a7ad"
hub_hi = "#d5e1df"
body = "#dce8e6"
body_hi = "#f4faf7"
body_shade = "#9fb5b4"
teal = "#168c91"
teal_hi = "#27b2ae"
teal_dark = "#11656d"
window = "#244554"
window_hi = "#3e6b78"
window_glint = "#78a3ab"
door_glass = "#2c5260"
route_bg = "#15252d"
route_led = "#f2c84b"
headlight = "#fff0a6"
red = "#e75950"

# Main bus silhouette and underbody.
result.poly([(3,9),(7,6),(54,6),(59,9),(61,14),(61,25),(58,27),(6,27),(3,24)], outline)
result.rect(4,10,56,14,body)
result.rect(6,7,48,3,body_hi)
result.rect(4,23,56,3,teal_dark)
result.rect(8,26,48,2,outline)
result.set(4,24,teal)
result.set(5,25,teal)
result.set(59,24,teal_dark)

# Window band, including sloped front windshield.
result.rect(7,9,43,9,outline)
result.rect(8,10,41,7,window)
result.poly([(50,9),(55,9),(59,13),(59,17),(51,17)], outline)
result.poly([(51,10),(54,10),(58,13),(58,16),(51,16)], window)

# Window reflections and separators.
for x in (16,25,34,43):
    result.rect(x,9,2,9,outline)
result.line(9,10,15,10,window_hi)
result.line(18,10,24,10,window_hi)
result.line(27,10,33,10,window_hi)
result.line(36,10,42,10,window_hi)
result.line(45,10,48,10,window_hi)
result.set(10,11,window_glint)
result.set(19,11,window_glint)
result.set(28,11,window_glint)
result.set(37,11,window_glint)
result.line(52,11,55,12,window_hi)

# Rear electronic route display.
result.rect(6,7,12,4,route_bg)
result.rect(7,8,2,2,route_led)
result.set(10,8,route_led)
result.set(11,8,route_led)
result.set(13,8,route_led)
result.set(14,8,route_led)
result.set(15,9,route_led)

# Rear door: narrow double-leaf assembly.
result.rect(18,17,9,9,outline)
result.rect(19,18,3,7,door_glass)
result.rect(23,18,3,7,door_glass)
result.line(19,22,21,22,window_hi)
result.line(24,22,25,22,window_hi)
result.rect(22,18,1,8,deep)
result.set(20,24,body_shade)
result.set(24,24,body_shade)

# Front door: broad low-floor double doors.
result.rect(43,17,10,10,outline)
result.rect(44,18,3,7,door_glass)
result.rect(48,18,4,7,door_glass)
result.rect(47,18,1,8,deep)
result.line(44,22,46,22,window_hi)
result.line(49,22,51,22,window_hi)
result.rect(44,25,8,1,body_shade)

# Body accents, handles, panel lines.
result.rect(7,19,10,3,teal)
result.rect(7,22,10,1,teal_hi)
result.rect(28,19,14,3,teal)
result.rect(28,22,14,1,teal_hi)
result.line(6,18,17,18,body_shade)
result.line(28,18,42,18,body_shade)
result.set(25,20,hub_hi)
result.set(50,20,hub_hi)
result.line(54,19,58,19,body_shade)
result.line(54,20,58,20,body_shade)

# Front and rear lighting / bumpers.
result.rect(59,18,2,3,headlight)
result.set(60,17,body_hi)
result.rect(2,19,2,3,red)
result.rect(2,23,3,2,deep)
result.rect(59,24,3,2,deep)
result.set(58,23,teal_hi)

# Wheel wells restore dark arches over body.
result.circle(14,25,5,outline)
result.circle(51,25,5,outline)
# Mask upper wheel circles back into body to create compact squared arches.
result.rect(8,20,12,4,body)
result.rect(45,20,12,4,body)
result.rect(9,22,10,2,teal)
result.rect(46,22,10,2,teal)
# Tires and hubs.
for cx in (14,51):
    result.circle(cx,26,5,tire)
    result.circle(cx,26,3,rubber_hi)
    result.circle(cx,26,2,hub)
    result.circle(cx,26,1,hub_hi)
    result.set(cx,26,deep)
    result.set(cx-3,25,"#596b70")

# Ground-facing shadow pixels and final silhouette details.
result.line(20,27,45,27,deep)
result.set(7,26,outline)
result.set(57,26,outline)
result.set(3,12,body_shade)
result.set(3,13,body_shade)
result.set(60,13,outline)

view(result, scale=8, margin=0)
finish(result)
