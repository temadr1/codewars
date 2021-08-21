def josephus_survivor(n, k):
    n_l = []
    i = 0
    for i in range(1, n+1):
        n_l.append(i)
    while len(n_l) != 1:
        i += k-1
        while i >= len(n_l):
            i -= len(n_l)
        n_l.remove(n_l[i])
    return n_l[0]
