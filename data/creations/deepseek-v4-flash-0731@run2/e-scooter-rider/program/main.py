from pixelbench_api import new_canvas, finish


def build():
    c = new_canvas(32, 32)

    wheel = '#202022'
    hub = '#b6bcc4'
    frame = '#6d7685'
    grip = '#3a3f47'
    helmet = '#e63946'
    stripe = '#f7f3e8'
    skin = '#ffd9b3'
    eye = '#2b2b2b'
    shirt = '#3d7ea6'
    pants = '#2f3e4e'
    shoe = '#5c3a21'

    # --- scooter ---
    c.circle(8, 26, 3, wheel)
    c.circle(24, 26, 3, wheel)
    c.circle(8, 26, 1, hub)
    c.circle(24, 26, 1, hub)
    c.rect(6, 24, 20, 2, frame)      # standing deck
    c.rect(22, 14, 2, 10, frame)     # steering stem
    c.rect(21, 12, 6, 2, frame)      # handlebar
    c.rect(25, 12, 2, 2, grip)       # grip end

    # --- rider ---
    c.rect(11, 16, 2, 2, pants)      # back hip
    c.rect(10, 17, 2, 6, pants)      # back leg
    c.rect(9, 23, 3, 2, shoe)        # back foot
    c.rect(16, 16, 4, 2, pants)      # front thigh (knee forward)
    c.rect(18, 18, 2, 5, pants)      # front shin
    c.rect(17, 23, 3, 2, shoe)       # front foot
    c.rect(12, 12, 6, 5, shirt)      # torso leaning forward
    c.line(15, 12, 21, 12, shirt)    # arm reaching to handlebar
    c.rect(22, 12, 2, 2, skin)       # hand on grip
    c.rect(15, 11, 2, 1, skin)       # neck
    c.circle(15, 8, 2, helmet)       # helmet dome
    c.rect(14, 7, 2, 1, stripe)      # helmet stripe
    c.rect(17, 7, 2, 3, skin)        # face
    c.set(18, 8, eye)                # eye

    c.rect(4, 30, 24, 1, (0, 0, 0, 70))  # soft ground shadow

    return c


c = build()
print(c.stats_text())
print(c.matrix_text(region=(10, 4, 28, 27)))
finish([c])
