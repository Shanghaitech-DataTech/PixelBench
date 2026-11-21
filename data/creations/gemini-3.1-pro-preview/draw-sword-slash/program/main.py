import pixelbench_api
from pixelbench_api import input_canvas, new_canvas, view, save, finish

def main():
    c = new_canvas(120, 100)
    c.blit(input_canvas, 30, 20)
    
    c2 = c.copy()
    
    # Erase correctly
    for y in range(35, 55):
        for x in range(0, 62):
            color = input_canvas.get(x, y)
            if color == 0: continue
            
            erase = False
            
            # Left arm (sleeve)
            if 36 <= y <= 45 and 25 <= x <= 38:
                if color in [1, 2, 3, 4, 5, 6, 10]:
                    if x < 35 or (x < 38 and y >= 42):
                        erase = True
            
            # Left hand
            if 40 <= y <= 45 and 36 <= x <= 47:
                if color in [9, 11, 12, 13, 14]:
                    erase = True
                    
            # Sword blade (left of hand)
            if 43 <= y <= 53 and x < 38:
                erase = True
                
            # Sword hilt (right of hand)
            if 39 <= y <= 45 and x >= 45:
                if color in [1, 2, 5, 6, 10, 12, 14]:
                    erase = True
                    
            # Dark pixels below hand/hilt
            if 44 <= y <= 47 and 35 <= x <= 47:
                if color in [1, 2, 5, 6, 10, 12, 14]:
                    erase = True
                    
            # Clean up straggler pixels
            if 42 <= y <= 46 and 35 <= x <= 40:
                if color in [9, 11, 13]:
                    erase = True
                    
            if erase:
                c2.set(x + 30, y + 20, None)
                
    # Draw Left Arm swinging up and right
    # Start from shoulder area (around x=30+30, y=20+38) -> (60, 58)
    # End hand around (90, 40)
    
    # Draw arm sleeve
    c2.poly([(60, 58), (85, 42), (90, 48), (62, 65)], 4) # Base arm color
    c2.poly([(60, 58), (85, 42), (86, 44), (61, 60)], 3) # Highlight
    c2.poly([(62, 63), (90, 48), (88, 46), (62, 61)], 5) # Shadow
    
    # Draw hand
    c2.circle(92, 44, 2, 11)
    
    # Draw sword hilt
    c2.line(88, 48, 96, 40, 10)
    
    # Draw sword blade
    # The blade extends from hand (92, 44) up and right
    c2.line(94, 42, 110, 26, 1)
    c2.line(95, 43, 111, 27, 2)
    c2.line(94, 41, 110, 25, 1)
    
    # Draw slash trail
    c2.path("M 20 70 Q 50 80 100 35", 1, fill=False)
    c2.path("M 18 68 Q 48 78 98 33", 1, fill=False)
    c2.path("M 22 72 Q 52 82 102 37", 1, fill=False)
    
    finish([c, c2])

if __name__ == "__main__":
    main()
