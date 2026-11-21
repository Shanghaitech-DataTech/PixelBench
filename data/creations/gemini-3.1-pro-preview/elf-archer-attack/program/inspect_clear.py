import pixelbench_api
from pixelbench_api import input_canvas, view

def main():
    f2 = input_canvas.copy()
    # Let's just clear the bow and arm to see what's left
    # Top bow
    f2.clear(x=26, y=0, w=10, h=19)
    # Bracer arm
    f2.clear(x=17, y=19, w=18, h=6)
    # Bottom bow
    f2.clear(x=26, y=25, w=10, h=12)
    
    view(f2)

if __name__ == "__main__":
    main()
