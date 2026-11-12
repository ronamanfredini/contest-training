from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        self.result = []

        if not root:
            return []

        if not root.left and not root.right and targetSum == root.val:
            return [[root.val]]

        def dfs(root, currentSum, currentList):
            if not root:
                return

            s = currentSum + root.val
            if not root.left and not root.right:
                if s == targetSum:
                    self.result.append(currentList)
                return

            leftCopy = currentList.copy()
            rightCopy = currentList.copy()

            leftCopy.append(root.val)
            rightCopy.append(root.val)

            dfs(root.left, s, leftCopy)
            dfs(root.right, s, rightCopy)

        dfs(root, 0, [])

        return self.result
        


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a LeetCode level-order list, e.g. build_tree([1, 2])."""
    if not values or values[0] is None:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    children = iter(nodes[1:])
    for node in nodes:
        if node is None:
            continue
        node.left = next(children, None)
        node.right = next(children, None)
    return nodes[0]


def print_tree(node: Optional[TreeNode], prefix: str = "", label: str = "root") -> None:
    """Print the tree sideways, one node per line, e.g. print_tree(build_tree([1, 2]))."""
    if node is None:
        return
    print(f"{prefix}{label}: {node.val}")
    print_tree(node.left, prefix + "    ", "L")
    print_tree(node.right, prefix + "    ", "R")


def run_case(values: list[Optional[int]], target_sum: int, expected: Optional[list[list[int]]] = None) -> None:
    """Run one case and print the tree, the result and PASS/FAIL when expected is given."""
    root = build_tree(values)
    got = Solution().pathSum(root, target_sum)
    print(f"root={values} targetSum={target_sum}")
    print_tree(root)
    if expected is None:
        print(f"  got={got}\n")
        return
    status = "PASS" if sorted(got) == sorted(expected) else "FAIL"
    print(f"  got={got} expected={expected} -> {status}\n")


run_case([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22)
