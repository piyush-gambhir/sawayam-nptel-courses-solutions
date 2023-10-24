def dfs(node, graph, visited):
    """Perform Depth First Search from a given node."""
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)


def find_classes(n, m, connections):
    # Initialize an empty graph
    graph = {i: [] for i in range(1, n+1)}

    # Populate the graph based on the given connections
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()  # to keep track of visited nodes
    count = 0  # to keep track of number of connected components

    # Iterate over each node in the graph
    for node in graph:
        if node not in visited:
            count += 1
            dfs(node, graph, visited)

    return count


def main():
    # Take input for n and m
    n, m = map(int, input().split())

    # Take input for connections
    connections = [tuple(map(int, input().split())) for _ in range(m)]

    # Find and print the number of classes
    print(find_classes(n, m, connections), end='')


main()
