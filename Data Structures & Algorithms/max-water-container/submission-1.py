class Solution:
    def maxArea(self, heights: List[int]) -> int:
        rangeHeights = sorted(set(heights))[::-1]
        maxHeight = max(heights)
        maxVolume = 0
        for height in rangeHeights:
            left = 0
            right = len(heights) - 1
            curLeft = len(heights) + 1
            curRight = 0
            while left < right:
                if heights[left] < height:
                    left += 1
                else:
                    curLeft = left
                if heights[right] < height:
                    right -= 1
                else:
                    curRight = right
                if curLeft != len(heights) + 1 and curRight != 0:
                    maxVolume = max(maxVolume, (curRight - curLeft) * min(heights[curLeft], heights[curRight]))
                    break
        return maxVolume