# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

from utils import list_to_search_btree, TreeNode

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root 

root = TreeNode(6)

root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p, q = root.left, root.right

expected = root

obj = Solution()
assert expected == obj.lowestCommonAncestor(root, p, q)

p, q = root.left, root.left.right
expected = root.left
assert expected == obj.lowestCommonAncestor(root, p, q)

tests_data = [
    ([6,2,8,0,4,7,9,None,None,3,5], [2,0,4,None,None,3,5], [8,7,9], [6,2,8,0,4,7,9,None,None,3,5]),
    ([6,2,8,0,4,7,9,None,None,3,5], [2,0,4,None,None,3,5], [4,3,5], [2,0,4,None,None,3,5]),
    ([2,1], [2,1], [1], [2,1])
]
obj = Solution()

for data in tests_data:
    expected = list_to_search_btree(data[-1])
    root = list_to_search_btree(data[0])
    p = list_to_search_btree(data[1])
    q = list_to_search_btree(data[2])
    assert expected.is_same_tree(obj.lowestCommonAncestor(root, p, q))