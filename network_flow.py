def check_source_edges_full(src, edges):
    for edge in edges:
        if edge[0] == src:
            pass

def get_all_nodes_from_edges(edges):
    '''
    Gets the unique nodes in the graph
    '''
    nodes = set()
    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
    return nodes

def find_max_fat_path(src, dst, edges):
    '''
    DFS to find the path with maximum flow
    The edges should be already filtered for non-full egdes and non-zero residual edges.
    '''
    visited_nodes = []
    stack = []
    stack.append(src)
    all_nodes = get_all_nodes_from_edges(edges)
    paths = []
    while set(visited_nodes)!=all_nodes:
        curr_node = stack.pop()
        total_flow = float('inf')

        for edge in edges:
            #find the children of curr_node and append them to stack if they don't have full flow
            if edge[0]==curr_node:
                stack.append(edge[1])
                #finding minimum of remaining_Flow
                total_flow = min(total_flow, edge[2]-edge[3])
        visited_nodes.append(curr_node)
        #check if the current node is destination or not. If yes, restart the search
        if curr_node==dst:
            paths.append([visited_nodes, total_flow])
            visited_nodes = []
            stack = []
            stack.append(src)


def Max_Flow_Fat(inp):
    src = inp[0]
    dst = inp[1]
    edges = inp[2]
    graph_with_flow = []
    residual_graph = []
    #Adding extra element on edges to keep track of used flow
    for edge in edges:
        #convert it to list for convenience
        edge = list(edge)
        edge.append(0)
        graph_with_flow.append(edge)
        residual_graph.append([edge[1], edge[0], edge[2], edge[3]])
    print(graph_with_flow)
    print(residual_graph)

    # set_of_input_edges = set(edges)
    # visited_edges = set()
    # source_edges_full = check_source_edges_full(src, edges)

    #need to change the condition to: while dfs stops finding new paths to the sink 
    # while (visited_edges!=set_of_input_edges) or (source_edges_full==False):








Max_Flow_Fat((0, 3, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))