exec(open("main.py", encoding="utf-8").read())
r = canvas("rays")
print(r.stats_text())
print(r.matrix_text(region=(30, 55, 226, 90)))
