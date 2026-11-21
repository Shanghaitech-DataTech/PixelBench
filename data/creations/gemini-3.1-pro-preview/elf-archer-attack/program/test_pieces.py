import pixelbench_api
from pixelbench_api import input_canvas, view, new_canvas

def main():
    head = input_canvas.select(0, 0, 25, 17).preview()
    torso = input_canvas.select(10, 17, 15, 10).preview()
    legs = input_canvas.select(8, 27, 25, 20).preview()
    bracer_arm = input_canvas.select(17, 19, 18, 6).preview()
    back_arm = input_canvas.select(6, 17, 8, 10).preview()
    bow_top = input_canvas.select(26, 0, 9, 20).preview()
    bow_grip = input_canvas.select(30, 20, 5, 5).preview()
    bow_bot = input_canvas.select(24, 25, 11, 15).preview()
    
    f = new_canvas(80, 50)
    f.blit(head, 0, 0)
    f.blit(torso, 30, 0)
    f.blit(legs, 50, 0)
    f.blit(bracer_arm, 0, 20)
    f.blit(back_arm, 25, 20)
    f.blit(bow_top, 40, 20)
    f.blit(bow_grip, 55, 20)
    f.blit(bow_bot, 65, 20)
    
    view(f)

if __name__ == "__main__":
    main()
