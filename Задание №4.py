# Задание №4
n = int(input("Введите n: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()

