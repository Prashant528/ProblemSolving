from collections import defaultdict, deque

class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph
        self.residual_graph = defaultdict(dict)
        
    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        # Initialize reverse edge with 0 capacity
        self.graph[v][u] = 0
        self.residual_graph[u][v] = capacity
        self.residual_graph[v][u] = 0

    def ford_fulkerson_dfs(self, source, sink):
        max_flow = 0

        while True:
            result = self.find_augmenting_path_dfs(source, sink)
            
            if result is None:
                break

            path, bottleneck = result
            max_flow += bottleneck

            # Update residual graph
            for u, v in zip(path, path[1:]):
                self.residual_graph[u][v] -= bottleneck
                self.residual_graph[v][u] += bottleneck

        flow_assignment = []
        for u in self.graph:
            for v, capacity in self.graph[u].items():
                if capacity - self.residual_graph[u][v] > 0:
                    flow_assignment.append((u, v, capacity - self.residual_graph[u][v]))

        return max_flow, flow_assignment

    def find_augmenting_path_dfs(self, source, sink):
        visited = set()
        stack = [(source, [source])]
        
        while stack:
            u, path = stack.pop()
            
            if u == sink:
                bottleneck = min(self.residual_graph[path[i]][path[i+1]] for i in range(len(path)-1))
                return path, bottleneck

            visited.add(u)
            
            for v, capacity in self.residual_graph[u].items():
                if v not in visited and capacity > 0:
                    stack.append((v, path + [v]))

        return None
    
    def ford_fulkerson_bfs(self, source, sink):
        max_flow = 0

        while True:
            result = self.find_augmenting_path_bfs(source, sink)
            
            if result is None:
                break

            path, bottleneck = result
            max_flow += bottleneck

            # Update residual graph
            for u, v in zip(path, path[1:]):
                self.residual_graph[u][v] -= bottleneck
                self.residual_graph[v][u] += bottleneck

        flow_assignment = []
        for u in self.graph:
            for v, capacity in self.graph[u].items():
                if capacity - self.residual_graph[u][v] > 0:
                    flow_assignment.append((u, v, capacity - self.residual_graph[u][v]))

        return max_flow, flow_assignment
    
    def find_augmenting_path_bfs(self, source, sink):
        visited = set()
        queue = deque([(source, [source])])

        while queue:
            u, path = queue.popleft()

            if u == sink:
                bottleneck = min(self.residual_graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
                return path, bottleneck

            visited.add(u)

            for v, capacity in self.residual_graph[u].items():
                if v not in visited and capacity > 0:
                    queue.append((v, path + [v]))

        return None

def create_graph(edges):
    nodes = set()
    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
    graph = {}
    for node in nodes:
        graph[node] = {}
    return graph

def Max_Flow_Fat(inp):
    src = inp[0]
    dst = inp[1]
    edges = inp[2]
    graph = create_graph(edges)
    ff = FordFulkerson(graph)

    for edge in edges:
        ff.add_edge(*edge)

    max_flow, flow_assignment = ff.ford_fulkerson_dfs(src, dst)
    # print("Maximum Flow:", max_flow)
    # print("Flow Assignment:", flow_assignment)
    return (max_flow, flow_assignment)

def Max_Flow_Short(inp):
    src = inp[0]
    dst = inp[1]
    edges = inp[2]
    graph = create_graph(edges)
    ff = FordFulkerson(graph)

    for edge in edges:
        ff.add_edge(*edge)

    max_flow, flow_assignment = ff.ford_fulkerson_bfs(src, dst)
    # print("Maximum Flow:", max_flow)
    # print("Flow Assignment:", flow_assignment)
    return (max_flow, flow_assignment)


#sample tests
inp = (0, 3, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
print(Max_Flow_Fat(inp))
print(Max_Flow_Short(inp))

inp = (0, 4,  [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)])
print(Max_Flow_Fat(inp))
print(Max_Flow_Short(inp))

inp = (0, 5, [(0, 1, 16), (0, 2, 13), (1, 3, 12), (2, 1, 4), (2, 4, 14), (3, 2, 9), (3, 5, 20), (4, 3, 7), (4, 5, 4)])
print(Max_Flow_Fat(inp))
print(Max_Flow_Short(inp))
