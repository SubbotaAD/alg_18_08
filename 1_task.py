mass = [5, 1, 4, 2, 8]
n = len(mass)
i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if mass[j] > mass[j + 1]:
            mass[j], mass[j + 1] = mass[j + 1], mass[j]
        j += 1
    i += 1
print(mass)
