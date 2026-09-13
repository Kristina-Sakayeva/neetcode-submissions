class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        three_sum = []
        nums.sort()
        seen = set()
        for index, i in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            if i in seen:
                continue
            seen_here = set()
            while left < right:
                if nums[left] in seen_here:
                    left += 1
                    continue
                if nums[right] in seen_here:
                    right -= 1
                    continue
                if nums[left] + nums[right] == -1*i:
                    three_sum.append([i,nums[left],nums[right]])
                    seen_here.add(nums[left])
                    seen_here.add(nums[right])
                    right -= 1
                    left += 1
                elif nums[left] + nums[right] > -1*i:
                    right -= 1
                elif nums[left] + nums[right] < -1*i:
                    left += 1
            seen.add(i)
        return three_sum
                