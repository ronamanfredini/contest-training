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
    const queue = [];
    const levels = [];

    if (root) {
      queue.push(root);
    }
    
    while (queue.length > 0) {
      const qLen = queue.length;
      const level = [];
      
      for (let i = 0; i < qLen; i++) {
        const node = queue.shift();
        if (node) {
          level.push(node.val);
          queue.push(node.left);
          queue.push(node.right);
        }
      }

      if (level.length > 0) {
        levels.push(level);
      }
    }

    return levels
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
