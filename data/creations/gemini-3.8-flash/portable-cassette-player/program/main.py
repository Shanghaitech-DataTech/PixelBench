import sys
from pixelbench_api import *

def build_portable_cassette_player():
    base = new_canvas(32, 32)
    glass = new_canvas(32, 32)

    # ==========================================
    # COLOR PALETTE
    # ==========================================
    c_outline = "#13171f"
    c_shadow = "#0c0e14"

    # Classic Cobalt Metallic Blue (TPS-L2 style)
    c_blue_darkest = "#152538"
    c_blue_dark = "#1d3857"
    c_blue_base = "#2a5987"
    c_blue_mid = "#3872a8"
    c_blue_light = "#4f8fc9"
    c_blue_hi = "#7eb5e6"

    # Brushed Aluminum / Silver
    c_silver_darkest = "#323740"
    c_silver_dark = "#525a66"
    c_silver_mid = "#828c9c"
    c_silver_light = "#b6c1d1"
    c_silver_hi = "#e6ecf5"
    c_silver_white = "#ffffff"

    # Retro Orange / Red Accents
    c_orange_dark = "#9c2a13"
    c_orange = "#e64a22"
    c_orange_hi = "#ff754d"
    c_led_glow = "#ff1f1f"
    c_led_dark = "#590b0b"

    # Cassette Tape Shell & Label
    c_cas_shell = "#ded7cc"
    c_cas_shell_dark = "#aba294"
    c_cas_shell_hi = "#f4efe6"
    c_cas_label = "#f7f5ee"
    c_cas_stripe = "#d93f1c"
    c_cas_notes = "#8a8174"
    c_cas_interior = "#10131a"
    c_cas_roller = "#c99c44"

    # Magnetic Tape
    c_tape_dark = "#2b160c"
    c_tape_mid = "#4a2818"
    c_tape_light = "#6e3b23"

    # Reel Hubs
    c_hub_white = "#ffffff"
    c_hub_hole = "#10131a"

    # Headphone Jack & Cable
    c_cable_black = "#15171e"
    c_cable_body = "#252a33"
    c_cable_mid = "#424b59"
    c_cable_hi = "#728196"
    c_jack_metal = "#d4dae6"

    # ==========================================
    # 1. HEADPHONE JACK & CABLE
    # ==========================================
    # 3.5mm plug barrel at x = 21..22, y = 3..5
    base.set(21, 5, c_jack_metal)
    base.set(22, 5, c_silver_dark)
    base.rect(21, 3, 2, 2, c_cable_black)
    base.set(21, 3, c_cable_mid)
    base.set(21, 4, c_silver_light)
    base.set(22, 4, c_silver_dark)
    base.set(21, 2, c_cable_mid)
    base.set(22, 2, c_cable_black)

    # Cord Path - Coiling smoothly along the right side
    cord_data = [
        # Arch over from jack
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
        # Curve inward toward player
        (28, 9, c_cable_mid),
        (28, 10, c_cable_body),
        (27, 11, c_cable_hi),
        (27, 12, c_cable_body),
        (26, 13, c_cable_mid),
        (26, 14, c_cable_hi),
        (26, 15, c_cable_body),
        # Curve back outward
        (27, 16, c_cable_hi),
        (27, 17, c_cable_body),
        (28, 18, c_cable_hi),
        (28, 19, c_cable_hi),
        (29, 20, c_cable_body),
        (29, 21, c_cable_hi),
        (29, 22, c_cable_hi),
        (29, 23, c_cable_body),
        (29, 24, c_cable_black),
        # Natural loop at bottom right
        (28, 25, c_cable_mid),
        (28, 26, c_cable_hi),
        (27, 27, c_cable_body),
        (26, 28, c_cable_hi),
        (25, 29, c_cable_hi),
        (25, 30, c_cable_body),
        (26, 31, c_cable_mid),
        (27, 31, c_cable_hi),
        (28, 31, c_cable_hi),
        (29, 30, c_cable_body),
        (29, 29, c_cable_mid),
        (29, 28, c_cable_black),
        (28, 27, c_cable_mid)
    ]
    for x, y, col in cord_data:
        base.set(x, y, col)

    # ==========================================
    # 2. TOP PLAYBACK CONTROLS (Mechanical Push Buttons)
    # ==========================================
    # REWIND [ ◄◄ ] (x = 7..8, y = 4..6)
    base.rect(7, 4, 2, 3, c_silver_mid)
    base.line(7, 4, 8, 4, c_silver_hi)
    base.set(7, 5, c_silver_light)
    base.set(8, 5, c_silver_dark)
    base.set(8, 6, c_silver_darkest)

    # FAST FORWARD [ ►► ] (x = 10..11, y = 4..6)
    base.rect(10, 4, 2, 3, c_silver_mid)
    base.line(10, 4, 11, 4, c_silver_hi)
    base.set(10, 5, c_silver_light)
    base.set(11, 5, c_silver_dark)
    base.set(11, 6, c_silver_darkest)

    # PLAY [ ► ] (x = 13..15, y = 5..6 - depressed active state!)
    base.rect(13, 5, 3, 2, c_silver_light)
    base.line(13, 5, 15, 5, c_silver_white)
    base.set(13, 6, c_silver_light)
    base.set(14, 6, c_silver_mid)
    base.set(15, 6, c_silver_dark)
    base.set(14, 5, c_orange) # Play indicator

    # STOP / EJECT [ ■ ] (x = 17..18, y = 4..6)
    base.rect(17, 4, 2, 3, c_silver_mid)
    base.line(17, 4, 18, 4, c_silver_hi)
    base.set(17, 5, c_silver_light)
    base.set(18, 5, c_silver_dark)
    base.set(18, 6, c_silver_darkest)

    # ==========================================
    # 3. CASSETTE PLAYER BODY
    # ==========================================
    base.rect(6, 7, 18, 22, c_blue_base)
    base.rect(6, 7, 18, 22, c_outline, fill=False)
    # Rounded corners
    base.set(6, 7, "transparent")
    base.set(23, 7, "transparent")
    base.set(6, 28, "transparent")
    base.set(23, 28, "transparent")
    base.set(7, 7, c_outline)
    base.set(22, 7, c_outline)
    base.set(7, 28, c_outline)
    base.set(22, 28, c_outline)

    # Top brushed aluminum plate (y = 7..9)
    base.rect(7, 7, 16, 3, c_silver_mid)
    base.line(7, 7, 22, 7, c_silver_hi)
    base.line(7, 8, 22, 8, c_silver_light)
    base.line(7, 9, 22, 9, c_silver_dark)
    # Hot Line accent button (x = 19..20, y = 8..9)
    base.rect(19, 8, 2, 2, c_orange)
    base.set(19, 8, c_orange_hi)
    base.set(20, 9, c_orange_dark)

    # Playback symbols on silver plate (y = 9)
    base.set(7, 9, c_silver_darkest)   # ◄
    base.set(8, 9, c_silver_darkest)   # ◄
    base.set(10, 9, c_silver_darkest)  # ►
    base.set(11, 9, c_silver_darkest)  # ►
    base.set(14, 9, c_orange_dark)     # ► (active play)
    base.set(17, 9, c_silver_darkest)  # ■

    # Body Highlights & Shading
    base.line(7, 10, 7, 27, c_blue_hi)
    base.line(22, 10, 22, 27, c_blue_darkest)
    base.line(7, 27, 22, 27, c_blue_dark)
    base.line(8, 28, 21, 28, c_outline)

    # ==========================================
    # 4. VOLUME CONTROLS
    # ==========================================
    # A) Left-side Knurled Thumbwheel Dial (x = 4..5, y = 14..18)
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

    # B) Front Volume Slider & Lower Panel (y = 22..28)
    base.line(7, 22, 22, 22, c_blue_darkest)

    # Volume icon (speaker wedge): x = 8..10, y = 24..25
    base.set(8, 25, c_silver_light)
    base.set(9, 24, c_silver_white)
    base.set(9, 25, c_silver_white)
    base.set(9, 26, c_silver_mid)
    base.set(10, 24, c_blue_light)
    base.set(10, 25, c_blue_light)

    # Volume gradation scale (y = 24):
    base.set(12, 24, c_silver_dark)
    base.set(14, 24, c_silver_mid)
    base.set(16, 24, c_silver_light)
    base.set(18, 24, c_silver_hi)
    base.set(20, 24, c_silver_white)

    # Volume slider track (y = 25):
    base.line(12, 25, 20, 25, c_shadow)
    base.line(12, 26, 20, 26, c_blue_darkest)

    # Volume slider knob (x = 16..17, y = 24..26):
    base.rect(16, 24, 2, 3, c_silver_hi)
    base.set(16, 24, c_silver_white)
    base.set(17, 26, c_silver_dark)
    base.set(16, 25, c_orange) # Orange center notch indicator

    # Battery LED at x = 8, y = 27
    base.set(7, 27, c_led_dark)
    base.set(8, 27, c_led_glow)

    # "STEREO" metallic badge (x = 12..20, y = 27):
    base.line(12, 27, 20, 27, c_silver_darkest)
    base.set(13, 27, c_silver_mid)
    base.set(15, 27, c_silver_light)
    base.set(17, 27, c_silver_mid)
    base.set(19, 27, c_silver_light)

    # ==========================================
    # 5. CASSETTE DOOR & TRANSPARENT WINDOW
    # ==========================================
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
    # Retro orange stripe on row 13
    base.line(9, 13, 20, 13, c_cas_stripe)
    # Notes / text marks on row 14
    base.set(10, 14, c_cas_stripe) # "A" side marker
    base.set(12, 14, c_cas_notes)  # handwriting track line
    base.set(14, 14, c_cas_notes)
    base.set(16, 14, c_cas_notes)
    base.set(18, 14, c_cas_notes)

    # Cassette Center Cutout: x = 9 to 20, y = 15 to 18
    base.rect(9, 15, 12, 4, c_cas_interior)

    # --- REEL 1: Left Tape Reel (Fuller tape spool) ---
    # Center at (11, 16)
    base.rect(9, 15, 5, 4, c_tape_mid)
    base.set(9, 15, c_cas_interior)
    base.set(13, 15, c_cas_interior)
    base.set(9, 18, c_cas_interior)
    base.set(13, 18, c_cas_interior)
    base.set(10, 15, c_tape_light)
    base.set(11, 15, c_tape_light)
    base.set(12, 17, c_tape_dark)
    base.set(11, 18, c_tape_dark)

    # Left Hub (white 4-tooth cog with dark center hole)
    base.set(11, 16, c_hub_hole)
    base.set(11, 15, c_hub_white)
    base.set(11, 17, c_hub_white)
    base.set(10, 16, c_hub_white)
    base.set(12, 16, c_hub_white)

    # --- REEL 2: Right Tape Reel (Thinner tape roll) ---
    # Center at (18, 16)
    base.rect(16, 15, 5, 4, c_cas_interior)
    base.set(17, 15, c_tape_mid)
    base.set(19, 15, c_tape_mid)
    base.set(16, 16, c_tape_mid)
    base.set(20, 16, c_tape_mid)
    base.set(17, 17, c_tape_dark)
    base.set(19, 17, c_tape_dark)

    # Right Hub (white 4-tooth cog with dark center hole)
    base.set(18, 16, c_hub_hole)
    base.set(18, 15, c_hub_white)
    base.set(18, 17, c_hub_white)
    base.set(17, 16, c_hub_white)
    base.set(19, 16, c_hub_white)

    # --- Center Tape Bridge & Counter Tick Marks ---
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

    # ==========================================
    # 6. TRANSPARENT WINDOW GLASS HIGHLIGHTS (Layer 2)
    # ==========================================
    # Subtle diagonal glass reflections
    glass.line(9, 12, 13, 16, "#ffffff35")
    glass.line(10, 12, 14, 16, "#ffffff1c")
    glass.set(9, 12, "#ffffff65")
    glass.line(16, 12, 20, 16, "#ffffff30")
    glass.line(17, 12, 20, 15, "#a0d8f020")

    final = flatten([base, glass])
    return final

result = build_portable_cassette_player()
view(result)
finish(result)
