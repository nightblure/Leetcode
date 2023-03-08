# https://leetcode.com/problems/min-stack/

from collections import Counter, deque, defaultdict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f'value: {self.val}'

    def __repr__(self) -> str:
        return self.__str__()

    def is_same_tree(self, root):
        def _is_same_tree(root1, root2):
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False
            
            if root1.val != root2.val:
                return False
            
            return _is_same_tree(root1.left, root2.left) and _is_same_tree(root1.right, root2.right)
        
        return _is_same_tree(self, root)

    def insert(self, value):  
    
        if not self.left and value < self.val:
            self.left = TreeNode(value)
        elif not self.right and value > self.val:
            self.right = TreeNode(value)
        else:
            if value < self.val:
                self.left.insert(value)
            else:
                self.right.insert(value)

def display_func_value(f):
    def inner(*args, **kwargs):
        value = f(*args, **kwargs)
        print(value)
        return value
    return inner

def list_to_linked_list(values: list):
    head = ListNode(values[0])
    cur = head

    for value in values[1:]:
        cur.next = ListNode(value)
        cur = cur.next

    return head

def list_to_str(values, delimiter=None):
    if not delimiter:
        return f''.join([str(x) for x in values])
    return f'{delimiter}'.join([str(x) for x in values])

def list_to_order_btree(values):

    root = TreeNode(values.pop(0))
    nodes = deque([root])

    while nodes:
        node = nodes.pop()

        for _ in range(1):
            l = values.pop(0) if values else None
            left = TreeNode(l) if l else None
            r = values.pop(0) if values else None
            right = TreeNode(r) if r else None
            node.left = left
            node.right = right
            if l:
                nodes.appendleft(left)
            if r:
                nodes.appendleft(right)

    return root

def list_to_search_btree(values):
    if not values:
        return None
    
    root = TreeNode(values.pop(0))

    for value in values:
        if isinstance(value, int):
            root.insert(value)

    return root

