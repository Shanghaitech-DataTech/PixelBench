from pixelbench_api import new_canvas

c = new_canvas(64, 64, name="t")

TUNNEL   = col = c.color("#141828")
TRAIN    = c.color("#98a4ba")
TRAIN_D  = c.color("#748199")
STRIPE   = c.color("#5c687d")
WIN      = c.color("#ffd784")
HEAD     = c.color("#fffdf0")
GLOW     = c.color("#ffd87e")
TRAIN_L  = c.color("#c3cbdd")

c.rect(0, 12, 64, 22, TRAIN)
c.rect(0, 15, 64, 2, STRIPE)
c.rect(48, 15, 16, 1, STRIPE)
c.rect(48, 33, 16, 1, TRAIN_D)
c.rect(50, 17, 14, 2, TRAIN_D)
c.rect(52, 19, 8, 8, GLOW)
c.rect(54, 21, 6, 6, HEAD)
c.rect(56, 22, 3, 3, HEAD)
c.rect(60, 22, 4, 1, GLOW)
c.rect(61, 24, 3, 1, GLOW)
c.rect(60, 26, 4, 1, GLOW)
c.rect(52, 31, 12, 2, TRAIN_L)

print(c.matrix_text(region=(48, 15, 63, 33)))
