from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from LeetCode level-order list, e.g. build_tree([1, None, 2])."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        def dfs(root):
            if not root or not self.is_balanced:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(right - left) > 1:
                self.is_balanced = False
            
            return 1 + max(left, right)

        dfs(root)
        return self.is_balanced

if __name__ == "__main__":
    root = build_tree([1, 2, 3, None, None, 4, None, 5])
    print(Solution().isBalanced(root))  # expected: False
