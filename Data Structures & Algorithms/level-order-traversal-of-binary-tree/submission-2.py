# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def bfs(root):
            if not root:
                return []
            q = collections.deque()
            q.append(root)
            count = 0
            level = []
            res = []
            qlen = 1

            while q:
                node = q.popleft()
                level.append(node.val)
                count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if count == qlen:
                    res.append(level)
                    qlen = len(q)
                    level = []
                    count = 0
            return res
        
        return bfs(root)