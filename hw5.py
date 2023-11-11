import heapq as hq

def extract_vertices(edges):
    '''
    Utility: Extracts all the unique vertices from the list of edges.
    ''' 
    vertices = []
    for edge in edges:
        if edge[0] not in vertices:
            vertices.append(edge[0])
        if edge[1] not in vertices:
            vertices.append(edge[1])
    return vertices

def find_adjacent_nodes(current_node, edges):
    '''
    Utility: Returns the list of adjacent nodes (with their weights) of current node. Format = (vertex, weight)
    '''
    adj_nodes = []
    for edge in edges:
        if(edge[0] == current_node):
            adj_nodes.append((edge[1], edge[2]))
        elif edge[1]==current_node:
            adj_nodes.append((edge[0], edge[2]))
    return adj_nodes

def check_if_visited(node, visited_edges):
    '''
    Utility: Checks if the node is present in visited edges or not. If present, returns the edge too.
    '''
    for edge in visited_edges:
        if(edge[0] == node or edge[1]==node):
            return edge, True
    return None, False

def cycle_formed(node1, node2, visited_edges):
    '''
    Utility: Checks if adding node1 and node2 to visited_edges create a cycle 
    '''
    for edge in visited_edges:
        if node1==edge[0] and node2==edge[1]:
            return True
        elif node1==edge[1] and node2==edge[0]:
            return True
    return False


def MST_Prim(edges):
    '''
    Implementation of Prim's algorithm.
    '''
    vertices = extract_vertices(edges)
    inf = float('inf')
    visited_edges = []
    priority_q = []
    #initialize the priority queue as (weight, vertex)
    for idx in range(len(vertices)):
        #initialize the first vertex to 0, node.
        if idx == 0:
            priority_q.append((0,vertices[idx]))
        else:
            priority_q.append((inf,vertices[idx]))
    hq.heapify(priority_q)
    #repeat until the queue is empty
    while len(priority_q) != 0:
        current_node = hq.heappop(priority_q)
        adj_nodes = find_adjacent_nodes(current_node[1], edges)
        for adj_node in adj_nodes:
            if adj_node[0] != current_node[1]:
                visited_edge, present = check_if_visited(adj_node[0], visited_edges)
                if present:
                    #check if current weight is less than previous visited weight
                    if adj_node[1] < visited_edge[2] and not cycle_formed(current_node[1], adj_node[0], visited_edges):
                        #if yes, remove the older visited edge
                        visited_edges.remove(visited_edge)
                        #and add the new edge with new weight
                        visited_edges.append((current_node[1], adj_node[0], adj_node[1]))
                        #delete the priority queue entry for the adjacent node
                        for element in priority_q:
                            if element[0]==adj_node[1] and element[1] == adj_node[0]:
                                priority_q.remove(element)
                        #push in the priority queue in the format (weight, node)
                        hq.heappush(priority_q, (adj_node[1], adj_node[0]))
                elif not present:
                    #delete the priority queue entry for the adjacent node
                    for element in priority_q:
                        if element[1] == adj_node[0]:
                            priority_q.remove(element)
                    #push in the priority queue in the format (weight, node)
                    hq.heappush(priority_q, (adj_node[1], adj_node[0]))
                    visited_edges.append((current_node[1], adj_node[0], adj_node[1]))
    #formatting the output
    total_weight = 0
    new_edge_list = []
    for edges in visited_edges:
        (node1, node2) = edges[0], edges[1]
        new_edge_list.append((node1, node2))
        total_weight += edges[2]
    return total_weight, new_edge_list

def find_forest(node, forests):
    '''
    Utility: Checks for the forests of the node. Returns the index of forest if found. Else, returns None.
    '''
    for forest in forests:
        for edge in forest:
            if edge[0]==node or edge[1] ==node:
                return forests.index(forest)
    return None

def MST_Kruskal(edges):
    edges.sort(key = lambda i:i[2])
    forests = []

    for edge in edges:
        if edge[0]!=edge[1]:
            #get the indices of the forests
            node1_forest = find_forest(edge[0], forests)
            node2_forest = find_forest(edge[1], forests)
            if node1_forest==None and node2_forest==None:
                forests.append([edge])
            elif node1_forest==None and node2_forest!=None:
                forests[node2_forest].append(edge)
            elif node2_forest==None and node1_forest!=None:
                forests[node1_forest].append(edge)
            elif node1_forest!=None and node2_forest!=None and node1_forest!=node2_forest:
                #this is the case for both nodes lying in two different forests.
                joined_forest = forests[node1_forest] + forests[node2_forest] + [edge]
                #remove the individual forests
                forests.pop(max(node1_forest, node2_forest))
                forests.pop(min(node1_forest, node2_forest))
                #add the joined forest
                forests.append(joined_forest)
    #formatting the output
    final_forest = forests[0]
    total_weight = 0
    new_edge_list = []
    for edges in final_forest:
        (node1, node2) = edges[0], edges[1]
        new_edge_list.append((node1, node2))
        total_weight += edges[2]
    return total_weight, new_edge_list


edges1 = [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]
# print(extract_vertices(edges1))
print(MST_Prim(edges1))
edges2 = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
# print(extract_vertices(edges2))
print(MST_Prim(edges2))
edges3 = [(1,2,9),(1,3,4),(2,5,8), (5,4,5), (4,3,2), (3,6,7), (6,7,3), (7,5,6), (5,9,11), (9,7,12), (7,8,16), (6,8,14)]
print(MST_Prim(edges3))

edges1 = [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]
print(MST_Kruskal(edges1))
edges2 = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
print(MST_Kruskal(edges2))
edges3 = [(1,2,9),(1,3,4),(2,5,8), (5,4,5), (4,3,2), (3,6,7), (6,7,3), (7,5,6), (5,9,11), (9,7,12), (7,8,16), (6,8,14)]
print(MST_Kruskal(edges3))
