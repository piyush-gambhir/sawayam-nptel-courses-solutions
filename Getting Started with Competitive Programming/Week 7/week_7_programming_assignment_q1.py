import heapq

def prim_algorithm(edges, is_visited, start_vertex):
    total_cost = 0
    priority_queue = []
    
    for edge in edges[start_vertex]:
        heapq.heappush(priority_queue, (edge[1], start_vertex, edge[0]))
    
    while priority_queue:
        weight, vertex_u, vertex_v = heapq.heappop(priority_queue)
        
        if not is_visited[vertex_u] or not is_visited[vertex_v]:
            if not is_visited[vertex_u]:
                for edge in edges[vertex_u]:
                    heapq.heappush(priority_queue, (edge[1], vertex_u, edge[0]))
            is_visited[vertex_u] = True
            
            if not is_visited[vertex_v]:
                for edge in edges[vertex_v]:
                    heapq.heappush(priority_queue, (edge[1], vertex_v, edge[0]))
            is_visited[vertex_v] = True
            
            total_cost += weight
    return total_cost

if __name__ == '__main__':
    num_vertices, num_edges = map(int, input().split())
    edges = [[] for _ in range(num_vertices)]
    
    for _ in range(num_edges):
        vertex_u, vertex_v, weight = map(int, input().split())
        edges[vertex_u].append([vertex_v, weight])
        edges[vertex_v].append([vertex_u, weight])
    
    is_visited = [False] * num_vertices
    max_cost = float('-inf')
    
    for i in range(num_vertices):
        if not is_visited[i]:
            max_cost = max(max_cost, prim_algorithm(edges, is_visited, i))
    
    print(max_cost, end="")
