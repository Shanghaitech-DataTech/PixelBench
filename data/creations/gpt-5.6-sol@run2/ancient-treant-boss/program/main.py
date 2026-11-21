import random

random.seed(17)

# Tight, deliberately earthy palette.
C = {
    "night": "#07120f", "deep": "#0b1b16", "forest": "#102a20",
    "pine": "#163a28", "leaf": "#205035", "leaf2": "#2f6640",
    "mist": "#53775a", "ray": "#78936a", "ray2": "#9aaa78",
    "outline": "#120f0b", "bark0": "#21170f", "bark1": "#352317",
    "bark2": "#4a3020", "bark3": "#65452a", "bark4": "#84603a",
    "bark5": "#a07949", "moss0": "#263d1c", "moss1": "#3e5d28",
    "moss2": "#63813a", "vine": "#6b8c43", "glow0": "#183f21",
    "glow1": "#3fae48", "glow2": "#91ef5d", "glow3": "#d5ff83",
    "earth": "#17150f", "soil": "#292117", "stone": "#3a3828",
}

result = new_canvas(256, 256, C["night"], name="ancient-treant-boss")

# Distant forest wall.
result.rect(0, 43, 256, 172, C["deep"])
for x, top, width in [(0,25,19),(13,10,22),(33,35,18),(48,17,24),(71,29,16),(86,5,25),
                      (108,21,20),(126,1,25),(147,28,18),(164,8,25),(188,31,18),
                      (204,12,24),(226,24,18),(242,4,18)]:
    result.poly([(x,215),(x+width,215),(x+width-3,top+22),(x+width//2,top),(x+3,top+25)], C["forest"])
    result.rect(x+width//2-2, top+18, 5, 197-top, C["forest"])

# Canopy masses and small gaps.
for cx,cy,rx,ry,col in [
    (12,23,25,18,"pine"),(42,18,28,17,"leaf"),(76,26,30,19,"pine"),
    (111,14,27,18,"leaf"),(146,20,34,22,"pine"),(184,13,31,20,"leaf"),
    (222,22,37,23,"pine"),(247,7,25,20,"leaf")]:
    result.ellipse(cx,cy,rx,ry,C[col])
for x,y in [(5,53),(24,43),(55,50),(91,41),(171,43),(212,49),(239,38)]:
    result.rect(x,y,9,3,C["leaf2"])

# God rays behind the boss, stepped hard-edged silhouettes.
result.poly([(57,38),(76,38),(132,211),(105,211)], C["ray"])
result.poly([(82,34),(94,34),(136,184),(120,184)], C["mist"])
result.poly([(191,34),(208,37),(157,211),(135,211)], C["ray"])
result.poly([(216,44),(226,49),(173,201),(159,201)], C["mist"])
# Break rays into pixel bands.
for y in range(58, 202, 12):
    result.rect(0,y,256,2,C["forest"])

# Clearing floor.
result.rect(0,202,256,54,C["earth"])
result.poly([(0,217),(38,207),(75,212),(111,205),(152,211),(197,203),(256,214),(256,256),(0,256)], C["soil"])
result.line(0,226,49,214,C["stone"]); result.line(205,211,255,223,C["stone"])
for x,y,w in [(6,236,19),(32,220,10),(65,239,16),(184,235,15),(215,223,23),(236,245,12)]:
    result.rect(x,y,w,2,C["bark2"])

# Treant outer silhouette: legs, torso, shoulders and head as one dark mass.
result.path("M66 226 L73 202 L79 185 L75 166 L68 151 L73 130 L84 116 L91 96 L92 70 L103 52 L117 44 L138 46 L153 57 L163 78 L161 102 L171 119 L186 128 L190 151 L181 166 L177 188 L185 207 L194 227 L174 229 L158 214 L147 199 L137 213 L129 235 L112 235 L103 216 L91 205 L82 229 Z", C["outline"])

# Left arm, raised and bent, with claw twigs.
result.path("M91 105 L77 111 L64 124 L46 121 L32 107 L21 91 L27 84 L40 98 L52 107 L62 105 L51 91 L38 78 L42 71 L58 85 L69 95 L77 84 L84 89 Z", C["outline"])
result.path("M31 92 L17 79 L8 65 L13 61 L25 74 L21 56 L27 54 L34 75 L39 58 L45 58 L42 79 Z", C["outline"])
# Right arm, reaching outward with hooked claws.
result.path("M158 105 L173 112 L184 126 L202 127 L218 116 L231 98 L238 103 L227 124 L211 140 L192 145 L177 139 L168 151 L155 139 Z", C["outline"])
result.path("M226 108 L234 89 L237 72 L243 71 L242 91 L250 77 L255 81 L246 99 L256 96 L256 104 L241 113 Z", C["outline"])

# Crown branches, all under the same dark outline.
result.path("M99 65 L91 48 L78 37 L65 32 L67 25 L82 29 L91 37 L87 21 L93 18 L101 37 L105 15 L112 8 L117 11 L112 28 L120 21 L124 25 L116 43 Z", C["outline"])
result.path("M139 52 L147 34 L145 16 L151 8 L156 11 L154 30 L165 18 L171 20 L162 34 L178 28 L182 34 L162 44 L156 61 Z", C["outline"])

# Inner wood masses, leaving a thick outline visible.
result.path("M84 222 L89 200 L88 180 L82 163 L84 140 L95 119 L101 98 L101 72 L109 58 L120 51 L136 53 L147 63 L154 81 L151 105 L160 124 L173 136 L177 153 L169 168 L166 190 L176 216 L162 211 L148 188 L139 192 L128 223 L115 225 L106 197 L96 193 L94 216 Z", C["bark2"])
result.path("M102 73 L112 57 L128 52 L143 62 L151 81 L147 106 L157 127 L147 137 L142 121 L132 112 L119 114 L106 124 L98 112 Z", C["bark3"])
# Arm inner wood.
result.path("M93 112 L79 119 L65 133 L48 130 L34 115 L25 98 L31 94 L45 110 L58 117 L70 113 L81 99 Z", C["bark2"])
result.path("M37 91 L25 79 L16 65 L23 78 L27 60 L33 80 L41 65 L36 86 Z", C["bark3"])
result.path("M157 113 L171 119 L184 136 L201 137 L216 126 L230 107 L222 128 L207 144 L189 151 L175 142 L165 157 L154 139 Z", C["bark2"])
result.path("M223 118 L233 101 L239 78 L237 99 L248 85 L240 105 L251 101 L237 115 Z", C["bark3"])
# Crown inner branches.
result.path("M103 66 L97 47 L83 35 L70 31 L85 36 L92 46 L92 25 L101 48 L109 19 L106 47 L119 28 L111 58 Z", C["bark2"])
result.path("M137 59 L149 34 L151 15 L152 39 L168 23 L157 42 L177 34 L157 49 L151 68 Z", C["bark2"])

# Split chest plates and ancient central hollow.
result.path("M96 123 L108 115 L117 120 L112 151 L102 173 L96 193 L88 180 L84 158 Z", C["bark3"])
result.path("M142 118 L152 128 L163 151 L158 181 L149 193 L140 158 L137 136 Z", C["bark3"])
result.path("M113 117 L126 109 L139 118 L141 151 L136 174 L127 187 L116 171 L111 148 Z", C["bark1"])
result.path("M119 126 L128 118 L136 127 L136 151 L128 170 L119 152 Z", C["bark0"])

# Knotted face: brow ridges and long wooden nose.
result.poly([(103,82),(117,75),(126,80),(118,89),(104,91)], C["bark1"])
result.poly([(128,80),(142,75),(150,84),(148,91),(133,89)], C["bark1"])
result.poly([(121,87),(129,82),(137,89),(133,104),(127,113),(120,102)], C["bark4"])
result.line(124,92,126,103,C["bark5"])
# Eye sockets and layered green glow.
result.poly([(104,84),(114,81),(121,85),(115,92),(105,91)], C["glow0"])
result.poly([(134,84),(143,81),(149,86),(143,92),(134,91)], C["glow0"])
result.rect(108,85,9,4,C["glow1"]); result.rect(137,85,9,4,C["glow1"])
result.rect(111,85,5,3,C["glow2"]); result.rect(137,85,5,3,C["glow2"])
result.set(113,85,C["glow3"]); result.set(139,85,C["glow3"])
# Grim mouth in the trunk.
result.path("M111 106 L119 110 L128 108 L137 111 L145 106 L141 117 L131 121 L120 119 L113 115 Z", C["outline"])
for x,h in [(116,5),(122,8),(130,7),(138,5)]: result.rect(x,109,2,h,C["bark4"])

# Bark grain: coherent vertical shards and cross-cuts.
grains = [
 (105,61,99,76,"bark4"),(114,57,111,72,"bark5"),(140,61,145,75,"bark4"),
 (96,96,91,116,"bark4"),(155,93,150,111,"bark5"),(105,132,100,157,"bark5"),
 (111,154,106,181,"bark4"),(151,139,157,162,"bark4"),(145,163,151,183,"bark5"),
 (99,180,105,196,"bark1"),(117,180,119,211,"bark4"),(134,181,130,216,"bark5"),
 (89,134,80,147,"bark4"),(75,120,61,126,"bark4"),(54,123,40,113,"bark4"),
 (171,127,184,141,"bark4"),(187,141,204,137,"bark4"),(207,134,219,122,"bark5")]
for x0,y0,x1,y1,col in grains:
    result.line(x0,y0,x1,y1,C[col])
    if abs(y1-y0)>12: result.set(x1+1,y1-3,C[col])
# Dark fissures.
for pts in [[(108,69),(104,78),(108,80)],[(145,94),(141,103),(146,109)],
            [(101,142),(96,151),(98,160)],[(153,158),(157,168),(153,178)],
            [(121,190),(116,202),(120,216)],[(138,187),(142,200),(137,214)]]:
    result.poly(pts,C["bark0"],fill=False)

# Knots and cut branch scars.
for cx,cy in [(91,155),(164,157),(104,187),(148,202)]:
    result.circle(cx,cy,5,C["bark1"]); result.circle(cx,cy,3,C["bark4"],fill=False); result.set(cx,cy,C["outline"])

# Moss cap, shoulder pads and hanging scraps.
result.path("M91 71 L98 59 L106 54 L114 57 L119 51 L129 54 L138 51 L147 58 L152 70 L145 67 L140 72 L130 68 L122 73 L112 68 L104 74 Z", C["moss1"])
result.path("M75 119 L84 109 L96 111 L101 120 L92 123 L86 132 L77 129 Z", C["moss0"])
result.path("M154 112 L166 116 L176 128 L170 136 L161 128 L151 127 Z", C["moss1"])
for x,y,w in [(101,59,8),(121,61,7),(137,58,6),(81,118,8),(159,120,9)]:
    result.rect(x,y,w,3,C["moss2"])
# Moss drips.
for x,y,l in [(96,67,12),(111,68,9),(145,65,13),(85,125,11),(168,132,10),(155,125,8)]:
    result.line(x,y,x-1,y+l,C["moss1"]); result.set(x,y+l,C["moss2"])

# Vines with leaves on arms and body.
result.path("M88 84 C75 93 83 111 67 121 C55 130 66 145 50 154", C["vine"], fill=False)
result.path("M158 72 C172 85 162 104 177 114 C189 123 179 145 193 158", C["vine"], fill=False)
result.path("M149 57 C162 71 151 91 160 107 C168 121 158 142 164 155", C["moss2"], fill=False)
for x,y,side in [(80,100,-1),(69,121,1),(59,139,-1),(168,91,1),(178,116,-1),(185,139,1),(157,83,-1),(164,127,1)]:
    result.poly([(x,y),(x+side*7,y-3),(x+side*5,y+4)],C["vine"])

# Roots surge from the earth around the feet.
result.path("M114 209 L103 218 L91 225 L70 229 L51 242 L76 238 L98 235 L117 226 Z", C["outline"])
result.path("M117 215 L103 224 L84 230 L64 239 L94 233 L116 225 Z", C["bark3"])
result.path("M137 210 L151 219 L171 224 L190 239 L212 244 L193 232 L176 218 L149 207 Z", C["outline"])
result.path("M141 215 L155 224 L174 229 L198 241 L174 224 L148 214 Z", C["bark3"])
result.path("M112 223 L103 236 L102 252 L111 241 L121 229 Z", C["outline"])
result.path("M139 223 L148 238 L151 253 L141 242 L132 228 Z", C["outline"])
# Root highlights and earth overlap.
result.line(74,236,101,228,C["bark5"]); result.line(158,224,188,236,C["bark5"])
for x,y in [(47,242),(57,238),(79,244),(91,232),(166,234),(186,241),(202,245),(218,239)]:
    result.rect(x,y,8,3,C["soil"])

# Foreground grass and tiny floating spores in the rays.
for x,h in [(4,9),(15,13),(28,7),(43,12),(57,8),(197,10),(214,14),(228,8),(245,13)]:
    result.line(x,252,x-2,252-h,C["leaf2"]); result.line(x+1,252,x+5,255-h,C["moss1"])
for x,y,col in [(48,70,"ray2"),(62,90,"mist"),(199,71,"ray2"),(211,105,"mist"),(53,174,"ray2"),(207,181,"ray2"),(31,156,"mist"),(222,151,"mist")]:
    result.rect(x,y,2,2,C[col])

# A few crisp outline accents restore silhouette readability.
result.line(73,202,66,226,C["outline"]); result.line(182,207,194,227,C["outline"])
result.line(92,70,91,96,C["outline"]); result.line(163,78,161,102,C["outline"])

view(result, scale=2, margin=0)
finish(result)
