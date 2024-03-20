""" Instalar o bobo via `pip install bobo`

Para rodar o mini servidor, execute
`$ bobo -f 04_obtendo_informacoes.py`

se 04_obtendo_informacoes.py for o nome deste arquivo.
"""

import bobo
from inspect import signature

@bobo.query("/")
def hello(person):
    return f"Hello, {person}!"

if __name__ == "__main__":
    # Não vou comentar a discussão sobre os dunder defaults e code.
    print(signature(print))