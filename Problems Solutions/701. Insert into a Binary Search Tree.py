# https://leetcode.com/problems/insert-into-a-binary-search-tree/

from utils import TreeNode, list_to_search_btree

class Solution:
    def insertIntoBST(self, root, val: int):
        if not root:
            return TreeNode(val)

        if root.right and val > root.val:
            self.insertIntoBST(root.right, val)

        if root.left and val < root.val:
            self.insertIntoBST(root.left, val)

        if val > root.val and not root.right:
            root.right = TreeNode(val)
            
        if val < root.val and not root.left:
            root.left = TreeNode(val)
        
        return root

tests_data = [
    ([4,2,7,1,3], 5, [4,2,7,1,3,5]),
    ([40,20,60,10,30,50,70], 25, [40,20,60,10,30,50,70,None,None,25]),
    ([4,2,7,1,3,None,None,None,None,None,None], 5, [4,2,7,1,3,5])
]

obj = Solution()

for data in tests_data:
    expected = list_to_search_btree(data[-1])
    root = list_to_search_btree(data[0])
    root = obj.insertIntoBST(root, data[1])
    assert root.is_same_tree(expected)
