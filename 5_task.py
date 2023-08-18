def solve(tree, queue):
    for el in tree[queue[0]]:
        if el is not None:
            queue.append(el)
    print(queue[0])

    queue.pop(0)
    if len(queue) == 0:
        return

    solve(tree, queue)


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
queue = [start]
res = solve(tree, queue)
