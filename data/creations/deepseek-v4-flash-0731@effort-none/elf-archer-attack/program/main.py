from pixelbench_api import *

# Frame 1: Keep the original picture content
f1 = input_canvas.copy(name="frame1")

# Frame 2: Elf archer at maximum draw - bow fully drawn

# For the full-draw frame, I'll create a modified version where:
# - The bow is bent into a much deeper, more dramatic arc
# - The string is pulled back significantly toward the archer
# - The archer's stance shows the draw tension

# I'll preserve the elf character but dramatically reshape the bow area.

def make_frame2():
    f2 = input_canvas.copy(name="frame2")
    
    # The elf is in a side profile facing RIGHT.
    # The bow is held vertically in front of the archer.
    # At maximum draw, the bow is bent into a deep crescent shape.
    
    # The bow wood appears as a curved element. For full draw, the 
    # upper and lower bow limbs rotate outward from the grip.
    
    # Clear most of the right/bow region
    f2.clear(18, 0, 17, 37)
    
    # === REDRAW BOW AT FULL DRAW ===
    
    # The elf faces right. A fully-drawn bow from the side:
    # - The bow wood forms a deep bracket/parenthesis shape
    # - The upper limb tilts significantly from vertical
    # - The lower limb also bends dramatically
    
    # === UPPER BOW LIMB - deep bend ===
    # Upper tip pulled back toward the archer
    f2.set(19, 1, 1)
    f2.set(20, 1, 5)
    f2.set(21, 1, 1)
    f2.set(19, 2, 1)
    f2.set(20, 2, 6)
    f2.set(21, 2, 7)
    f2.set(22, 2, 1)
    f2.set(18, 3, 3)
    f2.set(19, 3, 7)
    f2.set(20, 3, 7)
    f2.set(21, 3, 1)
    f2.set(18, 4, 3)
    f2.set(19, 4, 7)
    f2.set(20, 4, 9)
    f2.set(21, 4, 1)
    
    # Upper limb middle - bow wood curving strongly
    f2.set(18, 5, 12)
    f2.set(19, 5, 3)
    f2.set(20, 5, 7)
    f2.set(21, 5, 7)
    f2.set(22, 5, 1)
    f2.set(17, 6, 13)
    f2.set(18, 6, 12)
    f2.set(19, 6, 7)
    f2.set(20, 6, 9)
    f2.set(21, 6, 1)
    f2.set(17, 7, 13)
    f2.set(18, 7, 15)
    f2.set(19, 7, 7)
    f2.set(20, 7, 16)
    f2.set(21, 7, 17)
    f2.set(22, 7, 1)
    
    # Upper limb continuing the arc, bow wood
    f2.set(17, 8, 3)
    f2.set(18, 8, 13)
    f2.set(19, 8, 15)
    f2.set(20, 8, 16)
    f2.set(21, 8, 7)
    f2.set(22, 8, 1)
    f2.set(17, 9, 3)
    f2.set(18, 9, 3)
    f2.set(19, 9, 12)
    f2.set(20, 9, 16)
    f2.set(21, 9, 17)
    
    # === BOW STRING - pulled taut toward archer ===
    # The string should be drawn back toward the elf's face/shoulder
    # The elf's face is around (10-14, 2-7)
    # The string at full draw should be near the elf's chest/shoulder area
    
    # String vertical/taut from upper to lower bow
    f2.set(26, 6, 20)
    f2.set(26, 7, 20)
    f2.set(26, 8, 20)
    f2.set(26, 9, 20)
    f2.set(26, 10, 20)
    f2.set(26, 11, 20)
    f2.set(25, 8, 20)
    f2.set(25, 9, 20)
    f2.set(25, 10, 20)
    f2.set(25, 11, 20)
    
    # String at the grip area - being pulled
    f2.set(25, 12, 20)
    f2.set(24, 12, 20)
    f2.set(24, 13, 20)
    f2.set(24, 14, 20)
    
    # === BOW GRIP ===
    # The grip where the elf holds the bow
    f2.set(18, 10, 3)
    f2.set(18, 11, 3)
    f2.set(18, 12, 3)
    f2.set(18, 13, 3)
    f2.set(18, 14, 3)
    f2.set(17, 10, 2)
    f2.set(17, 11, 2)
    f2.set(17, 12, 2)
    
    # === LOWER BOW LIMB - deep bend ===
    # Lower limb curves dramatically
    
    # Lower limb continuing from grip
    f2.set(18, 15, 2)
    f2.set(18, 16, 2)
    f2.set(18, 17, 3)
    f2.set(19, 18, 3)
    f2.set(19, 19, 12)
    
    # Lower limb bow wood with curve
    f2.set(19, 20, 12)
    f2.set(20, 21, 12)
    f2.set(20, 22, 12)
    f2.set(21, 23, 12)
    f2.set(21, 24, 12)
    
    # Lower limb curving outward
    f2.set(22, 25, 3)
    f2.set(22, 26, 3)
    f2.set(23, 27, 3)
    f2.set(23, 28, 3)
    
    # === ELF'S ARMS ===
    # The elf's bow-arm (front/left arm) extends toward the bow grip
    # The elf's draw arm (back/right arm) pulls the string
    
    # Draw arm extended, pulling string
    f2.set(19, 12, 20)  # arm toward string
    f2.set(20, 13, 20)  # hand at string
    
    # === LOWER BOW TIP bent back ===
    # Lower tip also curves with the deep bend
    f2.set(24, 29, 3)
    f2.set(25, 30, 3)
    f2.set(26, 31, 3)
    f2.set(27, 31, 1)
    
    # === POSE ADJUSTMENTS ===
    # The elf's body should be slightly more dynamic/tilted into the draw
    
    # ==== RESTORE PRESERVED ELF ELEMENTS ====
    # Parts of the original elf in the middle columns that I may have cleared
    # Let me restore key elf body elements from f1 in columns 18-20
    for y in range(8, 34):
        for x in range(18, 22):
            idx = f1.get(x, y)
            if idx > 0:
                f2.set(x, y, idx)
    
    # Now re-apply the full-draw bow on top for the key elements
    # Redo the bow bus at the string positions
    for y in [8, 9, 10, 11]:
        f2.set(26, y, 20)
    
    return f2

f2 = make_frame2()

print(f1.stats_text())
print(f2.stats_text())

# Submit both frames
finish([f1, f2])
