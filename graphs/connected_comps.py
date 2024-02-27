# count number of connected components in a undirected graph (# islands)
# approach:
    # 1. iterate through each node not already visted
    # 2. dfs on that node until its end. Keep track of visited nodes globally
    # 3. increment once dfs is done

def dfs_iter(graph, src, visited):
    stack = [ src ]

    while(len(stack)):
        curr_node = stack.pop()
        visited.add(curr_node)
        for neighbour in graph[curr_node]:
            if neighbour not in visited:
                stack.append(neighbour)

def dfs_rec(graph, src, visited):
    
    visited.add(src)
    for neighbour in graph[ src ]:
        if neighbour not in visited:
            dfs_rec(graph, neighbour, visited)

def bfs(graph, src, visited):
    queue = [ src ]
    
    while(len(queue)):
        curr_node = queue.pop()
        visited.add(curr_node)
        for neighbour in graph[ curr_node ]:
            if neighbour not in visited:
                queue.insert(0, neighbour)


def connected_comps(graph):
    # iterate through each node
    visited = set()
    count = 0
    for node in graph:
        if node not in visited:
            bfs(graph, node, visited)
            count += 1

    return count


def main():
    '''graph = {
             3 : [],
             4 : [6],
             6 : [4, 5, 7, 8],
             8 : [6],
             7 : [6],
             5 : [6],
             1 : [2],
             2 : [1]
            }'''

    graph = {
             0 : [8, 1, 5],
             1 : [0],
             5 : [0, 8],
             8 : [0, 5],
             2 : [3, 4],
             3 : [2, 4],
             4 : [3, 2]
            }

    print(connected_comps(graph))

main()
