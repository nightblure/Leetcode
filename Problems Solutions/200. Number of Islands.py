# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid) -> int:

        def mark_island(i, j, grid, n, m):
            grid[i][j] = "#"
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dir in directions:
                x, y = i + dir[0], j + dir[1]

                if x in range(0, n) and y in range(0, m) and grid[x][y] == "1":
                    mark_island(x, y, grid, n, m)
        
        n, m = len(grid), len(grid[0])
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    mark_island(i, j, grid, n, m)
                    count += 1

        return count

tests_data = (
    (
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ], 1
    ),
    (
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ], 3
    )
)
obj = Solution()

for data in tests_data:
    expected = data[1]
    assert expected == obj.numIslands(data[0])