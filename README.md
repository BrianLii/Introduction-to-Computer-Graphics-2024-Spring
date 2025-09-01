# Computer Graphics Final Project

In this project I implemented three types of effect, including Oil Painting Effect, Water Color Effect, and Stained Glass Effect. These effects can be can be applied to any given image.

## Result Demo

Top to bottom, left to right: input image, apply stained glass effect, apply oil painting effect, apply watercolor effect. (Refer to the submitted package for images with the original resolution)

<img src="report/resources/demo/grid.jpg" style="zoom:80%;" />

<div style="page-break-after: always;"></div>

## Oil Painting Effect

I implemented the algorithm described in [[1]](#reference). However, the naïve implementation proved to be time-inefficient. I discovered that determining the intensity bin with the highest number of pixels for each pixel can be optimized using several convolution operations across all intensity levels. This enhancement improved the time efficiency by more than 10 folds when generating a 1440p image.

Below is a visualization showing how the two parameters, radius and number of intensity levels, affect the final result.

* Rows: Radius $1, 2, 4, 8$.

  The radius affects the sharpness of the result.

* Columns: Number of intensity levels $5, 10, 20, 40$.

  The number of intensity levels affects the local color variety, such as in the pavement in the picture, although the effect is not very obvious.

<img src="report/resources/experiment/oil_painting/taj_mahal/grid.jpg" style="zoom:18%;" />

## Stained Glass

I implemented the algorithm described in [[2]](#reference). The process involves uniformly and randomly sampling points within the image, then using Delaunay triangulation to connect these points. The final image is produced by drawing each triangle one by one using the Python library `matplotlib`. To enhance the result, I further refine the sampled points by removing those that are too close to each other, which helps make the output more visually appealing. Below are the resulting images for different numbers of sampled points:

<img src="report/resources/experiment/stained_glass/taj_mahal/grid.jpg" style="zoom:13%;" />

## Water Color

The idea originated from [[3]](#reference). I discovered that combining a median filter with a kernel for image sharpening [[4]](#reference) creates an image resembling watercolor art. To enhance its realism, I adjusted the gamma and blended a watercolor paper texture into the output image. The results are shown below. From left to right, the images correspond to median filter kernel sizes of $1, 2, 4, 8$. Larger median filter kernels produce progressively blurrier results.

<img src="report/resources/experiment/water_color/taj_mahal/grid.jpg" style="zoom:33%;" />

### Reference

[1]: Oil Painting Effect Algorithm: **[Oil Painting Algorithm | The Supercomputing Blog](http://supercomputingblog.com/graphics/oil-painting-algorithm/)**

[2]: Stained Glass Effect Algorithm: **[Stained Glass Algorithm | The Supercomputing Blog](http://supercomputingblog.com/openmp/stained-glass-algorithm/)**

[3]: Water Color Effect Algorithm: **[VR_final/Water_color.py · nickshao/VR_final · GitHub](https://github.com/nickshao/VR_final/blob/master/Water_color.py)**

[4]: Kernel [**Kernel (image processing) - Wikipedia**](https://en.wikipedia.org/wiki/Kernel_(image_processing))


## How to run the program

1. Set Up the Environment

    * Prepare a Python 3.9 environment and install the required packages:
        ```bash
        pip install -r requirements.txt
        ```
2. Run the Demo Script
    * Execute the demo script to generate results, which will be saved in the demo/ folder.
    * Note: The ImageMagick package is needed to produce tile images (as shown in the report). If ImageMagick is not installed, you can either install it or comment out the corresponding line in the script.
        ```bash
        bash demo.sh
        ```
3. Adjusting Parameters
    * If you want to customize the parameters, below is the usage for each file:
        ```
        python oil_painting.py \
                --input=<input image> \
                [--output=<output image>] \
                [--radius=<radius>] \
                [--n_intensity=<number of intensity levels>]

        python stained_glass.py \
                --input=<input image> \
                --n_points=<number of sampled points> \
                [--output=<output image>] \
                [--seed=<random seed>]

        python water_color.py \
                --input=<input image> \
                [--output=<output image>] \
                [--radius=<size of the median filter>] \
                [--texture=<texture file>]
        ```
4. Reproduce the Report Results

    * To reproduce the results shown in the report, run the following script:

        ```
        bash make_report.sh
        ```
