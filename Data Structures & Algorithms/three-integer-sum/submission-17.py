class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        totalLen = len(nums)
        for left in range(totalLen - 2):
            leftNum = nums[left]
            mid = left + 1
            right = totalLen - 1
            while (left != mid):
                if right == mid:
                    break
                numMid = nums[mid]
                numRight = nums[right]
                if numMid + numRight == -leftNum:
                    if sorted([numMid, numRight, leftNum]) not in res:
                        res.append(sorted([numMid, numRight, leftNum]))
                        mid += 1
                    else:
                        mid += 1
                elif numMid + numRight > -leftNum:
                    right -= 1
                else:
                    mid += 1
        return res
