# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from utils import list_to_order_btree

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        
        r = 1
        nodes = [(root, 1)]

        while nodes:
            lvl = []
            
            node, lvl = nodes.pop()
            r = max(r, lvl)
            
            if node.left:
                nodes.append((node.left, lvl + 1))
            if node.right:
                nodes.append((node.right, lvl + 1))

        return r

tests_data = [
    ([3,9,20,None,None,15,7], 3),
    ([1,None,2], 2),
]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    tree = list_to_order_btree(data[0])
    assert expected == obj.maxDepth(tree)