# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## you can only start the value of count once you have gotten to the minimum
        ## value of the tree which is the furthest left node down
        self.res = root.val
        self.count = 0
        def inorder(root):
            if not root:
                return 0
            inorder(root.left)
            self.count += 1
            if self.count == k:
                self.res = root.val
                return
            inorder(root.right)
        inorder(root)
        return self.res