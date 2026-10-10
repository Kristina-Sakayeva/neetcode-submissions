class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def get_neighbors(pos):
            x, y = pos
            return [(x-1,y), (x+1, y), (x, y-1), (x, y+1)]
        
        def in_bounds(pos):
            x, y = pos
            return x < len(grid) and x >= 0 and y < len(grid[0]) and y >= 0
        
        def fresh_fruit(grid):
            for i in range(len(grid)):
                if 1 in grid[i]:
                    return True
            return False

        def bfs(rotten_fruit, grid):
            queue = rotten_fruit
            time = 0
            while queue:
                new_queue = []
                for cur in queue:
                
                    for neighbor in get_neighbors(cur):
                        if in_bounds(neighbor) and grid[neighbor[0]][neighbor[1]] == 1:
                            grid[neighbor[0]][neighbor[1]] = 2
                            new_queue.append(neighbor)
                queue = new_queue
                time += 1
            return time
        
        rotten_fruits = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    rotten_fruits.append((x,y))
        if rotten_fruits:
            time = bfs(rotten_fruits, grid)
            if not fresh_fruit(grid):
                return time - 1
        elif not fresh_fruit(grid):
            return 0
        return -1



        