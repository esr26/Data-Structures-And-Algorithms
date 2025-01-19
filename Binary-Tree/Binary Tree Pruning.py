# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):

            if not root: return 

            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if root and root.val ==0 and root.left == None and root.right == None:
                return None
            else:
                return root
                
        
        dfs(root)
            
        
        if root.val==0 and not root.left and not root.right: return None
        return root
        