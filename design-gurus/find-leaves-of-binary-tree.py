class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sol(root):
    levels = []

    def dfs(root):
        if not root:
            return False
        
        if not root.left and not root.right:
            return True

        l_leaf = dfs(root.left)
        r_leaf = dfs(root.right)

        if l_leaf:
            levels[-1].append(root.left.val)
            root.left = None

        if r_leaf:
            levels[-1].append(root.right.val)
            root.right = None

        return False

    while root.left or root.right:
        levels.append([])
        dfs(root)

    levels.append([root.val])

    return levels



# Example usage: [1,2,3,4]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print(sol(root))
# Output: [[4], [2, 3], [1]]