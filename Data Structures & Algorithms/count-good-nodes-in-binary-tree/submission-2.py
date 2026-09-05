# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def countGood(node, maxVal):

            if not node:
                return 0
            
            if node.val >= maxVal:
                good = 1
            else:
                good = 0

            maxVal = max(node.val, maxVal)

            left = countGood(node.left, maxVal)
            right = countGood(node.right, maxVal)

            return good + left + right
        return countGood(root, root.val)