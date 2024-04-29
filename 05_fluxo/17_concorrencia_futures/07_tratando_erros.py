""" Tratamento de erros no download de bandeiras

A função futures.as_completed devolve um iterador que produz futures à medida que terminam
"""

import os
import pathlib
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from tqdm import tqdm


BASEURL = "http://flupy.org/data/flags"
PASTA_DOWNLOADS = pathlib.Path(__file__).parent / "downloads"
BANDEIRAS = "cn in br us jp ru mx ph fr de".split()

MAX_WORKERS = 2

# ======================================================


def limpe_pasta_downloads():
    for gif in os.listdir(PASTA_DOWNLOADS):
        os.remove(PASTA_DOWNLOADS / gif)


def salve_uma_bandeira(pais: str) -> None:
    try:
        img = requests.get(BASEURL + f"/{pais}/{pais}.gif")
        with open(PASTA_DOWNLOADS / (pais + ".gif"), "wb") as fp:
            fp.write(img.content)
    except requests.exceptions.HTTPError:
        print("Erro na requisição. Bandeira:", pais.upper())
    except requests.exceptions.ConnectionError:
        print("Erro na conexão. Bandeira:", pais.upper())


def salve_muitas(gil: bool = True):
    workers = min(MAX_WORKERS, len(BANDEIRAS))
    executor: ThreadPoolExecutor | ProcessPoolExecutor = ThreadPoolExecutor(workers)
    if not gil:
        executor = ProcessPoolExecutor()

    # Agendando downloads
    todo = {}
    for b in BANDEIRAS:
        f = executor.submit(salve_uma_bandeira, b)
        todo[f] = b

    # Recebendo os downloads
    for future in tqdm(
        as_completed(todo), total=len(BANDEIRAS), desc="Bandeiras", unit=" bandeira"
    ):
        try:
            future.result()
        except:
            print("Erro")
    print("\n\tFim.\n")


def main():
    salve_muitas()


if __name__ == "__main__":
    limpe_pasta_downloads()
    main()
