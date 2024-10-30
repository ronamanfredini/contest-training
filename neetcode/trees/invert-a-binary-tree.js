// URL - https://neetcode.io/problems/invert-a-binary-tree

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

function insert(val, root) {
  if (!root) {
    return new TreeNode(val);
  }

  if (val < root.val) {
    root.left = insert(val, root.left);
  } else {
    root.right = insert(val, root.right);
  }

  return root
}

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
   * @return {TreeNode}
   */
  invertTree(root) {
    if (root === undefined || root === null) {
      return
    }
  
    const aux = root.left;
    root.left = root.right
    root.right = aux;

    this.invertTree(root.left)
    this.invertTree(root.right)

    return root
  }
}

const root = [3,2,1]
let initial = insert(root[0], null);
for (let i = 1; i < root.length; i++) {
  initial = insert(root[i], initial);
}


const s = new Solution();
console.log(s.invertTree(initial));



