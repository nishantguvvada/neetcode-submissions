import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                box_id = (r//3, c//3)
                char = board[r][c]
                if char != '.':
                    print(f"Cell ({r}, {c}) with value {char} is in box {box_id}")
                    if char in rows[r] or char in cols[c] or char in boxes[box_id]:
                        return False
                    rows[r].add(char)
                    cols[c].add(char)
                    boxes[box_id].add(char)
        return True