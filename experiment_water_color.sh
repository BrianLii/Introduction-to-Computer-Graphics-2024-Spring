p="experiment/water_color/taj_mahal/"
input="taj_mahal/sub.jpg"

mkdir -p $p

radius=("1" "2" "4" "8")
for rd in "${radius[@]}"; do
  python water_color.py \
      --input $input \
      --output ${p}${rd}.jpg \
      --radius $rd
done

montage "${p}1.jpg" "${p}2.jpg" "${p}4.jpg" "${p}8.jpg" \
        -tile 4x1 -geometry +0+0 "${p}grid.jpg"