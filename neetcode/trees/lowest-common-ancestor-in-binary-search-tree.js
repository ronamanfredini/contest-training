// URL - https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree


function insert(root, val) {
  if (!root) {
    return new TreeNode(val);
  }

  if (val < root.val) {
    root.left = insert(root.left, val);
  } else {
    root.right = insert(root.right, val);
  }

  return root;
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
   * @param {TreeNode} p
   * @param {TreeNode} q
   * @return {TreeNode}
   */

  lowestCommonAncestor(root, p, q) {
    const _lowestCommonAncestor = (root, p, q) => {
      const findNumber = (root, number) => {
        if (!root) {
          return false;
        }

        if (root.val === number) {
          return true;
        }

        return findNumber(root.left, number) || findNumber(root.right, number);

      }

      if (!root) {
        return false;
      }

      const found = _lowestCommonAncestor(root.left, p, q) || _lowestCommonAncestor(root.right, p, q);
      if (found) {
        return found;
      }

      return findNumber(root, p) && findNumber(root, q) ? root : false;
    }

    return _lowestCommonAncestor(root, p.val, q.val);
  }
}


const s = new Solution();

const root = new TreeNode(5);
insert(root, 3)
insert(root, 8)
insert(root, 1)
insert(root, 4)
insert(root, 7)
insert(root, 9)
insert(root, null)
insert(root, 2)


console.log(s.lowestCommonAncestor(root, new TreeNode(3), new TreeNode(4)))