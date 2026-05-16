class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0
        left = 0
        right = len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(height[left], leftMax)
                totalWater += leftMax - height[left]
                left += 1
            else:
                rightMax = max(height[right], rightMax)
                totalWater += rightMax - height[right]
                right -= 1

        return totalWater
