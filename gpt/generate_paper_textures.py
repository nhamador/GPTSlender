import numpy as np
from opensimplex import OpenSimplex
from PIL import Image

def generate_page_texture(width, height, scale, seed=42):
    noise_gen = OpenSimplex(seed=seed)
    noise_array = np.zeros((height, width))

    for y in range(height):
        for x in range(width):
            value1 = noise_gen.noise2(x / scale, y / scale)
            value2 = noise_gen.noise2(x / (scale * 5), y / (scale * 5))
            noise_array[y][x] = (value1 + value2 + 2) / 4

    paper_colors = np.array([[240, 230, 200], [230, 220, 190], [220, 210, 180], [210, 200, 170]])
    paper_indices = ((noise_array * 4) % 4).astype(int)
    page_image = Image.fromarray(np.uint8(paper_colors[paper_indices] * 255), 'RGB')

    # Add pixelated scribbles
    scribble_array = np.random.randint(0, 100, (height // 10, width // 10)) < 5
    scribble_image = Image.fromarray(np.uint8(scribble_array * 128), 'L')
    scribble_image = scribble_image.resize((width, height), Image.NEAREST)

    # Merge paper and scribbles
    page_image = Image.composite(page_image, Image.new('RGB', (width, height), (0, 0, 0)), scribble_image)
    page_image.save('page_texture.png')

generate_page_texture(512, 512, 100, seed=42)
