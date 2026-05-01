# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # some type of bfs
        # ans array --> add each set of children to array
        # while node in queue, pop, and add children to queue

        # if root empty: return []

        # initialize ans[], queue[]
        # initialize level = 0

        # add root to queue
        # while queue:
            # lenq = len(queue)
            # res.append([])
            # for _ in range(lenq):
                # node = queue.pop() from front
                # res[level].append(node.val)
                # if node.right:
                    # enqueue node.right
                # if node.left:
                    # enqueue node.left
            # level += 1
        # return ans[]

        if not root:
            return []
        ans = []
        queue = [root]
        level = 0
        while queue:
            lenq = len(queue)
            ans.append([])
            for _ in range(lenq):
                node = queue.pop(0)
                ans[level].append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            level += 1
        return ans