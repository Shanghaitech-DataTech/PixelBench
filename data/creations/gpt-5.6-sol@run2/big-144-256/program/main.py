out = input_canvas.copy(name='output')

# New colours, tuned to the cool, low-contrast palette of the source.
vine_shadow = out.color('#163b2d', 'vine_shadow')
vine_mid = out.color('#245d3c', 'vine_mid')
vine_light = out.color('#3a7650', 'vine_light')
vine_tip = out.color('#579066', 'vine_tip')
cloak_edge = out.color('#171b2b', 'cloak_edge')
cloak_dark = out.color('#22233b', 'cloak_dark')
cloak_mid = out.color('#34345b', 'cloak_mid')
cloak_light = out.color('#4a4b76', 'cloak_light')
cloak_glint = out.color('#66678d', 'cloak_glint')
staff_dark = out.color('#382d2b', 'staff_dark')
staff_mid = out.color('#75533b', 'staff_mid')
glow_deep = out.color('#2b7d78', 'glow_deep')
glow_mid = out.color('#58c8b4', 'glow_mid')
glow_bright = out.color('#b3f2ca', 'glow_bright')
glow_core = out.color('#efffd4', 'glow_core')

# Vines climbing from the low vegetation up the tower's left face.
# Main old stem is irregular and occasionally disappears behind stone details.
out.path('M35 221 C34 204 39 193 36 177 C33 161 39 149 36 134 C34 122 39 111 37 99', vine_shadow, fill=False)
out.path('M36 220 C36 202 41 192 38 177 C35 161 40 149 38 135 C36 121 40 111 38 100', vine_mid, fill=False)
# Forks across masonry.
out.path('M38 185 C44 179 46 171 47 162 C48 153 54 148 57 142', vine_mid, fill=False)
out.path('M37 166 C31 158 29 151 31 143 C33 136 29 129 27 124', vine_shadow, fill=False)
out.path('M39 145 C45 139 47 131 45 124 C43 117 47 110 50 105', vine_mid, fill=False)
out.path('M38 125 C33 119 32 112 34 106', vine_light, fill=False)
out.path('M41 199 C47 194 51 189 51 181', vine_light, fill=False)

# Clusters of angular leaves, with sparse highlights facing the open sky.
leaves = [
 (35,211,-1),(38,203,1),(34,195,-1),(40,188,1),(35,180,-1),(39,172,1),
 (34,163,-1),(31,155,-1),(31,145,1),(28,136,-1),(27,126,1),
 (42,180,1),(46,173,-1),(47,164,1),(50,155,-1),(54,148,1),(57,142,-1),
 (40,143,1),(44,136,-1),(46,128,1),(44,120,-1),(47,112,1),(50,105,-1),
 (37,122,-1),(34,114,1),(35,106,-1),(45,194,1),(50,186,-1),(51,180,1)
]
for i,(x,y,d) in enumerate(leaves):
    col = vine_light if i % 4 else vine_tip
    if d < 0:
        out.poly([(x,y),(x-5,y-3),(x-6,y),(x-2,y+3)], col)
        out.set(x-3,y-1,vine_tip)
    else:
        out.poly([(x,y),(x+5,y-4),(x+6,y-1),(x+2,y+3)], col)
        out.set(x+3,y-2,vine_tip)

# A second, thinner curtain crossing the upper central stones.
out.path('M67 163 C63 152 67 143 64 133 C61 123 65 114 63 104', vine_shadow, fill=False)
out.path('M67 161 C65 151 68 143 66 133 C63 123 67 114 65 104', vine_mid, fill=False)
out.path('M66 139 C72 134 74 128 74 120', vine_mid, fill=False)
out.path('M65 122 C59 118 57 113 58 107', vine_light, fill=False)
for x,y,d in [(66,154,-1),(67,146,1),(65,136,-1),(71,132,1),(74,122,-1),(64,122,1),(59,116,-1),(58,108,1),(65,106,-1)]:
    if d < 0: out.poly([(x,y),(x-4,y-3),(x-5,y),(x-1,y+2)], vine_light)
    else: out.poly([(x,y),(x+4,y-3),(x+5,y),(x+1,y+2)], vine_light)

# Mage entering the archway: staff and its glow sit behind the near arm.
# Subtle square-edged halo so it remains pixel-art rather than a soft effect.
out.circle(72,187,6,'#388e8380')
out.circle(72,187,4,glow_deep)
out.set(68,184,glow_mid); out.set(76,185,glow_mid); out.set(75,190,glow_mid)
out.line(72,190,70,221,staff_dark)
out.line(73,190,71,221,staff_mid)
out.set(70,220,staff_dark); out.set(71,220,staff_mid)
# Crooked crown around the crystal.
out.line(72,190,68,186,staff_mid); out.line(72,190,76,186,staff_mid)
out.line(68,186,69,182,staff_mid); out.line(76,186,75,182,staff_dark)
out.circle(72,184,3,glow_mid)
out.poly([(72,179),(75,184),(72,189),(69,184)], glow_bright)
out.set(72,181,glow_core); out.set(71,183,glow_core); out.set(72,184,glow_core)

# Boots visible beneath the trailing cloak, one leg advanced into the doorway.
out.rect(50,216,5,7,cloak_edge)
out.rect(61,214,5,8,cloak_edge)
out.rect(49,221,7,2,'#111a22')
out.rect(61,220,7,2,'#111a22')
# Back-facing cloak silhouette and asymmetric walking hem.
out.poly([(57,187),(49,190),(45,200),(46,216),(50,219),(55,217),(59,220),(64,216),(69,219),(68,202),(65,191)], cloak_edge)
out.poly([(57,188),(50,192),(48,201),(49,214),(54,216),(58,214),(62,218),(66,214),(65,201),(63,192)], cloak_dark)
out.poly([(57,190),(53,194),(52,204),(54,214),(58,212),(60,216),(62,211),(62,198)], cloak_mid)
# Cape folds converge under the shoulders and widen toward the hem.
out.line(53,195,52,211,cloak_light)
out.line(61,194,63,211,cloak_light)
out.line(57,196,58,213,cloak_glint)
out.set(51,207,cloak_glint); out.set(63,204,cloak_glint)
out.line(48,202,46,211,cloak_edge)
out.line(66,201,68,211,cloak_edge)
# Raised right arm grips the staff while moving forward.
out.poly([(63,193),(67,195),(71,192),(73,194),(68,200),(64,199)], cloak_edge)
out.poly([(64,194),(67,196),(71,193),(72,195),(68,198),(65,197)], cloak_mid)
out.rect(70,192,3,3,'#7b695f')
# Hood from behind: pointed crown, dark inner rim, and lit shoulder edges.
out.poly([(57,178),(51,183),(49,190),(53,195),(62,195),(66,190),(63,183)], cloak_edge)
out.poly([(57,180),(52,184),(51,189),(54,193),(61,193),(64,189),(62,184)], cloak_mid)
out.poly([(57,180),(54,185),(54,190),(57,192),(60,190),(61,184)], cloak_dark)
out.line(52,188,54,193,cloak_light)
out.line(62,185,63,191,cloak_light)
out.set(56,181,cloak_glint); out.set(55,193,cloak_glint); out.set(61,193,cloak_glint)
# A few foreground grass pixels overlap the cloak hem, grounding the figure.
out.line(47,223,48,217,vine_shadow)
out.line(67,223,66,217,vine_mid)
out.line(58,223,57,219,vine_shadow)

view(out, scale=3, margin=0)
finish(out)
