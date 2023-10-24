package main

import (
	"sort"
)

func _merge(i1 []int, i2 []int) [][]int {
    var r [][] int

    if i1[1] < i2[0] {
        r = append(append(r, i1), i2)
    } else if i1[0] <= i2[0] && i1[1] >= i2[1] {
        r = append(r, i1)
    } else if i2[0] <= i1[1] {
        var i = []int {i1[0], i2[1]} 
        r = append(r, i)
    }

    return r
}

func merge(intervals [][]int) [][]int {
    var r [][]int

    sort.Slice(
        intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })

    r = append(r, intervals[0])

    for _, i2 := range(intervals[1:]) {
        var i1 = r[len(r) - 1]
        var merged = _merge(i1, i2)

        // pop last element from result slice
        r = r[:len(r) - 1]

        for _, i := range(merged) {
            r = append(r, i)
        }
    }

    return r
}