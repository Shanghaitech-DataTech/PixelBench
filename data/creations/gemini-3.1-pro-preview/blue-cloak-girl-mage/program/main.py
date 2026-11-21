import sys
from pixelbench_api import new_canvas, flatten, view, finish

def draw():
    c = new_canvas(64, 64)

    # Colors
    c.color("#ffe0d0", "skin")
    c.color("#dca690", "skin_shadow")
    
    c.color("#b4a7d6", "hair")
    c.color("#8e7cc3", "hair_shadow")
    
    c.color("#1c2331", "cloak")
    c.color("#0f131a", "cloak_shadow")
    c.color("#2c3e50", "cloak_hl")
    
    c.color("#f8f9fa", "dress")
    c.color("#ced4da", "dress_shadow")
    
    c.color("#ffffff", "boots")
    c.color("#e9ecef", "boots_shadow")
    
    c.color("#d4af37", "trim")
    
    c.color("#5c4033", "staff")
    c.color("#3b2818", "staff_shadow")
    
    c.color("#ffb347", "amber")
    c.color("#ffdf00", "amber_hl")
    c.color("#cc5500", "amber_shadow")
    
    c.color("#000000", "black")
    c.color("#ffffff", "white")
    c.color("#101018", "outline")

    # 1. Back Hair
    c.circle(32, 19, 9, "hair_shadow")
    c.rect(23, 19, 19, 15, "hair_shadow")
    
    # 2. Cloak Back
    c.path("M 22 30 L 42 30 L 48 56 L 16 56 Z", "cloak_shadow")
    
    # 3. Legs
    c.rect(28, 46, 3, 6, "skin_shadow")
    c.rect(34, 46, 3, 6, "skin_shadow")
    
    # 4. Boots
    c.rect(27, 50, 4, 10, "boots")
    c.rect(34, 50, 4, 10, "boots")
    c.rect(26, 58, 5, 4, "boots")
    c.rect(34, 58, 5, 4, "boots")
    c.rect(29, 50, 2, 12, "boots_shadow")
    c.rect(36, 50, 2, 12, "boots_shadow")
    c.line(27, 51, 30, 51, "trim")
    c.line(34, 51, 37, 51, "trim")
    
    # 5. Dress & Belt
    c.path("M 27 30 L 37 30 L 40 46 L 24 46 Z", "dress")
    c.path("M 32 30 L 37 30 L 40 46 L 32 46 Z", "dress_shadow")
    c.line(26, 44, 38, 44, "trim")
    c.line(25, 45, 39, 45, "trim")
    
    c.rect(26, 38, 13, 3, "cloak_shadow")
    c.rect(30, 37, 5, 5, "trim")
    c.rect(31, 38, 3, 3, "cloak_shadow")
    
    # 6. Neck & Head
    c.rect(30, 27, 4, 4, "skin_shadow")
    c.circle(32, 20, 6, "skin")
    c.rect(28, 20, 9, 8, "skin")
    c.poly([(28, 27), (32, 30), (36, 27)], "skin")
    
    # 7. Face
    c.rect(28, 22, 2, 3, "black")
    c.rect(35, 22, 2, 3, "black")
    c.set(29, 22, "white")
    c.set(36, 22, "white")
    c.set(27, 25, "skin_shadow")
    c.set(37, 25, "skin_shadow")
    c.line(31, 26, 33, 26, "skin_shadow")
    
    # 8. Front Hair
    c.circle(32, 18, 8, "hair")
    c.poly([(24,18), (28,22), (32,19), (36,22), (40,18), (41,14), (23,14)], "hair")
    c.poly([(23,18), (22,29), (25,27), (25,18)], "hair")
    c.poly([(41,18), (42,29), (39,27), (39,18)], "hair")
    
    # 9. Hat
    c.ellipse(32, 15, 16, 3, "cloak")
    c.ellipse(32, 15, 14, 2, "cloak_shadow")
    c.poly([(23, 14), (32, 2), (41, 14)], "cloak")
    c.poly([(32, 14), (32, 2), (41, 14)], "cloak_shadow")
    c.poly([(25, 12), (32, 7), (39, 12), (32, 14)], "trim")
    
    # 10. Cloak Front Drapes
    c.path("M 21 30 C 17 40 15 50 17 58 C 21 60 26 58 26 44 C 26 39 25 34 25 30 Z", "cloak")
    c.path("M 43 30 C 47 40 49 50 47 58 C 43 60 38 58 38 44 C 38 39 39 34 39 30 Z", "cloak")
    
    c.circle(32, 31, 2, "trim")
    c.circle(32, 31, 1, "amber_hl")
    
    # 11. Sleeves
    c.path("M 25 30 C 21 36 20 42 21 46 C 23 48 26 46 26 42 C 26 38 27 34 27 30 Z", "cloak_hl")
    c.path("M 39 30 C 42 34 45 39 46 42 L 43 44 C 41 39 39 34 37 30 Z", "cloak_hl")
    
    # 12. Left Hand
    c.circle(22, 47, 2, "skin")
    
    # 13. Staff & Right Hand
    c.rect(46, 14, 2, 48, "staff")
    c.rect(47, 14, 1, 48, "staff_shadow")
    c.poly([(45, 14), (49, 14), (48, 17), (46, 17)], "trim")
    
    c.circle(46, 42, 2, "skin")
    c.set(45, 41, "skin")
    c.set(45, 42, "skin")
    
    # 14. Gem
    c.circle(47, 11, 4, "amber_shadow")
    c.circle(47, 11, 3, "amber")
    c.circle(46, 10, 1, "amber_hl")
    
    # 15. Outline
    c.outline("outline")
    
    # 16. Transparent Effects
    c2 = new_canvas(64, 64)
    c2.color("#00000044", "shadow_trans")
    c2.color("#ffb34766", "glow1")
    c2.color("#ffb34733", "glow2")
    
    c2.ellipse(32, 19, 12, 2, "shadow_trans")
    c2.circle(47, 11, 12, "glow2")
    c2.circle(47, 11, 8, "glow1")
    
    final = flatten([c, c2])
    return final

final = draw()
finish(final)
