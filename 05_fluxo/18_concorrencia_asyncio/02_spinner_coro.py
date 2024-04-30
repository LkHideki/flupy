""" Spinner, mas com coroutines

O código foi copiado de

https://github.com/fluentpython/example-code/blob/master/18-asyncio-py3.7/spinner_asyncio.py

com pequenas modificações.
"""

import asyncio
import itertools


async def spin(msg):
    ellipsis = itertools.cycle([".  ", ".  ", ".. ", ".. ", "...", "...", "..."])
    for char in itertools.cycle("|/-\\"):
        status = char + " " + msg + next(ellipsis)
        print(status, flush=True, end="\r")
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    print(" " * len(status), end="\r")


async def slow_function():
    await asyncio.sleep(3)
    return 42


async def supervisor():
    spinner = asyncio.create_task(spin("aguardando a resposta para tudo"))
    print("spinner object:", spinner)
    result = await slow_function()
    spinner.cancel()
    return result


def main():
    result = asyncio.run(supervisor())
    print("Answer:", result)


if __name__ == "__main__":
    main()
