def tarjan(g):
    times = dict()  # times of discovery in dfs
    low_succ = dict()  
    # low_succ[v] is the lowest time of an in-tree
    # successor of v, followed by at most one out-tree edge 
    bridges = set()
    def dfs(v, pred, t):
        times[v] = low_succ[v] = t
        for w in g[v]:
            if w not in times:
                t = dfs(w, v, t+1)
                low_succ[v] = min(low_succ[v], low_succ[w])
            elif pred != w:
                low_succ[v] = min(low_succ[v], times[w])
        if low_succ[v] == times[v] and pred is not None:
            bridges.add((pred, v))
        return t
    dfs(0, None, 0)
    return bridges
