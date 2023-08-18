mass = [5, 2, 4, 6, 1, 3]
n = len(mass)
for i in range(1, n):
    j = i - 1
    change = mass[i]
    while change < mass[j]:
        mass[j + 1] = mass[j]
        j -= 1
        if j < 0:
            break
    mass[j + 1] = change
print(mass)
