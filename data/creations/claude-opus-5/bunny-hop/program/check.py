exec(open("main.py").read().replace("view(f1)", "").replace("view(f2)", ""))
print(f2.matrix_text(region=(0, 20, 30, 35)))
