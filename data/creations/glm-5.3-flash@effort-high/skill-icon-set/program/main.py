# Skill icon set: 64x64, 2x2 grid of 32x32 icons
# fireball, ice shield, healing, lightning - dark outline, transparent bg

DARK = "#1b1b2f"

# ---------------- Fireball ----------------
fire = new_canvas(32, 32, name="fireball")
# comet tail swoosh (upper-left)
fire.path("M 2 2 Q 12 4 19 12 L 15 16 Q 8 9 2 2 Z", "#f3722c")
# main ball
fire.circle(19, 19, 8, "#e8491d")
fire.circle(19, 19, 5, "#ffd166")
fire.circle(18, 18, 2, "#fff3b0")
# flame licks: one merged into the ball, one detached teardrop
fire.poly([(15, 12), (17, 5), (19, 12)], "#f3722c")
fire.poly([(23, 11), (25, 5), (27, 11)], "#f3722c")
fire.outline(DARK)
fire.set(19, 26, DARK)  # close the 1px gap in the bottom outline ring

# ---------------- Ice shield ----------------
ice = new_canvas(32, 32, name="ice_shield")
ice.path("M 16 3 L 27 7 L 27 15 Q 27 25 16 29 Q 5 25 5 15 L 5 7 Z", "#4ea8de")
ice.path("M 16 6 L 24 9 L 24 15 Q 24 22 16 26 Q 8 22 8 15 L 8 9 Z", "#a9def9")
# snowflake asterisk in the centre
ice.line(16, 10, 16, 21, "#e0fbfc")
ice.line(11, 15, 21, 15, "#e0fbfc")
ice.line(13, 12, 19, 18, "#e0fbfc")
ice.line(19, 12, 13, 18, "#e0fbfc")
ice.set(16, 15, "#ffffff")
# top-left shine
ice.line(10, 8, 13, 7, "#ffffff")
ice.outline(DARK)

# ---------------- Healing cross ----------------
heal = new_canvas(32, 32, name="healing")
heal.rect(13, 5, 6, 22, "#3fa34d")
heal.rect(5, 13, 22, 6, "#3fa34d")
heal.rect(14, 7, 4, 18, "#8ac926")
heal.rect(7, 14, 18, 4, "#8ac926")
# sparkle at upper-left arm
heal.set(10, 9, "#ffffff")
heal.set(10, 8, "#ffffff")
heal.set(10, 10, "#ffffff")
heal.set(9, 9, "#ffffff")
heal.set(11, 9, "#ffffff")
heal.outline(DARK)

# ---------------- Lightning bolt ----------------
bolt = new_canvas(32, 32, name="lightning")
bolt.poly([(13, 2), (23, 2), (18, 13), (25, 13), (11, 30), (15, 17), (8, 17)], "#ffd60a")
bolt.poly([(15, 4), (19, 4), (15, 12), (12, 12)], "#fff3b0")
bolt.outline(DARK)

# ---------------- Assemble 2x2 grid ----------------
result = new_canvas(64, 64, name="skill_icon_set")
result.blit(fire, 0, 0)
result.blit(ice, 32, 0)
result.blit(heal, 0, 32)
result.blit(bolt, 32, 32)

print(result.stats_text())
print(fire.stats_text())
print(ice.stats_text())
print(heal.stats_text())
print(bolt.stats_text())

finish(result)
