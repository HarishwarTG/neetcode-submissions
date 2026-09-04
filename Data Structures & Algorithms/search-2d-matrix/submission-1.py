class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows =  len(matrix) #3
        cols = len(matrix[0]) #4

        top, bot = 0, rows-1

        while top <= bot:
            mid_row = (bot + top) // 2
            if target < matrix[mid_row][0]:
                bot = mid_row - 1
            elif target > matrix[mid_row][cols - 1]:
                top = mid_row + 1
            else:
                break
        
        if not (top<=bot): return False
        l = 0
        r = cols -1

        while l <=r:
            mid = (l + r) // 2
            if target > matrix[mid_row][mid]:
                l = mid + 1
            elif target < matrix[mid_row][mid]:
                r = mid - 1
            else:
                return True
        
        return False


        