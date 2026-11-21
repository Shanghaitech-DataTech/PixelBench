# Dragon hatchling RPG enemy sprite, 64x64, transparent background.
from pixelbench_api import new_canvas, view, finish

c = new_canvas(64, 64, background=None, name="dragon_hatchling")

# Restrained pixel-art palette.
OUT = "#17202b"
DEEP = "#263747"
SHADOW = "#355462"
GREEN = "#47736f"
MID = "#5f9181"
LIGHT = "#82ad91"
PALE = "#d2c895"
BELLY = "#e6d8a6"
HORN = "#c4b982"
MOUTH = "#6d2932"
TONGUE = "#b94a55"
EYE = "#f2c84b"
WHITE = "#f4e7bf"

# Tail silhouette curling left, with dorsal spikes.
c.poly([(31,41),(25,42),(21,45),(17,47),(13,47),(10,45),(7,46),(10,49),
        (6,50),(10,52),(7,55),(12,54),(11,58),(15,55),(17,58),(19,53),
        (23,51),(28,50),(34,48)], OUT)
c.poly([(31,43),(25,44),(21,47),(17,49),(12,49),(10,48),(13,51),(10,52),
        (15,52),(14,55),(18,52),(22,49),(28,48),(34,46)], SHADOW)
c.line(16,50,27,46,LIGHT)
c.set(12,49,MID); c.set(19,50,MID); c.set(24,47,GREEN)

# Rear wing: half spread behind the body.
c.poly([(29,31),(24,25),(15,23),(7,17),(11,27),(6,29),(16,33),(24,38)], OUT)
c.poly([(26,31),(22,27),(16,26),(10,21),(13,29),(10,30),(17,31),(23,35)], GREEN)
# Wing membrane panels.
c.poly([(11,20),(17,25),(15,29),(12,27)], MID)
c.poly([(18,25),(23,27),(22,33),(16,30)], SHADOW)
c.line(11,20,16,30,DEEP); c.line(17,25,22,34,DEEP)
c.set(13,24,LIGHT); c.set(19,28,MID)

# Far wing rising behind the head.
c.poly([(34,32),(37,21),(43,14),(48,7),(48,17),(56,10),(53,24),(58,25),
        (50,31),(43,38)], OUT)
c.poly([(37,31),(39,22),(44,16),(47,11),(47,21),(53,15),(51,26),(55,26),
        (49,29),(43,35)], GREEN)
c.poly([(40,24),(46,15),(46,25),(43,32)], MID)
c.poly([(48,22),(52,17),(50,27),(45,33)], SHADOW)
c.line(46,21,43,33,DEEP); c.line(51,25,45,34,DEEP)
c.set(43,20,LIGHT); c.set(49,23,MID)

# Rear legs, planted wide.
c.poly([(27,43),(25,49),(21,53),(18,53),(17,56),(27,56),(29,51),(34,48)], OUT)
c.poly([(28,45),(27,50),(24,53),(21,53),(20,54),(26,54),(28,50),(33,47)], GREEN)
c.poly([(42,43),(44,49),(48,52),(53,52),(56,55),(46,56),(41,52),(38,47)], OUT)
c.poly([(41,45),(43,50),(47,54),(52,54),(50,52),(47,51),(45,47)], SHADOW)
# Toe breaks.
c.set(20,55,HORN); c.set(24,55,HORN); c.set(48,55,HORN); c.set(52,54,HORN)

# Main crouched body silhouette.
c.poly([(25,28),(31,24),(39,24),(45,28),(48,35),(47,43),(43,49),(37,52),
        (29,51),(24,47),(21,40),(22,33)], OUT)
c.poly([(27,29),(32,26),(38,26),(43,29),(46,35),(45,42),(41,47),(36,50),
        (30,49),(26,46),(23,40),(24,34)], GREEN)
# Body shadow and shoulder.
c.poly([(24,36),(30,38),(34,46),(32,49),(27,46),(23,40)], SHADOW)
c.poly([(28,29),(34,26),(40,27),(43,31),(36,33),(30,32)], MID)
c.set(30,28,LIGHT); c.set(34,27,LIGHT); c.set(27,34,MID)

# Pale segmented belly, curved under the chest.
c.poly([(36,31),(42,32),(44,36),(43,43),(39,48),(35,49),(36,45),(38,40),(38,35)], PALE)
c.rect(38,34,5,2,BELLY); c.rect(39,38,4,2,BELLY); c.rect(38,42,4,2,BELLY)
c.line(38,37,42,37,HORN); c.line(38,41,42,41,HORN); c.line(36,45,40,45,HORN)

# Neck rises toward the lowered head.
c.poly([(38,30),(40,23),(44,19),(50,19),(53,24),(49,32),(44,36)], OUT)
c.poly([(41,30),(42,24),(45,21),(49,21),(51,24),(48,30),(44,33)], MID)
c.poly([(42,29),(44,24),(48,22),(50,24),(47,29),(44,32)], LIGHT)
# Neck scales.
c.set(42,25,GREEN); c.set(45,22,BELLY); c.set(47,27,GREEN); c.set(44,30,PALE)

# Small swept horns behind the skull.
c.poly([(43,22),(39,18),(39,14),(42,18),(46,20)], OUT)
c.poly([(42,20),(40,17),(40,16),(44,20)], HORN)
c.poly([(49,21),(48,16),(51,13),(51,19),(53,22)], OUT)
c.poly([(50,19),(50,16),(51,15),(51,20)], HORN)

# Head and muzzle, lowered in a growl.
c.poly([(43,22),(47,19),(53,20),(56,23),(56,26),(61,28),(60,34),(55,36),
        (49,34),(44,31),(41,27)], OUT)
c.poly([(45,23),(48,21),(52,22),(54,24),(54,27),(58,29),(58,31),(54,32),
        (50,31),(46,30),(43,27)], MID)
# Brow and cheek planes.
c.poly([(45,23),(50,22),(54,24),(51,26),(46,26)], LIGHT)
c.poly([(45,28),(50,27),(55,29),(53,32),(48,30)], GREEN)
c.set(56,29,LIGHT); c.set(58,30,DEEP)

# Open mouth cut and lower jaw.
c.poly([(48,31),(54,32),(59,31),(57,35),(52,37),(47,35)], OUT)
c.poly([(49,32),(54,33),(58,32),(56,34),(52,35),(49,34)], MOUTH)
c.poly([(50,34),(54,34),(56,33),(54,35),(51,35)], TONGUE)
# Teeth and lip accents.
c.poly([(51,32),(53,32),(52,34)], WHITE)
c.poly([(56,32),(58,32),(56,34)], WHITE)
c.line(48,35,53,37,DEEP); c.line(53,37,57,35,OUT)

# Eye, nostril, and expressive brow.
c.rect(49,24,2,2,OUT); c.set(49,24,EYE); c.set(50,24,EYE); c.set(50,25,OUT)
c.line(47,23,52,23,OUT)
c.set(57,29,OUT)

# Forearms, tense and clawed.
c.poly([(29,34),(25,38),(24,44),(20,47),(21,50),(26,47),(28,41),(33,38)], OUT)
c.poly([(29,36),(27,39),(26,44),(23,47),(24,47),(26,45),(28,40),(32,38)], MID)
c.set(21,49,HORN); c.set(24,48,HORN)
c.poly([(41,36),(45,38),(47,43),(51,46),(50,49),(45,46),(43,42),(38,40)], OUT)
c.poly([(41,38),(44,39),(45,44),(48,47),(46,46),(43,43),(42,40),(39,40)], GREEN)
c.set(49,48,HORN); c.set(46,47,HORN)

# Pixel scale texture and silhouette highlights.
for x,y,col in [
    (31,31,LIGHT),(34,33,SHADOW),(28,37,LIGHT),(32,39,MID),(29,43,DEEP),
    (34,47,LIGHT),(40,29,PALE),(25,41,MID),(43,34,LIGHT),(36,28,SHADOW),
    (31,35,DEEP),(35,36,LIGHT),(33,42,DEEP),(37,31,MID)]:
    c.set(x,y,col)
# A few two-pixel chevron scales.
c.line(31,31,32,32,LIGHT); c.line(34,35,35,34,DEEP)
c.line(29,40,30,41,DEEP); c.line(34,45,35,44,LIGHT)

view(c, scale=8, margin=1, edges="all")
finish(c)
