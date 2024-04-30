""" Implementando o exemplo do spinner
"""

import threading, itertools, time, sys


class Signal:
    go = True


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    ellipsis = itertools.cycle([".  ", ".  ", ".. ", ".. ", "...", "...", "..."])
    for char in itertools.cycle("|/-\\"):
        status = char + " " + msg + next(ellipsis)
        write(status)
        flush()

        # o caractere \x08 de backspace move o cursor para trás
        write("\x08" * len(status))

        time.sleep(0.1)
        if not signal.go:
            break
    write(" " * len(status) + "\x08" * len(status))


def slow_function():
    time.sleep(3)
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=("thinking", signal))
    spinner.start()
    result = slow_function()
    print("spinner object:", spinner)
    signal.go = False
    spinner.join()
    return result


def main():
    result = supervisor()
    print("Answer:", result)


if __name__ == "__main__":
    main()
