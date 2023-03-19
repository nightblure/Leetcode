# https://leetcode.com/problems/range-sum-of-bst/

from utils import TreeNode, list_to_search_btree

class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        sum = 0
        nodes = [root]

        # DFS
        while nodes:
            node = nodes.pop()

            if node:
                if node.val >= low and node.val <= high:
                    sum += node.val
                nodes.append(node.left)
                nodes.append(node.right)              

        return sum

tests_data = [
    ([10,5,15,3,7,None,18], 7, 15, 32),
    ([10,5,15,3,7,13,18,1,None,6], 6, 10, 23),
]

obj = Solution()

for data in tests_data:
    expected = data[-1]
    root = list_to_search_btree(data[0])
    assert expected == obj.rangeSumBST(root, data[1], data[2])