class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def addTreasure(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == -1 or (r, c) in visited):
                return
            q.append((r, c))
            visited.add((r, c))
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r,c))
        distance = 0
        while q:
            for i in range(len(q)):
                r , c = q.popleft()
                grid[r][c] = distance
                addTreasure(r + 1, c)
                addTreasure(r - 1, c)
                addTreasure(r, c + 1)
                addTreasure(r, c - 1)
            distance += 1
                        
        