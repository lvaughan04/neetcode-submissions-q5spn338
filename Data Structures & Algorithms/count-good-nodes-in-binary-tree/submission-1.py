# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, -101)
        return self.res
    
    def dfs(self, root , currMax):
        if not root:
            return 
        if root.val >= currMax:
            self.res += 1
            currMax = root.val
        
        
        self.dfs(root.left, currMax) 
        self.dfs(root.right, currMax)