class Solution:
    def isValidSudoku(self, board) -> bool:
        seen = {}
        # if something unique comes up then use dictionary or hashmap
        for i in range(9):
            for j in range(9):
                curr = board[i][j]

                if curr != '.':
                    item1 = f'{curr} curr found in row {i}'
                    item2 = f'{curr} curr found in column {j}'
                    item3 = f'{curr} curr found in block {i//3}-{j//3}'
                    if item1 in seen or item2 in seen or item3 in seen:
                        return False
                    else:
                        seen.setdefault(item1)
                        seen.setdefault(item2)
                        seen.setdefault(item3)
        return True
