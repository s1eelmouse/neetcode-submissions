class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_outer = 0
        right_outer = len(matrix) - 1
        while left_outer <= right_outer:
            mid_outer = left_outer + (right_outer - left_outer) // 2
            if target < matrix[mid_outer][0]:
                right_outer = mid_outer - 1
            elif target > matrix[mid_outer][-1]:
                left_outer = mid_outer + 1
            else:
                left = 0
                right = len(matrix[0]) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if target == matrix[mid_outer][mid]:
                        return True
                        break
                    elif target < matrix[mid_outer][mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                break
        return False
