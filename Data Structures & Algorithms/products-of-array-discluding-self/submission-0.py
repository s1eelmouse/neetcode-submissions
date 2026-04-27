from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        revNums = nums[::-1]
        numProd = []
        revNumProd = []
        res = []
        for i in range(len(nums) - 1):
            numProd.append(prod(nums[i+1::]))
            revNumProd.append(prod(revNums[i+1::]))
        numProd.append(1)
        revNumProd.append(1)
        for i in range(len(nums)):
            res.append(numProd[i] * revNumProd[-(i + 1)])
        return res
