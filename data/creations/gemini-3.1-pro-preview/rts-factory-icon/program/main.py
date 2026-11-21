import pixelbench_api
from pixelbench_api import new_canvas, flatten, finish

def draw():
    # Colors
    OUTLINE = "#111111"
    BRICK_BASE = "#a33e36"
    BRICK_DARK = "#6b2621"
    BRICK_LIGHT = "#c95e55"
    CONCRETE_BASE = "#868a91"
    CONCRETE_DARK = "#52565c"
    CONCRETE_LIGHT = "#b1b5bd"
    DOOR_BASE = "#383a3f"
    DOOR_DARK = "#222326"
    DOOR_STRIPE = "#d9a02e"
    VENT_BASE = "#676b73"
    VENT_DARK = "#3f4247"
    GLOW = "#f2d15c"
    GLOW_LIGHT = "#fcf9a6"
    SMOKE = "#e0e5ec"
    SMOKE_DARK = "#a4abb6"

    # Layers
    l_smoke = new_canvas(32, 32, name="smoke")
    l_chimney = new_canvas(32, 32, name="chimney")
    l_main = new_canvas(32, 32, name="main")
    l_roof = new_canvas(32, 32, name="roof")
    l_vent = new_canvas(32, 32, name="vent")
    l_door_win = new_canvas(32, 32, name="door_win")

    # --- SMOKE ---
    l_smoke.circle(9, 2, 2, SMOKE)
    l_smoke.circle(12, 0, 1, SMOKE)
    l_smoke.circle(6, 1, 1, SMOKE)
    l_smoke.circle(8, 4, 1, SMOKE_DARK)
    l_smoke.set(9, 2, SMOKE_DARK)
    l_smoke.set(10, 3, SMOKE_DARK)
    l_smoke.outline(SMOKE_DARK)

    # --- CHIMNEY ---
    l_chimney.rect(7, 7, 5, 10, BRICK_BASE)
    l_chimney.line(7, 7, 7, 16, BRICK_LIGHT)
    l_chimney.line(11, 7, 11, 16, BRICK_DARK)
    l_chimney.rect(6, 5, 7, 2, CONCRETE_BASE)
    l_chimney.line(6, 5, 12, 5, CONCRETE_LIGHT)
    l_chimney.line(6, 6, 12, 6, CONCRETE_DARK)
    # Brick texture
    l_chimney.set(8, 9, BRICK_LIGHT); l_chimney.set(9, 9, BRICK_DARK)
    l_chimney.set(10, 12, BRICK_LIGHT); l_chimney.set(9, 12, BRICK_DARK)
    l_chimney.outline(OUTLINE)

    # --- MAIN BUILDING ---
    l_main.rect(5, 17, 22, 14, BRICK_BASE)
    l_main.line(5, 17, 5, 30, BRICK_LIGHT)
    l_main.line(26, 17, 26, 30, BRICK_DARK)
    l_main.line(5, 30, 26, 30, BRICK_DARK)
    # Shadow from roof
    l_main.line(5, 19, 26, 19, BRICK_DARK)
    # Brick pattern
    bricks = [(8,26), (14,21), (23,18), (7,25), (24,27), (9,28), (20,26)]
    for bx, by in bricks:
        l_main.set(bx, by, BRICK_LIGHT)
        l_main.set(bx+1, by, BRICK_DARK)
    
    # Annex
    l_main.rect(27, 25, 3, 6, CONCRETE_BASE)
    l_main.line(27, 25, 29, 25, CONCRETE_LIGHT)
    l_main.line(29, 26, 29, 30, CONCRETE_DARK)
    l_main.line(27, 26, 27, 30, CONCRETE_LIGHT)
    l_main.outline(OUTLINE)

    # --- ROOF ---
    l_roof.rect(3, 15, 26, 3, CONCRETE_BASE)
    l_roof.line(3, 15, 28, 15, CONCRETE_LIGHT)
    l_roof.line(3, 17, 28, 17, CONCRETE_DARK)
    l_roof.set(3, 16, CONCRETE_LIGHT)
    l_roof.set(28, 16, CONCRETE_DARK)
    # Warning stripe
    for x in range(13, 19, 2):
        l_roof.set(x, 16, DOOR_STRIPE)
    # Roof bump
    l_roof.rect(15, 14, 3, 2, CONCRETE_BASE)
    l_roof.line(15, 14, 17, 14, CONCRETE_LIGHT)
    # Chimney shadow
    l_roof.line(13, 15, 15, 15, CONCRETE_DARK)
    l_roof.line(13, 16, 14, 16, CONCRETE_DARK)
    l_roof.outline(OUTLINE)

    # --- VENT ---
    l_vent.rect(19, 11, 7, 5, VENT_BASE)
    l_vent.line(19, 11, 25, 11, CONCRETE_LIGHT)
    l_vent.line(19, 12, 19, 15, CONCRETE_LIGHT)
    l_vent.line(25, 12, 25, 15, CONCRETE_DARK)
    l_vent.rect(21, 12, 3, 3, VENT_DARK)
    l_vent.line(21, 13, 23, 13, VENT_BASE)
    # Pipe
    l_vent.rect(17, 13, 2, 3, CONCRETE_DARK)
    l_vent.set(17, 13, CONCRETE_LIGHT)
    # Antenna
    l_vent.line(5, 10, 5, 14, CONCRETE_DARK)
    l_vent.set(5, 9, GLOW)
    l_vent.outline(OUTLINE)

    # --- DOOR & WINDOWS ---
    # Door
    l_door_win.rect(13, 23, 6, 8, DOOR_BASE)
    l_door_win.line(13, 23, 18, 23, DOOR_DARK)
    l_door_win.line(13, 30, 18, 30, DOOR_STRIPE)
    l_door_win.set(14, 30, DOOR_DARK)
    l_door_win.set(16, 30, DOOR_DARK)
    l_door_win.set(18, 30, DOOR_DARK)
    
    # Left Window
    l_door_win.rect(7, 21, 4, 3, GLOW)
    l_door_win.line(7, 21, 10, 21, GLOW_LIGHT)
    l_door_win.set(8, 22, GLOW_LIGHT)
    
    # Right Window
    l_door_win.rect(21, 21, 4, 3, GLOW)
    l_door_win.line(21, 21, 24, 21, GLOW_LIGHT)
    l_door_win.set(22, 22, GLOW_LIGHT)
    
    l_door_win.outline(OUTLINE)

    # Flatten
    final = flatten([l_smoke, l_chimney, l_main, l_roof, l_vent, l_door_win])
    return final

result = draw()
finish(result)
