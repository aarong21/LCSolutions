# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(node, low, high):
            if not node: return True
            if not (low < node.val < high):
                return False
            return isValid(node.left, low, node.val) and isValid(node.right, node.val, high)
        
        return isValid(root, float('-inf'), float('inf'))


        # def ifLeft(node, left):
        #     if node.val < left.val:
        #         return False
        #     return True
        # def isRight(node,right):
        #     if node.val > right.val:
        #         return False
        #     return True
        # q = [root]
        # while q:
        #     node = q.pop(0)
        #     if node.left is not None:
        #         q.append(node.left)