from pixelbench_api import *

W = H = 256

# ---------- palette ----------
SKY_TOP = "#b9c9d6"
SKY_MID = "#cfdbe4"
SKY_LOW = "#e3ebf0"
MT_FAR  = "#9db0be"
MT_MID  = "#7b8fa0"
MT_NEAR = "#5d7182"
MIST    = "#eef4f7"
ROBE    = "#23242e"
ROBE_L  = "#343646"
ROBE_D  = "#16171e"
SASH    = "#8e2f2f"
SASH_D  = "#6a2020"
SKIN    = "#d9b48f"
SKIN_D  = "#b28e6c"
HAT     = "#c2a05e"
HAT_D   = "#8f7440"
HAIR    = "#17141a"
BLADE   = "#c3ccd4"
BLADE_D = "#8d98a2"
GUARD   = "#5a5f68"
OUT     = "#101014"
GROUND  = "#c6d2da"

bg = new_canvas(W, H, background=None, name="bg")

# sky gradient bands
for i, col in enumerate([SKY_TOP, "#c3d2dd", SKY_MID, "#d9e4ea", SKY_LOW]):
    bg.rect(0, i*22, W, 22, col)
bg.rect(0, 110, W, H-110, SKY_LOW)

# far mountains (jagged ridges)
bg.poly([(0,150),(30,118),(55,140),(80,105),(105,138),(128,112),(150,140),(178,108),(205,136),(230,115),(256,142),(256,256),(0,256)], MT_FAR)
# mist band over far mountains
bg.rect(0, 138, W, 14, MIST)
# mid mountains
bg.poly([(0,178),(40,150),(70,170),(100,142),(135,168),(165,146),(200,170),(232,150),(256,168),(256,256),(0,256)], MT_MID)
bg.rect(0, 172, W, 12, MIST)
# near ridge
bg.poly([(0,205),(45,182),(85,198),(120,180),(160,196),(200,182),(256,198),(256,256),(0,256)], MT_NEAR)
# ground / fog base
bg.rect(0, 214, W, H-214, GROUND)
bg.rect(0, 214, W, 6, MIST)
# drifting mist streaks
for y, x0, x1 in [(150, 10, 70), (158, 180, 250), (190, 20, 90), (196, 170, 240), (222, 0, 60), (228, 200, 256)]:
    bg.rect(x0, y, x1-x0, 3, MIST)

# ================= HERO =================
hero = new_canvas(W, H, background=None, name="hero")

def P(pts, col): hero.poly(pts, col)

# --- back hair (behind body) ---
P([(112,70),(120,66),(124,90),(122,120),(116,128),(112,100)], HAIR)
P([(150,72),(160,70),(166,100),(164,132),(156,126),(154,95)], HAIR)

# --- robe body ---
P([(116,96),(158,96),(168,116),(176,146),(186,182),(194,214),(88,214),(96,180),(104,146),(110,114)], ROBE)
# robe shading (right/dark side)
P([(150,96),(158,96),(168,116),(176,146),(186,182),(194,214),(178,214),(170,180),(160,146),(152,116)], ROBE_D)
# robe highlight folds (left, light catches)
P([(116,96),(124,96),(118,150),(108,214),(96,214),(104,178),(112,146)], ROBE_L)

# --- sleeves ---
# left arm reaching down-forward to sword hilt
P([(112,102),(126,100),(118,130),(106,152),(94,152),(98,128)], ROBE)
P([(94,152),(106,152),(104,162),(92,162)], ROBE)          # cuff
# right arm hanging, wide sleeve
P([(158,102),(170,108),(178,140),(184,168),(170,172),(162,140),(156,118)], ROBE)
P([(170,172),(184,168),(186,178),(170,182)], ROBE_D)      # cuff shadow

# --- sash / belt ---
P([(112,138),(164,138),(166,150),(110,150)], SASH)
P([(150,138),(164,138),(166,150),(152,150)], SASH_D)
# sash knot + trailing tail
P([(120,148),(130,148),(134,162),(140,178),(132,180),(126,162)], SASH)
P([(132,168),(140,178),(132,180)], SASH_D)

# --- neck & lower face ---
P([(128,84),(142,84),(142,96),(128,96)], SKIN)
P([(126,88),(131,88),(131,98),(126,98)], SKIN_D)   # jaw shadow side
# chin/mouth hint
hero.set(133, 91, SKIN_D); hero.set(134, 91, SKIN_D)

# --- wide conical hat (douli), tilted down over eyes ---
P([(136,40),(150,48),(164,58),(176,72),(96,78),(110,58),(124,46)], HAT)
# under-brim shadow
P([(96,78),(176,72),(176,78),(96,84)], HAT_D)
# hat ridge shading
P([(136,40),(150,48),(164,58),(176,72),(168,74),(150,52),(136,44)], HAT_D)
# ribs
hero.line(136,42,120,76,HAT_D); hero.line(136,42,150,74,HAT_D)
hero.line(136,42,100,78,HAT_D); hero.line(136,42,172,73,HAT_D)
# brim front edge line
hero.line(96,79,176,73,OUT)

# --- hair over shoulders / front strands ---
P([(114,72),(122,70),(120,100),(114,112),(110,96)], HAIR)
P([(150,74),(158,72),(162,104),(156,118),(150,102)], HAIR)
# loose strand blowing
P([(158,80),(168,88),(174,102),(170,104),(162,92),(156,84)], HAIR)

# --- sword (jian): tip on ground, hand resting on hilt ---
hero.rect(93,164,5,58,BLADE)                 # blade
hero.rect(93,164,2,58,BLADE_D)               # blade shade edge
hero.rect(92,220,7,8,BLADE_D)                # tip
hero.rect(88,158,15,5,GUARD)                 # guard
hero.rect(92,146,7,13,ROBE_D)                # grip
hero.set(95,144,GUARD)                       # pommel
hero.set(96,144,GUARD)
# hand on hilt
P([(90,148),(102,148),(104,158),(92,160),(88,156)], SKIN)
P([(88,156),(92,160),(90,164),(86,160)], SKIN_D)   # thumb/finger shade
hero.line(90,152,102,152,SKIN_D); hero.line(91,156,102,156,SKIN_D)

# --- feet / boots peeking under robe ---
P([(112,214),(128,214),(128,222),(110,222)], ROBE_D)
P([(158,214),(174,214),(176,222),(158,222)], ROBE_D)

# --- dark outline of whole figure ---
hero.outline(OUT)

print(bg.stats_text())
# ================= COMPOSE =================
result = flatten([bg, hero], name="result")

print(result.stats_text())
finish(result)




