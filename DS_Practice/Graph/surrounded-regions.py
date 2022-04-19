from queue import Queue


class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(m):
            for j in range(n):
                visited = set()  # For one region there will be one visited set since for loop is taking
                # Care of not to visit cell again
                if board[i][j] == 'O':
                    q = Queue()
                    q.put((i, j))
                    visited.add((i, j))
                    surrounded = True
                    while not q.empty(): # loop will find if 0 is surrounded by x
                        front = q.get()
                        if front[0] == 0 or front[0] == m - 1 or front[1] == 0 or front[1] == n - 1:
                            surrounded = False
                            break # break if found non surrounded region

                        for k in range(4):
                            cx = front[0] + directions[k][0]
                            cy = front[1] + directions[k][1]

                            if 0 <= cx < m and 0 <= cy < n and (cx, cy) not in visited and board[cx][cy] == 'O':
                                visited.add((cx, cy))
                                q.put((cx, cy))

                    if surrounded: # If surrounded then fill cells (for one region at a time)
                        for ix, jy in visited:
                            board[ix][jy] = 'X'
        return board


sol = Solution()
matrix = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
print(sol.solve(matrix))
print(sol.solve([["O", "O"], ["O", "O"]]))
print(sol.solve([["O", "X", "O"], ["X", "O", "X"], ["O", "X", "O"]]))
