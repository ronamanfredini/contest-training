class TreeNode:
   def __init__(self, x):
       self.val = x          # Value stored in the node.
       self.left = None      # Reference to the left child.
       self.right = None     # Reference to the right child.


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        def insert(root, val):
            if not root:
                return float('inf'), float('inf')
            
            if val < root.val:
                smallest_diff, parent_num = insert(root.left, val)
                diff_vs_current = abs(root.val - target)
                if diff_vs_current <= smallest_diff:
                    if root.val < parent_num:
                        parent_num = root.val
                    smallest_diff = diff_vs_current

                return smallest_diff, parent_num
            else:
                smallest_diff, parent_num = insert(root.right, val)
                diff_vs_current = abs(root.val - target)
                if diff_vs_current <= smallest_diff:
                    if root.val < parent_num:
                        parent_num = root.val
                    smallest_diff = diff_vs_current

                return smallest_diff, parent_num
        
        _, parent_num = insert(root, target)
            
        return parent_num

# [4,2,6,1,5,7]
example1 = TreeNode(5)
example1.left = TreeNode(3)
example1.left.left = TreeNode(1)
example1.left.right = TreeNode(4)
example1.right = TreeNode(8)
example1.right.left = TreeNode(6)
example1.right.right = TreeNode(9)

s = Solution()
print(s.closestValue(example1, 6.4))
