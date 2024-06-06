from argparse import ArgumentParser
from math import floor

import numpy as np
from PIL import Image, ImageEnhance
from scipy.ndimage import convolve, median_filter


def read_image(filename):
    return np.asarray(Image.open(filename))

def gamma_brighten(pixels):
    pixels = pixels.astype(np.int64)
    return (pixels / 255) ** 0.5 * 255

def denoise(pixels, radius):
    pixels = pixels.astype(np.int64)
    return median_filter(pixels, size=(radius, radius), mode='nearest', axes=(0, 1))

def sharpen(pixels):
    pixels = pixels.astype(np.int64)
    kernel = np.array([[-1, -1, -1],
                       [-1, +9, -1],
                       [-1, -1, -1],])
    pixels = np.stack(
        tuple(convolve(pixels[:, :, c], kernel, mode='nearest') for c in range(3)), axis=2)
    return np.clip(pixels, a_min=0, a_max=255)

def add_texture(image, texture_path):
    texture = Image.open(texture_path)
    texture = texture.convert('L').resize(image.size)
    texture = ImageEnhance.Brightness(texture).enhance(0.7)
    texture = ImageEnhance.Contrast(texture).enhance(1.5)
    texture = texture.convert('RGB')
    textured_image = Image.blend(image, texture, alpha=0.3)
    return textured_image

def main(args):
    pixels = read_image(args.input)
    pixels = gamma_brighten(pixels)

    radius = args.radius
    if radius == -1: 
        radius = max(round(min(pixels.shape[0], pixels.shape[1]) * 0.0035), 2)

    for _ in range(3):
        pixels = denoise(pixels, radius)
    
    pixels = sharpen(pixels)
    pixels = denoise(pixels, 3)

    image = Image.fromarray(np.uint8(pixels)).convert('RGB')
    image = add_texture(image, args.texture)
    image.save(args.output)
    print(f'The output image saved at {args.output}')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input', type=str, required=True)
    parser.add_argument('--output', type=str, default='output.jpg')
    parser.add_argument('--radius', type=int, default=-1)
    parser.add_argument('--texture', type=str, default='texture/watercolor.jpg')
    args = parser.parse_args()
    main(args)
