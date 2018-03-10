# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.flattern2(root)

    def flattern2(self, node):
        if not node:
            return None
        if not node.left and not node.right:
            return node
        left = self.flattern2(node.left)
        right = self.flattern2(node.right)
        node.right = left
        while left and left.right:
            left = left.right
        if left:
            left.right = right
        else:
            node.right = right
        node.left = None
        return node




if __name__ == '__main__':
    S = Solution()
    a1 = TreeNode(1)
    a2 = TreeNode(4)
    a3 = TreeNode(2)
    a4 = TreeNode(11)
    a5 = TreeNode(13)
    a6 = TreeNode(4)
    a7 = TreeNode(7)
    a8 = TreeNode(2)
    a9 = TreeNode(5)
    a10 = TreeNode(1)

    # a1.left = a2
    a1.left = a3
    # a2.left = a4
    # a3.left = a5
    # a3.right = a6
    # a4.left = a7
    # a4.right = a8
    # a6.left  = a9
    # a6.right = a10
    S.flatten(a1)
    print(a1)