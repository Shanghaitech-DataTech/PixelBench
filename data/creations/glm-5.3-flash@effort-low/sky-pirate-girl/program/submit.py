exec(open("main.py").read().replace('print(c.stats_text())', '').replace('print(c.matrix_text(region=(0,0,64,64)))', ''))
result = c
finish(result)
