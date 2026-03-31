class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        seen = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in seen or grid[r][c] == "0":
                return 
            
            seen.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)



    ## essentially each first initial call to dfs will result in 1 total island so i dont have to keep track of that within the code
    ## i might need to return something like true or false to indicate if i should increase the counter based on return value of true or false

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in seen:
                    res += 1
                    dfs(r, c)
        
        return res

            
