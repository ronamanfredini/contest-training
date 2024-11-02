// URL - https://neetcode.io/problems/same-binary-tree

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

function insert(root, val) {
    if (!root) {
        return new TreeNode(val);
    }

    if (val < root.val) {
        root.left = insert(root.left, val)
    } else {
        root.right = insert(root.right, val)
    }

    return root;
}

class Solution {
    /**
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p, q) {
        if (!q || !p) {
            return q?.val === p?.val
        }
        const isSameVal = p?.val === q?.val;
        return isSameVal && this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right);
    }
}

const p = [1,2,3], q = [1,2,3]

let pRoot = null
for (let p1 = 0; p1 < p.length; p1++) {
    pRoot = insert(pRoot, p[p1]);
}

let qRoot = null;
for (let q1 = 0; q1 < p.length; q1++) {
    qRoot = insert(qRoot, q[q1]);
}

const s = new Solution()
console.log(s.isSameTree(pRoot, qRoot))