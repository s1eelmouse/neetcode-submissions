class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        totalLen = len(nums)
        for mid in range(1, totalLen):
            midNum = nums[mid]
            left = 0
            right = totalLen - 1
            while (left != mid):
                if right == mid:
                    break
                numLeft = nums[left]
                numRight = nums[right]
                if numLeft + numRight == -midNum:
                    if sorted([numLeft, numRight, midNum]) not in res:
                        res.append(sorted([numLeft, numRight, midNum]))
                        left += 1
                    else:
                        left += 1
                elif numLeft + numRight > -midNum:
                    right -= 1
                else:
                    left += 1
        return res