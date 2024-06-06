mkdir -p results/{oil_painting,water_color,stained_glass}/taj_mahal

python oil_painting.py --input taj_mahal/720.jpg --output results/oil_painting/taj_mahal/720.jpg
python oil_painting.py --input taj_mahal/1080.jpg --output results/oil_painting/taj_mahal/1080.jpg
python oil_painting.py --input taj_mahal/1440.jpg --output results/oil_painting/taj_mahal/1440.jpg
python oil_painting.py --input taj_mahal/2160.jpg --output results/oil_painting/taj_mahal/2160.jpg

python water_color.py --input taj_mahal/720.jpg --output results/water_color/taj_mahal/720.jpg
python water_color.py --input taj_mahal/1080.jpg --output results/water_color/taj_mahal/1080.jpg
python water_color.py --input taj_mahal/1440.jpg --output results/water_color/taj_mahal/1440.jpg
python water_color.py --input taj_mahal/2160.jpg --output results/water_color/taj_mahal/2160.jpg

python stained_glass.py --input taj_mahal/1080.jpg --n_points=2000 --output results/stained_glass/taj_mahal/2000.jpg
python stained_glass.py --input taj_mahal/1080.jpg --n_points=5000 --output results/stained_glass/taj_mahal/5000.jpg
python stained_glass.py --input taj_mahal/1080.jpg --n_points=10000 --output results/stained_glass/taj_mahal/10000.jpg
python stained_glass.py --input taj_mahal/1080.jpg --n_points=20000 --output results/stained_glass/taj_mahal/20000.jpg