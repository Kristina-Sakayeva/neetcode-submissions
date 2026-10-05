class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid) - 1, len(grid[0]) - 1
        visted = set()

        def dfs(x, y):
            if x < 0 or x > rows or y < 0 or y > cols or grid[x][y] == 0 or (x,y) in visted:
                return 0
            
            visted.add((x,y))
            return 1 + dfs(x + 1, y) + dfs(x, y + 1) + dfs(x - 1, y) + dfs(x, y -1)

        max_island = 0
        for i in range(rows + 1):
            for j in range(cols + 1):
                if grid[i][j] == 1:
                    island_area = dfs(i, j)
                    if island_area > max_island:
                        max_island = island_area
                else:
                    visted.add((i, j))

        return max_island




        