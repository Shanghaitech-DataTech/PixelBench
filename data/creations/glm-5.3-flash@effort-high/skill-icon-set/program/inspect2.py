# final visual check of the fireball fix
exec(open("main.py").read().replace("finish(result)", "pass").replace("print(", "#print("))
print(fire.matrix_text(region=(0, 0, 32, 14)))
print(result.stats_text())
