class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0] * n for _ in range(n)]

        left , right = 0, n
        top , bottom = 0, n
        count = 1
        while left < right and top < bottom and count <= n * n:
            for c in range(left, right):
                matrix[top][c] = count
                count += 1
            top += 1

            if not top < bottom:
                break
            
            for r in range(top, bottom):
                matrix[r][right - 1] = count
                count += 1
            right -= 1
            
            if not left < right:
                break
            
            for c in range(right - 1, left - 1, -1):
                matrix[bottom-1][c] = count
                count += 1
            bottom -= 1
            
            for r in range(bottom - 1, top - 1, -1):
                matrix[r][left] = count
                count += 1
            left += 1
        
        return matrix