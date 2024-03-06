textos_larguras_fixas = """
0.......8..11
Alice   SP São Paulo
Bob     MG Belo Horizonte
Charlie BA Salvador
David   AM Manaus
Eve     SP Votorantim
Frank   RJ Rio de Janeiro
Grace   RJ Niterói
Henry   RJ Petrópolis
"""

NOME = slice(0, 8)
ESTADO = slice(8, 11)
CIDADE = slice(11, None)

for entrada in textos_larguras_fixas.strip().splitlines()[1:]:
    print(entrada[CIDADE], entrada[NOME], entrada[ESTADO])
