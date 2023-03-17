import numpy as np
from opensimplex import OpenSimplex
from PIL import Image

def generate_grass_texture(width, height, scale, seed=42):
    noise_gen = OpenSimplex(seed=seed)
    noise_array = np.zeros((height, width))

    for y in range(height):
        for x in range(width):
            value = noise_gen.noise2(x / scale, y / scale)
            noise_array[y][x] = (value + 1) / 2

    grass_colors = np.array([[107, 142, 35], [154, 205, 50]])
    grass_indices = (noise_array > 0.5).astype(int)
    grass_image = Image.fromarray(np.uint8(grass_colors[grass_indices] * 255), 'RGB')
    grass_image.save('grass_texture.png')

generate_grass_texture(512, 512, 100, seed=42)

