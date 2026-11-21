from pixelbench_api import *

# 64x64 subway platform scene
c = new_canvas(64, 64, background="#10151d", name="subway-platform")

# Palette
ink = "#0b1017"
near_black = "#121820"
steel = "#293541"
steel_hi = "#445461"
cream = "#d8d2b8"
light = "#f2e6b6"
cyan = "#6ec1c6"
cyan_hi = "#b6eef0"
blue = "#34738c"
train = "#78858a"
train_dark = "#4a5960"
train_hi = "#aeb9b8"
window = "#183247"
red = "#d4564a"
yellow = "#e7b84e"
platform = "#58616a"
platform_hi = "#8b9394"
skin = "#c88d69"
coat1 = "#2d6173"
coat2 = "#9b4d43"
coat3 = "#4e3d68"
white = "#e8ece4"

# Ceiling and tunnel depth bands
c.rect(0, 0, 64, 5, ink)
c.rect(0, 5, 64, 2, steel)
c.rect(0, 7, 64, 1, steel_hi)
# Ceiling strip lights, diminishing to the right
for x, w in [(2,10),(17,8),(31,7),(44,5),(54,4)]:
    c.rect(x, 2, w, 1, cream)
    c.set(x, 3, "#625f55")

# Train body, visible behind platform screen doors
c.rect(0, 9, 64, 29, train_dark)
c.rect(0, 10, 64, 3, train_hi)
c.rect(0, 13, 64, 19, train)
c.rect(0, 32, 64, 5, "#68757a")
c.rect(0, 36, 64, 2, ink)
# Speed streaks along train skin
c.rect(1, 14, 15, 1, "#9ca8a7")
c.rect(21, 14, 9, 1, "#95a1a0")
c.rect(36, 14, 16, 1, "#aab3b1")
c.rect(55, 14, 8, 1, "#8e9a9a")
c.rect(2, 33, 21, 1, "#899497")
c.rect(29, 33, 13, 1, "#899497")
c.rect(47, 33, 16, 1, "#899497")

# Train windows and rushing interior highlights
for x, w in [(1,11),(15,10),(28,11),(42,9),(54,9)]:
    c.rect(x, 17, w, 11, ink)
    c.rect(x+1, 18, w-2, 9, window)
    c.rect(x+2, 19, max(2,w-5), 2, cyan)
    c.rect(x+w-3, 19, 1, 7, "#275168")
# motion smears through windows
c.rect(2, 23, 8, 1, cyan_hi)
c.rect(16, 25, 7, 1, "#85b8b8")
c.rect(29, 22, 9, 1, cyan_hi)
c.rect(43, 24, 6, 1, "#85b8b8")
c.rect(55, 21, 7, 1, cyan_hi)
# red beltline
c.rect(0, 29, 64, 2, red)
c.rect(0, 29, 64, 1, "#ed7767")

# Cab end entering from the right: angled mask, windshield, marker lights
c.poly([(53,13),(63,15),(63,32),(53,31)], "#536269")
c.poly([(55,16),(63,17),(63,26),(55,25)], ink)
c.poly([(56,17),(63,18),(63,24),(56,24)], "#193548")
c.rect(61, 19, 2, 2, cyan_hi)
c.rect(60, 27, 3, 2, light)
c.set(59,27,yellow)
c.rect(53, 29, 11, 2, red)
c.line(53, 13, 53, 31, train_hi)

# Platform screen doors: glass tint and strong vertical mullions
c.rect(0, 8, 64, 30, "#70a9aa33")
c.rect(0, 8, 64, 2, near_black)
for x in [0, 13, 26, 39, 52, 63]:
    c.rect(x, 8, 2 if x < 63 else 1, 32, ink)
    if x < 63:
        c.rect(x+1, 10, 1, 27, steel_hi)
# door split rails and handles
for x in [7,20,33,46,59]:
    c.rect(x, 10, 1, 28, steel)
    c.rect(x-1, 25, 1, 4, light)
c.rect(0, 37, 64, 3, near_black)
c.rect(0, 37, 64, 1, steel_hi)

# Station sign, generic and brand-free
c.rect(3, 6, 22, 7, ink)
c.rect(4, 7, 20, 5, "#276c79")
c.rect(5, 8, 3, 3, white)
c.rect(10, 8, 10, 1, white)
c.rect(10, 10, 7, 1, "#b8d4d1")
c.rect(22, 8, 1, 3, yellow)
# hanging direction sign
c.rect(44, 5, 1, 4, steel_hi)
c.rect(43, 8, 17, 6, ink)
c.rect(44, 9, 15, 4, "#e5dfc6")
c.line(46, 11, 49, 11, blue)
c.set(49,10,blue); c.set(49,12,blue)
c.rect(52, 10, 5, 1, near_black)

# Platform floor with depth lines
c.rect(0, 40, 64, 24, platform)
c.rect(0, 40, 64, 2, platform_hi)
c.rect(0, 43, 64, 3, "#b7a64f")
c.dither(0, 43, 64, 3, [yellow, "#9f8738"], pattern="checker")
c.rect(0, 46, 64, 1, ink)
c.line(0, 55, 63, 49, "#68727a")
c.line(0, 63, 63, 54, steel)
c.line(20, 63, 28, 46, "#6e777e")
c.line(48, 63, 44, 46, "#444e57")
# floor tile joints
c.line(7, 47, 3, 63, "#48535d")
c.line(58, 47, 63, 60, "#737b80")

# Bench behind passengers
c.rect(24, 42, 20, 2, ink)
c.rect(25, 41, 18, 2, "#a87948")
c.rect(26, 45, 16, 2, ink)
c.rect(27, 44, 14, 2, "#b88954")
c.rect(27, 47, 2, 8, near_black)
c.rect(39, 47, 2, 8, near_black)
c.rect(24, 54, 7, 2, steel_hi)
c.rect(37, 54, 7, 2, steel_hi)

# Passenger 1: standing left, looking at phone, backpack
# legs
c.rect(9, 52, 3, 10, ink); c.rect(14, 52, 3, 10, ink)
c.rect(8, 61, 5, 2, near_black); c.rect(14, 61, 5, 2, near_black)
# coat and head
c.poly([(8,39),(15,38),(18,52),(8,54)], coat1)
c.rect(7, 43, 2, 10, "#234b59")
c.rect(15, 40, 4, 2, coat1)
c.rect(18, 41, 2, 5, skin)
c.rect(18, 40, 3, 4, near_black)
c.rect(10, 34, 6, 6, skin)
c.rect(9, 33, 7, 4, near_black)
c.set(15,37,skin)
# phone
c.rect(20, 39, 2, 4, ink); c.set(20,40,cyan_hi)
# backpack silhouette
c.rect(5, 41, 4, 10, "#1b3039"); c.rect(4, 44, 2, 6, "#1b3039")

# Passenger 2: seated, leaning forward with elbows on knees
c.rect(30, 42, 7, 7, coat2)
c.poly([(29,48),(36,47),(40,53),(38,55),(33,51)], "#743b38")
c.circle(33, 38, 3, skin)
c.rect(30, 35, 6, 3, near_black)
c.set(36,38,skin)
# bent arms and clasped hands
c.line(31,45,27,51,coat2); c.line(32,45,38,50,coat2)
c.rect(26,50,3,2,skin); c.rect(38,49,3,2,skin)
# bent legs
c.poly([(31,49),(35,49),(32,57),(29,57)], ink)
c.poly([(37,50),(40,52),(45,57),(42,59)], ink)
c.rect(26,57,7,2,near_black); c.rect(42,58,6,2,near_black)

# Passenger 3: standing right, arm raised to adjust bag strap
c.rect(52,51,3,11,ink); c.rect(58,51,3,11,ink)
c.rect(50,61,6,2,near_black); c.rect(58,61,5,2,near_black)
c.poly([(51,39),(58,38),(61,53),(50,53)], coat3)
c.circle(55,34,3,skin)
c.rect(52,31,6,3,near_black); c.set(58,34,near_black)
# raised arm
c.line(58,41,61,34,coat3); c.line(61,34,60,29,skin)
c.rect(59,27,2,4,skin)
# shoulder bag
c.line(52,40,60,49,"#231e2c")
c.rect(59,46,4,7,"#292333")

# Small foreground highlights and platform edge marks
c.rect(1, 49, 5, 1, "#7e878b")
c.rect(20, 58, 5, 1, "#727b80")
c.rect(47, 48, 3, 1, "#92999a")

# A few hard light glints reinforce glass and motion
c.rect(3, 15, 7, 1, "#d6e2dc")
c.rect(30, 15, 5, 1, "#c9d8d5")
c.rect(56, 15, 6, 1, "#d6e2dc")

view(c, scale=8, margin=0)
finish(c)
