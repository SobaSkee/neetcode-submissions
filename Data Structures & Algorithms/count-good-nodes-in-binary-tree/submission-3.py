# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def isGood(node, maxValue):
            if not node:
                return 0

            if node.val >= maxValue:
                good = 1
            else:
                good = 0
            maxValue = max(node.val, maxValue)

            left = isGood(node.left, maxValue)
            right = isGood(node.right, maxValue)

            return good + left + right
        return isGood(root, root.val)