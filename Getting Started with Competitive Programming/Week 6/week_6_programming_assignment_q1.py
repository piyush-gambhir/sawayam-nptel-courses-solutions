import heapq


def smallest_sequence(n, edges):
    graph = {i: [] for i in range(1, n + 1)}

    # Construct the graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Sort adjacency lists for deterministic behavior in case of multiple edges
    for key in graph:
        graph[key].sort()

    visited = set()
    sequence = []
    pq = [1]  # start from node 1

    while pq:
        node = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            sequence.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, neighbor)

    return sequence


# To use:
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(' '.join(map(str, smallest_sequence(n, edges))), end='')
