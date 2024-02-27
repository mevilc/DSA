# determine largest component in a graph
# approach:
    # 1. iterate through each node that is not visited
    # 2. dfs and keep track of visited (unique) nodes
    # 3. return max of those components
    
def dfs_iter(graph, src):
    stack = [ src ]
    visited = set()
    
    while (len(stack)):
        curr_node = stack.pop()
        visited.add(curr_node)
        for neighbour in graph[ curr_node ]:
            if neighbour not in visited:
                stack.append(neighbour)
    
    return len(visited)

def largest_comp(graph):
    n_nodes = set()
    for node in graph:
        #if node not in visited:
        n_nodes.add( dfs_iter(graph, node) )
    return max(n_nodes)

def main():
    graph = {
             0 : [8, 1, 5],
             1 : [0],
             5 : [0, 8],
             8 : [0, 5],
             2 : [3, 4],
             3 : [2, 4],
             4 : [3, 2]
            }


    print(largest_comp(graph))

main()
