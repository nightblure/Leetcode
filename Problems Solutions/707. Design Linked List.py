# https://leetcode.com/problems/design-linked-list/description

from utils import list_to_linked_list, ListNode, is_same_linked_lists

class Node:
    def __init__(self, v, next=None):
        self.value = v
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.count = 0
    
    def __get_node_by_index(self, index) -> Node:
        node = self.head
        
        for _ in range(index):
            node = node.next
        
        return node        

    def get(self, index: int) -> int:
        if index not in range(0, self.count):
            return -1
        return self.__get_node_by_index(index).value

    def addAtHead(self, val: int) -> None:
        new_head = Node(val, self.head)
        self.head = new_head
        self.count += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            last_node = self.__get_node_by_index(self.count - 1)
            last_node.next = Node(val)
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index not in range(0, self.count + 1):
            return

        if index == self.count:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            node = self.__get_node_by_index(index - 1)
            next = node.next
            node.next = Node(val)
            node.next.next = next
            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index not in range(0, self.count):
            return
        
        if index == 0:
            self.head = self.head.next
        elif index == self.count - 1:
            self.__get_node_by_index(self.count - 2).next = None
        else:
            node = self.__get_node_by_index(index - 1)
            node.next = node.next.next
        
        self.count -= 1
