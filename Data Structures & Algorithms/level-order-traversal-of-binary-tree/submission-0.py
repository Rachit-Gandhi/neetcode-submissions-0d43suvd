# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = deque()
        solutions=[]
        solution = []
        if root:
            nodes.append(root)
        level = 0
        while len(nodes)>0:
            for i in range (len(nodes)):
                curr = nodes.popleft()
                solution.append(curr.val)
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)
            level+=1
            solutions.append(solution)
            solution= []
        return solutions
        