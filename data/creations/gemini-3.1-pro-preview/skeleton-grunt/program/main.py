import pixelbench_api as api

def draw():
    c = api.new_canvas(32, 32)
    
    grid = ["T" * 32 for _ in range(32)]
    def put(r, col, char):
        grid[r] = grid[r][:col] + char + grid[r][col+len(char):]

    # Head
    put(4, 14, "LLLLL")
    put(5, 13, "LWWWWWL")
    put(6, 13, "LWBBWBL")
    put(7, 13, "LWWBBWL")
    put(8, 14, "LWWBWL")
    put(9, 15, "LBWBL")
    put(10, 16, "LLL")

    # Sword
    put(8, 9, "i")
    put(9, 9, "i")
    put(10, 8, "ijj")
    put(11, 8, "ijj")
    put(12, 8, "ijj")
    put(13, 8, "ijj")
    put(14, 8, "kkk")
    put(15, 9, "r")
    put(16, 9, "L")
    put(17, 9, "k")

    # Right Arm
    put(11, 14, "D")
    put(12, 13, "W")
    put(13, 12, "L")
    put(14, 11, "D")
    put(15, 10, "W")

    # Body / Ribs
    put(11, 15, "LMWML")
    put(12, 15, "MLMLM")
    put(13, 15, "LMWML")
    put(14, 15, "MWWWM")
    put(15, 16, "MLM")
    put(16, 16, "LWL")
    put(17, 15, "LLMLL")
    put(18, 15, "DMMMD")

    # Left Shoulder/Arm (behind shield)
    put(11, 20, "D")
    put(12, 20, "L")

    # Right Leg
    put(19, 15, "W")
    put(20, 15, "L")
    put(21, 16, "W")
    put(22, 16, "D")
    put(23, 15, "W")
    put(24, 14, "L")
    put(25, 14, "W")
    put(26, 14, "D")
    put(27, 12, "WLL")
    put(28, 12, "LL")

    # Left Leg
    put(19, 19, "L")
    put(20, 19, "L")
    put(21, 18, "L")
    put(22, 18, "D")
    put(23, 18, "L")
    put(24, 19, "L")
    put(25, 19, "L")
    put(26, 19, "D")
    put(27, 18, "LLL")
    put(28, 18, "LL")

    # Shield
    put(10, 24, "kkk")
    put(11, 22, "kdwwmdk")
    put(12, 21, "kwdwmmdmk")
    put(13, 21, "kwdwjmdmk")
    put(14, 21, "kmdjijddk")
    put(15, 21, "kmdmjdddk")
    put(16, 21, "kddmddddk")
    put(17, 22, "kdddddk")
    put(18, 24, "kkk")

    palette = {
        "W": "#e2e2e2",
        "L": "#a0a6a0",
        "M": "#6a736a",
        "D": "#3a423a",
        "B": "#141814",
        "w": "#a6734d",
        "m": "#734626",
        "d": "#402212",
        "i": "#d2d6d6",
        "j": "#8a9393",
        "k": "#4a5454",
        "r": "#6b2626",
    }

    for y in range(32):
        for x in range(32):
            char = grid[y][x]
            if char != "T":
                c.set(x, y, palette[char])
                
    api.finish(c)

draw()
