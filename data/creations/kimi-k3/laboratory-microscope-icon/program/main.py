from pixelbench_api import *  # noqa

# ---- 32x32 laboratory microscope icon, three-quarter view -----------------
c = new_canvas(32, 32, background=None, name="microscope")

DK   = "#23262f"   # dark outline
BODY = "#dbe2ea"   # body highlight
MID  = "#9aa6b4"   # body mid tone
SDE  = "#707b89"   # side faces (three-quarter depth)
BST  = "#5d6672"   # base top
BSF  = "#454d58"   # base front
STG  = "#39424c"   # stage plate
SIL  = "#e9edf3"   # slide
GLS  = "#8fd6e8"   # glass / lens glint
LEN  = "#33658f"   # objective lens front
ILM  = "#ffd66b"   # illuminator light

# ---- base: front face, then tilted top face -------------------------------
c.rect(3,26,17,4, BSF)
c.poly([(3,26),(11,23),(27,23),(20,26)], BST)

# ---- pillar rising from back-right of base ---------------------------------
c.rect(24,13,3,10, MID)
c.rect(26,13,1,10, SDE)

# ---- arm: curved back connecting pillar to the head ------------------------
c.path("M26,19 C26,11 21,6 13,6 L13,11 C18,11 22,13 23,19 Z", SDE)

# ---- focus knob on the pillar side -----------------------------------------
c.rect(22,15,2,3, MID)

# ---- eyepiece + body tube ---------------------------------------------------
c.rect(7,1,6,3, DK)                                # eyepiece cap
c.set(8,2, MID)
c.rect(8,4,4,8, BODY)                              # tube front face
c.rect(12,4,2,8, SDE)                              # tube side face
c.set(9,5, "#ffffff")                              # glint
c.rect(9,12,5,3, MID)                              # prism head block
c.rect(14,12,2,3, SDE)                             # head side face

# ---- nosepiece + objectives -------------------------------------------------
c.rect(10,15,5,2, DK)                              # revolving nosepiece
c.set(14,16, MID)                                  # nosepiece screw glint
c.rect(10,17,3,3, LEN)                             # main objective (3-wide keeps a core pixel)
c.set(11,19, GLS)                                  # lens glass glint
c.rect(14,17,2,2, LEN)                             # second objective (stowed)

# ---- stage ------------------------------------------------------------------
c.poly([(5,20),(20,20),(23,22),(8,22)], STG)       # plate
c.rect(9,20,6,1, SIL)                              # slide
c.set(12,21, GLS)                                  # specimen glass

# ---- illuminator on the base top, under the stage ---------------------------
c.rect(13,24,3,2, BST)                             # illuminator housing
c.set(14,24, ILM)

# ---- outlines ----------------------------------------------------------------
c.outline(DK)
c.set(9,5, "#ffffff")                              # glass glint kept over outline

view(c, scale=12)
print(c.stats_text())
finish(c)
