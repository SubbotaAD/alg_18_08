mass = [4, 9, 7, 6, 2, 3]
n = len(mass)
for i in range(n - 1):
    index = i
    for j in range(i + 1, n):
        if mass[j] < mass[index]:
            index = j
    mass[i], mass[index] = mass[index], mass[i]
print(mass)
