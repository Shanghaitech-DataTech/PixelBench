from pixelbench_api import load
c = load("exports/result.png", add=False)
print(c.stats_text())
# cottage region
print(c.matrix_text(region=(30, 50, 82, 96)))
