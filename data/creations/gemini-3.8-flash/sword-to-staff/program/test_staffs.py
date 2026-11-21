# test_staffs.py
# Let's test different staff designs on copies of input_canvas

def clear_sword(c):
    # Erase sword blade and crossguard and grip to background
    # Background color is #ffffff (c0)
    bg = c.color("#ffffff")
    
    # Sword blade was at x=42..44, y=41..55
    for y in range(41, 56):
        for x in range(41, 46):
            if c.get(x, y) in [c.color("#eaedf3"), c.color("#c9ced8"), c.color("#8e96a5")]:
                c.set(x, y, bg)
                
    # Crossguard was at x=40..46, y=39..40
    for y in range(39, 41):
        for x in range(40, 47):
            c.set(x, y, bg)
            
    # Grip at y=38
    for x in range(40, 45):
        c.set(x, y=38, colour=bg)

# Let's verify clear_sword
c1 = input_canvas.copy(name="test1")
clear_sword(c1)
view(c1)
finish(c1)
