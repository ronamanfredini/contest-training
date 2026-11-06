# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0
        def dfs(root, localMax):
            if not root:
                return
            
            if root.val > localMax:
                localMax = root.val
            if root.val == localMax:
                self.good_nodes += 1
            
            dfs(root.left, localMax)
            dfs(root.right, localMax)        

        dfs(root, root.val)
        return self.good_nodes


if __name__ == "__main__":
    #         2
    #       /   \
    #      1     1
    #     /     / \
    #    3     1   5
    # root=[2,1,1,3,null,1,5]  expected: 3  (2, 3, 5)
    root = TreeNode(2,
                    TreeNode(1, TreeNode(3)),
                    TreeNode(1, TreeNode(1), TreeNode(5)))
    print(Solution().goodNodes(root))

    #         3
    #        /
    #       3
    #      / \
    #     4   2
    # root=[3,3,null,4,2]  expected: 3  (3, 3, 4)
    root = TreeNode(3,
                    TreeNode(3, TreeNode(4), TreeNode(2)))
    print(Solution().goodNodes(root))
