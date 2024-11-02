// URL - https://neetcode.io/problems/depth-of-binary-tree

function insert(val, root) {
    if (!root) {
        return new TreeNode(val);
    }

    if (val < root.left) {
        root.left = insert(val, root.left);
    } else {
        root.right = insert(val, root.right);
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
     * @return {number}
     */
    maxDepth(root) {
        if (!root) {
            return 0;
        }

        return Math.max(this.maxDepth(root.left) + 1, this.maxDepth(root.right) + 1);
    }
}

const root = [1,2,3,null,null,4].filter(n => !!n);

let initial = insert(root[0], null);
for (let i = 1; i < root.length; i++) {
  initial = insert(root[i], initial);
}


const s  = new Solution()
console.log(s.maxDepth(initial))
