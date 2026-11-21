# inspect each icon shape
exec(open("main.py").read().replace("finish(result)", "pass").replace("print(", "#print("))
for cc in (fire, ice, heal, bolt):
    print("=====", cc.name, "=====")
    print(cc.matrix_text())
