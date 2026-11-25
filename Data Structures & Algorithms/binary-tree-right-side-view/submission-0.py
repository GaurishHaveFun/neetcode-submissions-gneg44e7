# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def bfs(root):
            if not root:
                return []
            
            res = []
            queue = collections.deque()
            queue.append(root)

            while queue:
                lev = len(queue)
                count = 0
                while count < lev:
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    if count == lev - 1:
                        res.append(node.val)
                    count += 1
            
            return res
        return bfs(root)



