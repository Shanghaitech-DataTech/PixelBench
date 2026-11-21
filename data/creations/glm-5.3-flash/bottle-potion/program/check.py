c = canvas("output")
# any background-white pixel strictly inside the bottle silhouette?
bad = []
for y in range(22, 62):
    for x in range(2, 62):
        if c.get(x, y) == 1:
            bad.append((x, y))
print("white pixels inside bottle area:", bad)

# dump the bubble neighbourhoods
for (bx, by, br) in [(27,27,1),(24,31,2),(38,29,1),(45,34,2),(42,49,2)]:
    print(f"--- bubble ({bx},{by},r={br}) ---")
    for y in range(by-3, by+4):
        print(f"y={y}: " + "".join({1:'.',2:'#',11:'P',12:'L',13:'D',14:'S',15:'o',16:'*'}[c.get(x,y)] for x in range(bx-4, bx+5)))
