my_list = [[0] * 3 for _ in range(3)]

my_list[1][1] = 9
# print(my_list)


t = (1, 2, [3, 4])
print('Original:', t)
try:
    t[2] += t[2]
except Exception as e:
    print("Houve uma exceção:", e)

print(t)
print("Mesmo assim funcionou")