# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from utils import list_to_order_btree

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)

tests_data = [
    ([3,9,20,None,None,15,7], 3),
    ([1,None,2], 2),
]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    tree = list_to_order_btree(data[0])
    assert expected == obj.maxDepth(tree)