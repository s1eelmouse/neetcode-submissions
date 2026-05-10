class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        totalLen = len(nums)
        for left in range(totalLen - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            leftNum = nums[left]
            mid = left + 1
            right = totalLen - 1
            while left != mid:
                if right <= mid:
                    break
                numMid = nums[mid]
                numRight = nums[right]
                if numMid + numRight == -leftNum:
                    res.append([numMid, numRight, leftNum])
                    mid += 1
                    right -= 1
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif numMid + numRight > -leftNum:
                    right -= 1
                else:
                    mid += 1
        return res
