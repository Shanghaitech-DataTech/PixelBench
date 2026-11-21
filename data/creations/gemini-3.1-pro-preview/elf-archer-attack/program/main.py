import pixelbench_api
from pixelbench_api import input_canvas, view, new_canvas, finish

def main():
    f1 = new_canvas(60, 47)
    f1.blit(input_canvas, 15, 0)
    
    f2 = new_canvas(60, 47)
    f2.blit(input_canvas, 15, 0)
    
    # Erase bow
    f2.clear(15+26, 0, 9, 20)
    f2.clear(15+24, 25, 11, 15)
    f2.clear(15+30, 20, 5, 5)
    
    # Erase bracer arm
    f2.clear(15+17, 19, 18, 6)
    
    # Erase back arm
    f2.clear(15+5, 17, 8, 10)
    
    # Torso patch
    f2.rect(15+11, 17, 6, 2, f2.color("#9cde5a")) # green
    f2.rect(15+11, 19, 6, 5, f2.color("#f6d39b")) # skin light
    f2.rect(15+11, 24, 6, 2, f2.color("#c5956a")) # skin dark
    
    f2.line(15+11, 18, 15+16, 18, f2.color("#4f7229"))
    f2.rect(15+11, 21, 6, 3, f2.color("#e0c89e"))
    f2.rect(15+11, 24, 6, 2, f2.color("#c5956a"))
    
    # Back arm pulling back
    # Upper arm
    f2.line(15+12, 18, 15+4, 18, f2.color("#f6d39b"))
    f2.line(15+12, 19, 15+4, 19, f2.color("#e0c89e"))
    f2.line(15+12, 20, 15+4, 20, f2.color("#c5956a"))
    
    # Forearm
    f2.line(15+4, 18, 15+13, 14, f2.color("#f6d39b"))
    f2.line(15+4, 19, 15+14, 15, f2.color("#e0c89e"))
    f2.line(15+4, 20, 15+15, 16, f2.color("#c5956a"))
    
    # Bracer arm
    bracer_arm = new_canvas(35, 47)
    bracer_arm.blit(input_canvas, 0, 0)
    bracer_arm.clear(0, 0, 35, 19)
    bracer_arm.clear(0, 25, 35, 47)
    bracer_arm.clear(0, 19, 17, 6)
    bracer_arm.clear(31, 19, 4, 6)
    
    f2.blit(bracer_arm, 15 + 4, 0)
    
    # Connect bracer arm to shoulder
    f2.rect(15+16, 19, 5, 4, f2.color("#f6d39b"))
    f2.rect(15+16, 23, 5, 2, f2.color("#c5956a"))
    f2.rect(15+16, 21, 5, 2, f2.color("#e0c89e"))
    
    # Bow
    bow_top = new_canvas(35, 47)
    bow_top.blit(input_canvas, 0, 0)
    bow_top.clear(0, 0, 26, 20)
    bow_top.clear(0, 20, 35, 47)
    
    bow_bot = new_canvas(35, 47)
    bow_bot.blit(input_canvas, 0, 0)
    bow_bot.clear(0, 0, 35, 25)
    bow_bot.clear(0, 25, 24, 22)
    
    bow_grip = new_canvas(35, 47)
    bow_grip.blit(input_canvas, 0, 0)
    bow_grip.clear(0, 0, 35, 20)
    bow_grip.clear(0, 25, 35, 47)
    bow_grip.clear(0, 20, 30, 5)
    
    sel_top = bow_top.select(26, 0, 9, 20)
    rot_top = sel_top.rotate(-25, algorithm="rotsprite").preview()
    
    sel_bot = bow_bot.select(24, 25, 11, 15)
    rot_bot = sel_bot.rotate(25, algorithm="rotsprite").preview()
    
    bow_dx = 5
    f2.blit(bow_grip, 15 + bow_dx, 0)
    f2.blit(rot_top, 15 + bow_dx + 26 - 6, 0 - 3)
    f2.blit(rot_bot, 15 + bow_dx + 24 - 2, 25)
    
    # String
    string_color = f2.color("#f1f7f7")
    f2.line(46, 0, 29, 14, string_color)
    f2.line(45, 38, 29, 14, string_color)
    
    # Hand
    f2.rect(15+13, 13, 3, 3, f2.color("#f6d39b"))
    f2.rect(15+13, 14, 2, 2, f2.color("#c5956a"))
    
    finish([f1, f2])

if __name__ == "__main__":
    main()
