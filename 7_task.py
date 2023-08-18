n = 15
mass = [True] * n

for i in range(1, n):
    if mass[i] == True:
        k = i + 1
        for j in range(i + k, n, k):
            mass[j] = False
    else:
        continue


for i in range(n):
    if mass[i] == True:
        print(i + 1)
