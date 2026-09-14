class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1,
        2: 2}

        def ways_to_climb(steps):
            if steps in memo:
                return memo[steps]
            
            memo[steps] = ways_to_climb(steps - 1) + ways_to_climb(steps - 2)
            return memo[steps]
        return ways_to_climb(n)