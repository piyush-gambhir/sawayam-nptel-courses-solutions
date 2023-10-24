from collections import deque


class EdmondsKarp:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}
        self.parent = {}

    def add_edge(self, u, v, capacity):
        self.graph.setdefault(u, {})[v] = capacity
        self.graph.setdefault(v, {})[u] = 0

    def bfs(self, source, sink):
        self.parent = {node: None for node in self.graph.keys()}
        self.parent[source] = source

        queue = deque([(source, float('inf'))])

        while queue:
            current, bottleneck = queue.popleft()
            if current == sink:
                return bottleneck

            for neighbor, capacity in self.graph[current].items():
                if self.parent[neighbor] is None and capacity > 0:
                    new_bottleneck = min(bottleneck, capacity)
                    self.parent[neighbor] = current

                    if neighbor == sink:
                        return new_bottleneck

                    queue.append((neighbor, new_bottleneck))

        return 0

    def max_flow(self, source, sink):
        max_flow_value = 0

        while True:
            bottleneck = self.bfs(source, sink)
            if bottleneck == 0:
                break

            max_flow_value += bottleneck

            current = sink
            while current != source:
                previous = self.parent[current]
                self.graph[previous][current] -= bottleneck
                self.graph[current][previous] += bottleneck
                current = previous

        return max_flow_value


if __name__ == "__main__":
    E = int(input().strip())
    ek = EdmondsKarp(15)

    for _ in range(E):
        u, v, w = input().strip().split()
        w = int(w)
        ek.add_edge(u, v, w)

    print(ek.max_flow("S", "T"), end="")
