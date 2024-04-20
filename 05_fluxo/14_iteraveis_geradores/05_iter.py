class Bla:
    def __getitem__(self, index: int):
        return index

x = Bla()
try:
    print(iter(x))
except TypeError:
    print('O objeto não é iterável')