def solve(tree, start):
    print(start)
    for el in tree[start]:
        if el is not None:
            solve(tree, el)


tree = {
    1: [2, 7],
    2: [3, 4],
    3: [None, None],
    4: [5, None],
    5: [None, None],
    6: [None, None],
    7: [None, 9],
    8: [None, None],
    9: [None, None],
}
start = 1
res = solve(tree, start)
