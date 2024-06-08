# Computer Graphics Final Project

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

## Division of work

This final project was completed independently.