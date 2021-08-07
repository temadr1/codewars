def anagrams(word, words):
    a = dict()
    a_check = dict()
    res = []
    for i in word:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    for i in words:
        for j in i:
            if j not in a_check:
                a_check[j] = 1
            else:
                a_check[j] += 1
        if a_check == a:
            res.append(i)
        a_check = dict()
    return res
