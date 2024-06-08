bash experiment_oil_painting.sh
bash experiment_water_color.sh
bash experiment_stained_glass.sh

rm -rf report/resources/{demo, experiment}
cp -r demo experiment report/resources