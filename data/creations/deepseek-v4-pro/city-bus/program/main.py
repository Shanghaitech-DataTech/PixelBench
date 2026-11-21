from pixelbench_api import new_canvas, finish

c = new_canvas(64, 32, name="city_bus")

# ---- palette ----
body = c.color((46, 111, 183), name="body")
body_dark = c.color((27, 67, 112), name="body_dark")
roof_light = c.color((150, 195, 235), name="roof_light")
window = c.color((170, 220, 255), name="window")
window_dark = c.color((110, 170, 210), name="window_dark")
frame = c.color((15, 30, 50), name="frame")
door_glass = c.color((140, 195, 230), name="door_glass")
door_line = c.color((25, 55, 90), name="door_line")
tire = c.color((30, 30, 32), name="tire")
hub = c.color((160, 165, 172), name="hub")
hub_dark = c.color((110, 115, 122), name="hub_dark")
headlight = c.color((255, 236, 170), name="headlight")
headlight_dark = c.color((200, 160, 80), name="headlight_dark")
route_bg = c.color((10, 20, 35), name="route_bg")
route_text = c.color((255, 210, 60), name="route_text")
bumper = c.color((40, 45, 50), name="bumper")

# ---- main body shell ----
c.poly([(3, 22), (3, 6), (4, 4), (56, 4), (60, 8), (60, 21), (59, 22)],
       body, fill=True)

# lower darker skirt band
c.rect(3, 18, 57, 3, body_dark)

# rear edge shading
c.line(3, 6, 3, 22, body_dark)

# ---- windshield (slanted front top) ----
c.poly([(56, 5), (59, 8), (59, 13), (56, 10)], window, fill=True)
c.line(56, 4, 60, 8, frame)

# ---- windows (three panes) ----
def window_pane(x0, x1):
    w = x1 - x0 + 1
    c.rect(x0, 7, w, 6, frame)
    c.rect(x0 + 1, 8, w - 2, 4, window)
    c.rect(x0 + 1, 10, w - 2, 2, window_dark)

window_pane(6, 17)
window_pane(27, 35)
window_pane(46, 54)

# beltline between windows and lower body
c.line(5, 13, 59, 13, frame)

# ---- doors ----
# rear door
c.rect(19, 13, 7, 9, frame)
c.rect(20, 14, 5, 7, door_glass)
c.line(22, 14, 22, 20, door_line)
# front door
c.rect(37, 13, 8, 9, frame)
c.rect(38, 14, 6, 7, door_glass)
c.line(40, 14, 40, 20, door_line)

# ---- front lights / bumper ----
c.rect(58, 16, 3, 3, headlight)
c.line(58, 18, 60, 18, headlight_dark)
c.rect(57, 19, 4, 3, bumper)

# ---- electronic route display ----
c.rect(48, 5, 9, 2, route_bg)
for x, y in [(49, 5), (50, 5), (52, 5), (53, 5), (55, 5),
             (49, 6), (51, 6), (53, 6), (55, 6)]:
    c.set(x, y, route_text)

# ---- wheels ----
for cx in (14, 50):
    c.circle(cx, 23, 4, tire)
    c.circle(cx, 23, 2, hub)
    c.circle(cx, 23, 1, hub_dark)

# ---- unifying dark outline, then a light top edge on the roof ----
c.outline(frame)
c.line(4, 4, 56, 4, roof_light)

print(c.stats_text())
print(c.matrix_text())
finish(c)
