from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
