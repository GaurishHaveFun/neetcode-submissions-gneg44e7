class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        sys.setrecursionlimit(10000)
        stack = []
        dele = set(to_delete)

        def dfs(root, boolean):
            if not root:
                return None
            
            delete = root.val in dele

            if boolean and not delete:
                stack.append(root)
            root.left = dfs(root.left, delete)
            root.right = dfs(root.right, delete)

            if delete:
                return None
            else:
                return root
        
        dfs(root, True)
        return stack
