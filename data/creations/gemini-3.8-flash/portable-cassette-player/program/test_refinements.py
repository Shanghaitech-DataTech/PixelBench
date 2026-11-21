from pixelbench_api import *

def test_refinements():
    base = new_canvas(32, 32)
    glass = new_canvas(32, 32)

    # Palette
    c_outline = "#14171f"
    c_shadow = "#0c0e14"

    # Blue body
    c_blue_darkest = "#16283d"
    c_blue_dark = "#1e3c5c"
    c_blue_base = "#2a5b8a"
    c_blue_mid = "#3873a8"
    c_blue_light = "#5092cc"
    c_blue_hi = "#80b8e6"

    # Silver
    c_silver_darkest = "#353a42"
    c_silver_dark = "#565e6b"
    c_silver_mid = "#858f9e"
    c_silver_light = "#b8c3d1"
    c_silver_hi = "#e8edf5"
    c_silver_white = "#ffffff"

    # Retro Accents
    c_orange_dark = "#a82d13"
    c_orange = "#eb4d23"
    c_orange_hi = "#ff784f"
    c_led_glow = "#ff2020"
    c_led_dark = "#660c0c"

    # Cassette Tape
    c_cas_shell = "#dfd8cd"
    c_cas_shell_dark = "#aba294"
    c_cas_shell_hi = "#f4efe6"
    c_cas_label = "#f7f5ee"
    c_cas_stripe = "#db401c"
    c_cas_stripe_blue = "#1e5385"
    c_cas_interior = "#11141a"
    c_cas_roller = "#c99c44"

    # Magnetic Tape
    c_tape_dark = "#2b160c"
    c_tape_mid = "#4d2818"
    c_tape_light = "#6e3b23"

    # Reel Hubs
    c_hub_white = "#ffffff"
    c_hub_hole = "#11141a"

    # Cable
    c_cable_black = "#16181f"
    c_cable_body = "#262c36"
    c_cable_mid = "#444d5c"
    c_cable_hi = "#78879e"
    c_jack_metal = "#d4dae6"

    # --- HEADPHONE JACK & CABLE ---
    # Metal collar (y=5)
    base.set(21, 5, c_jack_metal)
    base.set(22, 5, c_silver_dark)
    # Barrel (y=3..4)
    base.rect(21, 3, 2, 2, c_cable_black)
    base.set(21, 3, c_cable_mid)
    base.set(21, 4, c_silver_light)
    base.set(22, 4, c_silver_dark)
    # Rubber boot (y=2)
    base.set(21, 2, c_cable_mid)
    base.set(22, 2, c_cable_black)

    # Smooth curving cable down the right side and looping under
    cord = [
        (21, 1, c_cable_mid),
        (22, 1, c_cable_hi),
        (23, 1, c_cable_hi),
        (24, 1, c_cable_mid),
        (25, 2, c_cable_hi),
        (26, 2, c_cable_body),
        (27, 3, c_cable_hi),
        (28, 4, c_cable_hi),
        (28, 5, c_cable_body),
        (29, 6, c_cable_hi),
        (29, 7, c_cable_hi),
        (29, 8, c_cable_body),
        (29, 9, c_cable_black),
        (28, 10, c_cable_mid),
        (28, 11, c_cable_body),
        (27, 12, c_cable_hi),
        (27, 13, c_cable_body),
        (26, 14, c_cable_mid),
        (26, 15, c_cable_hi),
        (26, 16, c_cable_body),
        (27, 17, c_cable_hi),
        (28, 18, c_cable_hi),
        (29, 19, c_cable_body),
        (29, 20, c_cable_hi),
        (29, 21, c_cable_hi),
        (29, 22, c_cable_body),
        (28, 23, c_cable_black),
        (28, 24, c_cable_mid),
        (27, 25, c_cable_hi),
        (26, 26, c_cable_body),
        (25, 27, c_cable_hi),
        (24, 28, c_cable_body),
        (22, 29, c_cable_hi),
        (21, 29, c_cable_mid),
        (19, 30, c_cable_hi),
        (18, 30, c_cable_hi),
        (17, 30, c_cable_body),
        (15, 30, c_cable_mid),
        (14, 30, c_cable_hi),
        (13, 30, c_cable_body),
        (11, 29, c_cable_hi),
        (10, 29, c_cable_mid),
        (9, 28, c_cable_body),
        (8, 27, c_cable_mid),
        (7, 26, c_cable_black)
    ]
    for x, y, col in cord:
        base.set(x, y, col)

    # --- TOP PLAYBACK BUTTONS ---
    # REW (x=7..8, y=4..6)
    base.rect(7, 4, 2, 3, c_silver_mid)
    base.line(7, 4, 8, 4, c_silver_hi)
    base.set(7, 5, c_silver_light)
    base.set(8, 5, c_silver_dark)
    base.set(8, 6, c_silver_darkest)

    # FF (x=10..11, y=4..6)
    base.rect(10, 4, 2, 3, c_silver_mid)
    base.line(10, 4, 11, 4, c_silver_hi)
    base.set(10, 5, c_silver_light)
    base.set(11, 5, c_silver_dark)
    base.set(11, 6, c_silver_darkest)

    # PLAY (x=13..15, y=5..6)
    base.rect(13, 5, 3, 2, c_silver_light)
    base.line(13, 5, 15, 5, c_silver_white)
    base.set(13, 6, c_silver_light)
    base.set(14, 6, c_silver_mid)
    base.set(15, 6, c_silver_dark)
    base.set(14, 5, c_orange)

    # STOP (x=17..18, y=4..6)
    base.rect(17, 4, 2, 3, c_silver_mid)
    base.line(17, 4, 18, 4, c_silver_hi)
    base.set(17, 5, c_silver_light)
    base.set(18, 5, c_silver_dark)
    base.set(18, 6, c_silver_darkest)

    # --- BODY ---
    base.rect(6, 7, 18, 22, c_blue_base)
    base.rect(6, 7, 18, 22, c_outline, fill=False)
    # Corners
    base.set(6, 7, "transparent")
    base.set(23, 7, "transparent")
    base.set(6, 28, "transparent")
    base.set(23, 28, "transparent")
    base.set(7, 7, c_outline)
    base.set(22, 7, c_outline)
    base.set(7, 28, c_outline)
    base.set(22, 28, c_outline)

    # Top silver plate: y=7..9
    base.rect(7, 7, 16, 3, c_silver_mid)
    base.line(7, 7, 22, 7, c_silver_hi)
    base.line(7, 8, 22, 8, c_silver_light)
    base.line(7, 9, 22, 9, c_silver_dark)
    # Hot Line accent button
    base.rect(19, 8, 2, 2, c_orange)
    base.set(19, 8, c_orange_hi)
    base.set(20, 9, c_orange_dark)

    # Playback symbols
    base.set(7, 9, c_silver_darkest)
    base.set(8, 9, c_silver_darkest)
    base.set(10, 9, c_silver_darkest)
    base.set(11, 9, c_silver_darkest)
    base.set(14, 9, c_orange_dark)
    base.set(17, 9, c_silver_darkest)

    # Body bevel
    base.line(7, 10, 7, 27, c_blue_hi)
    base.line(22, 10, 22, 27, c_blue_darkest)
    base.line(7, 27, 22, 27, c_blue_dark)
    base.line(8, 28, 21, 28, c_outline)

    # --- VOLUME CONTROLS ---
    # Left side thumbwheel
    base.set(5, 13, c_outline)
    base.set(5, 19, c_outline)
    base.set(4, 14, c_silver_darkest)
    base.set(4, 15, c_silver_white)
    base.set(4, 16, c_silver_darkest)
    base.set(4, 17, c_silver_white)
    base.set(4, 18, c_silver_darkest)
    base.set(5, 14, c_silver_dark)
    base.set(5, 15, c_silver_light)
    base.set(5, 16, c_silver_dark)
    base.set(5, 17, c_silver_light)
    base.set(5, 18, c_silver_dark)

    # Front volume control panel (y = 23 to 27)
    # Seam line separating door from lower panel
    base.line(7, 22, 22, 22, c_blue_darkest)

    # Volume icon (speaker wedge): x = 8..10, y = 24..25
    base.set(8, 25, c_silver_light)
    base.set(9, 24, c_silver_white)
    base.set(9, 25, c_silver_white)
    base.set(9, 26, c_silver_mid)
    base.set(10, 24, c_blue_light)
    base.set(10, 26, c_blue_light)

    # Volume gradation scale (y = 24):
    base.set(12, 24, c_silver_dark)
    base.set(14, 24, c_silver_mid)
    base.set(16, 24, c_silver_light)
    base.set(18, 24, c_silver_hi)
    base.set(20, 24, c_orange)

    # Volume slider track (y = 25):
    base.line(12, 25, 20, 25, c_shadow)
    base.line(12, 26, 20, 26, c_blue_darkest)

    # Volume slider knob: x = 16..17, y = 24..26
    base.rect(16, 24, 2, 3, c_silver_hi)
    base.set(16, 24, c_silver_white)
    base.set(17, 26, c_silver_dark)
    base.set(16, 25, c_orange) # Center orange notch on knob

    # Power/Battery LED at x = 8, y = 27
    base.set(7, 27, c_led_dark)
    base.set(8, 27, c_led_glow)

    # Subtle metallic badge on lower front: x = 12..20, y = 27
    base.line(12, 27, 20, 27, c_silver_darkest)
    base.set(13, 27, c_silver_mid)
    base.set(15, 27, c_silver_light)
    base.set(17, 27, c_silver_mid)
    base.set(19, 27, c_silver_light)

    # --- CASSETTE DOOR & TRANSPARENT WINDOW ---
    # Window Frame: x = 8 to 21, y = 11 to 21
    base.rect(8, 11, 14, 11, c_silver_dark)
    base.line(8, 11, 21, 11, c_silver_hi)
    base.line(8, 11, 8, 21, c_silver_light)
    base.line(21, 11, 21, 21, c_silver_darkest)
    base.line(8, 21, 21, 21, c_silver_darkest)

    # Window Interior Background:
    base.rect(9, 12, 12, 9, c_cas_interior)

    # Cassette Shell:
    base.rect(9, 12, 12, 9, c_cas_shell)
    base.line(9, 12, 20, 12, c_cas_shell_hi)
    base.line(9, 20, 20, 20, c_cas_shell_dark)

    # Cassette Paper Label: y = 13..14
    base.rect(9, 13, 12, 2, c_cas_label)
    base.line(9, 13, 20, 13, c_cas_stripe)
    base.line(9, 14, 20, 14, c_cas_stripe_blue)
    base.set(10, 14, c_cas_label)
    base.set(18, 13, c_cas_label)

    # Cassette Center Cutout: x = 9 to 20, y = 15 to 18
    base.rect(9, 15, 12, 4, c_cas_interior)

    # --- REEL 1: Left Tape Reel (Fuller tape spool) ---
    # Dark brown magnetic tape spool (radius 2.5):
    # Rows 14 to 18:
    base.line(10, 14, 12, 14, c_tape_mid)
    base.rect(9, 15, 5, 4, c_tape_mid)
    base.set(9, 15, c_cas_interior)
    base.set(13, 15, c_cas_interior)
    base.set(9, 18, c_cas_interior)
    base.set(13, 18, c_cas_interior)
    # Shading on wound tape
    base.set(10, 15, c_tape_light)
    base.set(11, 15, c_tape_light)
    base.set(12, 17, c_tape_dark)
    base.set(11, 18, c_tape_dark)

    # Left Spool Hub
    base.set(11, 16, c_hub_hole)
    base.set(11, 15, c_hub_white)
    base.set(11, 17, c_hub_white)
    base.set(10, 16, c_hub_white)
    base.set(12, 16, c_hub_white)

    # --- REEL 2: Right Tape Reel (Thinner tape roll) ---
    # Brown tape ring around right hub:
    base.rect(16, 15, 5, 4, c_cas_interior)
    # 1-pixel tape ring around hub:
    base.set(17, 15, c_tape_mid)
    base.set(18, 14, c_tape_mid)
    base.set(19, 15, c_tape_mid)
    base.set(16, 16, c_tape_mid)
    base.set(20, 16, c_tape_mid)
    base.set(17, 17, c_tape_dark)
    base.set(19, 17, c_tape_dark)
    base.set(18, 18, c_tape_dark)

    # Right Spool Hub
    base.set(18, 16, c_hub_hole)
    base.set(18, 15, c_hub_white)
    base.set(18, 17, c_hub_white)
    base.set(17, 16, c_hub_white)
    base.set(19, 16, c_hub_white)

    # --- Center Tape Bridge & Scale Tick Marks ---
    base.line(13, 18, 16, 18, c_tape_dark)
    base.set(14, 16, c_silver_dark)
    base.set(15, 16, c_silver_dark)

    # --- Cassette Bottom Tape Head Area (Trapezoid) ---
    base.line(9, 19, 20, 19, c_cas_shell)
    base.line(9, 20, 20, 20, c_cas_shell_dark)
    base.line(11, 19, 18, 19, c_tape_mid)
    base.line(12, 20, 17, 20, c_tape_dark)
    base.set(12, 19, c_cas_roller)
    base.set(17, 19, c_cas_roller)

    # --- GLASS LAYER ---
    glass.line(9, 12, 13, 16, "#ffffff35")
    glass.line(10, 12, 14, 16, "#ffffff1c")
    glass.set(9, 12, "#ffffff65")
    glass.line(16, 12, 20, 16, "#ffffff30")
    glass.line(17, 12, 20, 15, "#a0d8f020")

    final = flatten([base, glass])
    return final

c = test_refinements()
view(c)
