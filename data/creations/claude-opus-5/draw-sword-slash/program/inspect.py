exec(open("main.py").read().replace("finish([f1, f2])", "pass").replace("view(f1)","pass").replace("view(f2)","pass"))
z = f2.select(44, 6, 50, 44).resize(50*8, 44*8).preview("armzoom")
view(z, scale=1)
print(f2.matrix_text(region=(52, 20, 94, 50)))
