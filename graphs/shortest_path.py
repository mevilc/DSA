# find shortest path between start and end using BFS
# keep track of (node, distance) on queue

def shortest_path(graph, start, end):
    
    queue = [ (start, 0) ]
    visited = set( start )

    while(len(queue)):
        
        curr_elem = queue.pop()
        curr_node, curr_dist = curr_elem[0], curr_elem[1]
        
        if curr_node == end: return curr_dist

        for neighbour in graph[curr_node]:
            if neighbour not in visited:
                # add to queue
                queue.insert(0, (neighbour, curr_dist + 1) )
                # add to visited once added to queue
                visited.add(neighbour)

    return -1

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
             ["w", "x"],
             ["x", "y"],
             ["z", "y"],
             ["z", "v"],
             ["w", "v"],
            ]

    graph = build_graph(edges)

    print(graph)
    
    print(shortest_path(graph, "w", "z"))
main()
