# find number of islands ("L") in 2d grid
# approach: 
    # 1. iterate through node (position) and if its L and not visited, dfs on that node
    # 2. increment count


def dfs(grid, node, visited):
    stack = [ node ]
    r, c = node[0], node[1]
    # generate neigbours
    neighbours = []
    
    # edge cases: UL, UR, LL, LR
    
    # UL
    if node[0] == 0 and node[1] == 0: neighbours.append( (r + 1, c), (r, c + 1) )
    # UR
    elif node[0] == 0 and node[1] == len(grid[0]) - 1: 
        neighbours.append( (r + 1, c), (r, c - 1) )
    # LL
    elif node[0] == len(grid) - 1 and node[1] == 0: 
        neighbours.append( (r - 1, c), (r, c + 1) )
    # LR
    elif node[0] == len(grid) - 1 and node[1] == len(grid[0]) - 1: 
        neighbours.append( (r - 1, c), (r, c - 1) )

    else:
        neighbours.append( (r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1) )

    # actual dfs
    while (len(stack)):
        curr_node = stack.pop()

        visited.add(curr_node)

        for neighbour in neighbours:
            if neighbour not in visited:
                stack.append(neighbour)

            visited.add(curr_node)



def island_count(grid):
    visited = set()
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # check if land
            if grid[r][c] == "L":
                if grid[r][c] not in visited:
                    # node not visited
                    # dfs on this node (position)
                    node = (r, c)
                    dfs( grid, node, visited )
                    count += 1
    
    return count


def main():
    grid = [
            ["W", "L", "W", "W", "L", "W"],
            ["L", "L", "W", "W", "L", "W"],
            ["W", "L", "W", "W", "W", "W"],
            ["W", "W", "W", "L", "L", "W"],
            ["W", "L", "W", "L", "L", "W"],
            ["W", "W", "W", "W", "W", "W"]
           ]

    print(island_count(grid))
main()
