class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_valid(i,j):
            if i < 0 or i > len(grid) -1:
                return False
            elif j < 0 or j > len(grid[0]) - 1:
                return False
            return True
        def get_neighbors(i, j):
            neighbors = []
            if is_valid(i-1,j) and grid[i-1][j] == '1':
                neighbors.append((i-1,j))
            if is_valid(i+1,j) and grid[i+1][j] == '1':
                neighbors.append((i+1,j))
            if is_valid(i,j-1) and grid[i][j-1] == '1':
                neighbors.append((i,j-1))
            if is_valid(i,j+1) and grid[i][j+1] == '1':
                neighbors.append((i,j+1))
            return neighbors

        seen = set()
        count = 0
        for index_i, i in enumerate(grid):
            for index_j, j in enumerate(i):
                if grid[index_i][index_j] == '0':
                    continue
                if (index_i,index_j) in seen:
                    continue
                
                count += 1
                queue = [(index_i,index_j)]
                seen.add((index_i, index_j))
                while queue:
                    cur = queue.pop()
                    i = cur[0]
                    j = cur[1]

                    for neighbor in get_neighbors(i,j):
                        if neighbor not in seen:
                            queue.append(neighbor)
                            seen.add(neighbor)
        return count





        