class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val1 in enumerate(nums):
            for j, val2 in enumerate(nums[i+1::]):
                if val1 + val2 == target:
                    return [i,i+j+1]
                

        