""" WeakValueDictionary

Implementa um mapeamento mutável cujos valores são referências fracas a objetos.

Quando um referente é destruído, a chave é removida.
"""

import weakref


class Queijo:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

    def __repr__(self) -> str:
        return f"Queijo({self.tipo})"


estoque: weakref.WeakValueDictionary = weakref.WeakValueDictionary()
catalogo = [Queijo("Brie"), Queijo("Parmesão"), Queijo("Mussarela")]

for q in catalogo:
    estoque[q.tipo] = q

del catalogo
# del q

for q in estoque.keys():
    print(q)

# Por que tem um queijo no estoque??
# R: porque a variável `q` é global.


# O que ocorreu acima, é o mesmo que
for blabla in range(100): ...

print("O valor de blabla é", blabla)
# Ou seja, a variável blabla é global.
del blabla


''' Limitações de referências fracas

Instâncias de list e dict não podem ser referentes.

Uma subclasse de qualquer uma delas pode.
'''