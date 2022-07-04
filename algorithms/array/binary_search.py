def binary_search(l : list, e : int):
    i, j = 0, len(l) - 1
    while i <= j:
        m = (i + j) // 2
        if l[m] == e:
            return True
        elif l[m] > e:
            j = m - 1
        else:
            i = m + 1
    return False
