# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        self.dfs(root, result)
        result.sort()
        return result[k-1]

    def dfs(self, tree, arr):
        if not tree:
            return
        
        arr.append(tree.val)
        self.dfs(tree.left, arr)
        self.dfs(tree.right, arr)