class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = self.minDepth(root.left) if root.left else 1 << 31-1
        right = self.minDepth(root.right) if root.right else 1 << 31-1
        return min(left, right)+1
