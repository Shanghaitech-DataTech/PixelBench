import pixelbench_api
from pixelbench_api import input_canvas, view, new_canvas

def main():
    f1 = new_canvas(50, 47)
    f1.blit(input_canvas, 8, 0)
    
    f2 = f1.copy()
    
    # Let's extract the bow into a separate canvas to manipulate it
    bow = new_canvas(35, 47)
    # Top limb
    bow.blit(input_canvas.select(26, 0, 9, 20).preview(), 26, 0)
    # Grip
    bow.blit(input_canvas.select(30, 20, 5, 5).preview(), 30, 20)
    # Bottom limb
    bow.blit(input_canvas.select(24, 25, 11, 15).preview(), 24, 25)
    
    view(bow)

if __name__ == "__main__":
    main()
