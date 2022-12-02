# b=$1
b="poi_view"
arr=( 'base' 'dv50' 'dv100' 'dv200' 'dv250' 'dv500' 'dv750' 'dv1000' 'dv1500' 'dv2000' 'dv2500' 'dv3000' 'dv3500' )
for a in ${arr[@]}; do
	./stat.sh stress/dv/$b/$a/$b 1
done

echo "Check stress/dv/results"