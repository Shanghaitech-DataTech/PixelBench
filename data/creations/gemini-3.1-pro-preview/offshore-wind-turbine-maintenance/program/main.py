from pixelbench_api import new_canvas, finish

def draw():
    c = new_canvas(64, 64)

    # 1. Sky Gradient
    for y in range(48):
        if y < 12:
            color = "#4A90E2"
        elif y < 24:
            color = "#63A4FF"
        elif y < 36:
            color = "#80BFFF"
        else:
            color = "#A1D4FF"
        c.line(0, y, 63, y, color)

    # Clouds
    c.rect(10, 8, 8, 3, "#FFFFFF")
    c.rect(12, 6, 4, 5, "#FFFFFF")
    c.rect(10, 11, 6, 1, "#BDBDBD")

    c.rect(40, 15, 12, 4, "#FFFFFF")
    c.rect(43, 13, 6, 6, "#FFFFFF")
    c.rect(40, 19, 9, 1, "#BDBDBD")
    
    # Birds
    c.set(50, 8, "#1C1C1C")
    c.set(49, 7, "#1C1C1C")
    c.set(51, 7, "#1C1C1C")
    
    c.set(55, 10, "#1C1C1C")
    c.set(54, 9, "#1C1C1C")
    c.set(56, 9, "#1C1C1C")

    # 2. Ocean Gradient
    for y in range(48, 64):
        if y == 48:
            color = "#0B4776"
        elif y < 53:
            color = "#0F5E9C"
        elif y < 59:
            color = "#126EBA"
        else:
            color = "#1681D8"
        c.line(0, y, 63, y, color)

    # Wave Highlights
    c.line(5, 50, 15, 50, "#1CA3EC")
    c.line(40, 51, 55, 51, "#1CA3EC")
    c.line(20, 54, 35, 54, "#1CA3EC")
    c.line(2, 57, 18, 57, "#5CDB95")
    c.line(45, 58, 60, 58, "#5CDB95")
    c.line(10, 61, 28, 61, "#5CDB95")
    c.line(38, 62, 50, 62, "#5CDB95")

    # Wave Shadows
    c.line(10, 49, 20, 49, "#0B4776")
    c.line(45, 53, 55, 53, "#0B4776")
    c.line(5, 56, 15, 56, "#0B4776")
    c.line(50, 60, 60, 60, "#0B4776")

    # 3. Distant Turbines
    # Left turbine
    c.rect(10, 34, 2, 16, "#E0E0E0")
    c.line(10, 34, 10, 49, "#FFFFFF") # Highlight
    c.rect(9, 32, 4, 2, "#FFFFFF")    # Nacelle
    c.line(10, 33, 10, 26, "#FFFFFF") # Blade up
    c.line(10, 33, 5, 38, "#FFFFFF")  # Blade bl
    c.line(10, 33, 15, 38, "#FFFFFF") # Blade br
    c.line(8, 49, 13, 49, "#FFFFFF")  # Foam

    # Right turbine
    c.rect(54, 38, 2, 12, "#E0E0E0")
    c.line(54, 38, 54, 49, "#FFFFFF") # Highlight
    c.rect(53, 37, 4, 2, "#FFFFFF")   # Nacelle
    c.line(55, 38, 51, 35, "#FFFFFF") # Blade tl
    c.line(55, 38, 59, 35, "#FFFFFF") # Blade tr
    c.line(55, 38, 55, 44, "#FFFFFF") # Blade down
    c.line(52, 49, 57, 49, "#FFFFFF") # Foam

    # 4. Main Turbine
    # Tower
    c.rect(29, 0, 9, 40, "#E0E0E0")
    c.rect(29, 0, 2, 40, "#FFFFFF") # Highlight
    c.rect(36, 0, 2, 40, "#9E9E9E") # Shadow
    # Flanges
    c.line(29, 10, 37, 10, "#9E9E9E")
    c.line(29, 25, 37, 25, "#9E9E9E")
    # Door
    c.rect(32, 33, 4, 7, "#616161")
    c.rect(33, 34, 2, 6, "#424242")

    # Transition Piece
    c.rect(28, 42, 11, 16, "#FFB90F")
    c.rect(28, 42, 2, 16, "#FFD700") # Highlight
    c.rect(37, 42, 2, 16, "#CD8500") # Shadow
    c.line(28, 42, 38, 42, "#1C1C1C") # Black stripe
    # Foam at base
    c.line(25, 58, 42, 58, "#FFFFFF")
    c.line(26, 59, 41, 59, "#FFFFFF")

    # Platform Deck
    c.rect(20, 40, 27, 2, "#424242")
    
    # Platform Supports
    c.line(28, 45, 20, 41, "#616161")
    c.line(28, 46, 20, 42, "#616161")
    c.line(38, 45, 46, 41, "#616161")
    c.line(38, 46, 46, 42, "#616161")

    # Railings
    c.line(20, 36, 46, 36, "#9E9E9E")
    c.line(20, 38, 46, 38, "#9E9E9E")
    for rx in range(20, 47, 3):
        c.line(rx, 36, rx, 40, "#9E9E9E")
        
    # Life ring
    c.set(38, 37, "#FF4500")
    c.set(39, 37, "#FFFFFF")
    c.set(38, 38, "#FFFFFF")
    c.set(39, 38, "#FF4500")

    # Crane
    c.rect(42, 32, 2, 9, "#FFB90F")
    c.line(42, 32, 42, 40, "#FFD700") # Highlight
    c.line(42, 32, 46, 30, "#FFD700") # Boom
    c.line(46, 30, 46, 38, "#1C1C1C") # Cable
    c.set(46, 38, "#424242") # Hook
    c.set(42, 31, "#FF0000") # Warning light

    # Ladder
    c.line(24, 40, 24, 56, "#424242") # Left rail
    c.line(26, 40, 26, 56, "#424242") # Right rail
    for ry in range(41, 57, 2):
        c.set(25, ry, "#757575") # Rungs
    # Connections to TP
    c.set(27, 44, "#424242")
    c.set(27, 48, "#424242")
    c.set(27, 52, "#424242")

    # Boat landing bumpers
    c.rect(22, 54, 2, 6, "#FFD700")
    c.rect(27, 54, 2, 6, "#FFD700")
    c.line(24, 54, 26, 54, "#424242") # Crossbar
    c.line(24, 56, 26, 56, "#424242") # Crossbar

    # 5. CTV (Crew Transfer Vessel)
    c.poly([(4, 55), (21, 55), (19, 59), (4, 59)], "#BDBDBD") # Hull
    c.poly([(17, 55), (21, 55), (19, 59)], "#FF4500") # Orange bow
    c.line(4, 55, 21, 55, "#FFFFFF") # Deck highlight
    
    # Boat cabin
    c.rect(7, 50, 8, 5, "#E0E0E0")
    c.rect(7, 50, 2, 5, "#FFFFFF") # Cabin highlight
    c.rect(8, 51, 2, 2, "#0B4776") # Window 1
    c.rect(12, 51, 2, 2, "#0B4776") # Window 2
    c.rect(7, 49, 8, 1, "#424242") # Roof
    c.line(11, 46, 11, 49, "#1C1C1C") # Antenna
    
    # Boat railing
    c.line(5, 54, 16, 54, "#9E9E9E")
    for bx in range(5, 17, 3):
        c.set(bx, 54, "#9E9E9E")

    # 6. Technician
    # Climbing ladder at y=46
    c.set(25, 45, "#FFFFFF") # Helmet
    c.rect(24, 46, 3, 3, "#FF4500") # Jacket
    c.set(25, 46, "#FFFF00") # Reflective stripe
    c.set(25, 48, "#FFFF00") # Reflective stripe
    c.rect(24, 49, 3, 2, "#1C1C1C") # Pants
    c.set(23, 47, "#1C1C1C") # Left arm
    c.set(27, 46, "#1C1C1C") # Right arm
    c.set(25, 51, "#1C1C1C") # Left foot
    c.set(26, 50, "#1C1C1C") # Right foot

    finish(c)

draw()
