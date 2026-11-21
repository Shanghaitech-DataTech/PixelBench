from pixelbench_api import input_canvas, view, finish

def main():
    output = input_canvas.copy()

    # Top spout water
    output.set(31, 0, 'c6')
    output.set(32, 0, 'c3')
    
    output.set(30, 1, 'c6')
    output.set(31, 1, 'c3')
    output.set(32, 1, 'c6')
    output.set(33, 1, 'c3')
    
    output.set(29, 2, 'c6')
    output.set(30, 2, 'c3')
    output.set(33, 2, 'c6')
    output.set(34, 2, 'c3')
    
    output.set(28, 3, 'c6')
    output.set(29, 3, 'c3')
    output.set(34, 3, 'c6')
    output.set(35, 3, 'c3')
    
    output.set(28, 4, 'c6')
    output.set(29, 4, 'c3')
    output.set(34, 4, 'c6')
    output.set(35, 4, 'c3')
    
    output.set(27, 5, 'c6')
    output.set(28, 5, 'c3')
    output.set(35, 5, 'c6')
    output.set(36, 5, 'c3')
    
    output.set(27, 6, 'c6')
    output.set(28, 6, 'c3')
    output.set(35, 6, 'c6')
    output.set(36, 6, 'c3')
    
    output.set(27, 7, 'c6')
    output.set(28, 7, 'c3')
    output.set(35, 7, 'c6')
    output.set(36, 7, 'c3')
    
    output.set(27, 8, 'c6')
    output.set(28, 8, 'c3')
    output.set(35, 8, 'c6')
    output.set(36, 8, 'c3')

    # Splashes for top spout
    output.set(26, 9, 'c3')
    output.set(29, 9, 'c3')
    output.set(34, 9, 'c3')
    output.set(37, 9, 'c3')

    # Tier 1 to Tier 2
    for y in range(13, 19):
        # Left
        output.set(25, y, 'c6')
        output.set(26, y, 'c3')
        # Middle
        output.set(31, y, 'c6')
        output.set(32, y, 'c3')
        # Right
        output.set(37, y, 'c6')
        output.set(38, y, 'c3')
        
    # Splash Tier 1 -> Tier 2
    output.set(24, 19, 'c3')
    output.set(27, 19, 'c3')
    output.set(30, 19, 'c3')
    output.set(33, 19, 'c3')
    output.set(36, 19, 'c3')
    output.set(39, 19, 'c3')

    # Tier 2 to Tier 3
    for y in range(22, 30):
        # Stream 1
        output.set(21, y, 'c6')
        output.set(22, y, 'c3')
        # Stream 2
        output.set(27, y, 'c6')
        output.set(28, y, 'c3')
        # Stream 3
        output.set(35, y, 'c6')
        output.set(36, y, 'c3')
        # Stream 4
        output.set(41, y, 'c6')
        output.set(42, y, 'c3')

    # Splash Tier 2 -> Tier 3
    output.set(20, 30, 'c3')
    output.set(23, 30, 'c3')
    output.set(26, 30, 'c3')
    output.set(29, 30, 'c3')
    output.set(34, 30, 'c3')
    output.set(37, 30, 'c3')
    output.set(40, 30, 'c3')
    output.set(43, 30, 'c3')

    # Tier 3 to Bottom Pool
    for y in range(32, 44):
        # Stream 1
        output.set(19, y, 'c6')
        output.set(20, y, 'c3')
        # Stream 5
        output.set(43, y, 'c6')
        output.set(44, y, 'c3')

    for y in range(32, 46):
        # Stream 2
        output.set(25, y, 'c6')
        output.set(26, y, 'c3')
        # Stream 4
        output.set(37, y, 'c6')
        output.set(38, y, 'c3')

    for y in range(32, 47):
        # Stream 3
        output.set(31, y, 'c6')
        output.set(32, y, 'c3')

    # Splash Tier 3 -> Bottom Pool
    output.set(18, 44, 'c3')
    output.set(21, 44, 'c3')
    output.set(24, 46, 'c3')
    output.set(27, 46, 'c3')
    output.set(30, 47, 'c3')
    output.set(33, 47, 'c3')
    output.set(36, 46, 'c3')
    output.set(39, 46, 'c3')
    output.set(42, 44, 'c3')
    output.set(45, 44, 'c3')

    finish(output)

if __name__ == "__main__":
    main()