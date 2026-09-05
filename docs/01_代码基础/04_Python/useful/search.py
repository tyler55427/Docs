class Queue:
    def __init__(self, search_function):
        self.search_function = search_function
        self.elements = []
        
    def push(self, item, priority=0):
        if self.search_function == 'dfs':
            self.elements.append(item)
        elif self.search_function == 'bfs':
            self.elements.append(item)
        elif self.search_function == 'ucs':
            self.elements.append((priority, item))
            self.elements.sort()
            
    def pop(self):
        if self.search_function == 'dfs':
            return self.elements.pop()
        elif self.search_function == 'bfs':
            return self.elements.pop(0)
        elif self.search_function == 'ucs':
            return self.elements.pop(0)[1]
    
    def is_empty(self):
        return len(self.elements) == 0

def Best_First_Search(problem, search_function, search_version='graph', heuristic=None):
    """"
    Performs a best-first search on the given problem.
    """
    
    # current state, parent_state, action, cost
    initial_state = (problem.initial_state, 0, None, 0)
    
    # use different queue for different search functions
    queue = Queue(search_function)
    queue.push(initial_state)
    
    visited = set()
        
    while not queue.is_empty():
        current_state, parent_state, actions, costs = queue.pop()
        if problem.is_goal(current_state):
            return actions
        
        if current_state not in visited:
            if search_version == 'graph':
                visited.add(current_state)
                
            for next_state, action, cost in problem.get_successors(current_state):
                heuristic_cost = heuristic(next_state) if heuristic else 0
                new_state = (next_state, current_state, actions + action, costs + cost)
                queue.push(new_state, costs + cost + heuristic_cost)
                
    return None  
    