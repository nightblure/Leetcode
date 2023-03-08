# https://leetcode.com/problems/validate-binary-search-tree/

from utils import list_to_order_btree

class Solution:
    def isValidBST(self, root) -> bool:

        def isvalid(node, low_bound, upper_bound):
            if not node:
                return True
                            
            if not (low_bound < node.val < upper_bound):
                return False
            
            return isvalid(node.left, low_bound, node.val) and isvalid(node.right, node.val, upper_bound)
        
        return isvalid(root, -float('inf'), float('inf'))

tests_data = [
    ([2,1,3], True),
    ([5,1,4,None,None,3,6], False),
]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    tree = list_to_order_btree(data[0])
    assert expected == obj.isValidBST(tree)