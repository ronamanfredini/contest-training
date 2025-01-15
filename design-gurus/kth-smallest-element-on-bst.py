class TreeNode:
   def __init__(self, x):
       self.val = x       # Value of the node.
       self.left = None   # Reference to the left child.
       self.right = None  # Reference to the right child.


class Solution:
    def __init__(self):
        # `count` keeps track of the number of nodes we've traversed in-order.
        self.count = 0
        
        # `result` will hold our final answer.
        self.result = 0

    # This method is the public API that finds the kth smallest element in a BST.
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def in_order_traverse(root):
            if root:
                self.count += 1
                if self.count == k:
                    return root.val
                left = in_order_traverse(root.left)
                if left:
                    return left
                right = in_order_traverse(root.right)
                if right:
                    return right
        
        result = in_order_traverse(root)
        return result

s = Solution()

# [5, 3, 6, 2, 4, null, null, 1]
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)



print(s.kthSmallest(root, 3)) # 1

