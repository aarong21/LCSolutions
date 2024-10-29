# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, height):
            if not root: return height
            return max(dfs(root.left, height+1), dfs(root.right, height+1))
        return dfs(root, 0)
        
        