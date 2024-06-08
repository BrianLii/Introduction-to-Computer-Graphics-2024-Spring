input=demo/original.jpg
mkdir -p demo

python oil_painting.py --input $input --output demo/oil_painting.jpg
python water_color.py --input $input --output demo/water_color.jpg
python stained_glass.py --input $input --n_points=10000 --output demo/stained_glass.jpg

montage demo/original.jpg demo/stained_glass.jpg \
        demo/oil_painting.jpg demo/water_color.jpg \
        -tile 2x2 -geometry +0+0 "demo/grid.jpg"