from pixelbench_api import *
import colorsys

def transform_by_category(r, g, b, category):
    h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
    
    if category == "Sky/Clouds":
        h = 0.58
        s = min(1.0, s * 1.5)
        v = min(1.0, v * 1.3)
    elif category == "Trees/Dark":
        h = 0.35
        s = min(1.0, s * 0.8)
        v = min(1.0, v * 1.2)
    elif category == "Mountain Highlights":
        h = 0.15
        s = min(1.0, s * 0.3)
        v = min(1.0, v * 1.1)
    elif category == "Mountains":
        h = 0.6
        s = min(1.0, s * 0.5)
        v = min(1.0, v * 1.2)
        
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return [int(r*255), int(g*255), int(b*255), 255]

def main():
    pal = input_canvas.palette()
    
    color_y_sum = {}
    color_count = {}
    
    for y in range(147):
        for x in range(250):
            c = input_canvas.get(x, y)
            color_y_sum[c] = color_y_sum.get(c, 0) + y
            color_count[c] = color_count.get(c, 0) + 1
            
    sky_colors = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 25, 26, 30, 43, 58, 62, 63, 64, 67}
    
    color_category = {}
    for c, count in color_count.items():
        avg_y = color_y_sum[c] / count
        r, g, b, a = pal[c]['rgba']
        h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
        
        if c in sky_colors:
            category = "Sky/Clouds"
        elif v < 0.25:
            category = "Trees/Dark"
        elif avg_y >= 65 and v > 0.5:
            category = "Mountain Highlights"
        else:
            category = "Mountains"
            
        color_category[c] = category

    out = input_canvas.copy(name="output")
    
    # Remove sun
    for y in range(16, 60):
        for x in range(100, 150):
            c = out.get(x, y)
            if c not in sky_colors:
                src_c = out.get(x - 50, y)
                if src_c not in sky_colors:
                    src_c = 1
                out.set(x, y, src_c)
                
    res = new_canvas(250, 147, name="res")
    for y in range(147):
        for x in range(250):
            c = out.get(x, y)
            cat = color_category.get(c, "Sky/Clouds")
            r, g, b, a = pal[c]['rgba']
            new_rgba = transform_by_category(r, g, b, cat)
            res.set(x, y, new_rgba)
            
    finish(res)

if __name__ == "__main__":
    main()
