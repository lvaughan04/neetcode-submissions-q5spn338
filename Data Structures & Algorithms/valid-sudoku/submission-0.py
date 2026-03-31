class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                value = board[r][c]
                if value == ".":
                    continue
                box = (r // 3), (c // 3)
                
                if value in rows[r] or value in cols[c] or value in boxes[box]:
                    return False
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)
        
        return True