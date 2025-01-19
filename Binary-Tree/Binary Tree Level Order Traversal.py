
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []

        queue = deque([(0,root)])
        res = []
        d = 1
        final = [[root.val]]
        while queue:
            curr_d, node = queue.popleft()

            if curr_d == d:
                res.append(node.val)
            elif curr_d > 0:
                final.append(res)
                res = [node.val]
                d = curr_d
            
            if node.left:
                queue.append((curr_d+1, node.left))
            if node.right:
                queue.append((curr_d+1, node.right))

        if res:
            final.append(res)

        return final

        