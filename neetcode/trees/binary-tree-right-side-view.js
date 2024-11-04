// URL - https://neetcode.io/problems/binary-tree-right-side-view

// URL - https://neetcode.io/problems/level-order-traversal-of-binary-tree
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class TreeNode {
  constructor(val = 0, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

class Solution {
  /**
   * @param {TreeNode} root
   * @return {number[][]}
   */
  rightSideView(root) {
    if (!root) {
      return [];
    }

    function aux(root, level = 0, sublists = []) {
      if (!root) {
        return;
      }

      if (!sublists[level]) {
        sublists[level] = [];
      }

      sublists[level].push(root.val);
      aux(root.left, level + 1, sublists);
      aux(root.right, level + 1, sublists);


      return sublists;
    }

    const levels = aux(root);
    const result = [];
    for (const level of levels) {
      result.push(level.pop())
    }

    return result
  }
}

const s = new Solution();
const root = new TreeNode(1);
root.left = new TreeNode(2)
root.left.left = new TreeNode(4)
root.left.right = new TreeNode(5)
root.right = new TreeNode(3)
root.right.left = new TreeNode(6)
root.right.right = new TreeNode(7)

console.log(s.rightSideView(root))
