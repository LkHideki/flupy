from concurrent.futures import ProcessPoolExecutor
from random import random
from time import sleep


def funcao_bla(x):
    sleep(random() * 2)
    print(x)
    return x


def main():
    with ProcessPoolExecutor() as executor:
        res = executor.map(funcao_bla, range(1, 21))

    for n in res:
        print(n, end=", ")


if __name__ == "__main__":
    main()
