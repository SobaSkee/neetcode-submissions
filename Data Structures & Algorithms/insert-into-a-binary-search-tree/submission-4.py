# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def findPlace(node):
            # if not node.left and not node.right:
            #     print(node.val)
            #     return node
            
            if val < node.val and node.left:
                return findPlace(node.left)
            if val > node.val and node.right:
                return findPlace(node.right)
            return node

        nodeToInsert = findPlace(root)

        if val < nodeToInsert.val:
            nodeToInsert.left = TreeNode(val)
        else:
            nodeToInsert.right = TreeNode(val)
        return root
                