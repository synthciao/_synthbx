# b=$1
b="poi_view"
arr=( 'base' 'iv50' 'iv100' 'iv200' 'iv300' 'iv400' 'iv500' 'iv600' 'iv700' 'iv800' 'iv900' 'iv1000' 'iv1500' 'iv2000' 'iv3000' 'iv5000' 'iv3000' 'iv5000' )
for a in ${arr[@]}; do
	./stat.sh stress/iv/$b/$a/$b 1
done

echo "Check stress/iv/results"