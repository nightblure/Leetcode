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
    def preorderTraversal(self, root):
        answer = []
        
        def dfs(node):
            if not node:
                return
            # Visit root first, then the left subtree, then the right subtree.
            answer.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return answer
    
    def iterPreorderTraversal(self, root):
        answer = []
        stack = [root]

        # Note that we add curr_node's right child to the stack first.
        while stack:
            curr_node = stack.pop()
            if curr_node:
                answer.append(curr_node.val)
                stack.append(curr_node.right)
                stack.append(curr_node.left)
                
        return answer