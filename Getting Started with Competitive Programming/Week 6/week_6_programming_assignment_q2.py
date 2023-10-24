import heapq


def min_irrigation_time(n, s, edges_info):
    # Construct the graph from edges_info
    graph = {i: [] for i in range(n)}
    for i, info in enumerate(edges_info):
        m = info[0]
        for j in range(1, 2 * m + 1, 2):
            dest, weight = info[j], info[j + 1]
            graph[i].append((dest, weight))

    # Dijkstra's algorithm
    dist = [float('inf')] * n
    dist[s] = 0
    pq = [(0, s)]  # (distance, node)

    while pq:
        curr_dist, node = heapq.heappop(pq)
        if curr_dist > dist[node]:  # Ignore outdated distance info
            continue

        for neighbor, weight in graph[node]:
            if curr_dist + weight < dist[neighbor]:
                dist[neighbor] = curr_dist + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))

    # If any distance is still infinite, return -1
    if any(d == float('inf') for d in dist):
        return -1
    return max(dist)


# To use:
n, s = map(int, input().split())
edges_info = [list(map(int, input().split())) for _ in range(n)]
print(min_irrigation_time(n, s, edges_info), end="")
