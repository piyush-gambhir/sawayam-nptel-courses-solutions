from collections import deque


class Edge:
    def __init__(self, v, flow, C, rev):
        self.v = v
        self.flow = flow
        self.C = C
        self.rev = rev


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.level = [-1] * V

    def addEdge(self, u, v, C):
        a = Edge(v, 0, C, len(self.adj[v]))
        b = Edge(u, 0, 0, len(self.adj[u]))
        self.adj[u].append(a)
        self.adj[v].append(b)

    def BFS(self, s, t):
        self.level = [-1] * self.V
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for e in self.adj[u]:
                if self.level[e.v] < 0 and e.flow < e.C:
                    self.level[e.v] = self.level[u] + 1
                    q.append(e.v)
        return self.level[t] >= 0

    def sendFlow(self, u, flow, t, start):
        if u == t:
            return flow

        for i in range(start[u], len(self.adj[u])):
            start[u] = i
            e = self.adj[u][i]
            if self.level[e.v] == self.level[u] + 1 and e.flow < e.C:
                curr_flow = min(flow, e.C - e.flow)
                temp_flow = self.sendFlow(e.v, curr_flow, t, start)
                if temp_flow > 0:
                    e.flow += temp_flow
                    self.adj[e.v][e.rev].flow -= temp_flow
                    return temp_flow
        return 0

    def DinicMaxflow(self, s, t):
        if s == t:
            return -1

        total = 0
        while self.BFS(s, t):
            start = [0] * (self.V + 1)
            while True:
                flow = self.sendFlow(s, float('inf'), t, start)
                if flow == 0:
                    break
                total += flow
        return total


if __name__ == "__main__":
    n, m, t = map(int, input().split())
    maxf = Graph(n + 1)

    p = int(input())
    arr = list(map(int, input().split()))

    for i in arr:
        maxf.addEdge(0, i, 1)
        maxf.addEdge(i, 0, 1)

    for _ in range(m):
        u, v = map(int, input().split())
        maxf.addEdge(u, v, 1)
        maxf.addEdge(v, u, 1)

    print(maxf.DinicMaxflow(0, t))
