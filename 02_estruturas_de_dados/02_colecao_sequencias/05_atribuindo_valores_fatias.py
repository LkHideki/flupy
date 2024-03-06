l = list(range(1,16))
print(l)

l[3:-3] = [0]
print(l)

del l[-2:]
print(l)

del l[:-1:2]
print(l)