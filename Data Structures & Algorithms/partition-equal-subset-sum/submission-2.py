class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total / 2

        if int(target) != target:
            return False
        
        target = int(target)
        
        sums = [False for i in range(target + 1)]
        sums[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                if sums[i - num]:
                    sums[i] = True
        return sums[target]