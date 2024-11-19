
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lis = []
        if not root:
            return lis

        queue = deque([root])
        lis.append([root.val])
        temp = deque()

        # while nodes in queue to check children
        while queue:
            node = queue.popleft()
            if node.left:
                temp.append(node.left)
            if node.right:
                    temp.append(node.right)
            # once queue is empty, temp list contains whole row
            # add temp values into lis as []
            if not queue:
                if temp:
                    lis.append([n.val for n in temp])
                # use children nodes as next queue
                queue = temp
                # clear temp to store new children nodes
                temp = deque()

        return lis
