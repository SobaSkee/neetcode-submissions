class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            left_2 = 0
            right_2 = len(matrix[mid]) - 1
            while left_2 <= right_2:
                mid_2 = (left_2 + right_2) // 2
                if matrix[mid][mid_2] == target:
                    return True
                elif matrix[mid][mid_2] < target:
                    left_2 = mid_2 + 1
                else:
                    right_2 = mid_2 - 1
            if target > matrix[mid][-1]:
                left = mid + 1
            else:
                right = mid - 1
        return False