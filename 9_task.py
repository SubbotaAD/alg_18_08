def gen(n):
    if n == 1:
        return [[1]]
    else:
        cur = gen(n - 1)
        res = []
        for el_cur in cur:
            for i in range(len(el_cur) + 1):
                new_el = el_cur.copy()
                new_el.insert(i, n)
                res.append(new_el)
        return res


n = 3
res = gen(n)
for el in res:
    print(*el)
