#!/opt/homebrew/bin/pypy3
from time import time as pc
from random import sample

t0 = pc()

n_agulhas = 500
n_palhas = int(100e6)

# agulhas = [randint(1, n_palhas + n_agulhas) for _ in range(n_agulhas)]
agulhas = set(sample(range(1, n_agulhas + n_palhas+1), n_agulhas))
# palheiro_com_agulhas = dict.fromkeys(range(n_palhas + n_agulhas), 0)
# for i in agulhas:
#     palheiro_com_agulhas[i] = 1
palheiro_com_agulhas = set(range(1, n_agulhas + n_palhas+1))
len(palheiro_com_agulhas)

found = 0
for n in palheiro_com_agulhas:
    if n in agulhas:
        found += 1

print(f"tempo: {pc()-t0:.2f}s\n{found}")