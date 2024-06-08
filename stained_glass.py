from argparse import ArgumentParser
from math import floor, sqrt

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.spatial import Delaunay


def read_image(filename):
    return np.asarray(Image.open(filename))

def main(args):
    np.random.seed(args.seed)
    pixels = read_image(args.input)
    height, width, _ = pixels.shape
    n_points = args.n_points

    min_dist = floor(sqrt(height * width / n_points))
    points = np.stack((np.random.randint(min_dist/1.6, height-min_dist/1.6, size=n_points), np.random.randint(min_dist/1.6, width-min_dist/1.6, size=n_points)), axis=1)
    points = np.concatenate((points, np.array([[0, y] for y in range(0, width - min_dist, min_dist)])), axis=0)
    points = np.concatenate((points, np.array([[height, y] for y in range(0, width - min_dist, min_dist)])), axis=0)
    points = np.concatenate((points, np.array([[x, 0] for x in range(0, height - min_dist, min_dist)])), axis=0)
    points = np.concatenate((points, np.array([[x, width] for x in range(0, height - min_dist, min_dist)])), axis=0)
    points = np.concatenate((points, np.array([[height - 1, width - 1]])), axis=0)

    mask = np.ones(points.shape[0], dtype=bool)
    for i in range(n_points):
        for j in range(i):
            if mask[j] and (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2 < min_dist ** 2:
                mask[i] = False
    points = points[mask]

    output_width = 20
    plt.figure(figsize=(output_width, output_width / width * height))
    plt.xlim(left=0, right=width-1)
    plt.ylim(top=0, bottom=height-1)

    triangles = Delaunay(points).simplices
    for triangle in triangles:
        centroid = np.floor(np.mean(points[triangle], axis=0)).astype(np.int64)
        color = pixels[centroid[0],centroid[1]] / 255
        triangle = points[np.append(triangle,triangle[0])]
        plt.fill(triangle[:,1], triangle[:,0], color=color)
        plt.plot(triangle[:,1], triangle[:,0], color='black', linewidth=0.1)

    plt.axis('off')
    plt.savefig(args.output, bbox_inches='tight', pad_inches=0)
    with Image.open(args.output) as img:
        img = img.resize((width, height))
        img.save(args.output)
    print(f'The output image saved at {args.output}')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input', type=str, required=True)
    parser.add_argument('--n_points', type=int, required=True)
    parser.add_argument('--output', type=str, default='output.jpg')
    parser.add_argument('--seed', type=int, default=2024)
    args = parser.parse_args()
    main(args)