"""Wuxia swordsman figure, drawn on its own transparent layer."""
from pixelbench_api import new_canvas

OUT    = "#11131a"
ROBE   = "#2b3348"
ROBE_S = "#1d2332"
ROBE_SS= "#141926"
ROBE_H = "#3d4963"
ROBE_L = "#515f80"
TRIM   = "#9aa6c4"
SASH   = "#8e3034"
SASH_S = "#5d1d22"
SASH_H = "#b6494c"
HAT    = "#c9a96b"
HAT_H  = "#e6cd92"
HAT_S  = "#9c7d45"
HAT_D  = "#6d5530"
SKIN   = "#d8a87e"
SKIN_S = "#b2805c"
SKIN_D = "#8a5c40"
SKIN_X = "#5e3b2b"
HAIR   = "#191922"
HAIR_H = "#303142"
BLADE  = "#c6d0da"
BLADE_H= "#eef4f8"
BLADE_S= "#8a95a3"
HILT   = "#272c38"
HILT_H = "#3b4252"
GOLD   = "#c9a24a"
GOLD_H = "#ebcd7c"
WHITE  = "#e9eef4"


def build(W=256, H=256):
    f = new_canvas(W, H, name="fig")

    # ============================================================ robe
    body = ("M 96 96 C 104 90 132 90 140 96 "
            "C 146 106 149 120 151 134 "
            "C 155 170 158 206 166 240 "
            "L 72 240 "
            "C 80 206 84 170 88 134 "
            "C 90 120 90 106 96 96 Z")
    f.path(body, ROBE)

    # wind-blown hem, viewer's left
    f.path("M 84 194 C 70 206 58 224 52 242 C 64 243 76 240 84 235 "
           "C 80 222 81 206 84 194 Z", ROBE)
    f.path("M 84 198 C 74 208 64 224 58 240 C 66 240 74 237 80 233 "
           "C 78 222 80 208 84 198 Z", ROBE_H)
    # trailing hem, viewer's right
    f.path("M 158 200 C 170 212 180 228 184 242 C 174 243 166 240 160 236 "
           "C 160 224 159 210 158 200 Z", ROBE_S)

    # ------------------------------------------------------------ shading
    # right third in shadow (light from the upper left)
    f.path("M 130 92 C 136 92 140 96 140 96 C 146 106 149 120 151 134 "
           "C 155 170 158 206 166 240 L 136 240 C 136 190 134 130 130 92 Z", ROBE_S)
    # lit left edge
    f.path("M 96 96 C 100 92 106 90 110 90 C 104 124 100 180 99 240 "
           "L 88 240 C 84 206 84 170 88 134 C 90 120 90 106 96 96 Z", ROBE_H)
    f.path("M 97 100 C 100 96 104 94 107 94 C 102 128 98 182 97 236 "
           "L 91 236 C 89 200 89 164 92 134 C 93 120 93 108 97 100 Z", ROBE_L)

    # fold lines
    for (x0, y0, x1, y1, col) in (
            (114, 100, 110, 238, ROBE_SS),
            (104, 136, 100, 238, ROBE_SS),
            (128, 100, 131, 238, ROBE_SS),
            (142, 140, 148, 238, ROBE_SS),
            (122, 146, 120, 238, ROBE_S),
            (136, 150, 139, 236, ROBE_S),
            (108, 150, 105, 236, ROBE_H),
            (118, 160, 116, 236, ROBE_H)):
        f.line(x0, y0, x1, y1, col)
    # hem edge shadow
    f.path("M 72 240 L 166 240 L 166 236 C 140 232 100 232 72 236 Z", ROBE_SS)

    # ============================================================ sleeves
    # left (viewer) sleeve, wide and flowing
    f.path("M 98 96 C 88 106 80 126 76 148 C 74 160 86 166 95 157 "
           "C 97 134 101 112 107 98 Z", ROBE)
    f.path("M 99 98 C 91 108 84 126 80 146 C 78 156 86 160 92 154 "
           "C 93 132 97 112 103 99 Z", ROBE_H)
    f.line(88, 118, 82, 150, ROBE_SS)
    f.line(95, 110, 90, 152, ROBE_SS)
    # right sleeve, holds the sword
    f.path("M 136 94 C 148 100 156 114 160 130 C 162 139 152 143 146 137 "
           "C 143 118 138 102 131 97 Z", ROBE)
    f.path("M 142 98 C 150 106 156 118 159 130 C 160 137 154 140 150 136 "
           "C 148 120 145 106 140 99 Z", ROBE_S)
    f.line(148, 108, 153, 134, ROBE_SS)

    # ============================================================ sash
    f.rect(88, 130, 64, 14, SASH)
    f.line(88, 130, 151, 130, SASH_H)
    f.line(88, 143, 151, 143, SASH_S)
    f.rect(134, 130, 18, 14, SASH_S)
    f.rect(112, 132, 16, 10, SASH_S)
    f.rect(114, 134, 12, 6, GOLD)
    f.rect(115, 135, 4, 2, GOLD_H)
    # knot tails: two narrow ribbons streaming left
    f.path("M 92 143 C 86 156 78 168 68 178 C 70 180 74 179 77 176 "
           "C 85 167 91 155 96 144 Z", SASH)
    f.path("M 93 144 C 88 155 82 165 74 174 C 75 175 77 174 79 172 "
           "C 86 163 91 154 95 145 Z", SASH_H)
    f.path("M 68 178 L 72 175 L 71 182 L 67 183 Z", SASH_S)
    f.path("M 100 143 C 97 157 92 170 85 182 C 88 183 91 180 93 175 "
           "C 97 164 100 152 102 144 Z", SASH_S)
    f.path("M 101 145 C 99 156 96 166 92 175 C 93 174 95 171 96 167 "
           "C 99 158 101 150 102 145 Z", SASH)
    f.path("M 85 182 L 89 181 L 87 188 L 83 187 Z", SASH_S)

    # ============================================================ neck
    f.rect(111, 88, 14, 10, SKIN_S)
    f.rect(111, 88, 14, 4, SKIN_X)
    f.rect(121, 88, 4, 10, SKIN_D)

    # collar, crossed over (narrower, more hanfu-like)
    f.path("M 118 92 L 132 100 L 128 112 L 118 104 Z", TRIM)
    f.path("M 118 92 L 105 100 L 109 113 L 118 104 Z", WHITE)
    f.path("M 118 94 L 108 101 L 111 109 L 118 103 Z", TRIM)
    f.path("M 118 104 C 122 112 123 122 121 132 L 113 132 C 113 118 115 111 118 104 Z",
           ROBE_S)
    f.line(118, 92, 118, 104, ROBE_SS)

    # ============================================================ loose hair
    # mass behind the head and shoulders
    f.path("M 102 58 C 92 76 88 100 92 128 C 96 110 98 84 106 64 Z", HAIR)
    f.path("M 132 56 C 142 78 148 104 142 128 C 138 106 134 82 128 62 Z", HAIR)
    # strands blown out to the left
    f.path("M 98 62 C 84 76 76 94 72 112 C 78 96 88 80 100 68 Z", HAIR)
    f.path("M 100 66 C 88 82 82 100 80 118 C 84 100 90 84 102 72 Z", HAIR_H)
    # strands on the right
    f.path("M 134 60 C 146 74 152 92 154 110 C 150 94 144 78 132 66 Z", HAIR)
    f.line(94, 80, 91, 112, HAIR_H)
    f.line(139, 82, 142, 114, HAIR_H)
    f.line(148, 92, 152, 108, HAIR_H)

    # ============================================================ face
    # head, three-quarter: cheek line on the left, jaw tapering right
    f.path("M 104 56 L 131 56 C 131 74 129 84 125 90 C 121 94 114 94 110 89 "
           "C 106 83 104 70 104 56 Z", SKIN)
    # shadow side (viewer's right)
    f.path("M 123 56 C 124 76 123 86 119 92 C 123 93 123 92 125 90 "
           "C 129 84 131 74 131 56 Z", SKIN_S)
    # brim shadow covers the eyes; cast-shadow line just under the brim
    f.rect(104, 56, 27, 18, SKIN_X)
    f.path("M 104 73 L 131 73 L 131 77 C 120 79 112 79 104 77 Z", SKIN_D)
    # nose
    f.line(114, 78, 114, 81, SKIN_D)
    f.set(113, 82, SKIN_D)
    f.set(115, 82, SKIN_S)
    # mouth
    f.line(115, 86, 120, 86, SKIN_D)
    f.set(114, 85, SKIN_D)
    # cheek / jaw shading
    f.line(108, 80, 109, 85, SKIN_S)
    f.line(126, 79, 127, 84, SKIN_D)
    f.line(113, 90, 120, 90, SKIN_S)

    # ============================================================ hat (douli)
    # tilted down toward the viewer: apex high and back, front rim low
    # back half of the brim
    f.path("M 60 50 C 60 38 88 28 116 28 C 146 28 172 36 172 44 "
           "C 172 54 144 62 114 62 C 84 62 60 58 60 50 Z", HAT_S)
    # cone, apex pushed up-left for the three-quarter tilt
    f.path("M 110 16 C 94 28 74 42 60 50 L 172 44 C 150 34 126 26 110 16 Z", HAT)
    f.path("M 110 16 C 116 28 120 38 122 47 L 172 44 C 150 34 126 26 110 16 Z", HAT_S)
    f.path("M 110 16 C 101 28 93 38 87 48 L 60 50 C 74 42 94 28 110 16 Z", HAT_H)
    # front brim sweeping down over the brow
    f.path("M 60 50 C 74 64 94 70 115 70 C 142 70 164 57 172 44 Z", HAT)
    f.path("M 60 50 C 72 61 88 67 104 69 C 97 61 91 54 87 48 Z", HAT_H)
    f.path("M 172 44 C 164 56 148 65 131 68 C 130 60 127 52 124 47 Z", HAT_S)
    # rim edge band
    f.path("M 60 50 C 74 64 94 70 115 70 C 142 70 164 57 172 44 "
           "C 173 47 173 49 172 51 C 161 65 142 74 115 74 C 93 74 72 66 59 53 "
           "C 58 52 58 51 60 50 Z", HAT_D)
    # weave: radial ribs
    for tx, ty in ((61, 51), (70, 60), (84, 67), (100, 70), (116, 71),
                   (132, 69), (148, 63), (163, 53), (171, 45)):
        f.line(110, 18, tx, ty, HAT_D)
    # weave: rings
    f.path("M 88 34 C 98 42 102 48 104 57", HAT_D, fill=False)
    f.path("M 132 34 C 127 42 124 49 124 57", HAT_D, fill=False)
    f.path("M 68 46 C 84 58 143 58 167 43", HAT_D, fill=False)
    f.set(110, 16, HAT_D)
    f.set(110, 17, HAT_D)
    # chin cord
    f.line(103, 72, 108, 92, HAT_D)
    f.line(129, 69, 127, 92, HAT_D)
    f.path("M 108 92 C 114 96 122 96 127 92", HAT_D, fill=False)

    # ============================================================ jian
    # blade, tip planted in the ground
    f.path("M 157 162 L 164 162 L 173 238 L 167 238 Z", BLADE)
    f.path("M 158 162 L 160 162 L 168 238 L 167 238 Z", BLADE_H)
    f.path("M 162 162 L 164 162 L 173 238 L 171 238 Z", BLADE_S)
    f.path("M 167 238 L 173 238 L 171 244 Z", BLADE_S)
    # guard (ricasso above it stays visible)
    f.path("M 147 155 L 175 155 L 171 162 L 152 162 Z", GOLD)
    f.line(147, 155, 175, 155, GOLD_H)
    f.line(152, 162, 171, 162, HILT)
    f.line(148, 156, 174, 156, HILT)
    # grip: visible above and below the fist
    f.rect(155, 128, 11, 27, HILT)
    f.rect(155, 128, 3, 27, HILT_H)
    for gy in range(130, 155, 4):
        f.line(155, gy, 165, gy, HILT_H)
    # pommel
    f.rect(152, 122, 16, 7, GOLD)
    f.rect(154, 124, 11, 3, GOLD_H)
    f.line(152, 128, 167, 128, HAT_D)
    # tassel hanging off the pommel
    f.path("M 160 129 C 167 139 171 152 168 166 C 174 152 171 137 164 127 Z", SASH)
    f.path("M 161 131 C 166 140 169 151 167 162 C 170 151 168 140 162 130 Z", SASH_H)
    f.path("M 167 166 L 170 164 L 170 171 L 166 172 Z", SASH_S)

    # ============================================================ hands
    # right hand wrapping the middle of the grip
    f.path("M 151 134 C 148 140 149 148 155 150 C 162 151 167 146 167 140 "
           "C 166 133 157 130 151 134 Z", SKIN)
    f.path("M 152 136 C 150 142 152 148 156 149 C 158 143 158 138 156 134 Z", SKIN_S)
    for ky in (139, 143, 147):
        f.line(158, ky, 166, ky, SKIN_D)
    f.line(153, 133, 165, 133, SKIN_S)
    # thumb over the front of the grip
    f.path("M 151 138 C 154 141 156 145 155 149 L 152 148 C 150 144 150 140 151 138 Z",
           SKIN_S)
    # left hand slipping from the sleeve
    f.path("M 82 152 C 78 159 81 166 88 166 C 94 165 96 158 93 152 Z", SKIN)
    f.path("M 82 154 C 80 160 83 165 88 165 C 87 160 84 156 85 153 Z", SKIN_S)
    f.line(86, 158, 92, 158, SKIN_D)
    f.line(86, 162, 91, 162, SKIN_D)

    # ============================================================ boots
    f.path("M 106 228 L 120 228 L 122 240 L 102 240 Z", ROBE_SS)
    f.path("M 128 230 L 140 230 L 144 240 L 128 240 Z", ROBE_S)
    f.line(102, 240, 122, 240, OUT)

    # ============================================================ rim light
    # cool rim along the lit left silhouette
    for (x0, y0, x1, y1) in ((96, 100, 90, 134), (90, 134, 86, 172),
                             (86, 176, 84, 196), (85, 200, 59, 238)):
        f.line(x0, y0, x1, y1, ROBE_L)
    f.line(99, 96, 96, 100, ROBE_L)

    return f
