exec(open('main.py').read())
print(result.matrix_text(region=(32,0,63,31)))
print(result.matrix_text(region=(0,32,31,63)))
