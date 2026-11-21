import math

HEX = {
    "outline":   "#141221",
    "robe_deep": "#1b1c2b",
    "robe_dark": "#26293d",
    "robe_mid":  "#353b57",
    "robe_light":"#4b5375",
    "robe_hi":   "#626b90",
    "trim":      "#98a2c2",
    "hair":      "#191622",
    "hair_hi":   "#3b3550",
    "skin":      "#e3b494",
    "skin_sh":   "#b8835f",
    "skin_dk":   "#7d5540",
    "skin_hi":   "#f4d2b4",
    "hat_l":     "#cbab6e",
    "hat_m":     "#a5824b",
    "hat_d":     "#7a5a30",
    "hat_dd":    "#4f3a1d",
    "sash":      "#93313f",
    "sash_d":    "#5d1d29",
    "sash_l":    "#b8505a",
    "metal":     "#d6dee7",
    "metal_d":   "#93a0af",
    "gold":      "#caa552",
    "gold_d":    "#8d6f2f",
    "sky_top":   "#8ea3ba",
    "sky_mid":   "#b4c3d2",
    "sky_low":   "#d9e2ea",
    "mist":      "#eef3f7",
    "mtn_far":   "#b3c2cf",
    "mtn_mid":   "#97aaba",
    "mtn_near":  "#7f93a6",
    "ground":    "#ccd8e2",
    "ground_d":  "#b3c2d0",
}

art = new_canvas(256, 256, background=HEX["sky_low"], name="result")
fig = new_canvas(256, 256, name="figure")

col = {}
for k, v in HEX.items():
    col[k] = art.color(v, name=k)


def C(k):
    return col[k]


def ell_pts(cx, cy, rx, ry, rot):
    a = math.radians(rot)
    ca, sa = math.cos(a), math.sin(a)
    return (cx - rx * ca, cy - rx * sa, cx + rx * ca, cy + rx * sa)


def ell(c, cx, cy, rx, ry, rot, colour, part="full"):
    x0, y0, x1, y1 = ell_pts(cx, cy, rx, ry, rot)
    if part == "full":
        d = ("M%.1f %.1f A%s %s %s 0 1 %.1f %.1f A%s %s %s 0 1 %.1f %.1f Z"
             % (x0, y0, rx, ry, rot, x1, y1, rx, ry, rot, x0, y0))
    elif part == "low":
        d = "M%.1f %.1f A%s %s %s 0 1 %.1f %.1f Z" % (x0, y0, rx, ry, rot, x1, y1)
    else:
        d = "M%.1f %.1f A%s %s %s 0 1 %.1f %.1f Z" % (x1, y1, rx, ry, rot, x0, y0)
    c.path(d, colour, fill=True)


def ell_edge(c, cx, cy, rx, ry, rot, colour):
    x0, y0, x1, y1 = ell_pts(cx, cy, rx, ry, rot)
    d = ("M%.1f %.1f A%s %s %s 0 1 %.1f %.1f A%s %s %s 0 1 %.1f %.1f"
         % (x0, y0, rx, ry, rot, x1, y1, rx, ry, rot, x0, y0))
    c.path(d, colour, fill=False)


# ---------------------------------------------------------------- background
b = art
b.rect(0, 0, 256, 256, C("sky_low"))
b.rect(0, 0, 256, 44, C("sky_top"))
b.dither(0, 44, 256, 20, [C("sky_top"), C("sky_mid")], pattern="bayer4")
b.rect(0, 64, 256, 34, C("sky_mid"))
b.dither(0, 96, 256, 24, [C("sky_mid"), C("sky_low")], pattern="bayer4")

b.poly([(0, 108), (14, 84), (30, 100), (52, 68), (70, 94), (90, 76),
        (108, 98), (130, 72), (150, 96), (172, 80), (192, 100), (214, 82),
        (234, 98), (250, 88), (255, 94), (255, 178), (0, 178)], C("mtn_far"))
b.poly([(0, 150), (16, 126), (38, 144), (56, 116), (78, 140), (96, 122),
        (118, 144), (140, 120), (162, 142), (186, 126), (208, 146),
        (230, 128), (248, 148), (255, 140), (255, 196), (0, 196)], C("mtn_mid"))
# distant pine treeline along the mist
for (tx, th) in ((6, 16), (20, 12), (34, 18), (46, 11), (58, 15),
                 (196, 14), (210, 18), (224, 12), (238, 16), (250, 11)):
    top = 188 - th
    b.poly([(tx - 5, 190), (tx, top), (tx + 5, 190)], C("mtn_mid"))
    b.line(tx, 190, tx, 194, C("mtn_mid"))
b.dither(2, 176, 62, 12, [C("mtn_far"), C("mtn_mid")], pattern="checker")
b.dither(190, 176, 64, 12, [C("mtn_far"), C("mtn_mid")], pattern="checker")

b.rect(0, 156, 256, 8, C("mist"))
b.dither(0, 150, 256, 6, [C("mist"), C("mtn_mid")], pattern="bayer4")
b.rect(0, 164, 256, 10, C("sky_low"))
b.dither(0, 158, 256, 6, [C("sky_low"), C("mist")], pattern="checker")
b.rect(0, 190, 256, 66, C("ground"))
b.dither(0, 180, 256, 10, [C("ground"), C("sky_low")], pattern="bayer4")
for i, yy in enumerate((202, 216, 232, 248)):
    b.line(6 + i * 5, yy, 250 - i * 5, yy, C("ground_d"))
b.dither(20, 204, 210, 2, [C("ground"), C("ground_d")], pattern="checker")
b.dither(14, 224, 226, 4, [C("ground"), C("mist")], pattern="checker")
b.ellipse(128, 150, 74, 58, C("mist"))
b.dither(56, 196, 148, 6, [C("ground"), C("ground_d")], pattern="bayer4")
b.ellipse(124, 242, 66, 9, C("ground_d"))
b.ellipse(124, 240, 40, 5, C("mist"))

# ---------------------------------------------------------------- figure
F = fig

F.poly([(112, 228), (128, 228), (126, 248), (108, 249)], C("robe_deep"))
F.poly([(140, 228), (156, 228), (160, 249), (142, 249)], C("robe_deep"))

# ---------------- back hair
F.path("M114 60 L146 58 C155 72 160 92 162 116 C164 142 160 166 152 184 "
       "C147 192 141 196 135 198 C133 180 131 160 127 140 "
       "C123 116 118 88 114 72 Z", C("hair"))

# ---------------- robe
robe = ("M102 110 C98 122 98 133 102 143 "
        "C96 166 90 198 87 220 C86 230 86 236 87 240 "
        "C104 246 132 248 152 246 C162 240 170 230 172 216 "
        "C175 192 167 164 159 143 C155 131 155 118 157 106 "
        "C147 100 137 97 128 97 C118 97 110 100 102 110 Z")
F.path(robe, C("robe_dark"))

F.path("M104 112 C100 123 100 133 104 143 C98 166 92 198 89 220 "
       "C88 230 88 236 89 239 C100 242 112 244 122 245 "
       "C120 218 116 190 113 166 C110 148 111 128 112 108 "
       "C109 109 106 110 104 112 Z", C("robe_mid"))
F.path("M158 108 C156 120 156 132 160 144 C168 165 176 192 173 216 "
       "C171 230 163 240 153 246 L147 246 C157 238 164 228 166 216 "
       "C169 192 161 164 154 143 C150 131 151 117 152 106 Z", C("robe_deep"))
F.path("M130 152 C134 178 140 214 143 246 L138 246 C135 214 129 178 126 152 Z",
       C("robe_deep"))
F.path("M116 152 C113 176 109 206 107 238 L111 238 C113 208 117 178 120 154 Z",
       C("robe_light"))
F.path("M145 158 C150 182 156 216 159 242 L163 240 C160 214 154 180 149 156 Z",
       C("robe_light"))
# wind-blown creases sweeping across the skirt
F.path("M118 176 C124 184 130 196 133 210 L130 212 C126 198 121 187 115 180 Z",
       C("robe_deep"))
F.path("M112 200 C120 208 128 220 133 232 L130 234 C125 222 118 211 109 204 Z",
       C("robe_deep"))
F.path("M140 186 C146 194 152 204 156 216 L152 218 C149 207 144 197 137 190 Z",
       C("robe_light"))
F.path("M124 216 C130 224 136 232 140 240 L136 241 C132 233 127 226 121 220 Z",
       C("robe_light"))
F.path("M87 236 C104 243 132 246 152 244 C162 238 169 228 172 216 "
       "L174 222 C171 234 164 244 152 248 C132 250 104 248 86 241 Z",
       C("robe_deep"))
F.path("M88 235 C104 241 130 243 151 241 L152 243 C132 245 104 243 87 237 Z",
       C("trim"))

# ---------------- collar (crossed)
F.path("M117 99 L124 98 L133 124 L126 126 Z", C("trim"))
F.path("M136 97 L143 101 L137 116 L130 114 Z", C("robe_light"))
F.path("M124 98 L133 124 L129 125 L121 100 Z", C("robe_hi"))

# ---------------- sash
F.path("M103 134 C114 141 143 143 159 136 L160 148 C142 156 113 154 104 146 Z",
       C("sash"))
F.path("M103 134 C114 141 143 143 159 136 L159 139 C143 147 113 145 103 137 Z",
       C("sash_l"))
F.path("M104 145 C114 153 142 155 160 147 L159 151 C142 159 113 157 104 149 Z",
       C("sash_d"))
F.path("M155 138 L168 134 L170 146 C163 154 158 164 155 176 L148 172 "
       "C152 160 156 148 155 138 Z", C("sash"))
F.path("M157 140 L166 137 L166 146 C160 154 156 164 153 174 L150 172 "
       "C153 160 156 150 157 140 Z", C("sash_l"))
F.path("M148 172 C146 184 143 194 137 204 L144 208 C150 196 153 184 153 172 Z",
       C("sash_d"))

# ---------------- near (left) sleeve: shoulder -> wrist, fabric hangs below
F.path("M102 108 C96 116 90 124 86 132 "
       "C82 146 78 166 77 186 C82 191 89 191 93 187 "
       "C96 170 99 150 102 134 C104 124 106 115 108 110 Z", C("robe_mid"))
F.path("M86 132 C82 146 78 166 77 186 C82 191 89 191 93 187 "
       "C91 176 92 160 94 144 L96 134 Z", C("robe_deep"))
F.path("M102 108 C96 116 90 124 86 132 L90 133 "
       "C95 124 100 116 106 110 Z", C("robe_light"))
F.path("M77 186 C82 191 89 191 93 187 L92 191 C86 194 79 192 75 188 Z",
       C("robe_deep"))
F.path("M99 138 C100 152 97 170 94 186 L97 184 C100 168 102 150 102 138 Z",
       C("robe_light"))
# contour seam so the sleeve reads against the robe
F.path("M106 112 C103 128 101 146 98 162 C96 174 94 182 92 188",
       C("outline"), fill=False)

# ---------------- far (right) sleeve
F.path("M157 106 C165 116 169 132 171 150 C173 168 172 184 169 196 "
       "C162 199 156 194 154 186 C152 168 153 148 154 130 "
       "C154 120 155 112 157 106 Z", C("robe_mid"))
F.path("M163 148 C166 164 168 182 167 194 C170 195 171 194 171 193 "
       "C173 180 172 162 169 146 Z", C("robe_light"))
F.path("M158 114 C161 126 162 144 161 158 C160 172 160 182 162 190 "
       "L157 189 C154 176 154 158 154 142 C154 130 155 122 158 114 Z",
       C("robe_deep"))
F.path("M161 186 C166 185 170 188 171 193 C172 198 169 202 164 203 "
       "C159 204 156 200 156 196 C156 191 158 187 161 186 Z", C("skin"))
F.line(158, 192, 169, 190, C("skin_sh"))
F.line(158, 196, 169, 194, C("skin_sh"))

# ---------------- sword (jian)
F.path("M69 139 L75 139 L70 208 L64 232 L63 208 Z", C("metal"))
F.path("M69 141 L71 141 L68 206 L66 220 L65 206 Z", C("metal_d"))
F.path("M64 232 L70 208 L72 212 L66 235 Z", C("metal"))
F.path("M61 134 L75 132 L76 137 L62 139 Z", C("gold"))
F.path("M62 137 L75 135 L75 137 L62 139 Z", C("gold_d"))
F.path("M64 102 L72 101 L77 133 L67 135 Z", C("robe_deep"))
F.line(66, 105, 72, 131, C("robe_dark"))
F.line(69, 104, 74, 130, C("robe_dark"))
F.ellipse(67, 100, 4, 4, C("gold"))
F.ellipse(66, 99, 2, 2, C("gold_d"))

# ---------------- hand on the hilt
F.poly([(72, 112), (86, 124), (82, 132), (68, 120)], C("skin_sh"))
F.poly([(74, 112), (86, 124), (84, 128), (74, 116)], C("skin"))
F.path("M60 114 C66 111 72 113 74 118 C76 124 73 130 67 131 "
       "C61 132 57 128 57 123 C57 119 58 116 60 114 Z", C("skin"))
F.poly([(74, 114), (80, 122), (77, 128), (71, 122)], C("skin_sh"))
F.line(59, 119, 73, 116, C("skin_sh"))
F.line(58, 123, 72, 120, C("skin_sh"))
F.line(59, 127, 71, 124, C("skin_sh"))
F.path("M60 114 C64 112 67 113 67 116 C67 118 63 119 61 118 "
       "C59 117 59 115 60 114 Z", C("skin_hi"))

# ---------------- neck & head
F.path("M119 90 L134 90 L136 104 L118 104 Z", C("skin_sh"))
F.ellipse(128, 81, 13, 15, C("skin_sh"))
F.ellipse(124, 80, 10, 13, C("skin"))
F.poly([(113, 83), (108, 88), (112, 91), (114, 89)], C("skin"))
F.path("M111 70 L142 70 L141 82 L110 84 Z", C("skin_dk"))
F.poly([(106, 83), (113, 81), (114, 90), (107, 90)], C("skin_dk"))
F.poly([(108, 87), (112, 85), (112, 89)], C("skin_hi"))
F.line(115, 92, 122, 93, C("skin_dk"))
F.line(115, 93, 122, 94, C("skin_sh"))
F.path("M117 94 C123 98 131 97 136 92 L137 99 C132 103 122 103 116 98 Z",
       C("skin_sh"))

# ---------------- loose hair strands
F.path("M114 68 C109 78 108 92 110 106 L116 104 C114 92 115 80 119 72 Z",
       C("hair"))
F.path("M141 66 C147 76 150 92 149 108 L154 108 C157 92 152 78 147 64 Z",
       C("hair"))
F.path("M155 104 C160 122 163 144 162 164 L167 164 C169 142 165 120 160 102 Z",
       C("hair"))
F.line(115, 74, 112, 102, C("hair_hi"))
F.line(145, 72, 148, 100, C("hair_hi"))
F.line(159, 112, 164, 152, C("hair_hi"))
F.path("M148 78 C152 92 153 104 152 116", C("hair_hi"), fill=False)

# ---------------- hat
F.path("M116 42 C100 52 88 64 84 78 L148 70 C158 67 164 63 167 60 Z",
       C("hat_m"))
F.path("M116 42 C102 52 92 64 87 78 L95 77 C99 64 107 53 117 45 Z",
       C("hat_l"))
F.path("M148 70 C158 67 164 63 167 60 L145 68 Z", C("hat_d"))
for i in range(5):
    xt = 116 + (i - 2) * 4
    xb = 90 + i * 18
    F.line(xt, 50 + abs(i - 2) * 4, xb, 76 - (i - 2) * 2, C("hat_d"))
F.line(116, 46, 102, 76, C("hat_l"))

ell(F, 126, 68, 42, 11, -11, C("hat_m"))
ell(F, 126, 68, 42, 11, -11, C("hat_d"), part="low")
ell_edge(F, 126, 68, 42, 11, -11, C("hat_dd"))

save("east_hero", fig)

# ---------------------------------------------------------------- outline
w, h, data = fig.to_rgba()
op = [[data[(y * w + x) * 4 + 3] > 0 for x in range(w)] for y in range(h)]
# flood-fill transparency from the border, then plug any interior hole
ext = [[False] * w for _ in range(h)]
stack = []
for x in range(w):
    for y in (0, h - 1):
        if not op[y][x] and not ext[y][x]:
            ext[y][x] = True
            stack.append((x, y))
for y in range(h):
    for x in (0, w - 1):
        if not op[y][x] and not ext[y][x]:
            ext[y][x] = True
            stack.append((x, y))
while stack:
    x, y = stack.pop()
    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if 0 <= nx < w and 0 <= ny < h and not op[ny][nx] and not ext[ny][nx]:
            ext[ny][nx] = True
            stack.append((nx, ny))
holes = 0
for y in range(h):
    for x in range(w):
        if not op[y][x] and not ext[y][x]:
            fig.set(x, y, C("outline"))
            holes += 1
print("interior holes plugged:", holes)
op = [[not ext[y][x] for x in range(w)] for y in range(h)]
ring = []
for y in range(h):
    for x in range(w):
        if op[y][x]:
            continue
        if ((x > 0 and op[y][x - 1]) or (x < w - 1 and op[y][x + 1])
                or (y > 0 and op[y - 1][x]) or (y < h - 1 and op[y + 1][x])):
            ring.append((x, y))
for (x, y) in ring:
    fig.set(x, y, C("outline"))

art.blit(fig, 0, 0)
save("east_hero", art)

# ---------------------------------------------------------------- look
CHAR = {
    "sky_top": ".", "sky_mid": ".", "sky_low": ".", "mist": " ", "ground": ".",
    "ground_d": ",",
    "mtn_far": "-", "mtn_mid": "~", "mtn_near": "~",
    "robe_deep": "#", "robe_dark": "#", "robe_mid": "=", "robe_light": "+",
    "robe_hi": "+", "trim": "T",
    "hair": "@", "hair_hi": "@",
    "skin": "o", "skin_sh": "o", "skin_dk": "O", "skin_hi": "o",
    "hat_l": "h", "hat_m": "h", "hat_d": "H", "hat_dd": "H",
    "sash": "s", "sash_d": "s", "sash_l": "s",
    "metal": "M", "metal_d": "M", "gold": "g", "gold_d": "g",
    "outline": "X",
}
idx_char = {col[k]: v for k, v in CHAR.items()}


def amap(canvas, step=2, x0=0, y0=0, x1=255, y1=255):
    out = []
    for y in range(y0, y1 + 1, step):
        row = []
        for x in range(x0, x1 + 1, step):
            best = None
            for dy in range(step):
                for dx in range(step):
                    ch = idx_char.get(canvas.get(x + dx, y + dy), "?")
                    if best is None or (ch not in " .-~," and best in " .-~,"):
                        best = ch
            row.append(best)
        out.append("".join(row))
    return "\n".join(out)


print(art.stats_text())
print("=== HEAD 1:1 (x84-172, y36-106) ===")
print(amap(art, 1, 84, 36, 172, 106))
print("=== FULL step2 ===")
print(amap(art, 2))
finish(art)
