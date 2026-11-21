import pixelbench_api
from pixelbench_api import input_canvas, view, new_canvas

def main():
    f1 = new_canvas(60, 47)
    f1.blit(input_canvas, 15, 0)
    
    legs = new_canvas(35, 47)
    legs.blit(input_canvas, 0, 0)
    legs.clear(0, 0, 35, 27)
    legs.clear(24, 27, 11, 20)
    
    torso = new_canvas(35, 47)
    torso.blit(input_canvas, 0, 0)
    torso.clear(0, 0, 35, 17)
    torso.clear(0, 27, 35, 20)
    torso.clear(17, 19, 18, 8)
    torso.clear(26, 0, 9, 47)
    torso.clear(6, 17, 5, 10)
    
    head = new_canvas(35, 47)
    head.blit(input_canvas, 0, 0)
    head.clear(0, 17, 35, 30)
    head.clear(26, 0, 9, 17)
    
    bracer_arm = new_canvas(35, 47)
    bracer_arm.blit(input_canvas, 0, 0)
    bracer_arm.clear(0, 0, 35, 19)
    bracer_arm.clear(0, 25, 35, 22)
    bracer_arm.clear(0, 19, 17, 6)
    bracer_arm.clear(31, 19, 4, 6)
    
    back_arm = new_canvas(35, 47)
    back_arm.blit(input_canvas, 0, 0)
    back_arm.clear(0, 0, 35, 17)
    back_arm.clear(0, 27, 35, 20)
    back_arm.clear(11, 17, 24, 10)
    back_arm.clear(0, 17, 6, 10)
    
    bow_top = new_canvas(35, 47)
    bow_top.blit(input_canvas, 0, 0)
    bow_top.clear(0, 0, 26, 20)
    bow_top.clear(0, 20, 35, 27)
    
    bow_bot = new_canvas(35, 47)
    bow_bot.blit(input_canvas, 0, 0)
    bow_bot.clear(0, 0, 35, 25)
    bow_bot.clear(0, 25, 24, 22)
    
    bow_grip = new_canvas(35, 47)
    bow_grip.blit(input_canvas, 0, 0)
    bow_grip.clear(0, 0, 35, 20)
    bow_grip.clear(0, 25, 35, 22)
    bow_grip.clear(0, 20, 30, 5)
    
    # We have some gaps in the torso where the arms were.
    # The torso missing pixels are around x=11..16, y=17..26
    # Let's fill the gaps in the torso by just stretching some colors
    
    # Draw string
    
    f2 = new_canvas(60, 47)
    f2.blit(legs, 15, 0)
    
    # Fill gaps in torso
    # Let's just draw some skin and green cloth where back_arm was
    # back_arm was at x=6..10, but that's left of torso. The torso is mostly x=11..20
    # The original back_arm was at 6,17 to 10,26.
    
    f2.blit(torso, 15, 0)
    
    # Fill torso holes
    # The arm hole on the right is at x=17..20, y=19..24
    # The arm hole on the left is at x=6..10, y=17..26
    # Let's just fill them manually with some colors.
    
    f2.blit(head, 15, 1) 
    
    bracer_dx = 4
    f2.blit(bracer_arm, 15 + bracer_dx, 0)
    
    back_dx = -4
    f2.blit(back_arm, 15 + back_dx, 0)
    
    bow_dx = 4
    f2.blit(bow_grip, 15 + bow_dx, 0)
    
    # Rotate bow limbs
    sel_top = bow_top.select(26, 0, 9, 20)
    rot_top = sel_top.rotate(-20, algorithm="rotsprite").preview()
    f2.blit(rot_top, 15 + bow_dx + 26 - 4, 0 - 2)
    
    sel_bot = bow_bot.select(24, 25, 11, 15)
    rot_bot = sel_bot.rotate(20, algorithm="rotsprite").preview()
    f2.blit(rot_bot, 15 + bow_dx + 24 - 1, 25)
    
    view(f2)

if __name__ == "__main__":
    main()
