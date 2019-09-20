class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = this.right = null;
    }
}
/**
 * @param {TreeNode} root
 * @return {number}
 */
let maxAncestorDiff = function (root) {
    let help = (node, left, right) => {
        if (!node) return 0;
        const v = Math.max(Math.abs(node.val - left), Math.abs(node.val - right));
        left = Math.min(left, node.val);
        right = Math.max(right, node.val);
        return Math.max(v, Math.max(help(node.left, left, right), help(node.right, left, right)));
    };
    return help(root, root.val, root.val);
}