# b104d146-6aac-447a-986d-bcb59584094e
from collections import deque

def numIslands(grid):
    if not grid:
        return 0

    visited=set()
    islands=0

    def bfs(r,c):
        q = deque()
        visited.add((r,c))
        q.append((r,c))
    
        while q:
            row,col = q.popleft()
            directions= [[1,0],[-1,0],[0,1],[0,-1]]
        
            for dr,dc in directions:
                r,c = row + dr, col + dc
                if (r) in range(len(grid)) and (c) in range(len(grid[0])) and grid[r][c] == '1' and (r ,c) not in visited:
                
                    q.append((r,c))
                    visited.add((r,c))

    for r in range(len(grid)):
        for c in range(len(grid[0])):
        
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r,c)
                islands +=1 

    return islands



def main():
    n = int(input())
    grid = []

    for i in range(n):
        row = input().split()
        grid.append(row)
    
    print(numIslands(grid))

main()