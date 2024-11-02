// URL - https://neetcode.io/problems/balanced-binary-tree

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

/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {boolean}
 */
const insert = (root, val) => {
    if (!root) {
        return new TreeNode(val);
    }

    if (val < root.val) {
        root.left = insert(root.left, val)
    } else {
        root.right = insert(root.right, val)
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
     * @return {number}
     */
    getHeight(root) {
        if (!root) {
            return 0;
        }

        return Math.max(this.getHeight(root.left) + 1, this.getHeight(root.right) + 1);
    }

    _isBalanced(root) {
        if (!root) {
            return true;
        }

        const lHeight = this.getHeight(root.left);
        const rHeight = this.getHeight(root.right);

        return Math.abs(lHeight - rHeight) <= 1
    }

    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isBalanced(root) {
        if (!root) {
            return true;
        }

        return this._isBalanced(root) && this._isBalanced(root.left) && this._isBalanced(root.right);
    }
}

const root = [2, 1, 3, 4]
let initial = null
for (let i =0; i < root.length; i++) {
    initial = insert(initial, root[i])
}

const s = new Solution();

console.log(s.isBalanced(initial))
