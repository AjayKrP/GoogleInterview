class Solution:
    def isValid(self, x, y, grid):
        if grid[0][0] == grid[1][1] == grid[2][2]:
            return True
        if grid[0][2] == grid[1][1] == grid[2][0]:
            return True
        if grid[0][y] == grid[1][y] == grid[2][y]:
            return True
        if grid[x][0] == grid[x][1] == grid[x][2]:
            return True
        
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[(i+1)*(j+1) for i in range(3)] for j in range(3)]
        
        for i in range(len(moves)):
            x, y = moves[i][0], moves[i][1]
            curr = 'x' if i%2 == 0 else '0'
            grid[x][y] = curr
            if (self.isValid(x, y, grid)):
                return 'A' if curr == 'x' else 'B'
        if len(moves) == 9:
            return "Draw"
        return 'Pending'
        
