# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# супер важно: обрабатывать ноды и добавлять в уровень надо строго слева-направо!
def levelOrder(root):
    if not root:
        return []

    lvls = [[root.val]]
    nodes = deque([root])

    while nodes:
        lvl = []

        for _ in range(len(nodes)):
            node = nodes.popleft()

            if node.left:
                lvl.append(node.left.val)
                nodes.append(node.left)

            if node.right:
                lvl.append(node.right.val)
                nodes.append(node.right)

        if lvl:
            lvls.append(lvl)

    return lvls
