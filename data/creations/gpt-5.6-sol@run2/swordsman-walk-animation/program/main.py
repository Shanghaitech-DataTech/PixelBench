# Two-frame 16-bit RPG swordsman walk cycle, 32x32 per frame.
result = new_canvas(64, 32, background=None, name="swordsman_walk")

# Compact SNES-style palette.
INK = "#172033"
DEEP = "#202b4f"
CAPE = "#293b73"
CAPE_HI = "#405796"
RED_D = "#7d2636"
RED = "#bd3b35"
RED_HI = "#ed7046"
SKIN_D = "#9e533e"
SKIN = "#e39a67"
SKIN_HI = "#ffd09a"
TUNIC_D = "#654437"
TUNIC = "#a96b43"
BELT = "#3b2930"
METAL_D = "#64738a"
METAL = "#b8c4cd"
METAL_HI = "#eef4ef"
BOOT = "#392c34"
BOOT_HI = "#62433b"
GOLD = "#d69b3a"


def P(points, color):
    result.poly(points, color)


def R(x, y, w, h, color):
    result.rect(x, y, w, h, color)


def draw_frame(ox, phase):
    # Coordinates are local to each 32x32 cell.
    q = lambda pts: [(ox + x, y) for x, y in pts]

    if phase == 0:
        # Rear cape, lifted slightly by the forward step.
        P(q([(10,11),(7,13),(6,18),(4,23),(8,23),(8,26),(12,23),(15,16),(14,12)]), INK)
        P(q([(10,12),(8,14),(8,18),(6,22),(10,21),(9,24),(12,22),(14,16),(13,13)]), CAPE)
        P(q([(9,14),(8,18),(12,17),(12,13)]), CAPE_HI)
        R(ox+6,21,3,1,DEEP)

        # Back leg stepping behind.
        P(q([(12,21),(16,21),(16,25),(19,28),(19,30),(15,30),(14,27),(11,25)]), INK)
        P(q([(13,22),(15,22),(15,25),(18,28),(18,29),(16,29),(14,26),(12,25)]), TUNIC_D)
        R(ox+16,28,4,3,BOOT)
        R(ox+17,28,2,1,BOOT_HI)

        # Front leg extended forward.
        P(q([(14,21),(19,21),(18,25),(22,27),(25,27),(25,30),(20,30),(16,27),(13,25)]), INK)
        P(q([(15,22),(18,22),(17,25),(21,28),(24,28),(24,29),(21,29),(16,26),(14,25)]), TUNIC)
        R(ox+21,28,5,3,BOOT)
        R(ox+22,28,3,1,BOOT_HI)

        # Body and belt.
        P(q([(11,12),(17,11),(20,14),(19,22),(17,25),(11,24),(9,20),(10,14)]), INK)
        P(q([(12,13),(16,12),(18,14),(18,21),(16,23),(12,23),(10,20),(11,14)]), TUNIC)
        R(ox+11,14,2,7,"#c88750")
        R(ox+10,20,9,3,BELT)
        R(ox+14,20,2,2,GOLD)

        # Head and red hair.
        P(q([(10,6),(12,3),(17,3),(20,5),(21,9),(19,13),(13,13),(10,10)]), INK)
        P(q([(13,5),(17,4),(19,6),(20,9),(18,11),(13,11),(11,9)]), SKIN)
        R(ox+18,7,3,2,SKIN_HI)
        R(ox+19,9,2,1,SKIN_D)
        R(ox+18,6,2,1,INK)
        P(q([(10,7),(11,4),(14,2),(18,3),(20,5),(18,6),(15,5),(14,8),(12,7),(12,11),(10,10)]), RED_D)
        P(q([(12,5),(14,3),(18,4),(19,5),(16,5),(14,7),(12,6)]), RED)
        R(ox+14,3,3,1,RED_HI)
        R(ox+10,9,2,4,RED)
        R(ox+9,11,2,2,RED_D)

        # Sword arm and hand.
        P(q([(17,13),(20,13),(23,16),(22,19),(20,19),(20,17),(17,16)]), INK)
        P(q([(18,14),(19,14),(22,16),(21,18),(20,17),(18,16)]), TUNIC)
        R(ox+21,16,3,3,SKIN_D)
        R(ox+22,16,2,2,SKIN)

        # Sword: diagonal up-right, with guard and bright edge.
        result.line(ox+22,16, ox+29,8, INK)
        result.line(ox+23,16, ox+30,9, METAL_D)
        result.line(ox+23,15, ox+29,9, METAL_HI)
        R(ox+21,14,1,5,INK)
        result.line(ox+20,15, ox+23,18, GOLD)
        R(ox+20,17,2,3,BELT)

    else:
        # Cape drops and swings backward as the torso bobs down.
        P(q([(10,12),(7,13),(5,17),(6,22),(3,25),(8,25),(10,23),(13,25),(15,18),(14,13)]), INK)
        P(q([(10,13),(8,14),(7,18),(8,21),(5,24),(9,23),(10,21),(12,23),(14,18),(13,14)]), CAPE)
        P(q([(9,15),(8,18),(9,20),(12,18),(12,14)]), CAPE_HI)
        R(ox+5,23,4,1,DEEP)

        # Back leg now reaches forward.
        P(q([(13,22),(17,21),(19,25),(23,27),(25,27),(25,30),(20,30),(16,27),(12,25)]), INK)
        P(q([(14,22),(16,22),(18,25),(22,28),(24,28),(24,29),(21,29),(17,26),(13,25)]), TUNIC_D)
        R(ox+21,28,5,3,BOOT)
        R(ox+22,28,3,1,BOOT_HI)

        # Front leg planted more vertically.
        P(q([(11,21),(16,21),(16,26),(14,29),(14,31),(9,31),(9,29),(12,25)]), INK)
        P(q([(12,22),(15,22),(15,25),(13,28),(13,29),(10,29),(10,28),(13,24)]), TUNIC)
        R(ox+9,29,6,2,BOOT)
        R(ox+10,29,3,1,BOOT_HI)

        # Body is one pixel lower in passing pose.
        P(q([(11,13),(17,12),(20,15),(19,23),(17,25),(11,25),(9,21),(10,15)]), INK)
        P(q([(12,14),(16,13),(18,15),(18,22),(16,24),(12,24),(10,21),(11,15)]), TUNIC)
        R(ox+11,15,2,7,"#c88750")
        R(ox+10,21,9,3,BELT)
        R(ox+14,21,2,2,GOLD)

        # Head shifted down and forward by one pixel.
        P(q([(11,7),(13,4),(18,4),(21,6),(22,10),(20,14),(14,14),(11,11)]), INK)
        P(q([(14,6),(18,5),(20,7),(21,10),(19,12),(14,12),(12,10)]), SKIN)
        R(ox+19,8,3,2,SKIN_HI)
        R(ox+20,10,2,1,SKIN_D)
        R(ox+19,7,2,1,INK)
        P(q([(11,8),(12,5),(15,3),(19,4),(21,6),(19,7),(16,6),(15,9),(13,8),(13,12),(11,11)]), RED_D)
        P(q([(13,6),(15,4),(19,5),(20,6),(17,6),(15,8),(13,7)]), RED)
        R(ox+15,4,3,1,RED_HI)
        R(ox+11,10,2,4,RED)
        R(ox+10,12,2,2,RED_D)

        # Arm swings slightly back; sword lowers for readable motion.
        P(q([(17,14),(20,14),(23,17),(23,20),(20,20),(20,18),(17,17)]), INK)
        P(q([(18,15),(19,15),(22,17),(22,19),(20,18),(18,17)]), TUNIC)
        R(ox+22,18,3,3,SKIN_D)
        R(ox+23,18,2,2,SKIN)

        # Long sword, near-horizontal diagonal.
        result.line(ox+23,18, ox+30,12, INK)
        result.line(ox+24,19, ox+31,13, METAL_D)
        result.line(ox+24,18, ox+30,12, METAL_HI)
        R(ox+22,16,1,5,INK)
        result.line(ox+21,17, ox+24,20, GOLD)
        R(ox+21,19,2,3,BELT)

    # A tiny eye highlight strengthens the right-facing read.
    result.set(ox + (19 if phase == 0 else 20), 7 if phase == 0 else 8, "#f8e6bf")


draw_frame(0, 0)
draw_frame(32, 1)

view(result, scale=12, margin=0)
finish(result)
