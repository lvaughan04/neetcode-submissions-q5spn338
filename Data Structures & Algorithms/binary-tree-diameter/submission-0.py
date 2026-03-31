# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(self, root):
            nonlocal res
            if not root:
                return 0
            
            heightLeft = dfs(self, root.left)
            heightRight = dfs(self, root.right)
            res = max(heightLeft + heightRight, res)
            return 1 + max(heightLeft, heightRight)
        dfs(self, root)
        return res

        