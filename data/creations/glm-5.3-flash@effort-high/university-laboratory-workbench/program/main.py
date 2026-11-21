# 64x64 university laboratory workbench
c = new_canvas(64, 64, background="#cfd8de", name="lab")

# ---- palette ----
WALL="#cfd8de"; TRIM="#aebbc4"; FRAME="#eef3f6"; SKY="#8ecae6"; CLOUD="#ffffff"
WOOD="#b07a45"; WOOD_HI="#c68f58"; SHADOW="#9c6a3a"
FRONT="#7c4f28"; SEAM="#5c3a1e"; DRAWER="#6b4423"; KNOB="#3a2a18"
M_D="#2f343b"; M_M="#565e68"; M_L="#8a939e"
GLASS="#d8edf4"; GLASS_D="#a9cdd9"
GREEN="#43a047"; BLUE="#1e88e5"; PINK="#e91e63"; YELLOW="#fdd835"
RED="#c62828"; BULB_HI="#e57373"
PAPER="#f7f6f0"; LINE="#9aa5ad"; SPINE="#b9c2c9"; COVER="#3b5ba5"
CREAM="#f0e6c0"; CAPB="#6d4c2f"; ILLUM="#f2e2a0"

# ---- wall & window ----
c.rect(0,0,64,30,WALL)
c.rect(37,3,17,14,FRAME)
c.rect(39,5,13,10,SKY)
c.rect(45,5,1,10,FRAME)
c.rect(39,9,13,1,FRAME)
c.rect(41,6,3,1,CLOUD); c.rect(42,7,3,1,CLOUD)
c.rect(0,28,64,2,TRIM)

# ---- bench ----
c.rect(0,30,64,11,WOOD)
c.rect(0,30,64,1,WOOD_HI)
c.rect(0,41,64,23,FRONT)
c.rect(0,41,64,1,SEAM)
# left drawers
c.rect(5,45,24,8,DRAWER); c.rect(6,46,22,6,FRONT); c.rect(15,48,4,2,KNOB)
c.rect(5,56,24,7,DRAWER); c.rect(6,57,22,5,FRONT); c.rect(15,58,4,2,KNOB)
# right cabinet doors
c.rect(34,45,25,18,DRAWER); c.rect(35,46,23,16,FRONT)
c.rect(46,46,1,16,SEAM)
c.rect(41,53,3,2,KNOB); c.rect(50,53,3,2,KNOB)

# ---- shadows on bench top ----
c.rect(5,31,19,1,SHADOW)    # microscope
c.rect(25,32,17,1,SHADOW)   # rack
c.rect(44,31,18,1,SHADOW)   # bottles

# ---- microscope (left, tallest object) ----
c.rect(6,28,17,3,M_D)          # base
c.rect(8,27,13,1,M_D)
c.rect(18,13,3,15,M_M)         # vertical arm
c.rect(13,11,7,3,M_M)          # head block
c.poly([(9,6),(11,6),(17,12),(15,12)],M_M)   # tilted eyepiece tube
c.rect(8,4,3,2,M_D)            # eyepiece cap
c.rect(12,14,7,2,M_D)          # nosepiece
for ox in (13,15,17):
    c.rect(ox,16,1,3,M_L)      # objectives
c.rect(7,20,12,2,M_M)          # stage
c.rect(7,20,12,1,M_L)
c.rect(11,23,5,2,ILLUM)        # illuminator
c.rect(13,25,2,2,M_M)          # mount post to base
c.rect(17,23,2,3,M_D)          # focus knob

# ---- test-tube rack (center) ----
tubes=[(28,GREEN),(31,BLUE),(34,PINK),(37,YELLOW)]
for tx,lq in tubes:
    c.rect(tx,15,2,15,GLASS)   # tube y15..29
    c.rect(tx,20,2,10,lq)      # liquid
    c.set(tx,15,CLOUD); c.set(tx+1,15,CLOUD)   # rim
    c.set(tx,22,GLASS)         # bubble
c.rect(26,24,15,1,DRAWER)      # top rail
c.rect(26,24,1,8,DRAWER)       # posts
c.rect(40,24,1,8,DRAWER)
c.rect(26,30,15,2,SEAM)        # base

# ---- labeled bottles (right) ----
# tall bottle
c.rect(46,10,3,2,CAPB)
c.rect(46,12,3,3,GLASS)
c.rect(45,15,5,3,GLASS)
c.rect(45,18,5,13,GLASS)
c.rect(46,20,3,11,GREEN)
c.rect(45,23,5,3,CREAM)        # label
c.rect(45,24,5,1,BLUE)         # label band
c.rect(45,18,1,13,GLASS_D)     # shading
# small bottle
c.rect(53,18,3,2,BLUE)
c.rect(53,20,3,2,GLASS)
c.rect(52,22,5,9,GLASS)
c.rect(53,25,3,6,PINK)
c.rect(52,26,5,2,CREAM)
c.rect(52,22,1,9,GLASS_D)
# tiny vial
c.rect(58,24,3,1,M_D)
c.rect(58,25,3,6,GLASS)
c.rect(58,28,3,3,YELLOW)
c.rect(58,25,1,6,GLASS_D)

# ---- open laboratory notebook (front center) ----
c.rect(30,39,24,2,COVER)       # cover edge
c.rect(30,33,11,6,PAPER)       # left page
c.rect(42,33,11,6,PAPER)       # right page
c.rect(41,33,1,6,SPINE)
for y in (35,37):
    c.line(32,y,39,y,LINE)
    c.line(43,y,51,y,LINE)
c.rect(50,33,1,3,RED)          # bookmark ribbon

# ---- pencil on bench (right of notebook) ----
c.rect(55,37,6,1,YELLOW)       # shaft
c.rect(54,37,1,1,CREAM)        # sharpened wood
c.set(53,37,M_D)               # graphite tip
c.rect(61,37,1,1,PINK)         # eraser

# ---- dropper / pipette (front left, lying down) ----
c.rect(14,35,3,3,RED)          # rubber bulb
c.set(15,34,BULB_HI)
c.rect(17,36,10,1,GLASS)       # glass tube
c.set(27,36,GLASS_D)           # tip
c.set(28,36,GLASS_D)
c.set(29,37,BLUE)              # hanging drop

print(c.stats_text())
finish(c)
