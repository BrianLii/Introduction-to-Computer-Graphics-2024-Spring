p="experiment/stained_glass/taj_mahal/"
input="taj_mahal/2160.jpg"

mkdir -p $p

n_points=("5000" "10000" "20000" "40000")
for n_p in "${n_points[@]}"; do
  python stained_glass.py \
      --input $input \
      --output ${p}${n_p}.jpg \
      --n_points=${n_p}
done

montage "${p}5000.jpg" "${p}10000.jpg" "${p}20000.jpg" "${p}40000.jpg" \
        -tile 2x2 -geometry +0+0 "${p}grid.jpg"