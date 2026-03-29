# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        level = 0
        tree_traversal = deque()
        solutions = []
        if root:
            tree_traversal.append(root)
        while len(tree_traversal)>0:
            length_level = len(tree_traversal)
            for i in range(length_level):
                curr = tree_traversal.popleft()
                if i == length_level-1:
                    solutions.append(curr.val)
                if curr.left:
                    tree_traversal.append(curr.left)
                if curr.right:
                    tree_traversal.append(curr.right)
            level+=1
        return solutions

            
                