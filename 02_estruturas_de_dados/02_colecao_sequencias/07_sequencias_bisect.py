# ref: https://code.activestate.com/recipes/577197-sortedcollection/
import bisect

frutas = [
    "manzana",
    "plátano",
    "naranja",
    "limón",
    "sandía",
    "uva",
    "pera",
    "mango",
    "piña",
    "fresa",
    "cereza",
    "melón",
]

frutas.sort()

x = bisect.bisect(frutas, "naranja")

for i,e in enumerate(frutas): print(i,e)

print(x)

bisect.insort(frutas, "naranja")

for i,e in enumerate(frutas): print(i,e)