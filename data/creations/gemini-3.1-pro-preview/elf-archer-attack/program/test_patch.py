import pixelbench_api
from pixelbench_api import input_canvas, view, new_canvas

def main():
    f1 = new_canvas(60, 47)
    f1.blit(input_canvas, 15, 0)
    
    torso = new_canvas(35, 47)
    torso.blit(input_canvas, 0, 0)
    torso.clear(0, 0, 35, 17)
    torso.clear(0, 27, 35, 20)
    torso.clear(26, 0, 9, 47)
    
    # We will just patch the torso directly on the final canvas
    f2 = new_canvas(60, 47)
    f2.blit(input_canvas, 15, 0)
    
    # Let's erase the bow
    f2.clear(15+26, 0, 9, 20)
    f2.clear(15+24, 25, 11, 15)
    f2.clear(15+30, 20, 5, 5)
    
    # Erase bracer arm
    f2.clear(15+17, 19, 18, 6)
    
    # Erase back arm
    f2.clear(15+6, 17, 7, 8)
    
    view(f2)

if __name__ == "__main__":
    main()
