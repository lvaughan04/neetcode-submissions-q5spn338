class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = len(matrix), len(matrix[0])

        isFirstRowSetToZero = False
        
        ## find the zeros
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    ## set the top column of row
                    matrix[0][j] = 0

                    if i == 0:
                        isFirstRowSetToZero = True
                    else:
                        matrix[i][0] = 0
        
        ## set the rest of array to zeros
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(ROWS):
                matrix[i][0] = 0
        if isFirstRowSetToZero:
            for j in range(COLS):
                matrix[0][j] = 0
        
        


        
        