from pixelbench_api import *

def main():
    c = new_canvas(32, 32)

    # --- Silhouette ---
    # Hot shoe
    c.rect(15, 2, 3, 1, '#a0a0a0')

    # Pentaprism
    c.rect(14, 3, 5, 1, '#a0a0a0')
    c.rect(13, 4, 7, 1, '#a0a0a0')
    c.rect(12, 5, 9, 3, '#a0a0a0')

    # Dials
    c.rect(6, 6, 4, 2, '#606060') # Left dial
    c.rect(7, 5, 2, 1, '#606060')
    c.set(7, 4, '#606060') # Crank knob

    c.rect(21, 6, 4, 2, '#606060') # Right dial
    c.rect(22, 5, 2, 1, '#606060')
    c.rect(25, 5, 3, 3, '#e0e0e0') # Shutter button

    # Top plate
    c.rect(5, 8, 23, 4, '#a0a0a0')
    c.rect(4, 9, 1, 3, '#a0a0a0')
    c.rect(28, 9, 1, 3, '#a0a0a0')

    # Leather body
    c.dither(4, 12, 25, 12, ['#2b1d14', '#3a271c'], pattern='checker')

    # Bottom plate
    c.rect(4, 24, 25, 2, '#a0a0a0')
    c.rect(5, 26, 23, 1, '#a0a0a0')
    c.rect(15, 27, 3, 1, '#a0a0a0') # Tripod mount

    # Strap lugs
    c.rect(3, 12, 1, 2, '#a0a0a0')
    c.rect(29, 12, 1, 2, '#a0a0a0')

    # Lens base
    c.circle(16, 17, 7, '#1a1a1a')

    # Outline
    c.outline('#1a1a1a')

    # --- Details ---
    # Leather shading
    c.line(4, 12, 4, 23, '#1a110b')
    c.line(28, 12, 28, 23, '#1a110b')
    c.line(4, 12, 28, 12, '#1a110b')
    c.line(4, 23, 28, 23, '#1a110b')

    # Bottom plate details
    c.line(4, 24, 28, 24, '#e0e0e0')
    c.line(5, 26, 27, 26, '#606060')
    c.set(4, 25, '#e0e0e0')
    c.set(28, 25, '#e0e0e0')
    c.line(15, 27, 17, 27, '#606060') # Tripod mount shadow

    # Top plate highlights and shadows
    c.line(5, 8, 27, 8, '#e0e0e0')
    c.set(4, 9, '#e0e0e0')
    c.set(28, 9, '#e0e0e0')
    c.line(5, 11, 27, 11, '#606060')

    # Pentaprism highlights and shadows
    c.rect(12, 5, 2, 3, '#e0e0e0')
    c.set(13, 4, '#e0e0e0')
    c.set(14, 3, '#e0e0e0')
    c.rect(19, 5, 2, 3, '#606060')
    c.set(19, 4, '#606060')
    c.set(18, 3, '#606060')

    # Hot shoe
    c.line(15, 2, 17, 2, '#e0e0e0')
    c.set(16, 2, '#1a1a1a')

    # Dials
    c.line(6, 6, 9, 6, '#e0e0e0')
    c.set(7, 5, '#e0e0e0')
    c.set(7, 4, '#111111')

    c.line(21, 6, 24, 6, '#e0e0e0')
    c.set(22, 5, '#e0e0e0')

    c.line(25, 5, 27, 5, '#ffffff')
    c.set(26, 5, '#c03030')

    # Front details
    c.rect(23, 9, 3, 1, '#2b2b2b')
    c.set(24, 9, '#606060')

    c.rect(7, 9, 2, 2, '#606060')
    c.set(8, 9, '#e0e0e0')

    c.rect(14, 6, 5, 2, '#1a1a1a')
    c.set(15, 6, '#ffffff')
    c.set(17, 6, '#ffffff')

    # Self-timer lever
    c.rect(8, 14, 2, 2, '#a0a0a0')
    c.set(8, 14, '#1a1a1a')
    c.line(9, 16, 9, 19, '#a0a0a0')
    c.set(9, 19, '#e0e0e0')

    # Buttons
    c.rect(24, 14, 2, 2, '#111111')
    c.set(24, 14, '#606060')

    c.rect(10, 20, 2, 2, '#111111')
    c.set(10, 20, '#606060')

    # Strap lugs details
    c.set(3, 12, '#e0e0e0')
    c.set(29, 12, '#e0e0e0')

    # Lens
    c.circle(16, 17, 7, '#1a1a1a')
    c.circle(16, 17, 6, '#2b2b2b')

    c.line(10, 17, 11, 17, '#404040')
    c.line(21, 17, 22, 17, '#404040')
    c.line(16, 11, 16, 12, '#404040')
    c.line(16, 22, 16, 23, '#404040')
    c.set(12, 13, '#404040')
    c.set(20, 13, '#404040')
    c.set(12, 21, '#404040')
    c.set(20, 21, '#404040')

    c.circle(16, 17, 5, '#a0a0a0')
    c.set(12, 14, '#e0e0e0')
    c.set(13, 13, '#e0e0e0')
    c.set(14, 12, '#e0e0e0')
    c.set(15, 12, '#e0e0e0')
    c.set(20, 19, '#606060')
    c.set(19, 20, '#606060')
    c.set(18, 21, '#606060')
    c.set(17, 21, '#606060')
    c.set(16, 13, '#c03030')

    c.circle(16, 17, 4, '#111111')

    c.circle(16, 17, 3, '#0b131e')
    c.circle(15, 16, 2, '#1a2c42')
    c.circle(14, 15, 1, '#2c4b6e')
    c.set(14, 15, '#6b9bc2')
    c.set(13, 14, '#ffffff')
    c.set(17, 18, '#415a77')
    c.set(18, 19, '#6b9bc2')

    finish(c)

if __name__ == "__main__":
    main()
