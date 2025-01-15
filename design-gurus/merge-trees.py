class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode
) -> TreeNode:
        if t1 or t2:
            t1_left = None
            t1_right = None
            t2_left = None
            t2_right = None
            t1_val = 0
            t2_val = 0

            if t1:
                t1_val = t1.val
                t1_left = t1.left
                t1_right = t1.right
            if t2:
                t2_val = t2.val
                t2_left = t2.left
                t2_right = t2.right
            
            t_new = TreeNode(t1_val + t2_val)

            t_new.left = self.mergeTrees(t1_left, t2_left)
            t_new.right = self.mergeTrees(t1_right, t2_right)

            return t_new
        

t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)

t2 = TreeNode(2)
t2.left = TreeNode(1)

s = Solution()
result = s.mergeTrees(t1, t2)
print(result.val)

