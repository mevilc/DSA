# has path: check if path exists between src and dst node
# acyclic graph

def has_path_dfs_rec(graph, src, dst):
    if src == dst: return True 
    #if (len(graph[src]) == 0): return
    
    for neighbour in graph[src]:
        if ( has_path_dfs_rec(graph, neighbour, dst) ): return True

    return False

def has_path_dfs_iter(graph, src, dst):
    if src == dst: return True
    stack = [ src ]
    
    while (len(stack)):
        curr_node = stack.pop()
        for neighbours in graph[curr_node]:
            if neighbours == dst: return True
            stack.append(neighbours)

    return False

def has_path_bfs(graph, src, dst):
    if src == dst: return True
    queue = [ src ]
    while (len(queue)):
        curr_node = queue.pop()
        for neighbour in graph[curr_node]:
            if neighbour == dst: return True
            queue.insert(0, neighbour)
    return False

def main():
    graph = {
             "f" : ["g", "i"],
             "g" : ["h"],
             "h" : [],
             "i" : ["g", "k"],
             "j" : ["i"],
             "k" : []
            }

    print(has_path_dfs_rec(graph, "f", "k"))
    print(has_path_dfs_iter(graph, "f", "k"))
    print(has_path_bfs(graph, "f", "k"))

main()
