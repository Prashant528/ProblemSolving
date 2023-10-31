def print_state(state):
    '''
    Utility: Prints the state in the format of puzzle. Easier to visualize.
    '''
    print('\n---------------------')

    for i in range(len(state)):
        print('| ', state[i], ' |', end = '' )
        if i == 2 or i == 5 or i==8:
            print('\n---------------------')

def move_left(state):
    '''
    Utility: Swaps a tile with the empty tile on the left.
    '''
    new_state = state[:]
    index_of_0 = new_state.index(0)
    if index_of_0 != 2 and index_of_0 != 5 and index_of_0 != 8:
        #swap
        temp = new_state[index_of_0]
        new_state[index_of_0] = new_state[index_of_0+1]
        new_state[index_of_0+1] = temp
    return new_state

def move_right(state):
    '''
    Utility: Swaps a tile with the empty tile on the right.
    '''
    new_state = state[:]
    index_of_0 = new_state.index(0)
    if index_of_0 != 0 and index_of_0 != 3 and index_of_0 != 6:
        #swap
        temp = new_state[index_of_0]
        new_state[index_of_0] = new_state[index_of_0-1]
        new_state[index_of_0-1] = temp
    return new_state

def move_up(state):
    '''
    Utility: Swaps a tile with the empty tile on the right.
    '''
    new_state = state[:]
    index_of_0 = new_state.index(0)
    if index_of_0 != 0 and index_of_0 != 1 and index_of_0 != 2:
        #swap
        temp = new_state[index_of_0]
        new_state[index_of_0] = new_state[index_of_0-3]
        new_state[index_of_0-3] = temp
    return new_state

def move_down(state):
    '''
    Utility: Swaps a tile with the empty tile on the right.
    '''
    new_state = state[:]
    index_of_0 = new_state.index(0)
    if index_of_0 != 6 and index_of_0 != 7 and index_of_0 != 8:
        #swap
        temp = new_state[index_of_0]
        new_state[index_of_0] = new_state[index_of_0+3]
        new_state[index_of_0+3] = temp
    return new_state

def ShortestPath_helper(goal_state, initial_states):
    # hashed_initial_state = hash_initial_states(initial_states)
    #a map to store the solutions for each initial states, initialize the move_counts to infinity.
    #It is made just to preserve the order of the initial_states while returning the solution.
    solution_map = []
    initial_states = [initial_states]
    for state in initial_states:
        solution_map.append([state, float('inf')])
    #initialize the queue, implemented here with a list
    queue = [[goal_state, 0]]
    #initialize the list to hold visited states
    visited_states = []
    #loop until we've reached all initial_states
    while(len(initial_states)>0):
        # print("Queue = ", queue)
        #dequeue the first element
        new_goal, move_count = queue[0]
        queue = queue[1:]
        #check if the new_goal is in the initial states or not.
        if new_goal in initial_states:
            #if the state has been found, find the state in solution map and update the count of moves.
            for state in solution_map:
                # print("Initial state found: ", new_goal)
                if state[0]==new_goal:
                    state[1] = move_count
            #remove it from the list of initial states since it has been found
            initial_states.remove(new_goal)
            # print("new initial states = ", initial_states)
        else:
            #add the goal state to the list of visited states
            visited_states.append(new_goal)
            # print("Visited states = ", visited_states)
            #generate all new states
            new_states = []
            new_states.append(move_left(new_goal))
            new_states.append(move_right(new_goal))
            new_states.append(move_up(new_goal))
            new_states.append(move_down(new_goal))
            # print(new_states)
            #enqueue the new states generated
            for new_state in new_states:
                if new_state not in visited_states:
                    queue.append([new_state, move_count+1])
    
    return solution_map[0][1]

def ShortestPath(goal, states):
    shortest_paths = []
    for state in states:
        shortest_paths.append(ShortestPath_helper(goal, state))
    return shortest_paths


initial_states = [[1,2,3,4,5,6,8,7,0], [1,2,3,8,0,4,7,6,5]]
goal_state = [1,2,3,8,0,4,7,6,5]
print(ShortestPath(goal_state, initial_states))
#Solution : [8,1]
