# https://leetcode.com/problems/lru-cache/description/

class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = self.prev = None

class LinkedList:
    def __init__(self):
        self.count = 0
        self.head = self.tail = None
    
    def append(self, k, v):
        node = Node(k, v)
        
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        
        self.count += 1
        return node

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        elif node == self.tail:
            self.tail = self.tail.prev
        else:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
        
        self.count -= 1

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = LinkedList()
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.nodes.remove(node)
            self.cache[key] = self.nodes.append(key, node.value)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.nodes.remove(self.cache[key])
        
        if self.capacity == self.nodes.count:
            head = self.nodes.head
            self.nodes.remove(head)
            del self.cache[head.key]
        
        self.cache[key] = self.nodes.append(key, value)

lRUCache = LRUCache(2)
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
lRUCache.get(1);    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    # return -1 (not found)
lRUCache.get(3);    # return 3
lRUCache.get(4);    # return 4