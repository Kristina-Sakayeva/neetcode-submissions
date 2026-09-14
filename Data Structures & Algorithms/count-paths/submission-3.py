class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        num_ways_reach = [[0 for i in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0 and j == 1:
                    num_ways_reach[0][1] = 1
                    continue
                if i == 1 and j == 0:
                    num_ways_reach[1][0] = 1
                    continue
                
                if i - 1 < 0:
                    num_ways_reach[i][j] = num_ways_reach[i][j - 1]
                elif j - 1 < 0:
                    num_ways_reach[i][j] = num_ways_reach[i - 1][j]
                else:
                    num_ways_reach[i][j] = num_ways_reach[i - 1][j] + num_ways_reach[i][j - 1]
        
        return num_ways_reach[m-1][n-1]
                

        