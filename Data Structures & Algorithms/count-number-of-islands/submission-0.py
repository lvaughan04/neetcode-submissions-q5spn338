class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r == row or c == col or grid[r][c] == "0" or grid[r][c] == "T"):
                return
            grid[r][c] = "T"
            dfs(r + 1, c) ##up
            dfs(r - 1, c) ##down
            dfs(r, c + 1) ##right
            dfs(r, c - 1) ##left
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res