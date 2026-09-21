def validPath(n,edges, source, destination):
    if not edges:
        return True
    if source == destination:
        return True
    D=defaultdict(list)
    for u,v in edges:
        D[u].append(v)
        D[v].append(u)
    seen=set()
    seen.add(source)
    stk=[source]
    while stk:
        node=stk.pop()
        for neigh_node in D[node]:
            if neigh_node not in seen:
                seen.add(neigh_node)
                stk.append(neigh_node)
                if neigh_node == destination:
                    return True
    return False