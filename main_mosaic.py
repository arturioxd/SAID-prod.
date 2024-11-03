from PIL import Image, ImageDraw

def draw_grid_with_images(base_image, grid_size, image_path):
    draw = ImageDraw.Draw(base_image)
    base_width, base_height = base_image.size
    grid_width, grid_height = grid_size
    
    cell_width = base_width // grid_width
    cell_height = base_height // grid_height
    
    for x in range(0, base_width, cell_width):
        for y in range(0, base_height, cell_height):
            average_color = calculate_average_pixel_color(base_image, x, y, cell_width, cell_height)
            cell_image = Image.open(image_path)
            tinted_cell_image = tint_image(cell_image, average_color)
            tinted_cell_image = tinted_cell_image.resize((cell_width, cell_height))
            base_image.paste(tinted_cell_image, (x, y))
    
    del draw

def calculate_average_pixel_color(image, x, y, width, height):
    
    pixel_array = image.load()
    r = g = b = 0
    total_pixels = 0
    
    for i in range(x, x + width):
        for j in range(y, y + height):
            if i < image.width and j < image.height: 
                pixel = pixel_array[i, j]
                r += pixel[0]
                g += pixel[1]
                b += pixel[2]
                total_pixels += 1
    
    if total_pixels == 0:
        return (0, 0, 0)
    
    average_color = (r // total_pixels, g // total_pixels, b // total_pixels)
    return average_color

def tint_image(image, tint_color):
    tinted_image = Image.new('RGB', image.size, tint_color)
    return Image.blend(image, tinted_image, alpha=0.55)

if __name__ == "__main__":
    base_image_path = "chief2.jpg"
    base_image = Image.open(base_image_path)
    grid_size = (40, 40) 
    
    image_path = "dada.jpg"
    
    draw_grid_with_images(base_image, grid_size, image_path)
    
    base_image.save("img2_mosaic.png")
#xdddd
