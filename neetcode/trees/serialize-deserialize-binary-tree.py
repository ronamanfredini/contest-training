from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    NONE = 'None'
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque()
        q.append(root)

        while len(q) > 0:
            r = q.popleft()
            if r:
                q.append(r.left)
                q.append(r.right)
                res.append(str(r.val))
            else:
                res.append(self.NONE)
        
        while len(res) > 0:
            if res[-1] == self.NONE:
                res.pop()
            else:
                break

        result = '#'.join(res)
        return result

    def validateNone(self, val):
        if val == self.NONE or val == None:
            return None
            
        return int(val)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = deque(data.split('#'))
        if len(tree) == 0:
            return None

        v = self.validateNone(tree.popleft())
        begin = TreeNode(v)
        q = deque([begin])

        while q:
            root = q.popleft()

            lVal = self.validateNone(tree.popleft() if len(tree) > 0 else None)
            rVal = self.validateNone(tree.popleft() if len(tree) > 0 else None)

            if lVal:
                lVal = TreeNode(lVal)
                q.append(lVal)

            if rVal:
                rVal = TreeNode(rVal)
                q.append(rVal)
        
            root.right = rVal
            root.left = lVal

        return begin








        

























def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a LeetCode level-order list."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q: deque[TreeNode] = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        for side in ("left", "right"):
            if i < len(values) and values[i] is not None:
                child = TreeNode(values[i])
                setattr(node, side, child)
                q.append(child)
            i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> list[Optional[int]]:
    """Convert a tree back to a LeetCode level-order list."""
    out: list[Optional[int]] = []
    q: deque[Optional[TreeNode]] = deque([root])
    while q:
        node = q.popleft()
        out.append(node.val if node else None)
        if node:
            q.extend([node.left, node.right])
    while out and out[-1] is None:
        out.pop()
    return out


def print_tree(node: Optional[TreeNode], label: str = "root", depth: int = 0) -> None:
    """Print the tree sideways with L/R labels."""
    if node is None:
        return
    print("    " * depth + f"{label}: {node.val}")
    print_tree(node.left, "L", depth + 1)
    print_tree(node.right, "R", depth + 1)


def run_case(values: list[Optional[int]], expected: list[Optional[int]]) -> None:
    """Round-trip a tree through Codec and compare to expected."""
    print(f"root={values}")
    root = build_tree(values)
    print_tree(root)
    codec = Codec()
    got = tree_to_list(codec.deserialize(codec.serialize(root)))
    print(f"  got={got} expected={expected} -> {'PASS' if got == expected else 'FAIL'}")


run_case([1, 2, 3, None, None, 4, 5], [1, 2, 3, None, None, 4, 5])
