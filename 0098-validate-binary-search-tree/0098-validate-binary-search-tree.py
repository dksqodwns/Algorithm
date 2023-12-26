import sys

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root,float('-inf'),float('inf'))
        
    def dfs(self, node, min, max):
        if not node:
            return True
        
        if ((node.val > min and node.val < max) and
            self.dfs(node.left, min, node.val) and
            self.dfs(node.right, node.val, max)):
            return True
        return False