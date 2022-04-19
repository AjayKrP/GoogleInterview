class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # -- main
        empty = 0
        start = 0, 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    start = (x, y)
                elif grid[x][y] == 0 or grid[x][y] == 2:  # --- NOTE [1]
                    empty += 1

        self.count = 0
        i, j = start

        # -- helper
        def dfs(x, y, empty):

            if x > len(grid) - 1 or x < 0 or y > len(grid[0]) - 1 or y < 0:
                return

            if grid[x][y] == 2 and empty == 0:
                self.count += 1
                return  # target found

            if grid[x][y] == "#":
                return

            if grid[x][y] == -1:
                return

            cell = grid[x][y]
            grid[x][y] = "#"
            empty -= 1  # one empty cell marked = one less empty cell --

            dfs(x + 1, y, empty)
            dfs(x, y + 1, empty)
            dfs(x - 1, y, empty)
            dfs(x, y - 1, empty)

            grid[x][y] = cell

        # empty += 1

        # ---
        dfs(i, j, empty)
        return self.count

