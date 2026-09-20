class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid_row = l + ((r - l) // 2)
            if target < matrix[mid_row][0]:
                r = mid_row - 1
            elif target > matrix[mid_row][-1]:
                l = mid_row + 1
            else:
                break
            
        row = matrix[mid_row]
        l = 0
        r = len(row) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if target < row[m]:
                r = m - 1
            elif target > row[m]:
                l = m + 1
            else:
                return True
        
        return False