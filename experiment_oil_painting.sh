p="experiment/oil_painting/taj_mahal/"
input="taj_mahal/sub.jpg"

mkdir -p $p

intensity=("5" "10" "20" "40")
radius=("1" "2" "4" "8")
for it in "${intensity[@]}"; do
  for rd in "${radius[@]}"; do
    python oil_painting.py \
        --input $input \
        --output ${p}${it}_${rd}.jpg \
        --n_intensity $it \
        --radius $rd
  done
done

montage "${p}5_1.jpg" "${p}5_2.jpg" "${p}5_4.jpg" "${p}5_8.jpg" \
        "${p}10_1.jpg" "${p}10_2.jpg" "${p}10_4.jpg" "${p}10_8.jpg" \
        "${p}20_1.jpg" "${p}20_2.jpg" "${p}20_4.jpg" "${p}20_8.jpg" \
        "${p}40_1.jpg" "${p}40_2.jpg" "${p}40_4.jpg" "${p}40_8.jpg" \
        -tile 4x4 -geometry +0+0 "${p}grid.jpg"
