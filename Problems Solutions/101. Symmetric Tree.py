# https://leetcode.com/problems/symmetric-tree/

from utils import list_to_order_btree

class Solution:
    def isSymmetric(self, root) -> bool:
        
        def is_symmetric(l, r):
            if not l and not r:
                return True

            if not (l and r):
                return False
            
            if l.val != r.val:
                return False
            
            return is_symmetric(l.left, r.right) and is_symmetric(l.right, r.left)
        
        return is_symmetric(root.left, root.right)

tests_data = [
    ([1,2,2,3,4,4,3], True),
    ([1,2,2,None,3,None,3], False),
]
obj = Solution()

for data in tests_data:
    t1 = list_to_order_btree(data[0]) 
    assert obj.isSymmetric(t1) is data[-1]