# Both frames share a wider transparent stage; the first retains every input pixel.
f1 = new_canvas(82, 64, name='frame1')
f1.blit(input_canvas, 3, 0)
f2 = new_canvas(82, 64, name='frame2')

# A tapered, rightward burst, behind the hand.
f2.poly([(45,21),(50,18),(49,15),(55,17),(59,12),(60,16),(66,14),(64,18),(72,16),(69,19),(79,20),(73,22),(78,24),(70,25),(73,28),(64,27),(62,30),(57,27),(52,29),(52,26),(46,26)], '#8f2911')
f2.poly([(46,22),(53,19),(52,17),(58,19),(61,15),(62,19),(68,17),(66,20),(76,20),(70,22),(76,23),(68,24),(70,26),(63,25),(61,28),(57,25),(53,27),(53,24),(46,25)], '#ec5612')
f2.poly([(48,22),(55,21),(55,19),(60,21),(63,18),(63,21),(72,21),(68,22),(73,23),(65,23),(66,25),(60,24),(59,26),(56,24),(49,24)], '#ff9c16')
f2.poly([(49,22),(58,22),(61,20),(62,22),(69,22),(64,23),(61,24),(58,23),(50,24)], '#ffe05a')
# Detached sparks and trailing tongues.
f2.line(54,15,57,13,'#f27219')
f2.set(59,11,'#ffb428')
f2.line(67,14,69,13,'#f27219')
f2.set(75,17,'#f4a30c')
f2.line(58,30,61,29,'#f27219')
f2.set(67,29,'#f4a30c')

# Repose the original pixel texture: the upper body advances, the front leg
# reaches forward, and the rear foot remains planted. Exclude the old flame.
fire = {input_canvas.color('#f27219'), input_canvas.color('#f4a30c'), input_canvas.color('#fed32c')}
for y in range(63):
    for x in range(47):
        col = input_canvas.get(x,y)
        if col in fire:
            continue
        # Invisible pixels have zero alpha.
        rgba = input_canvas.palette()[col]['rgba']
        if rgba[3] == 0:
            continue
        if y < 34:
            shift = 5 if y < 17 else 4
        elif y < 48:
            shift = 3 if x >= 18 else 0
        else:
            shift = 7 if x >= 18 else 0
        f2.set(x + 3 + shift, y, col)

print(f1.stats_text())
print(f2.stats_text())
finish([f1, f2])
