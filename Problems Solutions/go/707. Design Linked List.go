package main

import "fmt"

type Node struct {
	value int
	next  *Node
}

type MyLinkedList struct {
	head  *Node
	count int
}

func CreateFrom(items []int) MyLinkedList {
	var list = MyLinkedList{}
	for _, value := range(items){
		list.AddAtTail(value)
	}
	return list
}

func Constructor() MyLinkedList {
	var list = MyLinkedList{count: 0, head: nil}
	return list
}

func (l *MyLinkedList) Print() {
	var node = l.head
	fmt.Println(node.value)

	for node.next != nil {
		node = node.next
		fmt.Println(node.value)
	}
}

func (this *MyLinkedList) getNode(index int) *Node {
	var node = this.head
	for i := 0; i < index; i++ {
		node = node.next
	}
	return node
}

func (this *MyLinkedList) Get(index int) int {
	if index > this.count-1 {
		return -1
	}

	return this.getNode(index).value
}

func (this *MyLinkedList) AddAtHead(val int) {
	var node *Node = &Node{value: val}

	if this.head == nil {
		this.head = node
	} else {
		var oldHead = this.head
		this.head = node
		this.head.next = oldHead
	}

	this.count++
}

func (this *MyLinkedList) AddAtTail(val int) {
	var node *Node = &Node{value: val}

	if this.head == nil {
		this.head = node
	} else {
		this.getNode(this.count - 1).next = node
	}

	this.count++
}

func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index > this.count {
		return
	}

	if index == this.count {
		this.AddAtTail(val)
	} else if index == 0 {
		this.AddAtHead(val)
	} else {
		var prevNode = this.getNode(index - 1)
		var nextNode = prevNode.next
		prevNode.next = &Node{value: val}
		prevNode.next.next = nextNode
		this.count++
	}
}

func (this *MyLinkedList) DeleteAtIndex(index int) {
	if index > this.count-1 {
		return
	}

	if index == this.count-1 {
		this.getNode(this.count - 2).next = nil
	} else if index == 0 {
		this.head = this.head.next
	} else {
		var prevNode = this.getNode(index - 1)
		prevNode.next = prevNode.next.next
	}

	this.count--
}

func main() {
	var l = Constructor()
	l.AddAtHead(1)
	l.AddAtTail(3)
	l.AddAtIndex(1, 2)
	l.DeleteAtIndex(1)
	fmt.Println(l.Get(1), "\n")

	var nums = []int {1, 2, 3, 4, 5}
	l = CreateFrom(nums)
	l.Print()
}
