output = input_canvas.copy(name="output")
blue = output.color("#0097e0")
yellow = output.color("#ffe044")
for y in range(14, 50):
    for x in range(32, 56):
        if output.get(x, y) == blue:
            output.set(x, y, yellow)
print(output.stats_text())
print(output.matrix_text(region=(30,14,54,51)))
finish(output)
