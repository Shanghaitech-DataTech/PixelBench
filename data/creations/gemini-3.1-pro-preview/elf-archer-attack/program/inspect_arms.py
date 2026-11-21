import pixelbench_api
from pixelbench_api import input_canvas, view, new_canvas

def main():
    print(input_canvas.matrix_text(region=(17, 17, 34, 30)))
    print(input_canvas.matrix_text(region=(0, 15, 17, 26)))

if __name__ == "__main__":
    main()
