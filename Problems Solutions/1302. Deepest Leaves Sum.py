# https://leetcode.com/problems/deepest-leaves-sum/

from utils import list_to_order_btree
from collections import deque


class Solution:
    def deepestLeavesSum(self, root) -> int:
        nodes = deque([root])
        levels = []

        while nodes:
            lvl = []
            
            for _ in range(len(nodes)):
                node = nodes.pop()
                lvl.append(node.val)

                if node.left:
                    nodes.appendleft(node.left)
                if node.right:
                    nodes.appendleft(node.right)
            
            if lvl:
                levels.append(lvl)
        
        print(levels)
        return sum(levels[-1])

tests_data = [
    ([1,2,3,4,5,None,6,7,None,None,None,None,8], 15),
    ([6,7,8,2,7,1,3,9,None,1,4,None,None,None,5], 19),
]
obj = Solution()

for data in tests_data:
    tree = list_to_order_btree(data[0])
    assert data[-1] == obj.deepestLeavesSum(tree)