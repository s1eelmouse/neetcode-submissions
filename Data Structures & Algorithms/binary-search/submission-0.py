class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            mid = len(nums) // 2
            left = 0
            right = len(nums) - 1
            while nums[mid] != target:
                if nums[mid] < target:
                    left = mid
                    mid += len(nums[left:right + 1]) // 2
                else:
                    right = mid
                    mid -= len(nums[left:right + 1]) // 2
            if nums[mid] == target:
                return mid