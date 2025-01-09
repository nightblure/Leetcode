# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    if not root:
        return []

    lvls = [[root.val]]
    nodes = deque([root])

    while nodes:
        next_lvl = []

        for _ in range(len(nodes)):
            node = nodes.popleft()

            if node.left:
                next_lvl.append(node.left.val)
                nodes.append(node.left)

            if node.right:
                next_lvl.append(node.right.val)
                nodes.append(node.right)

        if next_lvl:
            lvls.append(next_lvl)

    return lvls
