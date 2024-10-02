class Root {
    /**
     * @type {Root | null}
     * @public
     */
    left;

    /**
     * @type {Root | null}
     * @public
     */
    right;

    /**
     * @type {number}
     * @public
     */
    value;

    constructor(value) {
        this.value = value
    }
}

/**
 * @param {Root} root 
 * @param {number} value 
 * @returns {Root}
 */
function insert(root, value) {
    if (!root) {
        return new Root(value);
    }

    if (value < root.value) {
        root.left = insert(root.left, value);
    }

    if (value > root.value) {
        root.right = insert(root.right, value);
    }

    return root;
}

/**
 * @param {Root} root 
 * @returns {Root}
 */
function invert(root) {
    if (!root) {
        return null;
    }

    const temp = root.left;

    root.left = invert(root.right);
    root.right = invert(temp);

    return root;
}

let root = insert(null, 1);

root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 6)
root = insert(root, 7)

console.log(JSON.stringify(root))
root = invert(root);
console.log(JSON.stringify(root))

const tree = {
    value: 1,
    left: {
      value: 2,
      left: {
        value: 4,
        left: null,
        right: null
      },
      right: {
        value: 5,
        left: null,
        right: null
      }
    },
    right: {
      value: 3,
      left: {
        value: 6,
        left: null,
        right: null
      },
      right: {
        value: 7,
        left: null,
        right: null
      }
    }
  };
  
const t = invert(tree)
console.log(t)
