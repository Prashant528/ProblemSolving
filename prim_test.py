import heapq

def MST_Prim(graph):
    # Initialize variables to keep track of the minimum spanning tree
    min_spanning_tree = set()
    total_weight = 0

    # Create a list to store vertices in the minimum spanning tree
    vertices_in_tree = set()

    # Choose an arbitrary starting vertex (0 in this case)
    start_vertex = graph[0][0]
    vertices_in_tree.add(start_vertex)

    # Create a priority queue (min-heap) to store edges
    edge_heap = [(weight, start_vertex, vertex) for (start_vertex, vertex, weight) in graph]
    heapq.heapify(edge_heap)

    # Continue until all vertices are included in the tree
    while len(vertices_in_tree) < len(graph):
        # Check if the edge_heap is empty
        if not edge_heap:
            break

        # Get the edge with the smallest weight that connects a vertex in the tree
        # to a vertex outside the tree
        weight, from_vertex, to_vertex = heapq.heappop(edge_heap)

        # If both vertices are already in the tree, skip this edge
        if from_vertex in vertices_in_tree and to_vertex in vertices_in_tree:
            continue

        # Add the edge to the minimum spanning tree
        min_spanning_tree.add((from_vertex, to_vertex, weight))
        total_weight += weight

        # Add the newly connected vertex to the set of vertices in the tree
        if from_vertex in vertices_in_tree:
            vertices_in_tree.add(to_vertex)
        else:
            vertices_in_tree.add(from_vertex)

    new_edge_list = []
    for edges in min_spanning_tree:
        (node1, node2) = edges[0], edges[1]
        new_edge_list.append((node1, node2))
    return total_weight, new_edge_list

edges1 = [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]
# print(extract_vertices(edges1))
print(MST_Prim(edges1))
edges2 = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
# print(extract_vertices(edges2))
print(MST_Prim(edges2))
edges3 = [(1,2,9),(1,3,4),(2,5,8), (5,4,5), (4,3,2), (3,6,7), (6,7,3), (7,5,6), (5,9,11), (9,7,12), (7,8,16), (6,8,14)]
print(MST_Prim(edges3))
