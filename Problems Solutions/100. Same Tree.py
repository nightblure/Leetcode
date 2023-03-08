# https://leetcode.com/problems/same-tree/description/

from utils import list_to_order_btree

class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

tests_data = [
    ([1,2,3], [1,2,3], True),
    ([1,2], [1,None,2], False),
    ([1,2,1], [1,1,2], False)
]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    t1 = list_to_order_btree(data[0]) 
    t2 = list_to_order_btree(data[1])
    result = obj.isSameTree(t1, t2)
    assert expected is result