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
            
            q = collections.deque()
            q.append(root)
            qlen = 1
            count = 0
            res = []

            while q:
                node = q.popleft()
                count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if count == qlen:
                    res.append(node.val)
                    qlen = len(q)
                    count = 0
            return res
        return bfs(root)