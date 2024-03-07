from array import array
from os import path
from random import random

with open("arquivo_numeros", "wb") as arq:
    my_array = array("d", [random() for _ in range(1_000_000 - 1)])
    my_array.insert(1, 19)
    my_array.tofile(arq)

if path.exists("arquivo_numeros"):
    with open("arquivo_numeros", "rb") as arq:
        arr = array("d")
        arr.fromfile(arq, int(1e6))
        print(*arr[:10], sep="\n")

    print(*array("d", map(lambda m: round(10 * m, 2), arr[:10])))
