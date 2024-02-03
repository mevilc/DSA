# check if a path exists from src to dst node in undirected graph
# cycles exist --> keep track of visited notes with a set

def has_path_dfs_iter(graph, src, dst):
    if src == dst: return True
    stack = [ src ]
    visited = set() # add to set when visited

    while (len(stack)):
        curr_node = stack.pop()
        for neighbour in graph[curr_node]:
            if neighbour == dst: return True
            
            if neighbour not in visited:
                # add to stack
                stack.append(neighbour)
            
            # once added to stack, then mark visited
            visited.add(neighbour)
    return False
    
   
def has_path_dfs_rec(graph, src, dst, visited):
   
    if src == dst: return True
    
    if src in visited: 
        # dont want to continue looking at its neighbours
        return False
    
    visited.add(src)
    
    for neighbour in graph[src]:
        if ( has_path_dfs_rec(graph, neighbour, dst, visited) ): return True

    return False


def has_path_dfs(graph, src, dst):
    if src == dst: return True
    queue = [ src ]
    visited = set()

    while (len(queue)):
        curr_node = queue.pop()
        for neighbour in graph[curr_node]:
            if neighbour == dst: return True
            if neighbour not in visited:
                queue.insert(0, neighbour)

            visited.add(neighbour)

    return False
    

def build_graph(edges):
    # create graph from edges
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph: graph[ a ] = []
        if b not in graph: graph[ b ] = []
        
        graph[ a ].append( b )
        graph[ b ].append( a )
    return graph

def main():
    edges = [
             ["i", "j"],
             ["k", "i"],
             ["m", "k"],
             ["k", "l"],
             ["o", "n"]
            ]

    graph = build_graph(edges)

    print(has_path_dfs_iter(graph, "j", "k"))

    # set lookup O(1)
    # passing in set through recursive calls
    visited = set()
    print(has_path_dfs_rec(graph, "j", "k", visited))
    
    print(has_path_dfs(graph, "j", "k"))

main()
