# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node, p , q):
            if node.val == p.val:
                return p
            elif node.val == q.val:
                return q
            elif (node.val > p.val and node.val < q.val) or (node.val < p.val and node.val > q.val):
                return node
            
            if node.val < p.val and node.val < p.val:
                return dfs(node.right, p , q)
            if node.val > p.val and node.val > p.val:
                return dfs(node.left, p, q)
        
        return dfs(root, p, q)