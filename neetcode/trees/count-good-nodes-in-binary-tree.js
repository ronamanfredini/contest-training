// URL - https://neetcode.io/problems/count-good-nodes-in-binary-tree

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
   * @return {number}
   */
  goodNodes(root) {
    let goodNodeCount = 0;
    const aux = (r, max = -101) => {
      if (!r) {
        return;
      }

      if (r.val >= max) {
        goodNodeCount++;
      }

      const maxVal = Math.max(r.val, max)

      aux(r.left, maxVal);
      aux(r.right, maxVal);
    }

    aux(root);
    return goodNodeCount;
  }
}

const s = new Solution();
const root = new TreeNode(3);
root.left = new TreeNode(3)
root.right = null
root.left.left = new TreeNode(4)
root.left.right = new TreeNode(2)

console.log(s.goodNodes(root))
