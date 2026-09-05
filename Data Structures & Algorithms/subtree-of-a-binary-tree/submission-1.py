# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.val == node2.val:
                return (sameTree(node1.left, node2.left) and
                sameTree(node1.right, node2.right))
            return False
            

        # depth first search on root tree for subroot
        def dfs(node):
            if not node:
                return False
            
            if sameTree(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)