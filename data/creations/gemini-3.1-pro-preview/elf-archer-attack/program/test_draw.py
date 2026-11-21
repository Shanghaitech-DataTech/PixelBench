import pixelbench_api
from pixelbench_api import input_canvas, view, new_canvas

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
    f2.clear(15+6, 17, 7, 8)
    
    # Patch torso
    # The torso is missing pixels at x=15+11..16, y=17..26
    # Let's fill it with skin and green top
    # Green top is around y=17..18
    f2.rect(15+11, 17, 6, 2, f2.color("#9cde5a")) # z
    f2.rect(15+11, 19, 6, 6, f2.color("#f6d39b")) # l
    f2.rect(15+11, 25, 6, 2, f2.color("#c5956a")) # c
    
    # Draw back arm pulling back
    # Shoulder is around 15+11, 17
    # Elbow goes back to 15+4, 19
    # Hand goes to 15+15, 21
    f2.line(15+11, 18, 15+4, 19, f2.color("#f6d39b"))
    f2.line(15+11, 19, 15+4, 20, f2.color("#c5956a"))
    f2.line(15+4, 19, 15+15, 21, f2.color("#f6d39b"))
    f2.line(15+4, 20, 15+15, 22, f2.color("#c5956a"))
    
    # Draw front arm extending forward
    # Shoulder is around 15+17, 19
    # Hand goes to 15+32, 21
    f2.line(15+17, 19, 15+32, 20, f2.color("#687862")) # F
    f2.line(15+17, 20, 15+32, 21, f2.color("#a4b496")) # G
    f2.line(15+17, 21, 15+32, 22, f2.color("#687862")) # F
    f2.line(15+17, 22, 15+32, 23, f2.color("#3c3c3c")) # E
    
    # Hand
    f2.rect(15+32, 20, 3, 3, f2.color("#f6d39b"))
    
    # Bow
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
    
    sel_top = bow_top.select(26, 0, 9, 20)
    rot_top = sel_top.rotate(-25, algorithm="rotsprite").preview()
    
    sel_bot = bow_bot.select(24, 25, 11, 15)
    rot_bot = sel_bot.rotate(25, algorithm="rotsprite").preview()
    
    bow_dx = 4
    f2.blit(bow_grip, 15 + bow_dx, 0)
    f2.blit(rot_top, 15 + bow_dx + 26 - 6, 0 - 3)
    f2.blit(rot_bot, 15 + bow_dx + 24 - 2, 25)
    
    # Draw string
    # Top tip is around 15 + bow_dx + 26 - 6 + 5, 0 - 3 + 2 = 42, -1 -> 42, 0
    # Bot tip is around 15 + bow_dx + 24 - 2 + 2, 25 + 13 = 43, 38
    # Hand is at 15+15, 21 = 30, 21
    f2.line(42, 0, 30, 21, f2.color("#f1f7f7"))
    f2.line(43, 38, 30, 21, f2.color("#f1f7f7"))
    
    view(f2)

if __name__ == "__main__":
    main()
