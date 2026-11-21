import pixelbench_api
from pixelbench_api import input_canvas, view, new_canvas

def main():
    f1 = new_canvas(60, 47)
    f1.blit(input_canvas, 15, 0)
    
    # Let's extract clean parts from input_canvas
    # Background is transparent
    
    legs = new_canvas(35, 47)
    legs.blit(input_canvas, 0, 0)
    legs.clear(0, 0, 35, 27) # clear above y=27
    # clear the bottom tip of the bow that overlaps legs
    legs.clear(24, 27, 11, 20)
    
    torso = new_canvas(35, 47)
    torso.blit(input_canvas, 0, 0)
    torso.clear(0, 0, 35, 17) # clear head
    torso.clear(0, 27, 35, 20) # clear legs
    torso.clear(17, 19, 18, 8) # clear bracer arm
    torso.clear(26, 0, 9, 47) # clear bow
    # clear drawing arm
    torso.clear(6, 17, 5, 10)
    
    head = new_canvas(35, 47)
    head.blit(input_canvas, 0, 0)
    head.clear(0, 17, 35, 30)
    head.clear(26, 0, 9, 17) # clear top of bow
    
    bracer_arm = new_canvas(35, 47)
    bracer_arm.blit(input_canvas, 0, 0)
    bracer_arm.clear(0, 0, 35, 19)
    bracer_arm.clear(0, 25, 35, 22)
    bracer_arm.clear(0, 19, 17, 6)
    bracer_arm.clear(31, 19, 4, 6) # clear bow grip
    
    back_arm = new_canvas(35, 47)
    back_arm.blit(input_canvas, 0, 0)
    back_arm.clear(0, 0, 35, 17)
    back_arm.clear(0, 27, 35, 20)
    back_arm.clear(11, 17, 24, 10) # clear torso
    back_arm.clear(0, 17, 6, 10)
    
    # Bow limbs
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
    
    f2 = new_canvas(60, 47)
    f2.blit(legs, 15, 0)
    f2.blit(torso, 15, 0)
    f2.blit(back_arm, 15, 0)
    f2.blit(head, 15, 0)
    f2.blit(bracer_arm, 15, 0)
    f2.blit(bow_bot, 15, 0)
    f2.blit(bow_top, 15, 0)
    f2.blit(bow_grip, 15, 0)
    
    view(f2)

if __name__ == "__main__":
    main()
