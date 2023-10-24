from collections import deque

INF = 1e9


class EdmondsKarp:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
        self.parent = [-1] * vertices

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity

    def bfs(self, source, sink):
        self.parent = [-1] * self.V
        queue = deque([(source, INF)])

        while queue:
            u, flow = queue.popleft()
            if u == sink:
                return flow

            for v, capacity in enumerate(self.graph[u]):
                if self.parent[v] == -1 and capacity > 0:
                    new_flow = min(flow, capacity)
                    self.parent[v] = u
                    if v == sink:
                        return new_flow
                    queue.append((v, new_flow))

        return 0

    def max_flow(self, source, sink):
        max_flow_value = 0

        while True:
            flow = self.bfs(source, sink)
            if flow == 0:
                break

            max_flow_value += flow
            v = sink

            while v != source:
                u = self.parent[v]
                self.graph[u][v] -= flow
                self.graph[v][u] += flow
                v = u

        return max_flow_value


# Input and execution
if __name__ == "__main__":
    n, m = map(int, input().split())
    ek = EdmondsKarp(n)

    for _ in range(m):
        u, v, w = map(int, input().split())
        ek.add_edge(u, v, w)

    source = 0
    sink = n - 1
    print(ek.max_flow(source, sink), end="")
