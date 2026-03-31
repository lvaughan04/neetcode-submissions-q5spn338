# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            last = False
            for i in range(qLen):
                node = q.popleft()
                if node:
                    if last == False:
                        res.append(node.val)
                        last = True
                    q.append(node.right)
                    q.append(node.left)

        return res
        