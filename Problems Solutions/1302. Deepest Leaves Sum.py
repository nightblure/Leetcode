# https://leetcode.com/problems/deepest-leaves-sum/

from utils import list_to_order_btree


class Solution:
    def deepestLeavesSum(self, root) -> int:
       nodes = [root]
       level_sum = 0
       
       while nodes:
        level_sum = 0

        for _ in range(len(nodes)):
            node = nodes.pop(0)
            level_sum += node.val
            
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return level_sum

tests_data = [
    ([1,2,3,4,5,None,6,7,None,None,None,None,8], 15),
    ([6,7,8,2,7,1,3,9,None,1,4,None,None,None,5], 19),
]
obj = Solution()

for data in tests_data:
    tree = list_to_order_btree(data[0])
    assert data[-1] == obj.deepestLeavesSum(tree)