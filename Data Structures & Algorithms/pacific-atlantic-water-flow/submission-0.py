class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ## essentially for each cell we have to reach either the (top or left sides) and (bottom or right sides) from a particular cell
        ## the only way to traverse a new cell is the cell's value is the same or lower to the cell you are on now
        ## case is for each neighbor of cells, if neighbor <= cell, dfs(cell)

        ## base case: keep to temp values that are passed in such as topLeft or bottomRight
        ##      if r < 0 or c < 0 topLeft = True, if c == COLS or r == ROWS, bottomRight is true
        ## if both topLeft and bottomRight, add r, c to result array

        res = []
        visited = set()
        ROWS, COLS = len(heights), len(heights[0])
        self.topLeft = False
        self.bottomRight = False

        def dfs(r, c, oldValue):
            if r < 0 or c < 0:
                self.topLeft = True
                return
            elif c == COLS or r == ROWS:
                self.bottomRight = True
                return
            if oldValue < heights[r][c] or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r + 1, c, heights[r][c])
            dfs(r - 1, c, heights[r][c])
            dfs(r, c + 1, heights[r][c])
            dfs(r, c - 1, heights[r][c])




        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, heights[r][c])
                if self.topLeft and self.bottomRight:
                    res.append([r, c])
                visited = set()
                self.topLeft = False
                self.bottomRight = False

        return res 