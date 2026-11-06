class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diamater = [0, 0]
        def dfs(root, relative_position = (0, 0)):
            if not root:
                return

            left, right = relative_position

            max_diamater[0] = max(max_diamater[0], left)
            max_diamater[1] = max(max_diamater[1], right)

            dfs(root.left, (left + 1, right - 1))
            dfs(root.right, (left - 1, right + 1))

        dfs(root)
        left, right = max_diamater

        distance = abs(-left - right)
        return distance