# simple bfs and dfs

def dfs_iterative(graph, start):
    # stack
    stack = [ start ]
    while (len(stack)):
        curr_node = stack.pop()
        for neighbour in graph[curr_node]:
            stack.append(neighbour)
        print(f"curr_node: {curr_node}")
    
def dfs_recursive(graph, start):
    # call stack
    print(f"curr_node: {start}")
    if len(graph[start]) == 0: return
    for neighbour in graph[start]:
        dfs_recursive(graph, neighbour)



def bfs(graph, start):
    # queue
    queue = [ start ]
    while (len(queue)):
        curr_node = queue.pop()
        for neighbour in graph[curr_node]:
            queue.insert(0, neighbour)
        print(f"curr_node: {curr_node}")
      
def main():
    # graph
    graph = {
             "a" : ["b", "c"],
             "b" : ["d"],
             "c" : ["e"],
             "d" : ["f"],
             "e" : [],
             "f" : []
            }
    
    print("DFS Iterative")
    dfs_iterative(graph, "a")
    
    print("DFS Recursive")
    dfs_recursive(graph, "a")

    print("BFS")
    bfs(graph, "a")
main()
