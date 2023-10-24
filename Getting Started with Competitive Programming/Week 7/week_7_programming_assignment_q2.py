from heapq import heappop, heappush


def prim_algorithm(edges, is_visited, start_vertex, multiplier):
    total_cost = 0
    priority_queue = []

    for edge in edges[start_vertex]:
        heappush(priority_queue, (edge[1], start_vertex, edge[0]))

    while priority_queue:
        weight, vertex_u, vertex_v = heappop(priority_queue)

        if not is_visited[vertex_u] or not is_visited[vertex_v]:
            if not is_visited[vertex_u]:
                for edge in edges[vertex_u]:
                    heappush(priority_queue, (edge[1], vertex_u, edge[0]))
            is_visited[vertex_u] = True

            if not is_visited[vertex_v]:
                for edge in edges[vertex_v]:
                    heappush(priority_queue, (edge[1], vertex_v, edge[0]))
            is_visited[vertex_v] = True

            total_cost += weight

    return 2 * multiplier * total_cost


if __name__ == '__main__':
    num_vertices, num_edges, multiplier = map(int, input().split())
    edges = [[] for _ in range(num_vertices + 1)]

    for _ in range(num_edges):
        vertex_u, vertex_v, weight = map(int, input().split())
        edges[vertex_u].append([vertex_v, weight])
        edges[vertex_v].append([vertex_u, weight])

    is_visited = [False] * (num_vertices + 1)

    max_cost = prim_algorithm(edges, is_visited, 1, multiplier)

    print(max_cost, end="")
