""" Memoryview

memoryview(•) é uma função nativa que permite manipular fatias de iteraveis
sem criar cópias.
"""

from array import array

arr = array("i", [78, 79, 80, 81])

memv = memoryview(arr)

k = memv[1:-1]

k[1] = 1000

print(arr)