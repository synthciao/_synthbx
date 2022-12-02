import os
from random import shuffle, choice

b = 'poi_view'

sizes = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 3000, 5000]

start = 2000

poiid1 = list(range(1, 1000))
poiid2 = list(range(1, 1000, 2))

cola = list(range(100, 250))
colb = list(range(250, 500))
colc = list(range(500, 600))

cold = ['d' + str(x) for x in list(range(100, 400))]
cole = ['e' + str(x) for x in list(range(100, 400))]
colf = ['f' + str(x) for x in list(range(100, 400))]


poi_update_expected = open(f'base/{b}/example/poi_update.expected', 'r').read().rstrip()
points_upadte_expected = open(f'base/{b}/example/points_update.expected', 'r').read().rstrip()
poi_view_update_facts = open(f'base/{b}/example/poi_view_update.facts', 'r').read().rstrip()

for s in sizes:
	fn = f'iv{s}'
	os.system(f'mkdir -p {fn}/{b}/example')
	os.system(f'cp -r base/{b}/schema {fn}/{b}')
	os.system(f'cp -r base/{b}/gcandidate {fn}/{b}')
	os.system(f'cp base/{b}/example/poi.facts {fn}/{b}/example')
	os.system(f'cp base/{b}/example/points.facts {fn}/{b}/example')

	l = start
	h = start + s

	pue = poi_update_expected
	psue = points_upadte_expected
	pvuf = poi_view_update_facts
    
	for i in range(l, h):
		ca, cb, cc, cd, ce, cf = choice(cola), choice(colb), choice(colc), choice(cold), choice(cole), choice(colf)
		tp = f'\n{i}\t{ca}\t{cb}\t{cc}'
		tps = f'\n{i}\t{cd}\t{ce}\t{cf}'
		tvu = f'\n{i}\t{ca}\t{cb}\t{cd}\t{ce}'
		
		pue += tp
		psue += tps
		pvuf += tvu
	
	pue += '\n'
	psue += '\n'
	pvuf += '\n'

	open(f'{fn}/{b}/example/poi_update.expected', 'w').write(pue)
	open(f'{fn}/{b}/example/points_update.expected', 'w').write(psue)
	open(f'{fn}/{b}/example/poi_view_update.facts', 'w').write(pvuf)