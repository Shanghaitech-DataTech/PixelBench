from pixelbench_api import new_canvas, finish

# Create 64x32 canvas for 2-frame walk animation (each frame 32x32)
c = new_canvas(64, 32, background=None, name="swordsman_walk")

# Define color palette for 16-bit RPG style
# Skin tones
skin_light = c.color((255, 220, 180), "skin_light")
skin_mid = c.color((230, 180, 140), "skin_mid")
skin_shadow = c.color((200, 140, 100), "skin_shadow")

# Red hair
hair_light = c.color((255, 100, 80), "hair_light")
hair_mid = c.color((220, 50, 40), "hair_mid")
hair_dark = c.color((180, 30, 20), "hair_dark")

# Dark blue cape
cape_light = c.color((80, 100, 180), "cape_light")
cape_mid = c.color((50, 70, 150), "cape_mid")
cape_dark = c.color((30, 40, 100), "cape_dark")

# Clothing (brown/tan tunic)
tunic_light = c.color((200, 160, 100), "tunic_light")
tunic_mid = c.color((160, 120, 60), "tunic_mid")
tunic_dark = c.color((120, 80, 40), "tunic_dark")

# Pants (dark gray)
pants_mid = c.color((80, 80, 90), "pants_mid")
pants_dark = c.color((50, 50, 60), "pants_dark")

# Boots (black/brown)
boot_dark = c.color((60, 40, 30), "boot_dark")
boot_mid = c.color((80, 55, 40), "boot_mid")

# Sword (metallic)
sword_light = c.color((255, 255, 240), "sword_light")
sword_mid = c.color((200, 200, 210), "sword_mid")
sword_dark = c.color((120, 120, 130), "sword_dark")
sword_hilt = c.color((180, 140, 60), "sword_hilt")

# Outline/shadow
outline = c.color((40, 30, 50), "outline")

# Helper function to draw swordsman at offset x
def draw_swordsman(frame_x, leg_forward):
    """
    Draw swordsman at horizontal offset frame_x
    leg_forward: True = left leg forward, False = right leg forward
    """
    base_x = frame_x
    base_y = 4  # Top of head
    
    # HEAD (8x8 area, centered around x=base_x+12)
    head_x = base_x + 8
    head_y = base_y + 2
    
    # Hair (back)
    c.set(head_x + 0, head_y + 0, hair_dark)
    c.set(head_x + 1, head_y + 0, hair_dark)
    c.set(head_x + 2, head_y + 0, hair_mid)
    c.set(head_x + 3, head_y + 0, hair_mid)
    c.set(head_x + 4, head_y + 0, hair_mid)
    c.set(head_x + 0, head_y + 1, hair_dark)
    c.set(head_x + 1, head_y + 1, hair_dark)
    c.set(head_x + 2, head_y + 1, hair_mid)
    c.set(head_x + 3, head_y + 1, hair_mid)
    c.set(head_x + 4, head_y + 1, hair_mid)
    c.set(head_x + 5, head_y + 1, hair_light)
    c.set(head_x + 0, head_y + 2, hair_dark)
    c.set(head_x + 1, head_y + 2, hair_mid)
    c.set(head_x + 5, head_y + 2, hair_light)
    c.set(head_x + 6, head_y + 2, hair_light)
    c.set(head_x + 0, head_y + 3, hair_dark)
    c.set(head_x + 1, head_y + 3, hair_mid)
    c.set(head_x + 5, head_y + 3, hair_light)
    c.set(head_x + 6, head_y + 3, hair_light)
    
    # Face
    c.set(head_x + 2, head_y + 2, skin_light)
    c.set(head_x + 3, head_y + 2, skin_light)
    c.set(head_x + 4, head_y + 2, skin_light)
    c.set(head_x + 5, head_y + 2, skin_light)
    c.set(head_x + 2, head_y + 3, skin_light)
    c.set(head_x + 3, head_y + 3, skin_light)
    c.set(head_x + 4, head_y + 3, skin_light)
    c.set(head_x + 5, head_y + 3, skin_light)
    c.set(head_x + 2, head_y + 4, skin_mid)
    c.set(head_x + 3, head_y + 4, skin_mid)
    c.set(head_x + 4, head_y + 4, skin_mid)
    c.set(head_x + 5, head_y + 4, skin_mid)
    c.set(head_x + 6, head_y + 4, skin_mid)
    c.set(head_x + 2, head_y + 5, skin_mid)
    c.set(head_x + 3, head_y + 5, skin_mid)
    c.set(head_x + 4, head_y + 5, skin_mid)
    c.set(head_x + 5, head_y + 5, skin_mid)
    
    # Eye
    c.set(head_x + 5, head_y + 3, (40, 30, 50))
    
    # NECK
    c.set(head_x + 3, head_y + 6, skin_mid)
    c.set(head_x + 4, head_y + 6, skin_mid)
    
    # TORSO (tunic)
    torso_x = base_x + 8
    torso_y = base_y + 8
    c.set(torso_x + 0, torso_y + 0, tunic_dark)
    c.set(torso_x + 1, torso_y + 0, tunic_mid)
    c.set(torso_x + 2, torso_y + 0, tunic_mid)
    c.set(torso_x + 3, torso_y + 0, tunic_mid)
    c.set(torso_x + 4, torso_y + 0, tunic_mid)
    c.set(torso_x + 5, torso_y + 0, tunic_light)
    c.set(torso_x + 0, torso_y + 1, tunic_dark)
    c.set(torso_x + 1, torso_y + 1, tunic_mid)
    c.set(torso_x + 2, torso_y + 1, tunic_mid)
    c.set(torso_x + 3, torso_y + 1, tunic_mid)
    c.set(torso_x + 4, torso_y + 1, tunic_mid)
    c.set(torso_x + 5, torso_y + 1, tunic_light)
    c.set(torso_x + 0, torso_y + 2, tunic_dark)
    c.set(torso_x + 1, torso_y + 2, tunic_dark)
    c.set(torso_x + 2, torso_y + 2, tunic_mid)
    c.set(torso_x + 3, torso_y + 2, tunic_mid)
    c.set(torso_x + 4, torso_y + 2, tunic_mid)
    c.set(torso_x + 5, torso_y + 2, tunic_light)
    c.set(torso_x + 0, torso_y + 3, tunic_dark)
    c.set(torso_x + 1, torso_y + 3, tunic_dark)
    c.set(torso_x + 2, torso_y + 3, tunic_mid)
    c.set(torso_x + 3, torso_y + 3, tunic_mid)
    c.set(torso_x + 4, torso_y + 3, tunic_mid)
    c.set(torso_x + 5, torso_y + 3, tunic_light)
    c.set(torso_x + 0, torso_y + 4, tunic_dark)
    c.set(torso_x + 1, torso_y + 4, tunic_dark)
    c.set(torso_x + 2, torso_y + 4, tunic_dark)
    c.set(torso_x + 3, torso_y + 4, tunic_mid)
    c.set(torso_x + 4, torso_y + 4, tunic_mid)
    c.set(torso_x + 5, torso_y + 4, tunic_mid)
    
    # CAPE (dark blue, flowing behind)
    cape_x = base_x + 4
    cape_y = base_y + 7
    c.set(cape_x + 0, cape_y + 0, cape_dark)
    c.set(cape_x + 1, cape_y + 0, cape_mid)
    c.set(cape_x + 2, cape_y + 0, cape_mid)
    c.set(cape_x + 0, cape_y + 1, cape_dark)
    c.set(cape_x + 1, cape_y + 1, cape_dark)
    c.set(cape_x + 2, cape_y + 1, cape_mid)
    c.set(cape_x + 3, cape_y + 1, cape_mid)
    c.set(cape_x + 0, cape_y + 2, cape_dark)
    c.set(cape_x + 1, cape_y + 2, cape_dark)
    c.set(cape_x + 2, cape_y + 2, cape_mid)
    c.set(cape_x + 3, cape_y + 2, cape_light)
    c.set(cape_x + 0, cape_y + 3, cape_dark)
    c.set(cape_x + 1, cape_y + 3, cape_dark)
    c.set(cape_x + 2, cape_y + 3, cape_mid)
    c.set(cape_x + 3, cape_y + 3, cape_light)
    c.set(cape_x + 4, cape_y + 3, cape_light)
    c.set(cape_x + 0, cape_y + 4, cape_dark)
    c.set(cape_x + 1, cape_y + 4, cape_dark)
    c.set(cape_x + 2, cape_y + 4, cape_mid)
    c.set(cape_x + 3, cape_y + 4, cape_mid)
    c.set(cape_x + 4, cape_y + 4, cape_light)
    c.set(cape_x + 5, cape_y + 4, cape_light)
    
    # ARM (holding sword)
    arm_x = base_x + 12
    arm_y = base_y + 9
    c.set(arm_x + 0, arm_y + 0, skin_mid)
    c.set(arm_x + 1, arm_y + 0, skin_mid)
    c.set(arm_x + 2, arm_y + 0, skin_mid)
    c.set(arm_x + 3, arm_y + 0, skin_mid)
    c.set(arm_x + 4, arm_y + 0, skin_mid)
    c.set(arm_x + 5, arm_y + 0, skin_light)
    c.set(arm_x + 0, arm_y + 1, skin_mid)
    c.set(arm_x + 1, arm_y + 1, skin_mid)
    c.set(arm_x + 2, arm_y + 1, skin_mid)
    c.set(arm_x + 3, arm_y + 1, skin_mid)
    c.set(arm_x + 4, arm_y + 1, skin_light)
    c.set(arm_x + 5, arm_y + 1, skin_light)
    
    # SWORD (long sword, pointing forward-right)
    # Position varies slightly between frames
    sword_offset = 0 if leg_forward else 1
    sword_base_x = base_x + 16 + sword_offset
    sword_base_y = base_y + 8
    
    # Sword blade (diagonal, pointing up-right)
    c.set(sword_base_x + 0, sword_base_y + 0, sword_hilt)
    c.set(sword_base_x + 1, sword_base_y + 0, sword_hilt)
    c.set(sword_base_x + 2, sword_base_y + 0, sword_hilt)
    c.set(sword_base_x + 0, sword_base_y + 1, sword_hilt)
    c.set(sword_base_x + 1, sword_base_y + 1, sword_hilt)
    c.set(sword_base_x + 2, sword_base_y + 1, sword_dark)
    c.set(sword_base_x + 3, sword_base_y + 1, sword_mid)
    c.set(sword_base_x + 2, sword_base_y + 2, sword_dark)
    c.set(sword_base_x + 3, sword_base_y + 2, sword_mid)
    c.set(sword_base_x + 4, sword_base_y + 2, sword_mid)
    c.set(sword_base_x + 3, sword_base_y + 3, sword_mid)
    c.set(sword_base_x + 4, sword_base_y + 3, sword_light)
    c.set(sword_base_x + 5, sword_base_y + 3, sword_light)
    c.set(sword_base_x + 4, sword_base_y + 4, sword_light)
    c.set(sword_base_x + 5, sword_base_y + 4, sword_light)
    c.set(sword_base_x + 6, sword_base_y + 4, sword_light)
    c.set(sword_base_x + 5, sword_base_y + 5, sword_light)
    c.set(sword_base_x + 6, sword_base_y + 5, sword_light)
    c.set(sword_base_x + 7, sword_base_y + 5, sword_light)
    c.set(sword_base_x + 6, sword_base_y + 6, sword_light)
    c.set(sword_base_x + 7, sword_base_y + 6, sword_light)
    c.set(sword_base_x + 8, sword_base_y + 6, sword_light)
    
    # PANTS
    pants_x = base_x + 9
    pants_y = base_y + 13
    
    # LEGS - varies by frame
    if leg_forward:
        # Left leg forward, right leg back
        # Left leg (forward)
        c.set(pants_x + 0, pants_y + 0, pants_dark)
        c.set(pants_x + 1, pants_y + 0, pants_mid)
        c.set(pants_x + 2, pants_y + 0, pants_mid)
        c.set(pants_x + 0, pants_y + 1, pants_dark)
        c.set(pants_x + 1, pants_y + 1, pants_mid)
        c.set(pants_x + 2, pants_y + 1, pants_mid)
        c.set(pants_x + 0, pants_y + 2, pants_dark)
        c.set(pants_x + 1, pants_y + 2, pants_mid)
        c.set(pants_x + 2, pants_y + 2, pants_mid)
        c.set(pants_x + 1, pants_y + 3, pants_mid)
        c.set(pants_x + 2, pants_y + 3, pants_mid)
        c.set(pants_x + 3, pants_y + 3, pants_mid)
        
        # Right leg (back)
        c.set(pants_x + 4, pants_y + 0, pants_dark)
        c.set(pants_x + 5, pants_y + 0, pants_mid)
        c.set(pants_x + 4, pants_y + 1, pants_dark)
        c.set(pants_x + 5, pants_y + 1, pants_mid)
        c.set(pants_x + 6, pants_y + 1, pants_mid)
        c.set(pants_x + 4, pants_y + 2, pants_dark)
        c.set(pants_x + 5, pants_y + 2, pants_mid)
        
        # Left boot (forward)
        c.set(pants_x + 1, pants_y + 4, boot_dark)
        c.set(pants_x + 2, pants_y + 4, boot_mid)
        c.set(pants_x + 3, pants_y + 4, boot_mid)
        c.set(pants_x + 4, pants_y + 4, boot_mid)
        c.set(pants_x + 1, pants_y + 5, boot_dark)
        c.set(pants_x + 2, pants_y + 5, boot_dark)
        c.set(pants_x + 3, pants_y + 5, boot_mid)
        
        # Right boot (back, higher)
        c.set(pants_x + 5, pants_y + 3, boot_dark)
        c.set(pants_x + 6, pants_y + 3, boot_mid)
        c.set(pants_x + 5, pants_y + 4, boot_dark)
    else:
        # Right leg forward, left leg back
        # Left leg (back)
        c.set(pants_x + 0, pants_y + 0, pants_dark)
        c.set(pants_x + 1, pants_y + 0, pants_mid)
        c.set(pants_x + 0, pants_y + 1, pants_dark)
        c.set(pants_x + 1, pants_y + 1, pants_mid)
        c.set(pants_x + 2, pants_y + 1, pants_mid)
        c.set(pants_x + 0, pants_y + 2, pants_dark)
        c.set(pants_x + 1, pants_y + 2, pants_mid)
        
        # Right leg (forward)
        c.set(pants_x + 3, pants_y + 0, pants_dark)
        c.set(pants_x + 4, pants_y + 0, pants_mid)
        c.set(pants_x + 5, pants_y + 0, pants_mid)
        c.set(pants_x + 3, pants_y + 1, pants_dark)
        c.set(pants_x + 4, pants_y + 1, pants_mid)
        c.set(pants_x + 5, pants_y + 1, pants_mid)
        c.set(pants_x + 3, pants_y + 2, pants_dark)
        c.set(pants_x + 4, pants_y + 2, pants_mid)
        c.set(pants_x + 5, pants_y + 2, pants_mid)
        c.set(pants_x + 4, pants_y + 3, pants_mid)
        c.set(pants_x + 5, pants_y + 3, pants_mid)
        c.set(pants_x + 6, pants_y + 3, pants_mid)
        
        # Left boot (back, higher)
        c.set(pants_x + 1, pants_y + 3, boot_dark)
        c.set(pants_x + 2, pants_y + 3, boot_mid)
        c.set(pants_x + 1, pants_y + 4, boot_dark)
        
        # Right boot (forward)
        c.set(pants_x + 4, pants_y + 4, boot_dark)
        c.set(pants_x + 5, pants_y + 4, boot_mid)
        c.set(pants_x + 6, pants_y + 4, boot_mid)
        c.set(pants_x + 7, pants_y + 4, boot_mid)
        c.set(pants_x + 4, pants_y + 5, boot_dark)
        c.set(pants_x + 5, pants_y + 5, boot_dark)
        c.set(pants_x + 6, pants_y + 5, boot_mid)

# Draw frame 1 (left leg forward)
draw_swordsman(0, leg_forward=True)

# Draw frame 2 (right leg forward)  
draw_swordsman(32, leg_forward=False)

# Print stats
print(c.stats_text())

# Submit the result
finish(c)
