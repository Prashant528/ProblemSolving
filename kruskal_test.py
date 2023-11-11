def MST_Kruskal(graph):
    # Initialize variables to keep track of the minimum spanning tree
    min_spanning_tree = set()
    total_weight = 0

    # Create a dictionary to represent disjoint sets (connected components)
    disjoint_sets = {vertex: {vertex} for edge in graph for vertex in edge[:2]}

    # Sort the edges of the graph in non-decreasing order of weight
    sorted_edges = sorted(graph, key=lambda edge: edge[2])

    # Iterate through the sorted edges and add them to the minimum spanning tree
    for edge in sorted_edges:
        vertex1, vertex2, weight = edge

        # Check if adding this edge creates a cycle in the minimum spanning tree
        if vertex1 in disjoint_sets and vertex2 in disjoint_sets and disjoint_sets[vertex1] != disjoint_sets[vertex2]:
            min_spanning_tree.add(edge)
            total_weight += weight

            # Merge the disjoint sets (connected components) of the two vertices
            set1, set2 = disjoint_sets[vertex1], disjoint_sets[vertex2]
            set1.update(set2)

            # Update the references to the merged set in the dictionary
            for vertex in set2:
                disjoint_sets[vertex] = set1
    
        new_edge_list = []

    new_edge_list = []
    for edges in min_spanning_tree:
        (node1, node2) = edges[0], edges[1]
        new_edge_list.append((node1, node2))

    return total_weight, new_edge_list


edges1 = [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]
print(MST_Kruskal(edges1))
edges2 = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
print(MST_Kruskal(edges2))
edges3 = [(1,2,9),(1,3,4),(2,5,8), (5,4,5), (4,3,2), (3,6,7), (6,7,3), (7,5,6), (5,9,11), (9,7,12), (7,8,16), (6,8,14)]
print(MST_Kruskal(edges3))