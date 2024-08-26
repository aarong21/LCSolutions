"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []

        def bfs(root):
            if root:
                for child in root.children:
                    bfs(child)
                output.append(root.val)

        bfs(root)
        return output
        