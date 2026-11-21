import pixelbench_api
from pixelbench_api import input_canvas, view, new_canvas

def main():
    f1 = new_canvas(50, 47)
    f1.blit(input_canvas, 8, 0)
    
    # Let's extract parts
    head = input_canvas.select(0, 0, 25, 17).preview()
    torso = input_canvas.select(10, 17, 15, 10).preview()
    legs = input_canvas.select(8, 27, 25, 20).preview()
    
    # View the parts
    f2 = new_canvas(50, 47)
    f2.blit(legs, 8, 27)
    f2.blit(torso, 8, 17)
    f2.blit(head, 8, 0)
    
    view(f2)

if __name__ == "__main__":
    main()
