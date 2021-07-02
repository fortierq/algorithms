from collections import defaultdict


def min2(L):  # returns the second minimum in L
    losers = defaultdict(list)  # losers[n]: list of elements that lost vs n
    while len(L) > 1:
        L_ = []
        for i in range(0, len(L), 2):
            if i < len(L) - 1:
                m, M = (L[i], L[i+1]) if L[i] <= L[i+1] else (L[i+1], L[i])
                L_.append(m)
                losers[m].append(M)
        L = L_  # remaining winners
    return min(losers[L[0]])


assert min2([4, 1, 2, 3]) == 2
assert min2([7, 314]) == 314
assert min2([-4, 0, 77, 42]) == 0
