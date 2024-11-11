// URL - https://neetcode.io/problems/valid-binary-search-tree

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
   * @return {boolean}
   */
  isValidBST(root) {
      let min = Number.MAX_SAFE_INTEGER 
      let max = Number.MIN_SAFE_INTEGER
      const aux = (root) => {
            if (!root) {
              return true;
          }

          let isValid = true;

          min = Math.min(min, root.val)
          max = Math.max(max, root.val)

          if (root.left) {
              isValid = root.left.val < min;
          }

          if (isValid && root.right) {
              isValid = root.right.val > max
          }

          return isValid && aux(root.left, min, max) && aux(root.right, min, max)
      }

      if (!root) {
          return true;
      }

      return aux(root, Number.MAX_SAFE_INTEGER, Number.MIN_SAFE_INTEGER)
  }
}

const s = new Solution();
const root = new TreeNode(5);
root.left = new TreeNode(4)
root.right = new TreeNode(6)
root.right.left = new TreeNode(3)
root.right.right = new TreeNode(7)

console.log(s.isValidBST(root))

