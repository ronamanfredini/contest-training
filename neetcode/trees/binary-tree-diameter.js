// URL - https://neetcode.io/problems/binary-tree-diameter

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

function insert(val, root) {
    if (!root) {
        return new TreeNode(val);
    }

    if (val < root.val) {
        root.left = insert(val, root.left);
    } else {
        root.right = insert(val, root.right);
    }

    return root;
}



class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    getHeightOfTree = (root) => {
        if (!root) {
            return 0;
        }
    
        const lHeight = this.getHeightOfTree(root.left) + 1;
        const rHeight = this.getHeightOfTree(root.right) + 1;
    
        return Math.max(lHeight, rHeight)
    }

    /**
     * @param {TreeNode} root
     * @return {number}
     */
    getDiameterOfBtree = (root) => {
        if (!root) {
            return 0;
        }
    
        const leftHeight = this.getHeightOfTree(root.left)
        const rightHeight = this.getHeightOfTree(root.right);
    
        return leftHeight + rightHeight;
    }

    /**
     * @param {TreeNode} root
     * @return {number}
     */
    diameterOfBinaryTree(root) {
        return Math.max(this.getDiameterOfBtree(root), this.getDiameterOfBtree(root.left), this.getDiameterOfBtree(root.right));
    }
}

const root = [1, 7, 12, 8, 13, 4, 3, 5].filter(n => !!n);

let initial = null
for (let i = 0; i < root.length; i++) {
  initial = insert(root[i], initial);
}

const s  = new Solution()
console.log(s.diameterOfBinaryTree(initial))
