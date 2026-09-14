class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {1: 1,
        # 2: 2}

        # def ways_to_climb(steps):
        #     if steps in memo:
        #         return memo[steps]
            
        #     memo[steps] = ways_to_climb(steps - 1) + ways_to_climb(steps - 2)
        #     return memo[steps]
        # return ways_to_climb(n)
        ways_to_climb = [0 for i in range(n+1)]
        
        for steps in range(len(ways_to_climb)):
            if steps == 0:
                ways_to_climb[steps] = 0
                continue
            if steps == 1:
                ways_to_climb[steps] = 1
                continue
            if steps == 2:
                ways_to_climb[steps] = 2
                continue
            ways_to_climb[steps] = ways_to_climb[steps - 1] + ways_to_climb[steps-2]
        return ways_to_climb[steps]
