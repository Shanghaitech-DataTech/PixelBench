from pixelbench_api import *

W = H = 256
c = new_canvas(W, H, background="#c8d2cc", name="east-hero-full-body")

# Compact hand-tuned palette.
sky0 = "#c8d2cc"; sky1 = "#aebfba"; mist = "#d9dfd8"
far = "#8fa5a1"; mid = "#6f8886"; near = "#526b6b"; ink = "#172326"
ink2 = "#243438"; robe = "#29383d"; robe2 = "#34484d"; robe3 = "#465c60"
edge = "#10191c"; blue = "#557078"; pale = "#9caeaa"; skin = "#a98267"
red = "#733b3b"; red2 = "#9a5550"; straw = "#8b7450"; straw2 = "#b29a68"
steel = "#b8c5c2"; shine = "#e1e6df"; ground = "#3d5554"

# Sky texture and distant peaks.
c.rect(0, 0, 256, 256, sky0)
c.dither(0, 0, 256, 96, [sky0, sky1], pattern="bayer4")
c.poly([(0,91),(24,69),(38,80),(63,48),(79,69),(100,43),(127,80),(151,61),(174,86),(198,56),(222,78),(256,53),(256,130),(0,130)], far)
c.poly([(0,111),(31,87),(49,101),(76,73),(99,101),(127,72),(149,100),(175,79),(196,106),(227,82),(256,96),(256,150),(0,150)], mid)
# Snow/mist cuts across mountain faces.
c.poly([(0,104),(28,82),(41,90),(62,62),(73,83),(99,56),(118,86),(99,76),(77,91),(63,78),(48,105),(31,95),(0,121)], sky1)
c.poly([(113,92),(127,78),(141,96),(153,88),(174,99),(195,71),(211,92),(226,87),(256,105),(256,118),(220,105),(199,91),(177,111),(151,101),(137,108)], sky1)
# Atmospheric mist bands.
c.poly([(0,117),(36,109),(68,116),(103,108),(138,116),(175,106),(209,116),(256,105),(256,131),(219,126),(181,133),(139,125),(91,135),(46,125),(0,134)], mist)
c.poly([(0,145),(50,135),(91,144),(135,134),(177,143),(219,132),(256,138),(256,161),(210,154),(166,163),(119,151),(70,159),(22,151),(0,155)], sky1)
# Foreground ground and reeds.
c.poly([(0,215),(37,205),(68,211),(105,202),(139,213),(180,203),(216,211),(256,199),(256,256),(0,256)], ground)
c.dither(0, 220, 256, 36, [ground, near], pattern="checker")
for pts in [[(18,226),(21,180),(23,226)],[(31,227),(38,190),(35,228)],[(228,222),(234,176),(234,223)],[(242,223),(247,190),(246,224)],[(8,229),(5,201),(10,229)]]:
    c.poly(pts, near)
# Sparse bamboo silhouettes frame without competing with character.
c.line(16,58,25,207,near); c.line(20,106,3,91,near); c.line(21,129,42,107,near)
c.line(232,48,226,201,near); c.line(230,88,249,70,near); c.line(228,117,209,96,near)
for x,y,flip in [(8,91,0),(28,107,1),(42,108,0),(239,70,0),(211,96,1),(225,119,0)]:
    if flip: c.poly([(x,y),(x-16,y-6),(x-4,y+3)], near)
    else: c.poly([(x,y),(x+16,y-7),(x+5,y+4)], near)

# Flowing loose hair behind shoulders.
c.path("M103 76 C91 92 88 119 80 143 C89 140 92 130 96 119 C91 147 83 164 88 178 C100 160 106 132 110 97 Z", edge)
c.path("M139 75 C151 93 158 120 166 143 C157 139 151 129 147 118 C153 145 163 159 159 174 C146 156 139 129 133 96 Z", edge)
c.path("M99 84 C92 111 91 134 86 155", robe3, fill=False)
c.path("M144 84 C150 108 153 128 160 149", robe3, fill=False)

# Back leg and boots, wide heroic stance.
c.poly([(105,185),(125,187),(120,226),(108,244),(80,244),(82,237),(101,222)], edge)
c.poly([(130,185),(148,181),(153,221),(174,239),(171,246),(145,244),(132,225)], edge)
c.poly([(84,235),(108,235),(106,247),(77,247),(76,242)], ink)
c.poly([(147,235),(174,238),(178,246),(148,247)], ink)
c.rect(82,242,25,3, robe3); c.rect(150,242,24,3, robe3)

# Main robe silhouette: broad shoulder, tapered waist, wind-swept hem.
c.path("M101 83 C94 91 84 99 74 115 L87 132 L91 160 L78 205 C91 209 104 203 115 210 L128 205 C140 212 155 208 169 199 L153 159 L158 127 L171 115 C162 103 151 91 141 84 L127 79 Z", edge)
c.path("M104 88 C96 96 90 104 83 116 L94 127 L96 158 L85 199 C96 201 107 196 117 203 L127 197 L139 204 C147 203 155 199 162 194 L147 158 L152 126 L163 115 C155 102 145 94 138 88 L124 85 Z", robe)
# Lit robe planes and long folds.
c.poly([(104,91),(119,87),(114,148),(101,186),(96,199),(88,198),(99,157),(96,121)], robe2)
c.poly([(128,87),(139,91),(146,122),(140,158),(158,194),(145,201),(131,163)], ink2)
c.poly([(117,91),(127,86),(129,198),(119,203),(113,164)], robe3)
c.poly([(98,129),(112,137),(105,188),(94,200)], blue)
c.poly([(137,128),(149,124),(144,159),(158,194),(149,198)], robe2)
# Pixel stair-step fold highlights.
c.line(108,101,105,151,pale); c.line(105,151,96,190,pale)
c.line(132,102,136,158,blue); c.line(136,158,148,190,blue)
c.line(119,111,118,189,ink); c.line(144,106,146,145,edge)

# Wind-blown left sleeve.
c.path("M92 103 C77 105 61 113 48 126 L59 138 C72 132 83 124 98 121 Z", edge)
c.path("M91 108 C78 111 66 117 54 127 L60 133 C74 128 84 119 97 117 Z", robe2)
c.poly([(52,126),(60,119),(67,128),(59,138)], robe3)
c.line(65,124,88,113,pale)
# Right sleeve and arm descending toward sword grip.
c.path("M145 101 C158 102 169 113 178 126 L172 146 L160 144 L163 128 L150 120 Z", edge)
c.path("M148 107 C157 109 166 117 172 128 L168 140 L162 139 L165 127 L151 116 Z", robe2)
c.line(153,111,166,124,pale)

# Belt and sash.
c.poly([(93,145),(150,143),(153,153),(96,157)], edge)
c.poly([(97,147),(149,146),(149,151),(96,154)], red)
c.rect(117,145,13,10, straw)
c.rect(120,147,7,6, straw2)
c.path("M143 151 C155 164 161 179 177 187 L170 194 C153 181 146 169 136 157 Z", red)
c.line(144,157,170,189,red2)

# Neck, shadowed lower face and collar. Hat hides eyes entirely.
c.poly([(108,70),(138,70),(140,94),(126,104),(105,92)], edge)
c.poly([(111,73),(136,73),(136,89),(126,97),(108,87)], skin)
c.poly([(106,86),(124,102),(101,105),(94,94)], ink)
c.poly([(137,85),(124,102),(146,103),(151,94)], ink2)
c.poly([(111,84),(125,98),(135,85),(133,93),(125,101),(113,92)], robe3)
# Nose/chin hint below brim.
c.rect(119,78,16,3, "#795d4f"); c.set(132,81,skin)

# Douli crown and extra-wide tilted brim, strong dark outline.
c.path("M75 68 L110 34 C119 27 130 28 140 37 L173 64 L171 70 C142 80 105 82 72 75 Z", edge)
c.path("M82 66 L112 38 C120 31 129 32 137 40 L164 62 C138 69 108 73 82 70 Z", straw)
c.poly([(112,38),(124,31),(137,40),(145,59),(124,66)], straw2)
c.line(94,61,153,57,"#d0b87d"); c.line(103,50,145,48,"#d0b87d")
# Brim face plane and woven bands.
c.path("M68 68 C94 62 141 59 180 63 L174 73 C146 83 102 85 65 76 Z", edge)
c.path("M75 69 C105 65 142 63 172 66 C145 74 108 78 73 73 Z", straw2)
c.line(82,70,158,67,"#d8c58d"); c.line(92,74,151,70,straw)
# Deep shadow beneath the tilted brim.
c.poly([(82,76),(166,69),(148,85),(100,88)], edge)
c.poly([(101,79),(151,74),(137,83),(111,85)], ink2)

# Hand resting on jian pommel.
c.poly([(161,136),(171,134),(178,142),(173,151),(163,148),(158,143)], edge)
c.poly([(164,138),(170,137),(175,142),(171,147),(164,145),(161,142)], skin)
# Jian hilt, guard, straight double-edged blade and point.
c.poly([(177,136),(184,135),(193,229),(189,239),(185,230)], edge)
c.poly([(180,141),(182,140),(190,228),(189,233),(188,228)], steel)
c.line(182,144,190,226,shine)
c.poly([(185,230),(193,229),(189,239)], edge)
c.poly([(188,230),(191,230),(189,235)], shine)
c.poly([(166,135),(183,132),(185,137),(167,141)], edge)
c.poly([(169,135),(181,134),(181,136),(169,139)], straw2)
c.rect(176,119,7,17, edge); c.rect(178,120,3,14, red2)
c.circle(179,117,4,edge); c.circle(179,117,2,straw)

# Foreground mist wisps crossing feet.
c.path("M0 213 C33 204 62 218 91 211 C120 204 149 214 177 208 C207 201 231 207 256 202", sky1, fill=False)
c.path("M0 224 C29 216 52 226 76 221 C99 216 116 222 138 219", pale, fill=False)
# Small grass pixel clusters around silhouette.
for x,y in [(52,232),(64,240),(190,237),(207,226),(218,242),(42,246)]:
    c.line(x,y,x-3,y-10,near); c.line(x,y,x+4,y-7,near)

# A few intentional glints and edge breaks for crisp pixel readability.
c.set(105,93,shine); c.set(104,94,pale); c.set(153,105,pale)
c.rect(89,199,7,2,pale); c.rect(147,199,6,2,blue)

view(c, scale=2, margin=0)
finish(c)
