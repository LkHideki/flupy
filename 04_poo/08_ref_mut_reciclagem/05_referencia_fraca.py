''' Referência fraca

é uma referência, mas que não incrementa o contador de referências de um objeto (o referente).

Então, uma referência fraca não impede um objeto de ser destruído.

Exemplo de uso: cache.

'''
import weakref
import gc

a = {0, 1}

wr = weakref.ref(a)

print("a ->", a)

print("wr() ->", wr())

print("wr() is None ->", wr() is None)

print('Invocando o coletor...')
del a
gc.collect() # Invoca o coletor imediatamente

print("wr() is None ->", wr() is None)