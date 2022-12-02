import os
from random import shuffle, choice

b = 'poi_view'

sizes = [50, 100, 200, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500]

start = 6500

poi_update_expected = open(f'base/{b}/example/poi_update.expected', 'r').read().rstrip()
points_upadte_expected = open(f'base/{b}/example/points_update.expected', 'r').read().rstrip()
poi_view_update_facts = open(f'base/{b}/example/poi_view_update.facts', 'r').read().rstrip()

for s in sizes:
	fn = f'dv{s}'
	os.system(f'mkdir -p {fn}/{b}/example')
	os.system(f'cp -r base/{b}/schema {fn}/{b}')
	os.system(f'cp -r base/{b}/gcandidate {fn}/{b}')
	os.system(f'cp base/{b}/example/poi.facts {fn}/{b}/example')
	os.system(f'cp base/{b}/example/points.facts {fn}/{b}/example')

	h = start
	l = start - s

	pue = poi_update_expected.split('\n')
	psue = points_upadte_expected.split('\n')
	pvuf = poi_view_update_facts.split('\n')
    
	for i in range(h, l, -1):
		tvu = [t for t in pvuf if t.split('\t')[0] == str(i)][0]
		pvuf.remove(tvu)
  
		_, ca, cb, cd, ce = tvu.split('\t')
		tp = f'{i}\t{ca}\t{cb}'
		tps = f'{i}\t{cd}\t{ce}'
		
	
		x = [t for t in pue if '\t'.join(t.split('\t')[:-1]) == tp][0]
		pue.remove(x)
		y = [t for t in psue if '\t'.join(t.split('\t')[:-1]) == tps][0]
		psue.remove(y)
		
	
	pue = '\n'.join(pue) + '\n'
	psue = '\n'.join(psue) + '\n'
	pvuf = '\n'.join(pvuf) + '\n'

	open(f'{fn}/{b}/example/poi_update.expected', 'w').write(pue)
	open(f'{fn}/{b}/example/points_update.expected', 'w').write(psue)
	open(f'{fn}/{b}/example/poi_view_update.facts', 'w').write(pvuf)