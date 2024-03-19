""" Instalar o bobo via `pip install bobo`

Para rodar o mini servidor, execute
`$ bobo -f 04_obtendo_informacoes.py`

se 04_obtendo_informacoes.py for o nome deste arquivo.
"""

import bobo


@bobo.query("/")
def hello(person):
    return f"Hello, {person}!"
