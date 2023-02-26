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

    def postorderTraversal(self, root):

        def helper(root, answer):
            if not root:
                return
            
            helper(root.left, answer)
            helper(root.right, answer)
            answer.add(root.val)

        answer = []
        helper(root, answer)
        return answer