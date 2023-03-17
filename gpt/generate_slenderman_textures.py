import numpy as np
from opensimplex import OpenSimplex
from PIL import Image

def generate_slenderman_texture(width, height, scale, seed=42):
    noise_gen = OpenSimplex(seed=seed)
    noise_array = np.zeros((height, width))

    for y in range(height):
        for x in range(width):
            value1 = noise_gen.noise2(x / scale, y / scale)
            value2 = noise_gen.noise2(x / (scale * 3), y / (scale * 3))
            value3 = noise_gen.noise2(x / (scale * 7), y / (scale * 7))
            noise_array[y][x] = (value1 + value2 + value3 + 3) / 6

    slenderman_colors = np.array([[32, 32, 32], [64, 64, 64], [128, 128, 128]])
    slenderman_indices = ((noise_array * 3) % 3).astype(int)
    slenderman_image = Image.fromarray(np.uint8(slenderman_colors[slenderman_indices] * 255), 'RGB')
    slenderman_image.save('slenderman_texture.png')

generate_slenderman_texture(512, 512, 100, seed=42)
