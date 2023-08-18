def solve(string):
    count = 0
    for i in range(len(string)):
        if string[i] == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True


string = "()((()))()"
res = solve(string)
print(res)
