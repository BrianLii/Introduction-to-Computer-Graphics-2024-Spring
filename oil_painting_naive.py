from argparse import ArgumentParser

import numpy as np
from PIL import Image


def read_image(filename):
    return np.asarray(Image.open(filename))

def main(args):
    pixels = read_image(args.input).astype(np.int64)
    height, width, _ = pixels.shape
    radius, n_intensity = args.radius, args.n_intensity

    final_img = Image.new("RGB", (width, height), "white")
    for x in range(height):
        for y in range(width):
            sum_r = np.zeros((n_intensity, ), dtype=np.int64)
            sum_g = np.zeros((n_intensity, ), dtype=np.int64)
            sum_b = np.zeros((n_intensity, ), dtype=np.int64)
            intensity_count = np.zeros((n_intensity, ), dtype=np.int64)
            for r_x in range(max(x - radius, 0), min(x + radius, height)):
                for r_y in range(max(y - radius, 0), min(y + radius, width)):
                    r, g, b = pixels[r_x][r_y]
                    intensity = min(int((r + g + b) / 3. * n_intensity // 255), n_intensity - 1)
                    intensity_count[intensity] += 1
                    sum_r[intensity] += r
                    sum_g[intensity] += g 
                    sum_b[intensity] += b
            max_intensity = np.argmax(intensity_count)
            w = intensity_count[max_intensity]
            p_r = sum_r[max_intensity] // w
            p_g = sum_g[max_intensity] // w
            p_b = sum_b[max_intensity] // w
            final_img.putpixel((y, x), (p_r, p_g, p_b))
    final_img.save(args.output)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input', type=str, required=True)
    parser.add_argument('--output', type=str, default='output.jpg')
    parser.add_argument('--radius', type=int, default=5)
    parser.add_argument('--n_intensity', type=int, default=10)
    args = parser.parse_args()
    main(args)