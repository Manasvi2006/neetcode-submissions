class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0

        rows, col = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            queue = collections.deque()
            visited.add((r,c))
            queue.append((r,c))

            #make directions
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while queue:
                currRow, currCol = queue.popleft()
                for dr, dc in directions:
                    r = currRow + dr
                    c = currCol + dc
                    if(r in range(rows) and
                        c in range(col) and
                        grid[r][c] == "1" and
                        (r,c) not in visited):

                        visited.add((r,c))
                        queue.append((r,c))

        for r in range(rows):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands









