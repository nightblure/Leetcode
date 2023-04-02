# https://leetcode.com/problems/invert-binary-tree/

from utils import list_to_order_btree, TreeNode

class Solution:
    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

tests_data = [
    ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
    ([2,1,3], [2,3,1]),
]
obj = Solution()

for data in tests_data:
    expected = list_to_order_btree(data[-1])
    root = list_to_order_btree(data[0])
    assert expected.is_same_tree(obj.invertTree(root))