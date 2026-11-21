# slash effect: 48x48 sheet, two 24px frame cells, transparent background
c = new_canvas(48, 48, name="output")

W  = c.color("#ffffff", "white")
E  = c.color("#bedcf5", "edge")
T1 = c.color("#ffffffc0", "trail1")
T2 = c.color("#ffffff80", "trail2")


def crescent(cv, ax, ay, bx, by, out_x, in_x, colour):
    """Lens between two quadratic arcs: outer apex at out_x, inner apex at in_x."""
    my = (ay + by) / 2.0
    co = (out_x - 0.25 * ax - 0.25 * bx) * 2.0
    ci = (in_x - 0.25 * ax - 0.25 * bx) * 2.0
    cv.path("M %g %g Q %g %g %g %g Q %g %g %g %g"
            % (ax, ay, co, my, bx, by, ci, my, ax, ay), colour)


# ---- frame 1 : small white arc (cell x 0..23) ----
crescent(c, 12, 12, 7, 36, 20.0, 14.5, E)
crescent(c, 12, 14, 8, 34, 18.5, 15.0, W)

# ---- frame 2 : larger arc with trailing streak (cell x 24..47) ----
# trails first (behind), then the blade paints over any overlap
crescent(c, 32, 17, 31, 31, 34.0, 32.0, T2)
crescent(c, 33, 12, 30, 36, 37.0, 34.0, T1)
crescent(c, 34, 4, 28, 44, 46.0, 38.0, E)
crescent(c, 34, 7, 29, 41, 44.5, 39.0, W)

view(c)
bg = new_canvas(48, 48, background="#202430", name="check")
view(flatten([bg, c], name="preview"))
print(c.stats_text())
finish(c)
