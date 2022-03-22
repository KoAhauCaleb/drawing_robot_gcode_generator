from PIL import Image, ImageFilter


BED_MAX_X = 160 
BED_MAX_Y = -120

image_path = "R.jpg"

cmds_written = 0

def main():

    image = Image.open(image_path)
    
    img = image.convert('RGB')
    img = img.filter(ImageFilter.BLUR)
    img.show()

    palette = [
        0, 0, 0,
        255, 255, 255,
    ]

    print(palette)

    p_img = Image.new('P', (16, 16))
    p_img.putpalette(palette * 128)
    
    pallet = img.quantize(palette=p_img, dither=0).convert('L')
    pallet.show()

    

    small_img = pallet.resize((BED_MAX_X * 4, (-BED_MAX_Y) * 4))
    small_img.show()
    
    width, heigth = small_img.size
    
    pixels = small_img.load()

    commands = open("g_code_overwrite.txt", "a")
    commands.truncate(0)

    print(f"{pixels[0,0]}")

    visited = set()
    
    for h in range(heigth - 1, 1, -1):
        for w in range(width):
            if pixels[w,h] == 0 and (w,h) not in visited:
                
                commands.write(f"G0 Z2\n")

                path = create_path(w, h, visited, pixels, width, heigth, 8, 0)

                for i, point in enumerate(path):
                    
                    x_pix,y_pix = point

                    visited.add((x_pix,y_pix))
                    
                    x = round(x_pix * (BED_MAX_X/width), 2)
                    y = round(y_pix * (BED_MAX_Y/heigth), 2)

                    commands.write(f"G0 X{x} Y{y}\n")

                    if i == 0:
                        commands.write(f"G0 Z0\n")


def create_path(w, h, visited, pixels, width, heigth, max_len, run, route=None):
    
    if route is None:
        route = []

    if (w,h) in visited or (w,h) in route or run >= max_len:
        return []
    
    route.append((w,h))

    longest_path = []

    ways_taken = 0

    if pixels[w,h+1] == 0 and ways_taken < 3:
        path = create_path(w, h+1, visited, pixels, width, heigth, max_len, run + 1, route[:])
        if len(longest_path) < len(path):
            longest_path = path
        ways_taken += 1
    elif pixels[w+1,h+1] == 0 and ways_taken < 3:
        path = create_path(w+1, h+1, visited, pixels, width, heigth, max_len, run + 1, route[:])
        if len(longest_path) < len(path):
            longest_path = path
        ways_taken += 1
    elif pixels[w-1,h-1] == 0 and ways_taken < 3:
        path = create_path(w-1, h-1, visited, pixels, width, heigth, max_len, run + 1, route[:])
        if len(longest_path) < len(path):
            longest_path = path
        ways_taken += 1

    longest_path.append((w,h))

    return longest_path

def set_longest(longest_path, path):
    if len(longest_path) < len(path):
        longest_path = path

if __name__ == "__main__":
    main()