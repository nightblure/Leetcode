package main

func markIsland(n int, m int, grid [][]byte, i int, j int) {

    if !(i >= 0 && i < n && j >= 0 && j < m) {
        return
    }

    if grid[i][j] != 49 {
        return
    }

    grid[i][j] = 100

    var dirs = [][]int {
        {1, 0},
        {0, 1},
        {-1, 0},
        {0, -1},
    }

    for _, dir := range(dirs) {
        markIsland(n, m, grid, i + dir[0], j + dir[1])
    }
}

func numIslands(grid [][]byte) int {
    var count = 0
    var n = len(grid)
    var m = len(grid[0])

    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if grid[i][j] == 49 {
                count++
                markIsland(n, m, grid, i, j)
            }
        }
    }

    return count
}