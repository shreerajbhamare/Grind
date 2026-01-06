# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [root];l=1
        s = (root.val,l)
        while q:
            n = len(q)
            x = 0
            
            for i in range(n):
                t = q.pop(0)
                x += t.val
                if t.left: q.append(t.left)
                if t.right: q.append(t.right)
            if x > s[0]: s = (x,l)
            l+=1
        return s[1]

        