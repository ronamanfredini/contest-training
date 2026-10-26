class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, down = 0, len(matrix) - 1

        while top <= down:
            middle = top + ((down - top ) // 2)
            start = matrix[middle][0]
            end = matrix[middle][-1]

            if start <= target and end >= target:
                # this is the row
                left = 0
                right = len(matrix[middle]) - 1
                while left <= right:
                    m = left + ((right - left) // 2)
                    if matrix[middle][m] > target:
                        right = m - 1
                    elif matrix[middle][m] < target:
                        left = m + 1
                    else:
                        return True
                return False
            elif end < target:
                top = middle + 1
            elif start > target:
                down = middle - 1

        return False


s = Solution()

print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))