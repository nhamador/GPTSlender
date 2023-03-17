import numpy as np
from opensimplex import OpenSimplex
from PIL import Image, ImageDraw

def generate_jack_texture(width, height, scale, seed=42):
    noise_gen = OpenSimplex(seed=seed)
    noise_array = np.zeros((height, width))

    for y in range(height):
        for x in range(width):
            value = noise_gen.noise2(x / scale, y / scale)
            noise_array[y][x] = (value + 1) / 2

    bg_colors = np.array([[230, 230, 230], [220, 220, 220]])
    bg_indices = ((noise_array * 2) % 2).astype(int)
    bg_image = Image.fromarray(np.uint8(bg_colors[bg_indices] * 255), 'RGB')

    film_strip = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(film_strip)

    film_strip_width = width // 10
    for i in range(height // film_strip_width + 1):
        y1 = i * film_strip_width
        y2 = y1 + film_strip_width // 2
        draw.rectangle([0, y1, width, y2], fill=(0, 0, 0, 180))

    bg_image = bg_image.convert('RGBA')  # Convert the background image to 'RGBA' mode
    jack_image = Image.alpha_composite(bg_image, film_strip)
    jack_image.save('jack_texture.png')

generate_jack_texture(512, 512, 50, seed=42)
