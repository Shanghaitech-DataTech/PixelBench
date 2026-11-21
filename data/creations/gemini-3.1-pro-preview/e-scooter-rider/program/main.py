from pixelbench_api import new_canvas, view, finish

def draw_scooter():
    c = new_canvas(32, 32)
    
    # Colors
    tire_color = "#222222"
    hub_color = "#888888"
    deck_color = "#333333"
    accent_color = "#00E5FF"
    stem_color = "#AAAAAA"
    
    skin_color = "#FFCBA4"
    shirt_color = "#FF3366"
    pants_color = "#2E86C1"
    shoe_color = "#4A2311"
    helmet_color = "#FFD700"
    strap_color = "#222222"
    backpack_color = "#8E44AD"
    
    # Back arm
    c.line(14, 11, 17, 14, shirt_color)
    c.line(17, 14, 21, 12, skin_color)
    
    # Rider Back Leg
    c.rect(10, 24, 4, 2, shoe_color)
    c.poly([(12, 18), (15, 18), (14, 24), (11, 24)], pants_color)
    
    # Wheels
    c.circle(8, 27, 3, tire_color)
    c.circle(8, 27, 1, hub_color)
    
    c.circle(24, 27, 3, tire_color)
    c.circle(24, 27, 1, hub_color)
    
    # Fender
    c.line(5, 26, 7, 24, deck_color)
    c.line(8, 24, 10, 24, deck_color)
    
    # Deck
    c.rect(8, 25, 15, 2, deck_color)
    c.line(9, 25, 22, 25, accent_color)
    
    # Stem base
    c.rect(22, 24, 3, 3, deck_color)
    c.set(23, 24, accent_color)
    
    # Rider Front Leg
    c.rect(15, 24, 4, 2, shoe_color)
    c.poly([(14, 18), (17, 18), (18, 24), (15, 24)], pants_color)
    
    # Stem
    c.line(24, 26, 22, 12, stem_color)
    c.line(23, 26, 21, 12, stem_color)
    
    # Handlebars
    c.rect(20, 11, 4, 2, deck_color)
    c.set(20, 11, accent_color)
    
    # Torso (leaning forward)
    c.poly([(12, 18), (16, 18), (17, 10), (13, 10)], shirt_color)
    
    # Backpack
    c.poly([(10, 12), (13, 11), (12, 17), (9, 16)], backpack_color)
    
    # Head & Neck
    c.rect(15, 9, 2, 2, skin_color) # Neck
    c.rect(14, 5, 5, 4, skin_color) # Face
    c.set(17, 6, "#000000") # Eye
    c.set(19, 7, skin_color) # Nose
    
    # Helmet
    c.rect(13, 3, 6, 3, helmet_color) # Main dome
    c.rect(14, 2, 4, 1, helmet_color) # Top rounding
    c.rect(13, 6, 2, 2, helmet_color) # Back drop
    c.rect(19, 4, 2, 1, helmet_color) # Front brim
    
    # Strap
    c.line(14, 6, 14, 9, strap_color)
    c.set(15, 9, strap_color)
    c.set(16, 8, strap_color)
    
    # Front arm
    c.line(15, 11, 18, 14, shirt_color)
    c.line(16, 11, 19, 14, shirt_color)
    c.line(18, 14, 20, 11, skin_color)
    c.line(19, 14, 20, 12, skin_color)
    
    view(c)
    finish(c)

if __name__ == "__main__":
    draw_scooter()
