"""
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
"""
class Solution:
    def findSuccessor(root):
        cur = root.right
        while (cur and cur.left):
            cur = cur.left
        return cur

    def deleteNode(self, root, key):
        if not root:
            return root

        if root.val == key:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            p = self.findSuccessor(root)
            root.val = p.val
            root.right = self.deleteNode(root.right, p.val)
            return root

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root