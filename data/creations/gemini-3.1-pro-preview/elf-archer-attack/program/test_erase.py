import pixelbench_api
from pixelbench_api import input_canvas, view, new_canvas

def main():
    f1 = new_canvas(48, 47)
    f1.blit(input_canvas, 6, 0)
    
    f2 = f1.copy()
    
    # Erase bow and bracer
    # Top bow
    f2.clear(x=32, y=0, w=10, h=19)
    # Bracer arm
    f2.clear(x=23, y=19, w=18, h=6)
    # Bottom bow
    f2.clear(x=32, y=25, w=10, h=12)
    
    # Erase drawing arm (our left)
    # The arm is roughly around x=11 to 20, y=18 to 23
    f2.clear(x=11, y=18, w=10, h=6)
    
    view(f2)

if __name__ == "__main__":
    main()
