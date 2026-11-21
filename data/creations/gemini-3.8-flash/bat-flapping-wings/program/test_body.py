# Identify all pixels of input_canvas
# The body is:
# - Rows 0..3: all non-zero pixels are the head/ears (x=9..17)
# - Rows 4..5: x=9..17 are head/shoulders
# - Rows 6..10: x=10..16 are the torso/face/snout/belly!
#   Wait, what about x=9 and x=17 on rows 6..10?
#   In input_canvas:
#   Row 6: x=9 is 4 (wing bone), x=17 is 4 (wing bone)
#   Row 7: x=9 is 4 (wing bone), x=17 is 4 (wing bone)
#   Row 8: x=9 is 1 (wing outline), x=17 is 1 (wing outline)
#   Row 9: x=9 is 1 (wing outline), x=17 is 1 (wing outline)
#   Row 10: x=9 is 1 (wing outline), x=17 is 1 (wing outline)
# - Rows 11..12: x=10..16 is belly (x=9, 17 are transparent '.')
# - Rows 13..14: x=10..12 and 14..16 are legs/feet (x=13 is '.')
# - Row 15: x=11 and 15 are feet tips
# - Rows 16..21: ONLY wings!

# Let's print out the exact body mask:
print("Body pixels:")
for y in range(22):
    line = ""
    for x in range(27):
        val = input_canvas.get(x, y)
        if val == 0:
            line += "."
        elif x in range(10, 17):
            line += str(val)
        elif y in (1, 2, 3, 4, 5) and x in (9, 17):
            line += str(val)
        else:
            line += " " # wing pixel
    print(f"{y:2d}: {line}")
