import numpy as np
from opensimplex import OpenSimplex
from PIL import Image

def generate_tree_texture(width, height, scale, seed=42):
    noise_gen = OpenSimplex(seed=seed)
    noise_array = np.zeros((height, width))

    for y in range(height):
        for x in range(width):
            value1 = noise_gen.noise2(x / scale, y / scale)
            value2 = noise_gen.noise2(x / (scale * 2), y / (scale * 2))
            noise_array[y][x] = (value1 + value2 + 100) / 4

    tree_colors = np.array([[34, 139, 34], [0, 100, 0]])
    tree_indices = (noise_array > 0.5).astype(int)
    tree_image = Image.fromarray(np.uint8(tree_colors[tree_indices] * 255), 'RGB')
    tree_image.save('tree_texture.png')

generate_tree_texture(512, 512, 100, seed=42)
