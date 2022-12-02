# b=$1
b="poi_view"
arr=( 'base' 'io1000' 'io2000' 'io3000' 'io4000' 'io5000' 'io10000' 'io20000' 'io25000' 'io50000' )
for a in ${arr[@]}; do
	./stat.sh stress/io/$b/$a/$b 1
done

echo "Check stress/io/results"