# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs(curr):
            if not curr:
                return
            # perform swamp of children of both exist
            if curr.left and curr.right:
                right = curr.right
                curr.right = curr.left
                curr.left = right
                dfs(curr.left)
                dfs(curr.right)
            elif curr.left:
                curr.right = curr.left
                curr.left = None
                dfs(curr.right)
            elif curr.right:
                curr.left = curr.right
                curr.right = None
                dfs(curr.left)
            else:
                return
        dfs(root)
        return root


