# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid) -> int:

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def mark_island(i, j, grid, n, m):
            if i < 0 or i > n - 1 or j < 0 or j > m - 1:
                return

            if grid[i][j] != '1':
                return

            grid[i][j] = '#'

            for direction in directions:
                mark_island(i + direction[0], j + direction[1], grid, n, m)
            
            return grid
        
        n, m = len(grid), len(grid[0])
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    grid = mark_island(i, j, grid, n, m)
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