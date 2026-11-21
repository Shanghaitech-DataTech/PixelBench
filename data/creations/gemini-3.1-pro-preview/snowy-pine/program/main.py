from pixelbench_api import *

def main():
    output = input_canvas.copy(name='output')
    for y in range(135):
        for x in range(82):
            c = output.get(x, y)
            if c == 2: # c1
                output.set(x, y, 9) # gt09
            elif c == 1: # c0
                output.set(x, y, 8) # gt08
    finish(output)

if __name__ == "__main__":
    main()
