# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subRoot is null, it is automatically a subtree of root tree because 
        # we can look at any of the leaf nodes
        if not subRoot:
            return True

        # impossible for subRoot to be a subtree of root tree if subroot exists but root doesnt
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left)) and (self.sameTree(s.right, t.right))
        return False
