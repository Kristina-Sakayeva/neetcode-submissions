class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = int((right - left)/2)

        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
                mid = int((right - left)/2) + left
            elif nums[mid] < target:
                left = mid + 1
                mid = int((right - left)/2) + left

        return -1
        