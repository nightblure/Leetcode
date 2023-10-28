# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from utils import list_to_order_btree

class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        
        depth = 1
        nodes = [(root, 1)]

        while nodes:
            node, lvl = nodes.pop()

            if node is None:
                continue

            depth = max(depth, lvl)
            nodes.append((node.left, lvl + 1))
            nodes.append((node.right, lvl + 1))

        return depth

tests_data = [
    ([3,9,20,None,None,15,7], 3),
    ([1,None,2], 2),
]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    tree = list_to_order_btree(data[0])
    assert expected == obj.maxDepth(tree)