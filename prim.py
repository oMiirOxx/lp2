def prim(graph):
    mst = []
    visited = set()
    start_vertex = next(iter(graph))
    visited.add(start_vertex)
    edges = [(cost, start_vertex, to) for to, cost in graph[start_vertex].items()]

    while edges:
        cost, frm, to = min(edges)
        edges.remove((cost, frm, to))
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for to_next, cost_next in graph[to].items():
                if to_next not in visited:
                    edges.append((cost_next, to, to_next))

    return mst
graph = {'A': {'B': 2, 'C': 3}, 'B': {'A': 2, 'C': 4}, 'C': {'A': 3, 'B': 4}}
print(prim(graph))
