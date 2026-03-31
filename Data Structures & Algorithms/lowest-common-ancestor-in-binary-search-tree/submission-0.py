# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root):
            if p.val == root.val or q.val == root.val or p.val <= root.val and q.val > root.val or q.val <= root.val and p.val> root.val:
                return root

            if p.val and q.val > root.val:
                return dfs(root.right)
            elif p.val and q.val < root.val:
                return dfs(root.left)
        
        return dfs(root)

            
