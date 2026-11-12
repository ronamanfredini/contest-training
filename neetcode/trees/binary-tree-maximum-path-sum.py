from __future__ import annotations

from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def dfs(root):
            if not root:
                return 0

            maxLeft = max(dfs(root.left), 0)
            maxRight = max(dfs(root.right), 0)
            maxPath = max(maxLeft + root.val, maxRight + root.val, root.val)
            self.res = max(self.res, root.val, root.val + maxLeft + maxRight)

            return maxPath

        dfs(root)
        return self.res
        

class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a LeetCode level-order list."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue: deque[TreeNode] = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        for side in ("left", "right"):
            if i < len(values) and values[i] is not None:
                child = TreeNode(values[i])
                setattr(node, side, child)
                queue.append(child)
            i += 1
    return root


def print_tree(node: Optional[TreeNode], label: str = "root", depth: int = 0) -> None:
    """Print the tree sideways with L/R labels."""
    if node is None:
        return
    print(f"{'    ' * depth}{label}: {node.val}")
    print_tree(node.left, "L", depth + 1)
    print_tree(node.right, "R", depth + 1)


def run_case(values: list[Optional[int]], expected: Optional[int] = None) -> None:
    """Build the input, run maxPathSum, and print the result."""
    print(f"root={values}")
    root = build_tree(values)
    print_tree(root)
    got = Solution().maxPathSum(root)
    if expected is None:
        print(f"  got={got}")
        return
    print(f"  got={got} expected={expected} -> {'PASS' if got == expected else 'FAIL'}")


run_case([1, 2, None, 3, None, 4, None, 5])
