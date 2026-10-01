# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        leftB = float('-inf')
        rightB = float('inf')
        def dfs(node, leftB, rightB):
            if not node:
                return True
            if not (leftB < node.val < rightB):
                return False
            
            return dfs(node.left, leftB, node.val) and dfs(node.right, node.val, rightB)
        return dfs(root, leftB, rightB)