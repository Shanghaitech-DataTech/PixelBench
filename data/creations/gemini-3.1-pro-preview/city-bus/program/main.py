import pixelbench_api as pb

def draw_bus():
    c = pb.new_canvas(64, 32)

    body_color = "#e8e8e8"
    stripe_color = "#0066cc"
    window_color = "#1a2229"
    window_highlight = "#3a4a5a"
    tire_color = "#181818"
    hubcap_color = "#99aacc"
    display_color = "#ffaa00"
    bumper_color = "#2a2a2a"
    pillar_color = "#111111"

    # Roof AC
    c.rect(25, 6, 16, 2, "#cccccc")
    c.rect(26, 5, 14, 1, "#cccccc")
    c.rect(8, 7, 6, 1, "#bbbbbb")

    # Body
    points = [
        (5, 27), (4, 26), (4, 10), (6, 8), (57, 8), (59, 10), (60, 14), (60, 26), (59, 27)
    ]
    c.poly(points, body_color)

    # Roof highlight
    c.line(6, 8, 57, 8, "#ffffff")

    # Bottom shadow
    c.line(4, 25, 60, 25, "#d0d0d0")

    # Bumper
    c.rect(4, 26, 57, 2, bumper_color)
    c.set(4, 27, "transparent")
    c.set(60, 27, "transparent")

    # Exhaust
    c.set(4, 26, "#111111")

    # Stripe
    c.rect(4, 20, 57, 2, stripe_color)

    # Main window
    c.poly([
        (4, 18), (4, 12), (5, 11), (58, 11), (59, 14), (59, 18)
    ], window_color)

    # Window pillars
    for px in [12, 31, 38, 45]:
        c.line(px, 11, px, 18, pillar_color)

    # Doors
    # Rear door
    c.rect(20, 11, 5, 14, window_color)
    c.rect(20, 11, 5, 14, pillar_color, fill=False)
    c.line(22, 11, 22, 24, pillar_color)
    # Front door
    c.rect(52, 11, 5, 14, window_color)
    c.rect(52, 11, 5, 14, pillar_color, fill=False)
    c.line(54, 11, 54, 24, pillar_color)

    # Window highlights
    c.line(6, 13, 9, 13, window_highlight)
    c.line(14, 13, 17, 13, window_highlight)
    c.line(33, 13, 36, 13, window_highlight)
    c.line(40, 13, 43, 13, window_highlight)
    c.line(47, 13, 50, 13, window_highlight)
    
    # Door highlights
    c.set(21, 13, window_highlight)
    c.set(23, 13, window_highlight)
    c.set(53, 13, window_highlight)
    c.set(55, 13, window_highlight)

    # Steering wheel
    c.set(58, 16, "#111111")

    # Side display
    c.rect(26, 12, 5, 3, "#111111")
    c.line(27, 13, 29, 13, display_color)

    # Wheels
    for cx in [14, 46]:
        # Wheel well
        c.circle(cx, 27, 4, bumper_color)
        c.rect(cx-4, 28, 9, 4, "transparent")
        # Tire and hubcap
        c.circle(cx, 27, 3, tire_color)
        c.circle(cx, 27, 1, hubcap_color)

    # Lights
    c.set(59, 24, "#ffffcc")
    c.set(60, 24, "#ffffcc")
    c.set(59, 23, "#ff9900")

    c.set(4, 23, "#ff3333")
    c.set(4, 24, "#ff3333")
    c.set(4, 22, "#ff9900")

    # Mirror
    c.line(60, 15, 62, 13, "#333333")
    c.rect(61, 11, 2, 3, "#222222")

    pb.finish(c)

if __name__ == "__main__":
    draw_bus()
