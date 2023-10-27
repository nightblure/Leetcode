package main

import "fmt"

func linkedList() {
	var l = CreateLinkedListInstance()
	l.AddAtHead(1)
	l.AddAtTail(3)
	l.AddAtIndex(1, 2)
	l.DeleteAtIndex(1)
	fmt.Println(l.Get(1))

	var nums = []int {1, 2, 3, 4, 5}
	l = CreateFrom(nums)
	l.Print()
}

func mergeIntervals() {
	var data = [][]int {
		{4, 6}, {1, 3}, {5, 7},
	}
	var r = merge(data)
	fmt.Println(r)
}

func minStack() {
	var s = CreateMinStack()
	s.Push(1)
	s.Push(0)
	fmt.Println(s.GetMin())
}

func main() {
	// linkedList()
	// mergeIntervals()
	minStack()
}