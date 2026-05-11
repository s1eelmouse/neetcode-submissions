class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0
        left = 0
        right = len(height) - 1
        curHeight = 1
        curLeft = len(height) + 1
        curRight = 0
        maxHeight = max(height)
        while curHeight <= maxHeight:
            if height[left] < curHeight:
                left += 1
            else:
                curLeft = left
            if height[right] < curHeight:
                right -= 1
            else:
                curRight = right
            if curLeft < len(height) + 1:
                if min(height[curLeft], height[curRight]) >= curHeight:
                    for i in height[curLeft:curRight+1]:
                        if i < curHeight:
                            totalWater += 1
                    curHeight += 1
        return totalWater 