def tarjan(g):
    times = dict()  # times of discovery in dfs
    low_succ = dict()  
    # low_succ[v] is the lowest time of an in-tree
    # successor of v, followed by at most one out-tree edge 
    bridges = set()
    t = 0
    def dfs(v, pred):
        nonlocal t
        times[v] = low_succ[v] = t
        t += 1
        for w in g[v]:
            if w not in times:
                dfs(w, v)
                low_succ[v] = min(low_succ[v], low_succ[w])
            elif pred != w:
                low_succ[v] = min(low_succ[v], times[w])
        if low_succ[v] == times[v] and pred is not None:
            bridges.add((pred, v))
    dfs(0, None)
    return bridges

print(tarjan({
        0: {1, 2}, 
        1: {0, 3, 4}, 
        2: {5, 0}, 
        3: {0, 1}, 
        4: {1}, 
        5: {2, 6},
        6: {2}
    }))