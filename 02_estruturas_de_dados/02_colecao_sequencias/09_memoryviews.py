""" Memoryview

memoryview() é uma classe nativa que permite manipular fatias de iteraveis
sem criar cópias.
"""

from array import array

arr = array("i", [78, 79, 80, 81])
memv = memoryview(arr)

fatia = memv[1:-1]

fatia[1] = 1000

print(arr)


# outro exemplo (fora do livro)
# Como "editar" uma string (obj imutável)
nome = bytearray("lucas", 'utf-8') # Na verdade estamos mexendo num bytearray
print("nome antes :", nome)

mv = memoryview(nome)
mv[2] = ord("C") # e editando o próprio
print("nome depois:", nome)