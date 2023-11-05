type Node struct {
    key int
    value int
    prev *Node
    next *Node
}

type LinkedList struct {
    count int
    head *Node
    tail *Node
}

func (ll *LinkedList) Append(key, val int) *Node {
    node := &Node{key, val, nil, nil}

    if ll.head == nil {
        ll.head = node
        ll.tail = node
    } else {
        ll.tail.next = node
        node.prev = ll.tail
        ll.tail = node
    }

    ll.count++
    return ll.tail
}

func (ll *LinkedList) Remove(node *Node) {
    if node == ll.head {
        ll.head = ll.head.next
    } else if node == ll.tail {
        ll.tail = ll.tail.prev
    } else {
        prev := node.prev
        next := node.next
        prev.next = next
        next.prev = prev
    }

    ll.count--
}

type LRUCache struct {
    nodes LinkedList
    cache map[int]*Node
    capacity int 
}


func Constructor(capacity int) LRUCache {
    return LRUCache{capacity: capacity, nodes: LinkedList{}, cache: make(map[int]*Node)}
}


func (this *LRUCache) Get(key int) int {
    _, exists := this.cache[key]

    if !exists { 
        return -1
    }

    node := this.cache[key]
    this.nodes.Remove(node)
    this.cache[key] = this.nodes.Append(key, node.value)
    return node.value
}


func (this *LRUCache) Put(key int, value int)  {
    _, exists := this.cache[key]

    if exists {
        this.nodes.Remove(this.cache[key])
    }

    if this.nodes.count == this.capacity {
        head := this.nodes.head
        this.nodes.Remove(head)
        delete(this.cache, head.key)
    }

    this.cache[key] = this.nodes.Append(key, value)
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
