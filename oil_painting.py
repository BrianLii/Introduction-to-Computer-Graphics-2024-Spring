from argparse import ArgumentParser
from math import floor

import numpy as np
from PIL import Image
from scipy.ndimage import convolve


def read_image(filename):
    return np.asarray(Image.open(filename))

def main(args):
    pixels = read_image(args.input).astype(np.int64)
    height, width, _ = pixels.shape
    radius, n_intensity = args.radius, args.n_intensity
    if radius == -1: 
        radius = max(round(min(pixels.shape[0], pixels.shape[1]) * 0.003), 2)

    intensity = np.sum(pixels, axis=2) / 3 * n_intensity // 255
    intensity = np.clip(intensity, a_min=0, a_max=n_intensity - 1).astype(np.int64)
    intensity_count = np.zeros((n_intensity, height, width), dtype=np.int64)
    sum_r = np.zeros((n_intensity, height, width), dtype=np.int64)
    sum_g = np.zeros((n_intensity, height, width), dtype=np.int64)
    sum_b = np.zeros((n_intensity, height, width), dtype=np.int64)
    for i in range(n_intensity):
        kernel = np.ones((1 + radius * 2, 1 + radius * 2))
        intensity_map = (intensity == i).astype(np.int64)
        intensity_count[i] = convolve(intensity_map, kernel, mode='constant')
        sum_r[i] = convolve(pixels[:,:,0] * intensity_map, kernel, mode='constant')
        sum_g[i] = convolve(pixels[:,:,1] * intensity_map, kernel, mode='constant')
        sum_b[i] = convolve(pixels[:,:,2] * intensity_map, kernel, mode='constant')

    max_intensity = np.argmax(intensity_count, axis=0)
    max_intensity_count = np.max(intensity_count, axis=0)

    I, J = np.indices(max_intensity.shape)
    output_r = sum_r[max_intensity, I, J] // max_intensity_count
    output_g = sum_g[max_intensity, I, J] // max_intensity_count
    output_b = sum_b[max_intensity, I, J] // max_intensity_count

    output_image = np.stack((output_r, output_g, output_b), axis=2)
    Image.fromarray(np.uint8(output_image)).convert('RGB').save(args.output)
    print(f'The output image saved at {args.output}')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input', type=str, required=True)
    parser.add_argument('--output', type=str, default='output.jpg')
    parser.add_argument('--radius', type=int, default=-1)
    parser.add_argument('--n_intensity', type=int, default=10)
    args = parser.parse_args()
    main(args)