import random
random.seed(11)
exec(open("main.py").read().split("view(c)")[0])
print(c.matrix_text(region=(0, 42, 25, 58)))
