
def solution(root):
    paths = []
    def dfs(root, path = ''):
        if not root:
            return
        
        if not root.left and not root.right:
            path += str(root.val)
            paths.append(path)
            return
        
        path += str(root.val) + '->'
        dfs(root.left, path)
        dfs(root.right, path)
        
    dfs(root)
    return paths

class Solution():
    def binaryTreePaths(self, root):
        return solution(root)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



if __name__ == "__main__":
    sol = Solution()

    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)
    print("Example 2:", sol.binaryTreePaths(root2))

    root3 = TreeNode(2)
    root3.right = TreeNode(3)
    root3.right.right = TreeNode(4)
    root3.right.right.right = TreeNode(5)
    print("Example 3:", sol.binaryTreePaths(root3))