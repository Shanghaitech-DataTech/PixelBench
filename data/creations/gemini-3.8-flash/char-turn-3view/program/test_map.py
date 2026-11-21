# Let's test which mapping maps 0..65 to 0..27 and 0..118 to 0..49
# Specifically, we know the boundary xs and ys!
# xs = [0, 2, 5, 7, 9, 12, 14, 16, 19, 21, 24, 26, 28, 31, 33, 35, 38, 40, 42, 45, 47, 50, 52, 54, 57, 59, 61, 64, 66]
# Let's test standard formulas:
def test_map(W_src, W_dst):
    for mode in ["pil", "floor", "round", "int_ratio"]:
        boundaries = [0]
        cur = None
        m = []
        for x in range(W_dst):
            if mode == "pil":
                src = int(x * W_src / W_dst)
            elif mode == "floor":
                src = int(np.floor((x + 0.5) * W_src / W_dst))
            elif mode == "round":
                src = round(x * W_src / W_dst)
            elif mode == "int_ratio":
                src = (x * W_src) // W_dst
            m.append(src)
        b = [0] + [x for x in range(1, W_dst) if m[x] != m[x-1]] + [W_dst]
        print(f"mode={mode}: len={len(b)-1}, b={b[:10]}...")

test_map(28, 66)
test_map(50, 119)
