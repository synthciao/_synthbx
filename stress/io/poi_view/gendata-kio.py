import os
from random import shuffle, choice

b = 'poi_view'

sizes = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 25000, 50000]

start = 2000

poiid1 = list(range(1, 1000))
poiid2 = list(range(1, 1000, 2))

cola = list(range(100, 250))
colb = list(range(250, 500))
colc = list(range(500, 600))

cold = ['d' + str(x) for x in list(range(100, 400))]
cole = ['e' + str(x) for x in list(range(100, 400))]
colf = ['f' + str(x) for x in list(range(100, 400))]


poi_facts = open(f'base/{b}/example/poi.facts', 'r').read().rstrip()
poi_update_expected = open(f'base/{b}/example/poi_update.expected', 'r').read().rstrip()
points_facts = open(f'base/{b}/example/points.facts', 'r').read().rstrip()
points_upadte_expected = open(f'base/{b}/example/points_update.expected', 'r').read().rstrip()

for s in sizes:
    fn = f'io{s}'
    os.system(f'mkdir -p {fn}/{b}/example')
    os.system(f'cp -r base/{b}/schema {fn}/{b}')
    os.system(f'cp -r base/{b}/gcandidate {fn}/{b}')
    os.system(f'cp base/{b}/example/poi_view_update.facts {fn}/{b}/example')
    
    l = start
    m = start + s//2
    h = start + s
    
    pf = poi_facts
    pue = poi_update_expected
    psf = points_facts
    psue = points_upadte_expected
    
    for i in range(l, m):
        t = f'\n{i}\t{choice(cola)}\t{choice(colb)}\t{choice(colc)}'
        pf += t
        pue += t
    pf += '\n'
    pue += '\n'
    open(f'{fn}/{b}/example/poi.facts', 'w').write(pf)
    open(f'{fn}/{b}/example/poi_update.expected', 'w').write(pue)
        
    for i in range(m, h):
        t = f'\n{i}\t{choice(cold)}\t{choice(cole)}\t{choice(colf)}'
        psf += t
        psue += t
    psf += '\n'
    psue += '\n'
    open(f'{fn}/{b}/example/points.facts', 'w').write(psf)
    open(f'{fn}/{b}/example/points_update.expected', 'w').write(psue)