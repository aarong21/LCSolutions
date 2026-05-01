# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return []
        
        q = [root]
        ans.append(root.val)
        while q:
            lenq = len(q)
            for _ in range(lenq):
                node = q.pop(0)
                # ans.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            if q:
                ans.append(q[-1].val)
        return ans